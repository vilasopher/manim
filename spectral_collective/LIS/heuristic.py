from manim import *
import solarized as sol
import numpy.random as ra
from functools import partial

class HeuristicStaircase(Scene):
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
                of density $1$
            """,
            color=sol.BASE02,
            font_size=40
        ).shift(2.25*RIGHT + 3.1*UP)

        ar = Arrow(ORIGIN, 3*RIGHT, color=sol.BASE03).next_to(homogtext, DOWN)

        areatext = Tex(
            r"""
                $n$ points \\
                area $n$
            """,
            color=sol.BASE02,
            font_size=40
        ).next_to(ar, DOWN)

        self.every_other_point = [
            Dot(
                homogbox.get_corner(DOWN + LEFT) + 0.02 * (RIGHT+UP)
                + (3-2*0.02) * 1/40 * i * (RIGHT + UP),
                radius = 0.01,
                color = sol.RED
            ) for i in range(41)
        ]

        def point_updater(x, i):
            pt = x.get_center()

            lowercorner = homogbox.get_corner(DOWN+LEFT) + 0.02*(RIGHT+UP)
            uppercorner = homogbox.get_corner(UP+RIGHT) - 0.02*(RIGHT+UP)
            
            if pt[0] < lowercorner[0]:
                x.shift((lowercorner[0] - pt[0])*RIGHT)
            if pt[0] > uppercorner[0]:
                x.shift((uppercorner[0] - pt[0])*RIGHT)
            if pt[1] < lowercorner[1]:
                x.shift((lowercorner[1] - pt[1])*UP)
            if pt[1] > uppercorner[1]:
                x.shift((uppercorner[1] - pt[1])*UP)

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

        for i, p in enumerate(self.every_other_point):
            if i > 0 and i < len(self.every_other_point)-1:
                p.shift((ra.random()*0.2-0.1)*RIGHT
                        + (ra.random()*0.2-0.1)*UP)

        # time = 20:30

        self.play(
            FadeIn(homogbox),
            FadeIn(homogemptybox),
            FadeIn(ar, shift=0.25*RIGHT)
        )

        # time = 21:30
        
        self.wait()

        # time = 22:30

        self.play(FadeIn(homogtext, shift=DOWN))

        # time = 23:30

        self.wait(1.5)

        # time = 25

        self.play(FadeIn(areatext, shift=UP))
        
        # time = 26

        self.wait(20)

        # time = 46

        self.play(
            *(FadeIn(p) for p in self.every_other_point),
            *(FadeIn(hl) for hl in hlines),
            *(FadeIn(vl) for vl in vlines),
            run_time=0.5
        )
        
        self.wait()

        ra.seed(1)

        for _ in range(35):
            self.play(
                *(
                    p.animate.shift(
                        (ra.random()*0.2-0.1)*RIGHT
                        + (ra.random()*0.2-0.1)*UP
                    ) for i, p in enumerate(self.every_other_point)
                    if i > 0 and i < len(self.every_other_point)-1
                )
            )

            self.wait(2)


class HeuristicText(Scene):
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

        pointslength = Tex(
            r"""
                number of points $\approx$ length of path
            """,
            color=sol.BASE02,
            font_size=35
        ).shift(3.95*RIGHT)

        lnapprox = MathTex(
            r"""
                {{L(}} {{\sigma_n}} {{)}} {{\approx}}
            """,
            color = sol.BASE02,
            font_size=50
        ).set_color_by_tex(r"L", sol.RED).set_color_by_tex(r")", sol.RED)

        maxlengthurp = Tex(
            r"""
                \end{center}
                maximal length \\
                of up-right path
                \begin{center}
            """,
            color=sol.BASE02,
            font_size=35
        ).next_to(lnapprox, RIGHT)

        Group(lnapprox, maxlengthurp).next_to(pointslength, 2.375*DOWN).shift(0.35*LEFT)

        twosidelength = MathTex(
            r"""
            = \, 2 \cdot (\text{side length})
            """,
            color = sol.BASE02,
            font_size = 50
        ).next_to(maxlengthurp, DOWN).shift(0.175*RIGHT)

        twosqrtn = MathTex(
            r"""
            {{=}} \, {{ 2 \sqrt{n} }}
            """,
            color = sol.BASE02,
            font_size=50
        ).next_to(twosidelength, DOWN).align_to(twosidelength, LEFT)

        ln2rn = MathTex(
            r"""
            {{L(}} {{\sigma_n}} {{)}} {{\approx}} {{ 2 \sqrt{n} }}
            """,
            color = sol.BASE02,
            font_size=50
        ).next_to(pointslength, 2.75*DOWN).align_to(lnapprox, LEFT).set_color_by_tex(r"L", sol.RED).set_color_by_tex(r")", sol.RED)

        equals = MathTex(
            r"""
            {{=}}
            """,
            color = sol.BASE3,
            font_size=50
        ).next_to(twosqrtn, ORIGIN).align_to(twosqrtn, LEFT)

        minusorn = MathTex(
            r"""
            - \; o(\sqrt{n})
            """,
            color = sol.BASE02,
            font_size = 50
        ).next_to(ln2rn, RIGHT)

        tt = TexTemplate()
        tt.add_to_preamble(
            r"""
                \usepackage{amsmath, mathrsfs, mathtools}
            """
        )

        provable = Tex(
            r"""
            \textbf{Provable using this idea:}
            """,
            font_size = 40,
            color = sol.BASE02
        ).shift(2*DOWN).align_to(pointslength, LEFT)

        problimit = MathTex(
            r"""
            { {{L(}} {{\sigma_n}} {{)}} \over {{\sqrt{n}}} } {{\xlongrightarrow{\mathbb{P}}}} c
            \text{ for some } c
            """,
            color = sol.BASE02,
            font_size = 50,
            tex_template = tt
        ).next_to(provable, DOWN).shift(0.5*RIGHT + 0.1*UP).set_color_by_tex(r"L", sol.RED).set_color_by_tex(r")", sol.RED).align_to(ln2rn, LEFT)

        thmtext = Tex(
            r"""
            \textbf{Theorem:}
            """,
            font_size=40,
            color = sol.BASE02
        ).align_to(provable, UP + LEFT).shift(1.4*RIGHT)

        thmlimit = MathTex(
            r"""
            { {{L_n}} \over {{\sqrt{n}}} } {{\xlongrightarrow{\mathbb{P}}}} 2
            """,
            color = sol.BASE02,
            font_size=40,
            tex_template = tt
        ).align_to(problimit, DOWN + LEFT).set_color_by_tex(r"L_n", sol.RED)

        heuristic = Tex(
            r"""
            \textbf{Heuristic:}
            """,
            color = sol.BASE02,
            font_size = 40
        ).align_to(pointslength, DOWN + LEFT)

        self.add(box, homogbox)

        # time = 31

        self.play(FadeIn(pointslength, shift=0.5*UP))

        # time = 32

        self.wait(10)

        # time = 42

        self.play(FadeIn(lnapprox), FadeIn(maxlengthurp))

        # time = 43

        self.wait(15.5)

        # time = 58:30

        self.play(FadeIn(twosidelength, shift=0.5*UP))

        # time = 59:30

        self.wait(2.5)

        # time = 2

        self.play(FadeIn(twosqrtn, shift=0.5*UP))

        # time = 3

        self.wait(5)

        # time = 8

        self.play(
            TransformMatchingTex(Group(lnapprox, twosqrtn), Group(ln2rn, equals)),
            FadeOut(maxlengthurp),
            FadeOut(twosidelength)
        )
        self.remove(equals)

        # time = 9

        self.wait(6.5)

        # time = 15:30

        self.play(FadeIn(minusorn, shift=LEFT))

        # time = 16:30

        self.wait(13.5)

        # time = 30

        self.play(
            FadeOut(pointslength),
            FadeIn(heuristic),
            Group(ln2rn, minusorn).animate.shift(0.45 * UP)
        )

        # time = 31

        self.wait(25)

        # time = 56

        self.play(
            LaggedStart(
                Write(provable),
                FadeIn(problimit),
                lag_ratio=0.5
            )
        )

        self.wait(30)

        return
        # This stuff was used in an earlier iteration, but I think it's unneccessary
        self.play(
            FadeOut(provable),
            FadeIn(thmtext),
            TransformMatchingTex(problimit, thmlimit)
        )
        self.wait()
        self.play(
            Create(
                SurroundingRectangle(
                    Group(thmtext, thmlimit),
                    color = sol.BASE01
                )
            )
        )
        self.wait()
