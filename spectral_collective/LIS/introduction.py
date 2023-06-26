from manim import *
from glitch import *
from solarized import *
from random import random

class RandomPermutation(Scene):
    def construct(self):
        d = DecimalNumber(0, color=sol.BASE03)
        self.play(Glitch(d, inn=True))
        self.wait()