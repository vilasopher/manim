from manim import *
import solarized as sol
from sharedclasses import *

class Transparencies(Scene):
    def construct(self):
        #TODO
        pass

class Coupon(Scene):
    def construct(self):
        goal = MyMathTex(
            r"\mathrm{d}^\text{random-to-top}_{ {{\cn}} } ({{\ct}}) \leq \P[\text{decks don't align after } {{\ct}} \text{ shuffles}]",
        ).shift(2.75*UP)

        item1 = MyMathTex(
            r'\bullet \text{ after a card is chosen, its position is the same in both decks}',
            font_size=45
        ).shift(1.5*UP)

        item2 = MyMathTex(
            r'\bullet \text{ decks will align after every card is chosen at least once.}',
            font_size=45
        ).shift(0.75*UP).align_to(item1, LEFT)

        reduction = MyMathTex(
            r'\mathrm{d}^\text{random-to-top}_{ {{\cn}} } ({{\ct}}) \leq \P[\text{not every card is among the } {{\ct}} \text{ choices}]',
        ).shift(0.5*DOWN)

        ccptext = MyMathTex(
            r'\textbf{Coupon} \\ \textbf{Collector} \\ \textbf{Problem}',
            font_size=60
        ).shift(2.5*DOWN+3.5*RIGHT)

        ccpbox = SurroundingRectangle(
            ccptext, color=sol.BASE01, buff=MED_SMALL_BUFF, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=1)

        ccparrow = CurvedArrow(ccpbox.get_right(), reduction.get_corner(DOWN+RIGHT) + 0.1*(RIGHT+DOWN), color=sol.BASE01)

        ccp = Group(ccparrow, ccpbox, ccptext)
        
        expectation = MyMathTex(
            r'&\text{expected number of trials } {{\ct}} \\\
                &\text{before all } {{\cn}} \text{ cards are chosen} \\\
                &\text{is approximately } {{\cn}} \log({{\cn}})',
            font_size=45
        ).shift(2.5*DOWN + 2.25*LEFT)

        bigccpbox = SurroundingRectangle(
            Group(ccptext, expectation),
            color=sol.BASE01, buff=MED_SMALL_BUFF, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=1)

        self.play(FadeIn(goal, shift=DOWN))
        self.play(FadeIn(item1, shift=0.5*LEFT))
        self.play(FadeIn(item2, shift=0.5*LEFT))
        self.play(FadeIn(reduction, scale=0.75))
        self.play(FadeIn(ccp, scale=0.75))

        self.play(
            Transform(ccpbox, bigccpbox),
            FadeIn(expectation, shift=bigccpbox.get_left() - ccpbox.get_left(), scale=0.25)
        )

        self.wait(5)


class Analysis(Scene):
    def construct(self):
        implication = MyMathTex(
            r'\text{not every card has been chosen} \Rightarrow \substack{ \text{there is some card } C \\ \text{ which has not been chosen.}}'
        ).shift(3*UP)

        unionbound = MyMathTex(
            r'\P\big[\substack{ \text{not every card has been} \\ \text{chosen after } t \text{ shuffles}} \big] \leq \sum_{\text{card } C} \P\big[\substack{C \text{ has not been} \\ \text{chosen after } t \text{ shuffles}} \big]'
        ).shift(1.5*UP)
        unionbound[0][32].set_color(sol.BLUE)
        unionbound[0][71].set_color(sol.BLUE)

        brace = Brace(Group(unionbound[0][47], unionbound[0][-1]), DOWN, color=sol.BASE1).shift(0.1*UP)
        arrow = CurvedArrow(brace.get_bottom() + 0.5*(DOWN + RIGHT) + 0.025*DOWN, brace.get_bottom() + 0.025*DOWN, tip_shape=StealthTip, tip_length=0.1, color=sol.BASE1, radius=-0.5)
        probability = MyMathTex(
            r'\bigg({ {{\cn}} - 1 \over {{\cn}} }\bigg)^{{\ct}}',
            font_size=36
        ).next_to(arrow, RIGHT).shift(0.25*DOWN+0.1*LEFT)

        equality = MyMathTex(
            r'= {{\cn}} \bigg( 1 - {1 \over {{\cn}}} \bigg)^{{\ct}}'
        ).align_to(unionbound[0][40], LEFT)

        dbound1 = MyMathTex(
            r'\mathrm{d}^\text{random-to-top}_{{\cn}}({{\ct}}) \leq {{\cn}} e^{- {{\ct}} / {{\cn}}}'
        ).shift(2.5*DOWN)

        dbound2 = MyMathTex(
            r'\mathrm{d}^\text{top-to-random}_{{\cn}}({{\ct}}) \leq {{\cn}} e^{- {{\ct}} / {{\cn}}}'
        ).shift(1.75*DOWN + 3.75*LEFT)

        solving2 = MyMathTex(
            r'\Leftrightarrow',
            font_size=45
        ).shift(2.25*DOWN + 4*RIGHT)

        solving1 = MyMathTex(
            r'{{\cn}} e^{-{{\ct}} / {{\cn}} } \leq {{\ceps}}',
            font_size=45
        ).next_to(solving2, UP)

        solving3 = MyMathTex(
            r'\textstyle {{\ct}} \leq {{\cn}} \log({{\cn}}) + {{\cn}} \log \big({1 \over {{\ceps}} } \big)',
            font_size=45
        ).next_to(solving2, DOWN)

        tbound = MyMathTex(
            r'\textstyle \tau^\text{top-to-random}_{{\cn}}({{\ceps}}) \leq {{\cn}} \log({{\cn}}) + {{\cn}} \log\big({1 \over {{\ceps}}}\big)'
        ).shift(2.85*DOWN).align_to(dbound2, LEFT)

        fiftytwo1 = MyMathTex(
            r'\tau^\text{top-to-random}_{ {{52}} }({{50\%}})',
            font_size=40
        ).shift(1.75*DOWN + 4.5*RIGHT).set_color_by_tex(r'52', sol.GREEN).set_color_by_tex(r'50', sol.RED)

        fiftytwo2 = MyMathTex(
            r'\leq 242',
            font_size=80
        ).next_to(fiftytwo1, DOWN).shift(0.1*UP)

        fiftytwobox = SurroundingRectangle(
            Group(fiftytwo1, fiftytwo2), color=sol.BASE01, buff=SMALL_BUFF, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=1)

        fiftytwo = Group(fiftytwobox, fiftytwo1, fiftytwo2)
             

        self.play(FadeIn(implication, shift=DOWN))

        self.play(FadeIn(unionbound, scale=0.75))

        self.play(
            FadeIn(brace, shift=0.05*UP),
            Create(arrow),
            FadeIn(probability, shift=0.25*LEFT)
        )

        self.play(FadeIn(equality, scale=0.75))

        self.play(FadeIn(dbound1, scale=0.75))
        
        self.play(
            dbound1.animate.shift(0.75*UP + 3.75*LEFT),
            FadeIn(solving1, shift=UP+RIGHT)
        )
        self.play(FadeIn(Group(solving2, solving3), scale=0.75))

        self.play(FadeOut(dbound1), FadeIn(dbound2))
        self.play(
            FadeIn(tbound, shift=LEFT),
            FadeOut(Group(solving1, solving2), scale=0.75),
            FadeOut(solving3, shift=LEFT)
        )

        self.play(FadeIn(fiftytwo, scale=0.75))

        self.wait(5)