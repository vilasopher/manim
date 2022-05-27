from manim import *
import solarized as sol
from random import random

class Glitch(Animation):
    def __init__(self, mobject, out=False, **kwargs):
        self.out = out
        self.mobject = mobject
        super().__init__(self.mobject, **kwargs)

    def begin(self):
        self.colored_mobjects = [
            self.mobject.copy().set(color=c, z_index=-1)
            for c in [RED, GREEN, BLUE]
        ]

        self.mobject.set(last_rotation = 0)
        self.mobject.set(last_shift = np.array([0,0,0]))

        for cm in self.colored_mobjects:
            cm.set(last_rotation = 0)
            cm.set(last_shift = np.array([0,0,0]))

        self.mobject.add(*self.colored_mobjects)

        super().begin()

    def finish(self):
        self.mobject.remove(*self.colored_mobjects)
        super().finish()

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

class Test(Scene):
    def construct(self):
        l = Line([-1,-1,0],[1,1,0],color=sol.BASE03)

        self.wait()
        self.play(Glitch(l))
        self.wait()
        self.play(Glitch(l, out=True))
        self.wait()

        
