from manim import *
from freegroup import FreeGroup

class Test(Scene):
    def construct(self):
        f = FreeGroup(3)
        self.add(f)
        self.wait()
        self.play(f.animate.gridify())
        self.wait()

