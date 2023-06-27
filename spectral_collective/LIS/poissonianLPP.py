from manim import *
from glitch import *
import solarized as sol
from random import random

class Why(Scene):
    def construct(self):
        text = Tex(
            r"""
                Why is $L_n \approx 2 \sqrt{n}$?
            """,
            color = sol.BASE02,
            font_size = 100
        )
        heur = Tex(
            r"""
            (a heuristic argument)
            """,
            color = sol.BASE02,
            font_size = 60
        ).next_to(text, DOWN)

        self.play(FadeIn(text, shift=DOWN))
        self.wait()
        self.play(FadeIn(heur))
        self.wait()
    
class FunctionGraph(Scene):
    def construct(self):
        permutation = [4, 1, 2, 7, 6, 5, 8, 9, 3]
        subsequence = [  1, 2,    4,    6, 7 ]

        pnums = [
            DecimalNumber(
                j,
                color=sol.BASE03,
                num_decimal_places=0,
                font_size=60
            ).move_to(0.5*(i-4)*RIGHT)
            for i,j in enumerate(permutation)
        ]

        dnums = [
            DecimalNumber(
                i+1,
                color=sol.BASE03,
                num_decimal_places=0,
                font_size=60
            ).move_to(0.5*(i-4)*RIGHT + UP)
            for i in range(9)
        ]

        arrows = [
            MathTex(
                r"\mapsto",
                font_size=60,
                color=sol.BASE02
            ).rotate(-PI/2).move_to(0.5*(i-4)*RIGHT)
            for i in range(9)
        ]

        self.play(*(FadeIn(j) for j in pnums))

        self.wait()

        self.play(
            *(j.animate.shift(DOWN) for j in pnums),
            *(FadeIn(a, shift = 0.5*DOWN) for a in arrows),
            *(FadeIn(i) for i in dnums)
        )

        self.wait()

        box = Square(
            side_length=6,
            color=sol.BASE01
        ).shift(3*RIGHT)

        xticks = [
            Line(ORIGIN, 0.5*UP, color=sol.BASE01)
            .align_to(box, DOWN + LEFT)
            .shift(0.6 * (i+1) * RIGHT + 0.25 * DOWN)
            for i in range(9)
        ]

        xlabels = [
            DecimalNumber(
                i+1,
                num_decimal_places=0,
                color=sol.BASE01,
                font_size=30
            ).next_to(xticks[i], DOWN)
            for i in range(9)
        ]

        yticks = [
            Line(ORIGIN, 0.5*RIGHT, color=sol.BASE01)
            .align_to(box, DOWN + LEFT)
            .shift(0.6 * (i+1) * UP + 0.25 * LEFT)
            for i in range(9)
        ]

        ylabels = [
            DecimalNumber(
                i+1,
                num_decimal_places=0,
                color=sol.BASE01,
                font_size=30
            ).next_to(yticks[i], LEFT)
            for i in range(9)
        ]

        self.play(
            LaggedStart(
                Group(
                    *pnums,
                    *dnums,
                    *arrows
                ).animate.shift(4*LEFT),
                Create(box),
                AnimationGroup(
                    *(FadeIn(xt) for xt in xticks),
                    *(FadeIn(yt) for yt in yticks)
                ),
                AnimationGroup(
                    *(FadeIn(xl) for xl in xlabels),
                    *(FadeIn(yl) for yl in ylabels)
                ),
                lag_ratio = 0.2
            )
        )

        self.wait()

        dots = [
            Dot(color=sol.BASE03, radius=0.2)
            .align_to(box, DOWN + LEFT)
            .shift(0.6 * ((i+1)*RIGHT + j*UP) - 0.2*(RIGHT+UP))
            for i,j in enumerate(permutation)
        ]

        self.play(
            LaggedStart(
                *(
                    AnimationGroup(
                        FadeIn(
                            dots[i],
                            scale=1.5,
                            rate_function=rate_functions.rush_from,
                            run_time=0.5
                        ),
                        Wiggle(Group(dnums[i], pnums[i], arrows[i]), run_time=0.5)
                    )
                    for i in range(9)
                ),
                lag_ratio=0.75
            )
        )

        self.wait()
