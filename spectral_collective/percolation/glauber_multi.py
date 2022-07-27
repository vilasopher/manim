import numpy as np
from PIL import Image

import multiprocessing as mp
cc = 6 #mp.cpu_count()


shape = (100, 250)
steps_between_frames = 10000 * cc

positive_color = np.uint8([189, 40, 45])
negative_color = np.uint8([1, 55, 102])
background_color = np.uint8([253, 246, 227])

r_offset = 420
c_offset = 280

frame_rate = 60
run_time = 60
num_full_cycles = 3
oscillation_rpframe = num_full_cycles/(frame_rate * run_time)

hi_beta = 0.4407 + 0.44
lo_beta = 0.4407 - 0.44


def delta_E(grid, r,c):
    s = grid[r+1,c] + grid[r-1,c] + grid[r,c+1] + grid[r,c-1]
    return 2 * grid[r,c] * s

def glauber_thread(grid, beta):
    rs = np.random.randint(1, shape[0]-1, size=steps_between_frames // cc)
    cs = np.random.randint(1, shape[1]-1, size=steps_between_frames // cc)

    for i in range(steps_between_frames // cc):
        edEb = np.exp(- delta_E(grid, rs[i], cs[i]) * beta)

        if (1 + edEb) * np.random.random() < edEb:
            grid[rs[i], cs[i]] = -1 * grid[rs[i], cs[i]]

def glauber_steps(grid, beta):
    for i in range(cc):
        processes.append(
            mp.Process(
                target = glauber_thread,
                args = (grid, beta)
            )
        )

    for p in processes:
        p.start()

    for p in processes:
        p.join()


def set_pixels(pixels):
    for r in range(shape[0]):
        for c in range(shape[1]):
            pixels[
                8 * r + r_offset : 8 * (r+1) + r_offset,
                8 * c + c_offset : 8 * (c+1) + c_offset
            ] = positive_color if grid[r,c] == 1 else negative_color

def save_image(pixels, frame):
    img = Image.fromarray(pixels, mode='RGB')
    img.save(f'glauber/{frame}.png')
    img.close()


if __name__ == "__main__":
    print(f'setting up...')

    m = MyManager()
    m.start()

    grid = m.np_zeros(shape)

    for r in range(shape[0]):
        for c in range(shape[1]):
            grid[r,c] = -1 if c < shape[1] / 2 else 1

    pixels = np.zeros((1440, 2560, 3), dtype=np.uint8)

    for r in range(1440):
        for c in range(2560):
            pixels[r,c] = background_color

    print(f'finished setting up!')

    for frame in range(frame_rate * run_time):

        print(f'starting frame {frame}...')
        
        c = (1 + np.cos(2 * np.pi * frame * oscillation_rpframe)) / 2

        glauber_steps(grid, c * hi_beta + (1 - c) * lo_beta)

        print(f'finished glauber_steps for frame {frame}...')

        set_pixels(pixels)

        print(f'finished set_pixels for frame {frame}...')

        save_image(pixels, frame)

        print(f'saved frame {frame}!')
