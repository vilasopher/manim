import numpy as np
from random import random, seed, randint
from PIL import Image
from collections import deque
from scipy import stats

shape = (20160, 35840)

numverts = shape[0] * shape[1]

foreground = np.uint8([7,54,66])
background = np.uint8([253,246,227])

def int_to_rgb(col):
    return np.uint8([
        col // 2**16,
        (col % 2**16) // 2**8,
        col % 2**8
    ])

for s in range(8,20):
    p = 0.5
    seed(s)

    bfs = np.full(numverts, -1, dtype=np.intc)
    adj = np.full((numverts, 4), -1, dtype=np.intc)

    edgedirs = [(0,1), (1,0)]

    for n in range(numverts):
        i = n % shape[0]
        j = n // shape[0]

        print(s, p, 'adding edges at (' + str(j) + ',' + str(i) + ')')

        for d in range(2):
            e1, e2 = edgedirs[d]
            if i - e1 >= 0 and j - e2 >= 0 and random() < p:
                m = (i - e1) + (j - e2) * shape[0]
                adj[n,d] = m
                adj[m,d+2] = n

    mode = -1
    modecount = 0

    for n in range(numverts):
        if bfs[n] == -1:
            color = randint(0, 2**24)
            count = 0

            to_visit = deque([n])

            while len(to_visit) > 0:
                cur = to_visit.pop()
                bfs[cur] = color
                count += 1

                print(s, p, 'exploring cluster of ' + str(n), count)

                for d in range(4):
                    if adj[cur,d] != -1 and bfs[adj[cur,d]] == -1:
                        to_visit.append(adj[cur,d])

            if count > modecount:
                modecount = count
                mode = color

    # clear adjacency list
    adj = 0

    print(s, p, 'rendering allclusters...')

    pixels = np.zeros((*shape,3), dtype=np.uint8)

    for i in range(shape[0]):
        for j in range(shape[1]):
            pixels[i,j] = int_to_rgb(bfs[i + j * shape[0]])

    img = Image.fromarray(pixels, mode='RGB')
    img.save('huge/allclusters_shape=' + str(shape)
            + '_seed=' + str(s) 
            + '_parameter=' + str(p) +'.png')
    img.close()

    print(s, p, 'rendered allclusters!')

    print(s, p, 'rendering biggestcluster...')

    for i in range(shape[0]):
        for j in range(shape[1]):
            if bfs[i + j * shape[0]] == mode:
                pixels[i,j] = foreground
            else:
                pixels[i,j] = background

    img = Image.fromarray(pixels, mode='RGB')
    img.save('huge/biggestcluster_shape=' + str(shape)
            + '_seed=' + str(s) 
            + '_parameter=' + str(p) +'.png')
    img.close()

    print(s, p, 'rendered biggestcluster!')

    # clear pixels
    pixels = 0
