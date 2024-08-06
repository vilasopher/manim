from manim import *
import solarized as sol
from sharedclasses import *

class DemoTransparencies(Scene):
    def construct(self):
        perf1 = MyTex(
            r'perfectly random',
            font_size=55
        ).shift(RIGHT)
        perf1box = SurroundingRectangle(
            perf1, color=sol.BASE01, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75)

        perf2 = MyTex(
            r'still perfectly random',
            font_size=55
        ).shift(RIGHT + 0.25*DOWN)
        perf2box = SurroundingRectangle(
            perf2, color=sol.BASE01, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75)

        perf3 = MyTex(
            r'perfectly \\ random'
        ).shift(1.5*UP + 5*RIGHT)
        perf3box = SurroundingRectangle(
            perf3, color=sol.BASE01, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75)

        unshuffled = MyTex(
            r'unshuffled'
        ).shift(2.5*DOWN + 5*RIGHT)
        unshuffledbox = SurroundingRectangle(
            unshuffled, color=sol.BASE01, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75)

        #14:17:30
        self.play(FadeIn(perf1box, perf1, scale=0.75), run_time=0.5)
        self.wait()
        self.play(Group(perf1box, perf1).animate.shift(3*DOWN), run_time=0.5)
        self.wait(2)
        #14:22:30
        self.play(
            FadeTransform(perf1box, perf2box),
            FadeTransform(perf1, perf2),
            run_time=0.5
        )
        self.remove(perf1box, perf1)
        self.add(perf2box, perf2)
        self.wait(2.5)
        #14:24:30
        self.play(FadeOut(Group(perf2box, perf2), shift=2*DOWN), run_time=0.5)

        self.wait(6.5)

        #14:31:30
        self.play(
            FadeIn(perf3box, perf3, shift=LEFT),
            FadeIn(unshuffledbox, unshuffled, shift=LEFT),
            run_time=0.5
        )

        self.wait(10) #5.5

        #14:37:30
        self.play(
            FadeOut(perf3box, perf3, shift=RIGHT),
            FadeOut(unshuffledbox, unshuffled, shift=RIGHT),
            run_time=0.5
        )
    
class CouplingTransparencies(Scene):
    def construct(self):
        perf = MyTex(
            r'perfectly \\ random'
        ).shift(UP + 5.5*RIGHT)
        perfbox = SurroundingRectangle(
            perf, color=sol.BASE01, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75)

        unsh = MyTex(
            r'unshuffled'
        ).shift(0.75*DOWN).align_to(perf, LEFT)
        unshbox = SurroundingRectangle(
            unsh, color=sol.BASE01, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75)

        top = MyMathTex(
            r'\xleftarrow{\text{top}}'
        ).shift(5.5*LEFT + 0.25*UP)
        topbox = SurroundingRectangle(
            top, color=sol.BASE01, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75)

        tt.add_to_preamble(r'\DeclareSymbolFont{extraup}{U}{zavm}{m}{n}')
        tt.add_to_preamble(r'\DeclareMathSymbol{\varheart}{\mathalpha}{extraup}{86}')

        seeds = [
            Group(
                SurroundingRectangle(
                    x,
                    color=sol.BASE01,
                    corner_radius=0.1
                ).set_fill(sol.BASE2, opacity=0.85),
                x
            ) for x in [
                MyMathTex(
                    r'\text{Chosen card: } {{\textbf{' + s + r'} \varheart}}'
                ).set_color_by_tex(r'\varheart', sol.CRIMSON_RED).shift(0.25*UP)
                for s in [
                    '4', '5', '2', '4', '2', '6', '4', 'A'
                ]
            ]
        ]

        #15:09:00
        self.add(perfbox, perf, unshbox, unsh)

        self.wait(7.5)

        #15:16:30
        self.play(FadeIn(Group(topbox, top),scale=0.75))

        self.wait(4)

        #15:21:30
        self.play(
            FadeIn(seeds[0], scale=0.75),
            run_time=0.5
        )

        self.wait(1.5)

        #15:23:30
        self.play(
            FadeOut(seeds[0],shift=0.75*UP),
            FadeIn(seeds[1],shift=0.75*UP),
            run_time=0.5
        )

        self.wait(2.5)

        #15:26:30
        self.play(
            FadeOut(seeds[1],shift=0.75*UP),
            FadeIn(seeds[2],shift=0.75*UP),
            run_time=0.5
        )

        self.wait(2)

        #15:29:00
        self.play(
            FadeOut(seeds[2], shift=0.75*UP),
            FadeIn(seeds[3], shift=0.75*UP),
            run_time=0.5
        )

        self.wait(1.5)

        #15:31:00
        self.play(
            FadeOut(seeds[3],shift=0.75*UP),
            FadeIn(seeds[4],shift=0.75*UP),
            run_time=0.5
        )

        self.wait(2)

        #15:33:30
        self.play(
            FadeOut(seeds[4],shift=0.75*UP),
            FadeIn(seeds[5],shift=0.75*UP),
            run_time=0.5
        )

        self.wait(2.5)

        #15:36:30
        self.play(
            FadeOut(seeds[5],shift=0.75*UP),
            FadeIn(seeds[6],shift=0.75*UP),
            run_time=0.5
        )

        self.wait(1.5)

        #15:38:30
        self.play(
            FadeOut(seeds[6],shift=0.75*UP),
            FadeIn(seeds[7],shift=0.75*UP),
            run_time=0.5
        )

        self.wait(5)

class CheckMarkTransparencies(Scene):
    def construct(self):
        checks = [
            Group(
                SurroundingRectangle(
                    x,
                    color=sol.BASE02,
                    corner_radius=0.1
                ).set_fill(GREEN, opacity=1),
                x
            ) for x in [
                MyMathTex(
                    r'\checkmark',
                    color=sol.BASE03
                ).shift(0.25*UP + i * RIGHT)
                for i in [
                    -3.25, -1.9, -0.6, 0.6, 1.95, 3.25
                ]
            ]
        ]

        perf = MyTex(
            r'perfectly \\ random'
        ).shift(UP + 5.5*RIGHT)
        perfbox = SurroundingRectangle(
            perf, color=sol.BASE01, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75)

        unsh = MyTex(
            r'unshuffled'
        ).shift(0.75*DOWN).align_to(perf, LEFT)
        unshbox = SurroundingRectangle(
            unsh, color=sol.BASE01, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75)

        top = MyMathTex(
            r'\xleftarrow{\text{top}}'
        ).shift(5.5*LEFT + 0.25*UP)
        topbox = SurroundingRectangle(
            top, color=sol.BASE01, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75)

        self.add(perfbox, perf, unshbox, unsh, topbox, top)
        self.wait(1)

        #15:43:30
        self.play(FadeIn(checks[0], scale=0.75), run_time=0.5)

        self.wait(3.5)

        #15:47:30
        self.play(FadeIn(checks[1], scale=0.75), run_time=0.5)

        self.wait(4)

        #15:52:00
        self.play(FadeIn(checks[2], scale=0.75), run_time=0.5)

        self.wait(2)

        #15:54:30
        self.play(FadeIn(checks[3], scale=0.75), run_time=0.5)

        self.wait(2.75)

        #15:57:45
        self.play(
            LaggedStart(
                FadeIn(checks[4], scale=0.75),
                FadeIn(checks[5], scale=0.75),
                lag_ratio=0.5
            ),
            run_time=0.75
        )

        self.wait(10)

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

        #15:37:00
        self.play(FadeIn(goal, shift=DOWN))

        self.wait(3)

        #15:41:00
        self.play(FadeIn(item1, shift=0.5*LEFT))

        self.wait(6)

        #15:48:00
        self.play(FadeIn(item2, shift=0.5*LEFT))

        self.wait(12.5)

        #16:01:30
        self.play(FadeIn(reduction, scale=0.75))

        self.wait(7.5)

        #16:10:00
        self.play(FadeIn(ccp, scale=0.75))

        self.wait(3)

        #16:14:00
        self.play(
            Transform(ccpbox, bigccpbox),
            FadeIn(expectation, shift=bigccpbox.get_left() - ccpbox.get_left(), scale=0.25)
        )

        self.wait(10)


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

        fiftytwo = Group(fiftytwobox, fiftytwo1)

        #16:25:30
        self.play(FadeIn(implication, shift=DOWN))

        self.wait(4)

        #16:30:30
        self.play(FadeIn(unionbound, scale=0.75))

        self.wait(11)

        #16:42:30
        self.play(
            FadeIn(brace, shift=0.05*UP),
            Create(arrow),
            FadeIn(probability, shift=0.25*LEFT)
        )

        self.wait(7)

        #16:50:30
        self.play(FadeIn(equality, scale=0.75))

        self.wait(11)

        #17:02:30
        self.play(FadeIn(dbound1, scale=0.75))

        self.wait(14.5)
        
        #17:18:00
        self.play(
            dbound1.animate.shift(0.75*UP + 3.75*LEFT),
            FadeIn(solving1, shift=UP+RIGHT)
        )

        self.wait(3)

        #17:22:00
        self.play(FadeIn(Group(solving2, solving3), scale=0.75))

        self.wait(7)

        #17:30:00
        self.play(FadeOut(dbound1), FadeIn(dbound2))

        self.wait(2)

        #17:33:00
        self.play(
            FadeIn(tbound, shift=LEFT),
            FadeOut(Group(solving1, solving2), scale=0.75),
            FadeOut(solving3, shift=LEFT)
        )

        self.wait(7.5)

        #17:41:30
        self.play(FadeIn(fiftytwo, scale=0.75))

        self.wait(7)

        #17:49:30
        self.play(SpinInFromNothing(fiftytwo2))

        self.wait(10)