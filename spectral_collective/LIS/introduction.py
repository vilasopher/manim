from manim import *
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

        self.wait(5)

        self.play(
            LaggedStart(
                *(Write(i) for i in nums),
                lag_ratio=0.2
            ),
            run_time=2
        )

        # time = 7

        self.wait(3.75)

        # time = 10:45

        question = Tex(
            r"how long is the longest increasing subsequence?",
            color=sol.BASE02,
            font_size=60
        ).shift(2*DOWN)

        self.play(
            FadeIn(question),
            run_time=1.25
        )

        # time = 12
        
        self.wait(4)

        # time = 16

        self.play(
            LaggedStart(
                *(
                    nums[i].animate.shift(DOWN).set_color(sol.RED)
                    for i in subsequence
                ),
                lag_ratio = 0.1
            ),
            run_time=2
        )

        # time = 18

        self.wait(7.5)

        # time = 25:30

        self.play(
            LaggedStart(
                *(Wiggle(nums[i]) for i in subsequence),
                lag_ratio = 0.2
            ),
            run_time=2
        )

        # time = 27:30

        self.wait(1.75)

        # time = 29:15

        self.play(
            nums[4].animate.shift(UP).set_color(sol.BASE03),
            nums[3].animate.shift(DOWN).set_color(sol.RED)
        )

        # time = 30:15

        self.wait()

        # time = 31:15

        self.play(
            nums[3].animate.shift(UP).set_color(sol.BASE03),
            nums[5].animate.shift(DOWN).set_color(sol.RED)
        )

        # time = 32:15

        self.wait(1.25)

        # time = 33:30

        self.play(
            FadeOut(question, shift=DOWN),
            FadeIn(
                Tex(
                    r"length of longest increasing subsequence $=5$",
                    color = sol.BASE02,
                    font_size=60
                ).shift(2*DOWN),
                shift=DOWN
            )
        )

        self.wait(5)

class TheoremStatement(Scene):
    def construct(self):
        tt = TexTemplate()
        tt.add_to_preamble(
            r"""
                \usepackage{amsmath, mathrsfs, mathtools}
            """
        )

        deftext = Tex(
            r"""
            \textbf{Definitions:}
            """,
            font_size=60,
            color=sol.BASE02
        ).shift(3*UP+4.5*LEFT)

        defsigma = Tex(
            r"""
                $\sigma_n =$ a uniformly random permutation of $\{1, \dotsc, n\}$.
            """,
            color = sol.BASE02,
        ).next_to(deftext, DOWN).align_to(deftext, LEFT).shift(0.5*RIGHT)

        defL = MathTex(
            r"""
            {{L(}} \sigma_n {{)}} =
            \text{length of longest increasing subsequence of }
            \sigma_n.
            """,
            color=sol.BASE02
        ).next_to(defsigma, DOWN).align_to(defsigma, LEFT).set_color_by_tex(r"L(", sol.RED).set_color_by_tex(r")", sol.RED)

        theoremword = Tex(
            r"""\textbf{Theorem:}""",
            font_size = 100,
            color = sol.BASE02
        ).align_to(deftext, LEFT).shift(DOWN)

        theoremstatement = MathTex(
            r"""
                { {{L(}} {{\sigma_n}} {{)}} \over {{ \sqrt{n} }} } \xlongrightarrow{\mathbb{P}} {{ 2 }}.
            """,
            font_size = 100,
            color = sol.BASE02,
            tex_template = tt
        ).set_color_by_tex(r"L", sol.RED).set_color_by_tex(r")", sol.RED)

        approximate = MathTex(
            r"""
                {{L(}} {{\sigma_n}} {{)}} \approx {{ 2 }} {{ \sqrt{n} }}
            """,
            font_size = 100,
            color = sol.BASE02
        ).shift(DOWN).set_color_by_tex(r"L", sol.RED).set_color_by_tex(r")", sol.RED)

        theorem = Group(
            theoremword,
            theoremstatement.next_to(theoremword, RIGHT).shift(0.5*RIGHT + 0.2*DOWN)
        )

        hint = MathTex(
            r"""
            (\text{this means } \mathbb{P}\bigg[ \bigg| { {{L(}} \sigma_n {{)}} \over \sqrt{n} } - 2 \bigg| > \epsilon \bigg] \to 0
            \text{ for every } \epsilon > 0)
            """,
            font_size = 30,
            color=sol.BASE01,
            tex_template = tt
        ).set_color_by_tex(r"L", sol.RED).set_color_by_tex(r")", sol.RED).set_color_by_tex(r"0", sol.BASE01)
        hint.next_to(theorem, DOWN).align_to(theorem, RIGHT).shift(0.25*DOWN+1.25*RIGHT)

        self.wait(2)

        self.play(FadeIn(deftext), FadeIn(defsigma))

        # time = 39

        self.wait(4)

        self.play(FadeIn(defL))

        # time = 44

        self.wait(8)

        self.play(FadeIn(approximate))

        # time = 54

        self.wait(2.5)

        self.play(
            Write(theoremword),
            TransformMatchingTex(approximate, theoremstatement)
        )

        self.wait(1)
        
        self.play(
            FadeIn(hint, shift=UP)
        )

        # time = 58:30

        self.wait(3)

        self.play(
            FadeOut(hint, shift=DOWN),
            FadeOut(Group(deftext, defL, defsigma), shift=DOWN),
            theorem.animate.shift(DOWN)
        )

        self.wait(40)

class InThisVideo(Scene):
    def construct(self):
        # have three boxes, and put the future parts of the video in 
        # using some video editor
        pass

class BG(Scene):
    def construct(self):
        pass