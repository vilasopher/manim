from manim import *
import solarized as sol
from random import random

class GlitchSingleMobject(Animation):
    def __init__(self, mobject, intensity=0.03, fade=True, out=False, **kwargs):
        self.mobject = mobject
        self.intensity = intensity
        self.fade = fade
        self.out = out
        super().__init__(self.mobject, **kwargs)

    def begin(self):
        self.mobject.save_state()

        self.colored_mobjects = [
            self.mobject.copy().set(color=c, z_index=-3)
            for c in [sol.RED, sol.GREEN, sol.BLUE]
        ]

        self.mobject.add(*self.colored_mobjects)

        for mobj in self.mobject:
            mobj.set(last_rotation = 0)
            mobj.set(last_shift = np.array([0,0,0]))
            
            if self.fade:
                mobj.set_opacity(0.5)

        super().begin()

    def finish(self):
        super().finish()
        self.mobject.restore()

    def interpolate(self, alpha):
        for mobj in self.mobject:
            mobj.rotate(- mobj.last_rotation)
            mobj.shift(- mobj.last_shift)

            new_rotation = self.intensity * (random() - 0.5)
            new_shift = self.intensity * ((random() - 0.5) * UP + (random() - 0.5) * RIGHT)

            mobj.shift(new_shift)
            mobj.rotate(new_rotation)

            mobj.set(last_rotation = new_rotation)
            mobj.set(last_shift = new_shift)

    def clean_up_from_scene(self, scene):
        if self.out:
            scene.remove(self.mobject)
        super().clean_up_from_scene(scene)

def Glitch(mobject, intensity=0.1, out=False, **kwargs):
    return AnimationGroup(*(
        GlitchSingleMobject(mobj, intensity=intensity, out=out, **kwargs)
        for mobj in mobject
    ))

def GlitchEdges(graph, intensity=0.1, out=False, **kwargs):
    return AnimationGroup(
        AnimationGroup(*(
            GlitchSingleMobject(graph.edges[e], intensity=intensity, out=out, **kwargs)
            for e in graph.edges
        )), AnimationGroup(*(
            GlitchSingleMobject(graph.vertices[v], intensity=0, fade=False, out=out, **kwargs)
            for v in graph.vertices
        ))
    )
