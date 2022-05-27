from manim import *
import solarized as sol
from random import random
import networkx as nx

class GlitchSingleMobject(Animation):
    def __init__(self, mobject, out=False, **kwargs):
        self.out = out
        self.mobject = mobject
        super().__init__(self.mobject, **kwargs)

    def begin(self):
        self.mobject.save_state()

        self.colored_mobjects = [
            self.mobject.copy().set(color=c, z_index=-3)
            for c in [RED, GREEN, BLUE]
        ]

        self.mobject.add(*self.colored_mobjects)

        for mobj in self.mobject:
            mobj.set(last_rotation = 0)
            mobj.set(last_shift = np.array([0,0,0]))

        super().begin()

    def finish(self):
        super().finish()
        self.mobject.restore()

    def interpolate(self, alpha):
        for mobj in self.mobject:
            mobj.rotate(- mobj.last_rotation)
            mobj.shift(- mobj.last_shift)

            new_rotation = 0.1 * (random() - 0.5)
            new_shift = 0.1 * ((random() - 0.5) * UP + (random() - 0.5) * RIGHT)

            mobj.shift(new_shift)
            mobj.rotate(new_rotation)

            mobj.set(last_rotation = new_rotation)
            mobj.set(last_shift = new_shift)

    def clean_up_from_scene(self, scene):
        if self.out:
            scene.remove(self.mobject)
        super().clean_up_from_scene(scene)

def Glitch(mobject, out=False, **kwargs):
    return AnimationGroup(*(
        GlitchSingleMobject(mobj, out=out, **kwargs)
        for mobj in mobject
    ))

def GlitchEdges(graph, out=False, **kwargs):
    return AnimationGroup(*(
        GlitchSingleMobject(graph.edges[e], out=out, **kwargs)
        for e in graph.edges
    ))

class Test(Scene):
    def construct(self):
        g = Graph.from_networkx(
            nx.paley_graph(5),
            vertex_config=sol.VERTEX_CONFIG,
            edge_config=sol.EDGE_CONFIG
        )

        self.add(g)
        self.wait()
        self.play(GlitchEdges(g))
        self.wait()
        self.play(GlitchEdges(g, out=True))
        self.wait()
        