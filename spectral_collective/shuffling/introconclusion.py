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
            
class WhatIsShuffling(Scene):
    def construct(self):
        bg = RoundedRectangle(
            width=13,
            height=2.5,
            color=sol.BASE01,
            corner_radius=0.05
        ).set_fill(color=sol.BASE2, opacity=1).shift(2.5*DOWN)

        question = MyTex(
            r'\textbf{Question:} what is shuffling?',
            font_size=70
        ).align_to(bg, UP+LEFT).shift(0.25*(DOWN + RIGHT))

        answer1 = MyTex(
           r'\textbullet{} adding randomness to a deck of cards, step-by-step.' 
        ).next_to(question, DOWN).align_to(question, LEFT).shift(0.25*RIGHT)

        answer2 = MyTex(
            r'\textbullet{} after enough steps, the deck is random enough.'
        ).next_to(answer1, DOWN).align_to(answer1, LEFT)

        self.add(bg, question, answer1, answer2)

class DiaconisTable(Scene):
    def construct(self):

        overlay1 = SurroundingRectangle(
            Group(diaconistable[13], diaconistable[14]),
            color=sol.FOREST_GREEN,
            corner_radius=0.1
        ).set_fill(sol.FOREST_GREEN, opacity=0.25)

        overlay2 = SurroundingRectangle(
            Group(diaconistable[16], diaconistable[6]),
            color=sol.FOREST_GREEN,
            corner_radius=0.1
        ).set_fill(sol.FOREST_GREEN, opacity=0.25)

        overlay3 = SurroundingRectangle(
            Group(diaconistable[9], diaconistable[11]),
            color=sol.FOREST_GREEN,
            corner_radius=0.1
        ).set_fill(sol.FOREST_GREEN, opacity=0.25)

        self.play(FadeIn(diaconistable, scale=0.75))
        self.wait()
        self.play(FadeIn(overlay1, scale=1.25))
        self.wait()
        self.play(Transform(overlay1, overlay2))
        self.wait()
        self.play(Transform(overlay1, overlay3))
        self.wait()
        self.play(FadeOut(overlay1, scale=1.25))
        self.wait(5)

class Definition1Transparency(Scene):
    def construct(self):
        def1text = MyMathTex(
            r'\textbf{Definition 1: } \mathrm{d_{TV}}({{\cmuone}}, {{\cmutwo}}) = \frac{1}{2} \sum_{ {{\cx}} \in \Omega} |{{\cmuone}}({{\cx}}) - {{\cmutwo}}({{\cx}})|',
            font_size=55
        ).shift(2.5*UP)
        def1textbox = SurroundingRectangle(
            def1text, buff=MED_SMALL_BUFF, corner_radius=0.1,
            color=sol.BASE01
        ).set_fill(sol.BASE2, opacity=1)
        def1 = Group(def1textbox, def1text)

        self.play(FadeIn(def1))
        self.wait(3)
        self.play(FadeOut(def1))

class Conclusion(Scene):
    def construct(self):
        theirs = MyMathTex(
            r'&\textbf{Bayer-Diaconis:} \\ &\qquad\qquad \tau^\text{riffle}_{{\cn}}({{\ceps}}) = \frac{3}{2} \log_2({{\cn}}) + \Theta_{{\ceps}}(1)',
            font_size=60
        ).shift(2.5*UP + 1.6*LEFT)

        theirproof = MyMathTex(
            r'& \text{\emph{Proof: } analysis of a card trick, and the determination of the idempotents} \\\
                & \text{of a natural commutative subalgebra in the symmetric group algebra.}',
            font_size=40
        ).next_to(theirs, DOWN).shift(0.25*DOWN).align_to(theirs, LEFT)

        ours = MyMathTex(
            r'&\textbf{This Video:} \\ &\qquad\qquad \tau^\text{riffle}_{{\cn}}({{\ceps}}) \leq 2 \log_2({{\cn}}) + \Theta_{{\ceps}}(1)',
            font_size=60
        ).shift(1.5*DOWN).align_to(theirs, LEFT)

        ourproof = MyMathTex(
            r'\text{\emph{Proof:} you just watched it, congratulations!}',
            font_size=65
        ).next_to(ours, DOWN).shift(0.25*DOWN).align_to(theirs, LEFT)

        self.play(FadeIn(theirs, shift=UP))
        self.wait(4)
        self.play(FadeIn(ours, shift=UP))
        self.wait(4)
        self.play(Write(theirproof), run_time=3.5)
        self.wait(2)
        self.play(FadeIn(ourproof, scale=0.75))
        self.wait(5)