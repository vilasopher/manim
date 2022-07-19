from manim import *
import solarized as sol
from random import random

class GlitchSingleMobject(Animation):
    def __init__(self, mobject, intensity=0.01, fade=True, inn=False, out=False, **kwargs):
        self.mobject = mobject
        self.intensity = intensity
        self.fade = fade
        self.inn = inn
        self.out = out
        self.innflag = False
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
        if alpha <= 0:
            if self.inn:
                self.mobject.set_opacity(0)
                self.innflag = True
            return

        if alpha > 0 and self.innflag:
            self.mobject.set_opacity(0.5 if self.fade else 1)

        if alpha >= 1:
            self.mobject.restore()

            if self.out:
                self.mobject.set_opacity(0)

            return

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

def GlitchEdges(graph, intensity=0.05, out=False, **kwargs):
    return AnimationGroup(
        AnimationGroup(*(
            GlitchSingleMobject(graph.edges[e], intensity=intensity, out=out, **kwargs)
            for e in graph.edges
        )), AnimationGroup(*(
            GlitchSingleMobject(graph.vertices[v], intensity=0, fade=False, out=out, **kwargs)
            for v in graph.vertices
        ))
    )

def GlitchPercolate(graph, intensity=0.05, p=0.5, **kwargs):
    return AnimationGroup(
        AnimationGroup(*(
            GlitchSingleMobject(
                graph.edges[e],
                intensity=intensity,
                out = False if random() < p else True,
            **kwargs
            ) for e in graph.edges
        )), AnimationGroup(*(
            GlitchSingleMobject(
                graph.vertices[v],
                intensity=0,
                fade=False,
                out=False,
                **kwargs
            ) for v in graph.vertices
        ))
    )

class GlitchNumber(GlitchSingleMobject):
    def __init__(
        self,
        decnum,
        intensity=0.05, 
        lo=0, 
        hi=1, 
        fade=True, 
        inn=False,
        out=False, 
        **kwargs
    ):
        super().__init__(decnum, intensity, fade, inn, out, **kwargs)
        self.lo = lo
        self.hi = hi

    def interpolate(self, alpha):
        super().interpolate(alpha)
        if 0 < alpha and alpha < 1:
            for mobj in self.mobject:
                mobj.set_value(random() * (self.hi - self.lo) + self.lo)

                # TODO: This is buggy, something about set_value resets the mobject
                # and messes things up.

class GlitchNumberTest(Scene):
    def construct(self):
        l = DecimalNumber(0.25, color=sol.BASE03).shift(2 * LEFT)
        m = DecimalNumber(0.5, color=sol.BASE03)
        n = DecimalNumber(0.75, color=sol.BASE03).shift(2 * RIGHT)

        self.wait()

        self.play(
            LaggedStart(
                GlitchNumber(l, run_time=1),
                GlitchNumber(m, run_time=1),
                GlitchNumber(n, run_time=1)
            ), run_time=5
        )

        self.wait()
