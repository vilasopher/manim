import numpy.random as ra
import numpy as np
from PIL import Image

RES = (2160, 3840) 
BUFF = 80

data = np.zeros((RES[0]+2, RES[1]+2*BUFF), dtype=np.uint8) # 80 extra columns on each side, an extra row on top and bottom
data[-1] = np.ones(RES[1]+2*BUFF) # bottom row starts with a block
clocks = ra.exponential(1/24, size=RES[1]+2*BUFF-2) # never try the first or last column to avoid runtime errors
pixels = np.full((*RES,3), [253,246,227], dtype=np.uint8)

def hsv_to_rgb(h, s, v):
    if s:
        if h == 1.0: h = 0.0
        i = int(h*6.0); f = h*6.0 - i
        
        w = int(255*( v * (1.0 - s) ))
        q = int(255*( v * (1.0 - s * f) ))
        t = int(255*( v * (1.0 - s * (1.0 - f)) ))
        v = int(255*v)
        
        if i==0: return (v, t, w)
        if i==1: return (q, v, w)
        if i==2: return (w, v, t)
        if i==3: return (w, q, v)
        if i==4: return (t, w, v)
        if i==5: return (v, w, q)
    else: v = int(255*v); return (v, v, v)

def RGB(t):
    return np.uint8(hsv_to_rgb(t % 1, 1, 0.85))

def add_block(c, t):
    r = 0

    while r >= 0:
        if max(data[r,c-1], data[r+1,c], data[r,c+1]) == 1:
            data[r,c] = 1
            if c >= BUFF and c < RES[1] + BUFF and r > 0:
                pixels[r-1,c-BUFF] = RGB(t)

            r = -1
        else: 
            r += 1

time = 0
dt = 1/(60*360)
ticks = np.full(RES[1]+2*BUFF-2, dt)

for frame in range(3000):
    for _ in range(360):
        time += dt
        clocks -= ticks

        order = ra.permutation(np.arange(RES[1]+2*BUFF-2))
        for c in order:
            if clocks[c] <= 0:
                add_block(c+1, time)
                clocks[c] = ra.exponential(1/24)

    img = Image.fromarray(pixels)
    img.save(rf"data/images/frame{frame}.png") 
    print(rf"generated frame {frame}!")