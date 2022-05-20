from manim import *
import solarized as sol
from random import random

class Glitch(Animation):
    def __init__(self, mobject, out=False, **kwargs):
        self.mobject = mobject
        self.out = out

        super().__init__(self.mobject, **kwargs)

    def begin(self):
        self.mobject.add(*[
            self.mobject.copy().set(color=c, z_index=-1)
            for c in [RED, GREEN, BLUE]
        ])

        for mobj in self.mobject:
            mobj.save_state()

        super().begin()

    def finish(self):
        #self.mobject.remove(*self.colored_mobjects)
        self.mobject.become(self.oldmobject)
        super().finish()

    def interpolate(self, alpha):
        for mobj in self.mobject:
            mobj.restore()
            mobj.shift(0.1 * ((random() - 0.5) * UP + (random() - 0.5) * RIGHT))
            mobj.rotate(0.1 * (random() - 0.5))

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

        
