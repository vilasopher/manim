from manim import *
from glitch import *
import solarized as sol
from random import random

class DefinitionExample(Scene):
    def construct(self):
        permutation = [4, 1, 2, 7, 6, 5, 8, 9, 3]
        subsequence = [  1, 2,    4,    6, 7 ]

        nums = [
            DecimalNumber(
                j,
                color=sol.BASE03,
                num_decimal_places=0,
                font_size=120
            ).move_to((i-4)*RIGHT + UP)
            for i,j in enumerate(permutation)
        ]

        # TODO: figure out how to make this look good with glitch.

        self.play(
            LaggedStart(
                *(Write(i) for i in nums),
                lag_ratio=0.2
            )
        )

        self.wait()

        self.play(
            LaggedStart(
                *(
                    nums[i].animate.shift(DOWN).set_color(sol.RED)
                    for i in subsequence
                ),
                lag_ratio = 0.1
            )
        )

        self.wait()

        self.play(
            LaggedStart(
                *(Wiggle(nums[i]) for i in subsequence),
                lag_ratio = 0.2
            )
        )

        self.wait()

        self.play(
            nums[4].animate.shift(UP).set_color(sol.BASE03),
            nums[3].animate.shift(DOWN).set_color(sol.RED)
        )

        self.wait()

        self.play(
            nums[3].animate.shift(UP).set_color(sol.BASE03),
            nums[5].animate.shift(DOWN).set_color(sol.RED)
        )

        self.wait()

        self.play(
            FadeIn(
                Tex(
                    r"length of longest increasing subsequence $=5$",
                    color = sol.BASE02,
                    font_size=60
                ).shift(1.5*DOWN)
            )
        )

        self.wait()

class TheoremStatement(Scene):
    def construct(self):
        tt = TexTemplate()
        tt.add_to_preamble(
            r"""
                \usepackage{amsmath, mathrsfs, mathtools}
            """
        )

        definition = MathTex(
            r"""
                \textbf{Definition: } 
                &{{ L_n }} = \text{ length of longest increasing subsequence} \\
                &\text{in a uniformly random permutation of } \{1, \dotsc, n \}.
            """,
            color = sol.BASE02,
        ).shift(2*UP).set_color_by_tex(r"L_n", sol.RED)

        theoremword = Tex(
            r"""\textbf{Theorem:}""",
            font_size = 100,
            color = sol.BASE02
        ).align_to(definition, LEFT).shift(DOWN + 0.5*RIGHT)

        theoremstatement = MathTex(
            r"""
                { {{ L_n }} \over {{ 2 \sqrt{n} }} } \xlongrightarrow{\mathbb{P}} 1.
            """,
            font_size = 100,
            color = sol.BASE02,
            tex_template = tt
        ).set_color_by_tex(r"L_n", sol.RED)

        approximate = MathTex(
            r"""
                {{ L_n }} \approx {{ 2 \sqrt{n} }}
            """,
            font_size = 100,
            color = sol.BASE02
        ).shift(DOWN).set_color_by_tex(r"L_n", sol.RED)

        theorem = Group(
            theoremword,
            theoremstatement.next_to(theoremword, RIGHT).shift(0.5*RIGHT + 0.2*DOWN)
        )

        self.play(FadeIn(definition))

        self.wait()

        self.play(FadeIn(approximate))

        self.wait()

        self.play(
            Write(theoremword),
            TransformMatchingTex(approximate, theoremstatement)
        )

        self.wait()

class InThisVideo(Scene):
    def construct(self):
        # have three boxes, and put the future parts of the video in 
        # using some video editor
        pass