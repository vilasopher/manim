from manim import *
from math import sin, cos
from random import shuffle, random, seed
from numpy import array

CLEAR = rgba_to_color([0,0,0,0])
seed(0)

def spikeballs(vertices, d, r):
    vs = [(v, i) for v in vertices for i in range(d)]
    es = [(v, (v,i)) for (v,i) in vs]

    vcfg = {(v,i) : {"fill_color": RED} for (v,i) in vs}
    ecfg = {(v, (v,i)) : {"stroke_color": RED} for (v,i) in vs}

    return vs, es, vcfg, ecfg

class AddSpikes(Scene):
    def construct(self):
        n = 10
        vertices = list(range(n))
        d = 3
        r = 0.5

        vs, es, vcfg, ecfg  = spikeballs(vertices, d, r)

        shuffle(vs)

        g = Graph(vs + vertices, es, layout="spring", vertex_config = vcfg, edge_config = ecfg)

        self.play(Create(g))

        for j in range(n * d // 2):
            if vs[2*j][0] != vs[2*j+1][0]:
                self.play(g[vs[2*j]].animate.move_to(g[vs[2*j+1][0]]),
                          g[vs[2*j+1]].animate.move_to(g[vs[2*j][0]]))
                self.play(g.animate.remove_vertices(vs[2*j], vs[2*j+1]),
                          g.animate.add_edges((vs[2*j][0], vs[2*j+1][0])))
                self.play(g.animate.change_layout("spring"))
            else:
                self.play(g[vs[2*j]].animate.move_to(g[vs[2*j+1][0]]),
                          g[vs[2*j+1]].animate.move_to(g[vs[2*j][0]]))
                self.play(g.animate.remove_vertices(vs[2*j], vs[2*j+1]))
                self.play(g.animate.change_layout("spring"))
