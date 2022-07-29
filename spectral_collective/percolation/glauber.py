import numpy as np
from PIL import Image
import sys
import os
import time

shape = (200, 500)

positive_color = np.uint8([189, 40, 45])
negative_color = np.uint8([1, 55, 102])
background_color = np.uint8([253, 246, 227])

r_offset = 320
c_offset = 280

frame_rate = 60
run_time = 60

hi_beta   = 0.4407 + 0.2
crit_beta = 0.4407
lo_beta   = 0.4407 - 0.1

hi_log2   = 21
crit_log2 = 18
lo_log2   = 15

epsilon = 0.01

def i(frame):
    return (1 - np.cos( (2 * np.pi * frame) / (24 * 60) )) / 2

def j(frame):
    return (2/3) * (1 - np.cos( (2 * np.pi * (frame - 4 * 60)) / (20 * 60) )) / 2 

def k(frame):
    return (1/3) + (1/3) * (1 + np.cos( (2 * np.pi * (frame - 10 * 60)) / (12 * 60) )) / 2

def interp(frame):
    if frame < 24 * 60:
        return i(frame)
    if frame < 34 * 60:
        return j(frame)
    if frame < 40 * 60:
        return k(frame)
    if frame < 60 * 60:
        return 1/3

def beta(frame):
    return interp(frame) * hi_beta + (1 - interp(frame)) * lo_beta

def steps_between_frames(beta):
    s = 1 / (1 + np.exp( - (beta - crit_beta) / epsilon ))
    return int(2 ** (s * (hi_log2 - lo_log2) + lo_log2)) + 2**lo_log2

grid = np.zeros(shape)
for r in range(shape[0]):
    for c in range(shape[1]):
        if r == 0 or r == shape[0]-1 or c == 0 or c == shape[1]-1:
            grid[r,c] = -1 if c < shape[1] / 2 else 1
        else:
            grid[r,c] = -1 if np.random.random() < 1/2 else 1

def delta_E(r,c):
    s = grid[r+1,c] + grid[r-1,c] + grid[r,c+1] + grid[r,c-1]
    return 2 * grid[r,c] * s

def glauber_steps(beta, steps_between_frames):
    rs = np.random.randint(1, shape[0]-1, size=steps_between_frames)
    cs = np.random.randint(1, shape[1]-1, size=steps_between_frames)

    for i in range(steps_between_frames):
        edEb = np.exp(- delta_E(rs[i], cs[i]) * beta)

        if (1 + edEb) * np.random.random() < edEb:
            grid[rs[i], cs[i]] = -1 * grid[rs[i], cs[i]]


pixels = np.zeros((1440, 2560, 3), dtype=np.uint8)
for r in range(1440):
    for c in range(2560):
        pixels[r,c] = background_color

def set_pixels():
    for r in range(shape[0]):
        for c in range(shape[1]):
            pixels[
                4 * r + r_offset : 4 * (r+1) + r_offset,
                4 * c + c_offset : 4 * (c+1) + c_offset
            ] = positive_color if grid[r,c] == 1 else negative_color

def save_image(frame, d=None):
    dname='glauber'
    if not d is None:
        dname=f'glauber/{d}'

    img = Image.fromarray(pixels, mode='RGB')
    img.save(f'{dname}/{frame}.png')
    img.close()


if __name__ == "__main__":
    d = None


    if len(sys.argv) > 1:
        d = sys.argv[1]

        print(f'writing images to glauber/{d}/\n')

        try:
            os.mkdir(f'glauber/{d}')
        except FileExistsError:
            pass
    else:
        print(f'writing images to glauber/\n')

    for frame in range(frame_rate * run_time):
        print(f'Frame {frame} starting...')

        t1 = time.perf_counter()

        b = beta(frame)

        glauber_steps(b, steps_between_frames(b))

        t2 = time.perf_counter()
        print(f'Frame {frame} finished glauber_steps in {t2-t1:0.4f} seconds.')

        set_pixels()

        t3 = time.perf_counter()
        print(f'Frame {frame} finished set_pixels    in {t3-t2:0.4f} seconds.')

        save_image(frame, d)

        t4 = time.perf_counter()
        print(f'Frame {frame} finished save_image    in {t4-t3:0.4f} seconds.')

        print(f'Frame {frame} took {t4-t1:0.4f} seconds in total!\n')
