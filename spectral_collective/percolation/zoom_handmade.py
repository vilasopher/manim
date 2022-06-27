from PIL import Image
import numpy as np
import os

HUGE_FILENAME = f'allclusters_shape=(20160, 35840)_seed=7_parameter=0.5.png'
RESOLUTION = (1440, 2560)
FRAME_RATE = 60
RUN_TIME = 30
TOP_LEFT = (1170 * 14, 680 * 14)

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
            
            rlo = topleft[0] + int(r * scale)
            rhi = topleft[0] + int((r+1) * scale)
            rhi += 1 if rlo == rhi else 0

            clo = topleft[1] + int(c * scale)
            chi = topleft[1] + int((c+1) * scale)
            chi += 1 if clo == chi else 0

            selection = PIXELS[rlo:rhi, clo:chi]

            cropped[r,c] = np.average(selection, (0,1))

    return cropped

def lerp(p, q, t):
    return (int(p[0] + t * (q[0] - p[0])), int(p[1] + t * (q[1] - p[1])))

def weird_interpolation(t):
    return (1+np.cos((1+(2*t-1)**5)*np.pi))/2

def smoothing_function(t):
    smoothpart = weird_interpolation(t) * (1-np.cos(t*np.pi))/2 
    sqrtpart = (1 - weird_interpolation(t)) * np.sqrt(t)
    return smoothpart + sqrtpart

NUM_FRAMES = int(RUN_TIME * FRAME_RATE)
DIR_NAME = f'zooms/{HUGE_FILENAME}_topleft={TOP_LEFT}_runtime={RUN_TIME}'

try:
    os.mkdir(DIR_NAME)
except FileExistsError:
    pass

for f in range(NUM_FRAMES):
    print(f'Working on frame {f}...')

    alpha = f / NUM_FRAMES

    framepixels = crop(
        lerp(TOP_LEFT, (0,0), 1 - smoothing_function(1 - alpha)),
        MINIMUM_SCALE + smoothing_function(alpha) * (MAXIMUM_SCALE - MINIMUM_SCALE)
    )

    img = Image.fromarray(framepixels, mode='RGB')
    img.save(f'{DIR_NAME}/{f}.png')
    img.close()
