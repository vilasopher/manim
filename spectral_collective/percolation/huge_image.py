import numpy as np
from random import random, seed

shape = (5400, 9600)
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
        # TODO: THIS PART


