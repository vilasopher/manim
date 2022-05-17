import numpy as np
from random import random, seed, randint
from PIL import Image
from collections import deque
from scipy import stats

shape = (18000, 32000)

foreground = np.uint8([7,54,66])
background = np.uint8([253,246,227])

numverts = shape[0] * shape[1]

for s in range(10):
    p = 0.5
    seed(s)

    data = np.full((numverts, 5), -1, dtype=np.intc)
    pixels = np.zeros((*shape,3), dtype=np.uint8)

    edgedirs = [(0,1), (1,0)]

    for n in range(numverts):
        i = n % shape[0]
        j = n // shape[0]

        print(s, p, i, j)

        for d in range(2):
            e1, e2 = edgedirs[d]
            if i - e1 >= 0 and j - e2 >= 0 and random() < p:
                m = (i - e1) + (j - e2) * shape[0]
                data[n,d] = m
                data[m,d+2] = n

    for n in range(numverts):
        if data[n,4] == -1:
            color = randint(0, 2**24)

            print(s, p, n)

            to_visit = deque([n])
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

    print(s, p, 'rendering allclusters...')

    pixels = np.zeros((*shape,3), dtype=np.uint8)

    for i in range(shape[0]):
        for j in range(shape[1]):
            pixels[i,j] = int_to_rgb(data[i + j * shape[0], 4])

    img = Image.fromarray(pixels, mode='RGB')
    img.save('huge/allclusters_shape=' + str(shape)
            + '_seed=' + str(s) 
            + '_parameter=' + str(p) +'.png')

    print(s, p, 'rendered allclusters!')

    print(s, p, 'rendering biggestcluster...')

    m = stats.mode(data[:,4]).mode[0]

    pixels = np.full((*shape,3), background, dtype=np.uint8)

    for i in range(shape[0]):
        for j in range(shape[1]):
            if data[i + j * shape[0], 4] == m:
                pixels[i,j] = foreground

    img = Image.fromarray(pixels, mode='RGB')
    img.save('huge/biggestcluster_shape=' + str(shape)
            + '_seed=' + str(s) 
            + '_parameter=' + str(p) +'.png')

    print(s, p, 'rendered biggestcluster!')
