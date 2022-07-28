from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from more_graphs import PercolatingGraph, HPGraph, HPGrid
from glitch import Glitch, GlitchEdges, GlitchPercolate
from translucent_box import TranslucentBox
from duality import Duality, convert_edge
import random

# (8,5)   0.95

class DualityScene(Scene):
    def construct(self):
        g = Duality()

        self.wait()

        self.play(FadeIn(g.primal))

        self.wait(5.5)
        
        self.play(*(FadeIn(g.dual[v]) for v in g.dual.vertices))
        
        self.wait(3)

        self.play(*(Create(g.dual.edges[e]) for e in g.dual.edges))

        self.wait(5.5)

        self.play(FadeOut(g.dual))

        self.wait(2)

        self.play(FadeOut(g.primal), FadeIn(g.dual))

        self.wait(2)

        self.play(FadeIn(g.primal))

        self.wait(6)

        edict = { e : True if random.random() < 0.5 else False for e in g.primal.edges }
        elist = list(g.primal.edges)
        random.shuffle(elist)

        for v in g.primal.vertices:
            g.primal[v].set(z_index = 2)

        for v in g.dual.vertices:
            g.dual[v].set(z_index = 2)

        self.play(
            LaggedStart(
                *(
                    AnimationGroup(
                        Glitch(g.primal.edges[e], intensity = 0.03, out = edict[e]),
                        Glitch(g.dual.edges[convert_edge(*e)], intensity = 0.03, out = not edict[e]),
                        run_time = 0.5
                    ) for e in elist
                )
            ), run_time = 8
        )

        self.wait(1.5)

        self.play(FadeOut(g.primal))

        self.wait(0.75)

        self.play(
            GlitchEdges(g.dual),
            run_time=0.25
        )

class PrimalGlitchTransition(Scene):
    def construct(self):
        g = Duality()
        self.play(GlitchEdges(g.primal, intensity=0.03), run_time=0.5)

class DualGlitchTransition(Scene):
    def construct(self):
        g = Duality()
        self.play(GlitchEdges(g.dual, intensity=0.03), run_time=0.5)

class BothGlitchTransition(Scene):
    def construct(self):
        g = Duality()
        self.play(
            GlitchEdges(g.primal, intensity=0.03),
            GlitchEdges(g.dual, intensity=0.03),
            run_time=0.5
        )

class DualPercolateHi(Scene):
    def construct(self):
        g = Duality()
        g.percolate(0.75)
        self.play(GlitchEdges(g.dual, intensity=0.03), run_time=0.25)
        self.wait(2.5)
        self.play(GlitchEdges(g.dual, intensity=0.03), run_time=0.25)

class DualPercolateLo(Scene):
    def construct(self):
        g = Duality()
        g.percolate(0.25)
        self.play(GlitchEdges(g.dual, intensity=0.03), run_time=0.25)
        self.wait(1.75)
        self.play(FadeIn(g.primal))
        self.wait(1.75)
        self.play(
            GlitchEdges(g.primal, intensity=0.03),
            GlitchEdges(g.dual, intensity=0.03), 
            run_time=0.25
        )

class PercolateBoth(Scene):
    def construct(self):
        g = Duality()
        g.percolate()
        self.play(
            GlitchEdges(g.primal, intensity=0.03),
            GlitchEdges(g.dual, intensity=0.03), 
            run_time=0.25
        )
        self.wait(2.75)
        self.play(FadeOut(g.dual))
        self.wait(0.25)
        self.play(
            GlitchEdges(g.primal, intensity=0.03),
            run_time=0.25
        )

class PercolatePrimal(Scene):
    def construct(self):
        g = Duality()
        g.percolate()

        self.play(GlitchEdges(g.primal, intensity=0.03), run_time=0.25)
        self.wait(1.75)
        self.play(
            FadeIn(g.dual),
            FadeOut(g.primal)
        )
        self.wait(0.25)
        self.play(
            GlitchEdges(g.dual, intensity=0.03),
            run_time=0.25
        )

class PercolateDual(Scene):
    def construct(self):
        g = Duality()
        g.percolate()

        self.play(GlitchEdges(g.dual, intensity=0.03), run_time=0.25)
        self.wait(1.75)
        self.play(FadeIn(g.primal))
        self.wait(0.25)
        self.play(
            GlitchEdges(g.primal, intensity=0.03),
            GlitchEdges(g.dual, intensity=0.03),
            run_time=0.25
        )

class PercolateBothLonger1(Scene):
    def construct(self):
        g = Duality()
        g.percolate()

        self.play(
            GlitchEdges(g.primal, intensity=0.03),
            GlitchEdges(g.dual, intensity=0.03),
            run_time=0.25
        )

        self.wait(3)

        self.play(
            GlitchEdges(g.primal, intensity=0.03),
            GlitchEdges(g.dual, intensity=0.03),
            run_time=0.25
        )

class PercolateBothLonger2(PercolateBothLonger1):
    pass

class GlitchZoomOutA(MovingCameraScene):
    def construct(self):
        g = Duality((24, 14), 0.95)

        self.play(
            self.camera.frame.animate.scale(0.95/0.3),
            GlitchEdges(g.primal, intensity=0.03),
            GlitchEdges(g.dual, intensity=0.03),
            run_time = 0.5
        )


class GlitchZoomOutB(MovingCameraScene):
    def construct(self):
        g = Duality((24, 14), 0.3)

        self.camera.frame.save_state()
        self.camera.frame.scale(0.3/0.95)

        self.play(
            self.camera.frame.animate.restore(),
            GlitchEdges(g.primal, intensity=0.04),
            GlitchEdges(g.dual, intensity=0.04),
            run_time = 0.5
        )
