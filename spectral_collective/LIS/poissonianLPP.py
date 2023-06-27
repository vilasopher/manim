from manim import *
from glitch import *
import solarized as sol
import random as ra

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
        subsequence = [   1, 2, 3,       6, 7 ]

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
            Dot(color=sol.BASE03, radius=0.1)
            .align_to(box, DOWN + LEFT)
            .shift(0.6 * ((i+1)*RIGHT + j*UP) - 0.1*(RIGHT+UP))
            for i,j in enumerate(permutation)
        ]

        self.play(
            LaggedStart(
                *(
                    AnimationGroup(
                        FadeIn(
                            dots[i],
                            scale=1.5,
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

        LISlines = [
            Line(
                dots[subsequence[i]].get_center(),
                dots[subsequence[i+1]].get_center(),
                color=sol.RED
            )
            for i in range(4)
        ]

        self.play(
            LaggedStart(
                AnimationGroup(
                    dots[subsequence[0]]
                    .animate.set_color(sol.RED),
                    Group(
                        dnums[subsequence[0]],
                        pnums[subsequence[0]],
                        arrows[subsequence[0]]
                    ).animate.set_color(sol.RED),
                    run_time=0.5
                ),
                Succession(
                    *(
                        AnimationGroup(
                            Create(
                                LISlines[i],
                            ),
                            dots[subsequence[i+1]]
                            .animate.set_color(sol.RED),
                            Group(
                                dnums[subsequence[i+1]],
                                pnums[subsequence[i+1]],
                                arrows[subsequence[i+1]]
                            ).animate.set_color(sol.RED)
                        )
                        for i in range(4)
                    ),
                    run_time=2
                ),
                lag_ratio = 0.5
            )
        )

        self.wait()

        self.play(
            FadeOut(
                Group(
                    *pnums,
                    *dnums,
                    *arrows,
                    *xticks,
                    *yticks,
                    *xlabels,
                    *ylabels,
                    *LISlines
                )
            ),
            Group(*dots).animate.set_color(sol.BASE03)
        )

        self.wait()

        self.play(
            Group(*dots, box).animate.shift(3*LEFT)
        )

        self.wait()

        self.play(
            *(
                d.animate.scale(4)
                for d in dots
            )
        )

        self.wait()

        xordering = [
            DecimalNumber(
                i+1,
                num_decimal_places=0,
                color=sol.BASE2,
                font_size=30
            ).next_to(dots[i], ORIGIN).shift(0.25*LEFT)
            for i in range(9)
        ]

        yordering = [
            DecimalNumber(
                j,
                num_decimal_places=0,
                color=sol.BASE2,
                font_size=30
            ).next_to(dots[i], ORIGIN).shift(0.25*RIGHT)
            for i,j in sorted(enumerate(permutation), key = lambda x : x[1])
        ]

        xscanline = Line(
            ORIGIN,
            6*UP,
            color=sol.CYAN,
            z_index=-1
        ).align_to(box, DOWN+LEFT)

        yscanline = Line(
            ORIGIN,
            6*RIGHT,
            color=sol.CYAN,
            z_index=-1
        ).align_to(box, DOWN+LEFT)
        
        self.play(
            xscanline.animate(
                rate_func=rate_functions.linear,
                run_time=3
            ).shift(6*RIGHT),
            LaggedStart(
                *(FadeIn(xo) for xo in xordering),
                lag_ratio=0.5,
                run_time=3
            )
        ) 

        self.wait()

        self.play(
            yscanline.animate(
                rate_func=rate_functions.linear,
                run_time=3
            ).shift(6*UP),
            LaggedStart(
                *(FadeIn(yo) for yo in yordering),
                lag_ratio=0.5,
                run_time=3
            )
        ) 

        self.wait()

        smallarrows = [
            MathTex(
                r"\mapsto",
                color=sol.BASE2,
                font_size=30
            ).next_to(dots[i], ORIGIN)
            for i in range(9)
        ]

        self.play(*(FadeIn(sa, scale=1.5, run_time=0.5) for sa in smallarrows))

        self.wait()


        self.play(
            *(FadeOut(sa) for sa in smallarrows),
            *(FadeOut(xo) for xo in xordering),
            *(FadeOut(yo) for yo in yordering),
            run_time=0.5
        )
        self.play(
            AnimationGroup(*(d.animate.scale(1/2) for d in dots)),
            run_time=0.5
        )

        self.wait()

        #TODO: figure out how to make the points move without messing up

        ra.seed(3)

        self.play(
            *(d.animate.shift((ra.random()-0.5)*UP + (random()-0.5)*RIGHT)
              for d in dots)
        )

        self.play(
            *(d.animate.shift((ra.random()-0.5)*UP + (random()-0.5)*RIGHT)
              for d in dots)
        )

        self.play(
            *(d.animate.shift((ra.random()-0.5)*UP + (random()-0.5)*RIGHT)
              for d in dots)
        )

        self.wait()

class PoissonPointProcess(Scene):
    def construct(self):
        pass