import numpy as np
from random import random, seed, randint
from PIL import Image

shape = (1080, 1920)
p = 0.5
seed(0)

numverts = shape[0] * shape[1]

data = np.full((numverts, 5), -1, dtype=np.intc)

edgedirs = [(0,1), (1,0)]

for n in range(numverts):
    i = n % shape[0]
    j = n // shape[0]

    for d in range(2):
        e1, e2 = edgedirs[d]
        if i - e1 >= 0 and j - e2 >= 0 and random() < p:
            m = (i - e1) + (j - e2) * shape[0]
            data[n,d] = m
            data[m,d+2] = n

for n in range(numverts):
    if data[n,4] == -1:
        color = randint(0, 2**24)

        print(n)

        to_visit = [n]
        while len(to_visit) > 0:
            cur = to_visit.pop()
            data[cur,4] = color

            for d in range(4):
                if data[cur,d] != -1 and data[data[cur,d],4] == -1:
                    to_visit.append(data[cur,d])

def int_to_rgb(col):
    return np.uint8([
        col // 2**16,
        (col % 2**16) // 2**8,
        col % 2**8
        ])

print('rendering...')

pixels = np.uint8(
    [ [ int_to_rgb(data[i + j * shape[0], 4])
        for j in range(shape[1]) ]
        for i in range(shape[0]) ])

img = Image.fromarray(pixels, mode='RGB')
img.save("huge/test.png")

print('rendered!')
