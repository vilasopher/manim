from PIL import Image
import numpy as np
import os
import multiprocessing as mp

HUGE_FILENAME = f'allclusters_shape=(20160, 35840)_seed=5_parameter=0.5.png'
RESOLUTION = (1440, 2560)
FRAME_RATE = 60
RUN_TIME = 28
STARTING_CENTER = (434 * 14, 2107 * 14) #(1140 * 14, 400 * 14)  

Image.MAX_IMAGE_PIXELS = 2 ** 32

img = Image.open(f'huge/{HUGE_FILENAME}')
PIXELS = np.asarray(img)
img.close()

MINIMUM_SCALE = 1 / 14
MAXIMUM_SCALE = np.shape(PIXELS)[0] // RESOLUTION[0]

def crop(topleft, scale, frame_debug=None):

    if scale > MAXIMUM_SCALE:
        scale = MAXIMUM_SCALE

    if scale < MINIMUM_SCALE:
        scale = MINIMUM_SCALE

    cropped = np.zeros((*RESOLUTION, 3), dtype=np.uint8)

    for r in range(RESOLUTION[0]):
        for c in range(RESOLUTION[1]):

            if frame_debug is not None:
                print(f'Frame {frame_debug}, pixel ({r},{c})')
            
            rlo = int(topleft[0] + r * scale)
            rhi = int(topleft[0] + (r+1) * scale)
            rhi += 1 if rlo == rhi else 0

            if rlo < 0:
                rhi -= rlo
                rlo = 0
            
            if rhi > np.shape(PIXELS)[0]:
                rlo -= (rhi - np.shape(PIXELS)[0])
                rhi = np.shape(PIXELS)[0]

            clo = int(topleft[1] + c * scale)
            chi = int(topleft[1] + (c+1) * scale)
            chi += 1 if clo == chi else 0

            if clo < 0:
                chi -= clo
                clo = 0

            if chi > np.shape(PIXELS)[1]:
                clo -= (chi - np.shape(PIXELS)[1])
                chi = np.shape(PIXELS)[1]

            selection = PIXELS[rlo:rhi, clo:chi]

            cropped[r,c] = np.average(selection, (0,1))

    return cropped

def lerp(p, q, t):
    return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))

def weird_interpolation(t):
    return (1-np.cos((t**5)*np.pi))/2

def smoothing_function(t):
    smoothpart = weird_interpolation(t) * (1-np.cos(t*np.pi))/2 
    squarepart = (1 - weird_interpolation(t)) * t**2
    return smoothpart + squarepart

NUM_FRAMES = int(RUN_TIME * FRAME_RATE)
DIR_NAME = f'zooms/{HUGE_FILENAME}_center={STARTING_CENTER}_runtime={RUN_TIME}'

def thread_func(f):
    print(f'Starting frame {f+1}...')

    alpha = f / NUM_FRAMES

    scale = MINIMUM_SCALE + smoothing_function(alpha) * (MAXIMUM_SCALE - MINIMUM_SCALE)

    center = lerp(
        STARTING_CENTER,
        (np.shape(PIXELS)[0]/2, np.shape(PIXELS)[1]/2),
        smoothing_function(alpha)
    )

    topleft = (
        center[0] - scale * RESOLUTION[0] / 2,
        center[1] - scale * RESOLUTION[1] / 2
    )

    bottomright = (
        topleft[0] + scale * RESOLUTION[0],
        topleft[1] + scale * RESOLUTION[1]
    )

    if bottomright[0] > np.shape(PIXELS)[0]:
        topleft = (topleft[0] - (bottomright[0] - np.shape(PIXELS)[0]), topleft[1])

    if bottomright[1] > np.shape(PIXELS)[1]:
        topleft = (topleft[0], topleft[1] - (bottomright[1] - np.shape(PIXELS)[1]))

    if topleft[0] < 0:
        topleft = (0, topleft[1])

    if topleft[1] < 0:
        topleft = (topleft[0], 0)

    framepixels = crop(topleft, scale)

    img = Image.fromarray(framepixels, mode='RGB')
    img.save(f'{DIR_NAME}/{f+1}.png')
    img.close()
    
    print(f'Finished frame {f+1}...')

def main():
    try:
        os.mkdir(DIR_NAME)
    except FileExistsError:
        pass

    cc = mp.cpu_count()

    for b in range(NUM_FRAMES // cc):
        print(f'BATCH {b+1}:')

        processes = []

        for i in range(cc):
            processes.append(
                mp.Process(
                    target = thread_func,
                    args = (cc * b + i,)
                )
            )

        for p in processes:
            p.start()

        for p in processes:
            p.join()

if __name__ == '__main__':
    main()
