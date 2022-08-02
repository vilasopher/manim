from manim import *
from union_find import UnionFind
import numpy as np
import random
import solarized as sol
import networkx as nx

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
    return np.uint8([*(random.randint(0,255) for _ in range(3)), 255])

def HSV_random(*args):
    H = random.random() * 360
    S = np.random.normal(0.6, 0.2) % 1
    V = np.random.normal(0.6, 0.2) % 1
    C = V * S
    X = C * (1 - np.abs(H/60 % 2 - 1))
    m = V - C

    r, g, b = 0, 0, 0

    if H < 60:
        r, g, b = C, X, 0
    elif H < 120:
        r, g, b = X, C, 0
    elif H < 180:
        r, g, b = 0, C, X
    elif H < 240:
        r, g, b = 0, X, C
    elif H < 300:
        r, g, b = X, 0, C
    else:
        r, g, b = C, 0, X

    R = (r+m) * 255
    G = (g+m) * 255
    B = (b+m) * 255

    return np.uint8([R, G, B])

class StaticPercolationImage(ImageMobject):
    def __init__(
        self,
        shape,
        p=0.5,
        color_picker=completely_random,
        onecluster=False,
        oneclustercolor=sol.NODE,
        bgcolor=config.background_color
        ):

        G = nx.Graph()
        G.add_nodes_from(
            [ i + shape[0] * j for i in range(shape[0])
                               for j in range(shape[1]) ]
        )

        for n in G.nodes:
            i = n % shape[0]
            j = n // shape[0]
            for e1, e2 in [(0,1), (1,0)]:
                if i - e1 >= 0 and j - e2 >= 0 and random.random() < p:
                    G.add_edge((i,j), (i-e1, j-e2))
                    print(i,j)

        print('done')

        clusters = nx.connected_components(G)

        bgc = np.uint8(color_to_int_rgba(bgcolor))

        pixels = np.full((*shape, 4), bgc, dtype=np.uint8)
        
        if onecluster:
            bigcluster = max(clusters, key=len)
            occ = np.uint8(color_to_int_rgba(oneclustercolor))

            for v in bigcluster:
                i = n % shape[0]
                j = n // shape[0]
                pixels[(i,j)] = occ
        else:
            for cluster in clusters:
                rc = color_picker()

                for v in cluster:
                    i = n % shape[0]
                    j = n // shape[0]
                    pixels[(i,j)] = rc

        super().__init__(pixels)
        self.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        self.height = 8

class ClusterImage(ImageMobject):
    def __init__(self, shape, p=0, color_picker=HSV_random):
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
        self.set_p(p)

    def set_p(self, p):
        while len(self.coupling) > 0 and self.coupling[0][0] < p:
            r, e = self.coupling.pop(0)
            self.clusters.union(e[0], e[1])

        for v in self.vertices:
            w = self.clusters.find(v)
            self.pixel_array[v] = self.pixel_array[w]

    def get_TL_color(self):
        return self.pixel_array[0,0]

    def highlight_biggest_cluster(self, highlight_color, bg_color=None):
        h = color_to_int_rgba(highlight_color)
        b = None
        if not bg_color is None:
            b = color_to_int_rgba(bg_color)

        for v in self.vertices:
            if self.clusters.find(v) == self.clusters.biggest:
                self.pixel_array[v] = h
            else:
                if not b is None:
                    self.pixel_array[v] = b

class ClusterReveal(ClusterImage):
    def __init__(
        self,
        shape,
        background_image,
        color_to_replace,
        p=0,
        color_picker=HSV_random
    ):
        self.bg = background_image.pixel_array
        self.touched = np.full(shape, False)
        self.c2r = np.uint8([*color_to_replace[:3], 255])
        super().__init__(shape, p, color_picker)

    def set_p(self, p):
        while len(self.coupling) > 0 and self.coupling[0][0] < p:
            r, e = self.coupling.pop(0)
            self.clusters.union(e[0], e[1])

        for v in self.vertices:
            if (self.pixel_array[v] == self.c2r).all():
                self.touched[v] = True

            w  = self.clusters.find(v)

            if self.touched[w]:
                self.pixel_array[v] = self.bg[v]
            else:
                self.pixel_array[v] = self.pixel_array[w]
