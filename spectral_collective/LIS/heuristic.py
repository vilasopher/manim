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
        ).shift(5.25*RIGHT).align_to(box, UP)

        homogemptybox = Square(
            3,
            color=sol.BASE01, 
            z_index=2
        ).next_to(homogbox, ORIGIN)

        homogtext = Tex(
            r"""
                homogeneous \\
                of density $1$ \\
                $\xrightarrow{\hspace*{2cm}}$
            """,
            color=sol.BASE02,
            font_size=40
        ).shift(2.25*RIGHT + 2.25*UP)

        self.add(homogbox, homogemptybox, homogtext)

        # TODO: add text, and the staircase line