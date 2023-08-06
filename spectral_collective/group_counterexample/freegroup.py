from manim import *

U = (0,1,0)
D = (0,-1,0)
R = (1,0,0)
L = (-1,0,0)

def inverse(dir):
    if dir == U:
        return D
    if dir == D:
        return U
    if dir == R:
        return L
    if dir == L:
        return R

def hash(l):
    h = 0
    for i, dir in enumerate(l):
        if dir == U:
            h += 1*5**i
        if dir == D:
            h += 2*5**i
        if dir == R:
            h += 3*5**i
        if dir == L:
            h += 4*5**i
    return h

def unhash(h):
    l = []
    while h > 0:
        if h % 5 == 1:
            l.append(U)
        if h % 5 == 2:
            l.append(D)
        if h % 5 == 3:
            l.append(R)
        if h % 5 == 4:
            l.append(L)
        h = h // 5
    return l

def treelayout(hs, scale=4, ratio=0.5):
    layout = {
        h : sum(
            [
                scale*ratio**i*np.array(dir)
                for i, dir in enumerate(unhash(h))
                if i > 0
            ]
        )
        for h in hs
    }
    layout.update({0: ORIGIN})
    return layout

class FreeGroup(Graph):
    def __init__(self, N):
        self.vertices =  [0, 1, 2, 3, 4]
        self.edges = [(0,1), (0,2), (0,3), (0,4)]

        for i in range(N-1):
            for h in self.vertices[-4*(3**i):]:
                l = unhash(h)
                for dir in [U,D,R,L]:
                    if l[-1] != inverse(dir):
                        self.vertices.append(hash(l + [dir]))
                        self.edges.append((h, hash(l + [dir])))
        

        super().__init__(self.vertices, self.edges, layout=treelayout(self.vertices))

    def treeify(self, scale=4, ratio=0.5):
        self.change_layout(treelayout(self.vertices, scale, ratio))

    def gridify(self):
        layout = {
            h : sum([np.array(dir) for dir in unhash(h)])
            for h in self.vertices
        }
        print(layout)
        self.change_layout(layout)
