from manim import *
from sharedclasses import *
import solarized as sol

class Intro(Scene):
    def construct(self):
        questions = MyTex(
            r'\textbf{Questions:}',
            font_size=80
        ).shift(3*UP + 4.25*LEFT)

        verify = MyTex(
            r'\textbullet{} how can we verify this table?'
        ).next_to(questions, DOWN).align_to(questions, LEFT).shift(0.5*RIGHT + 0.25*DOWN)

        distance = MyTex(
            r"\textbullet{} what is the ``distance from perfect randomness''?"
        ).next_to(verify, DOWN).align_to(verify, LEFT)

        check1 = MyMathTex(
            r'\checkmark',
            color=sol.FOREST_GREEN
        ).next_to(verify, RIGHT).shift(0.1*UP)

        asterisk = MyMathTex(
            r'{{\checkmark}}^*'
        ).align_to(check1, DOWN + LEFT).set_color_by_tex(r'\checkmark', sol.FOREST_GREEN)

        check2 = MyMathTex(
            r'\checkmark',
            color=sol.FOREST_GREEN
        ).next_to(distance, RIGHT).shift(0.1*UP)

        inthisvideo = MyTex(
            r'\textbf{In this video, we will:}',
            font_size=80
        ).align_to(questions, LEFT).shift(0.25*DOWN)

        twoshuffles = MyTex(
            r'\textbullet{} analyze of the top-to-random and riffle shuffles'
        ).next_to(inthisvideo, DOWN).align_to(distance, LEFT).shift(0.25*DOWN)

        tvdistance = MyTex(
            r'\textbullet{} understand the total variation distance {{q}}'
        ).next_to(twoshuffles, DOWN).align_to(twoshuffles, LEFT).set_color_by_tex(r'q', sol.BASE3)

        coupling = MyTex(
            r'\textbullet{} use the coupling technique to get upper bounds'
        ).next_to(tvdistance, DOWN).align_to(tvdistance, LEFT)

        self.add(questions, verify, distance, check1, check2, asterisk,
                 inthisvideo, twoshuffles, tvdistance, coupling)