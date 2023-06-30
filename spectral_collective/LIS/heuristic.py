from manim import *
import solarized as sol
import numpy.random as ra

class Heuristic(Scene):
    def construct(self):
        box = Square(7.5, color=sol.BASE01).shift(3*LEFT)
        self.add(box)

        homogbox = Square(
            3,
            color=sol.BASE01
        ).set_fill(
            interpolate_color(
                sol.BASE3,
                sol.BASE03,
                PI/25,
            ),
            opacity=1
        ).shift(2*UP + 3*RIGHT)

        self.add(homogbox)