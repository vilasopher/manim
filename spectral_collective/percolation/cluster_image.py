from manim import *
from union_find import UnionFind
import numpy as np
import random
import solarized as sol

def random_pixels(shape, color_picker):
    return np.uint8(        
        [ [ color_picker(i,j) for j in range(shape[1]) ]
                              for i in range(shape[0]) ] )

def random_convex_color(*args, colorlist=sol.all_colors_rgb):
    n = len(colorlist)
    badones = int(n/2)
    coeffs = np.random.dirichlet(
            np.hstack((np.ones(badones)/100,
                np.ones(n-badones)*2))
        )
    return np.matmul(coeffs, colorlist)

def color_waves(i, j, colorlist=sol.all_colors_rgb):
    n = len(colorlist)
    return colorlist[(i + j) % n]

def random_color_choice(*args, colorlist=sol.all_colors_rgb):
    return random.choice(colorlist)

def completely_random(*args):
    return [random.randint(0,255) for _ in range(3)]

class ClusterImage(ImageMobject):
    def __init__(self, shape, p=0, color_picker=None):

        if color_picker is None:
            color_picker = completely_random

        super().__init__(random_pixels(shape, color_picker))
        self.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        self.height = 8

        self.vertices = [ (i,j) for i in range(shape[0])
                                for j in range(shape[1]) ]
        self.edges = [ ((i, j), (i - e1, j - e2))
                        for i, j in self.vertices
                        for e1, e2 in [(0,1), (1,0)]
                        if i - e1 >= 0 and j - e2 >= 0 ]

        self.coupling = sorted([ (random.random(), e)
                                 for e in self.edges ])

        self.clusters = UnionFind(self.vertices)
        self.update_clusters(p)

    def update_clusters(self, p):
        while len(self.coupling) > 0 and self.coupling[0][0] < p:
            r, e = self.coupling.pop(0)
            self.clusters.union(e[0], e[1])

        for v in self.vertices:
            w = self.clusters.find(v)
            self.pixel_array[v] = self.pixel_array[w]