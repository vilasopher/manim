from manim import *
import solarized as sol
import numpy.random as ra
from functools import partial

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

        self.every_other_point = [
            Dot(
                homogbox.get_corner(DOWN + LEFT) + 0.02 * (RIGHT+UP)
                + (3-2*0.02) * 0.05 * i * (RIGHT + UP),
                radius = 0.01,
                color = sol.RED
            ) for i in range(21)
        ]

        def point_updater(x, i):
            pt = x.get_center()

            lowercorner = homogbox.get_corner(DOWN+LEFT) + 0.02*(RIGHT+UP)
            uppercorner = homogbox.get_corner(UP+RIGHT) - 0.02*(RIGHT+UP)
            
            if pt[0] < lowercorner[0]:
                x.shift((lowercorner[0] - pt[0])*RIGHT)
            if pt[0] > uppercorner[0]:
                x.shift((uppercorner[0] - pt[0])*LEFT)
            if pt[1] < lowercorner[1]:
                x.shift((lowercorner[1] - pt[1])*UP)
            if pt[1] > uppercorner[1]:
                x.shift((uppercorner[0] - pt[1])*DOWN)

            if i > 0:
                pt = x.get_center()
                previous_point = self.every_other_point[i-1].get_center()

                if pt[0] < previous_point[0]:
                    x.shift((previous_point[0] - pt[0])*RIGHT)
                if pt[1] < previous_point[1]:
                    x.shift((previous_point[1] - pt[1])*UP)

        for i, p in enumerate(self.every_other_point):
            if i > 0 and i < len(self.every_other_point)-1:
                p.add_updater(
                    partial(
                        point_updater,
                        i=i
                    )
                )

        hlines = [
            Line(
                ORIGIN, ORIGIN,
                color = sol.RED
            ).add_updater(
                partial(
                    lambda x, i : x.put_start_and_end_on(
                        self.every_other_point[i].get_center() - 0.02*UP,
                        self.every_other_point[i].get_center()[0] * RIGHT
                        + self.every_other_point[i+1].get_center()[1] * UP
                        + 0.02*UP
                    ),
                    i=i
                ),
                call_updater = True
            )
            for i in range(len(self.every_other_point)-1)
        ]

        vlines = [
            Line(
                ORIGIN, ORIGIN,
                color = sol.RED
            ).add_updater(
                partial(
                    lambda x, i : x.put_start_and_end_on(
                        self.every_other_point[i].get_center()[0] * RIGHT
                        + self.every_other_point[i+1].get_center()[1] * UP - 0.02*RIGHT,
                        self.every_other_point[i+1].get_center() + 0.02*RIGHT
                    ),
                    i=i
                ),
                call_updater = True
            )
            for i in range(len(self.every_other_point)-1)
        ]

        self.add(*self.every_other_point, *hlines, *vlines)

        for _ in range(5):
            self.play(
                *(
                    p.animate.shift(
                        (ra.random()*0.2-0.1)*RIGHT
                        + (ra.random()*0.2-0.1)*UP
                    ) for i, p in enumerate(self.every_other_point)
                    if i > 0 and i < len(self.every_other_point)-1
                )
            )

        self.wait()
