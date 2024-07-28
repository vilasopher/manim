from manim import *
import solarized as sol
from numpy.random import random
from sharedclasses import *

class CoinBarChart(Group):
    def __init__(self, p, label=r'Coin', plabel=r'p', color=sol.RED):
        super().__init__()

        self.baseline = Line(color=sol.BASE03, z_index=1, start=1*LEFT, end=1*RIGHT)
        self.Hbar = Rectangle(
            height=p*5, width=0.75, stroke_width=0
        ).set_fill(
            interpolate_color(color, sol.BASE03, 0.2), opacity=1
        ).next_to(
            self.baseline, UP, buff=0
        ).align_to(
            self.baseline, LEFT
        ).shift(
            0.125 * RIGHT
        )
        self.Tbar = Rectangle(
            height=(1-p)*5, width=0.75, stroke_width=0
        ).set_fill(
            interpolate_color(color, sol.BASE3, 0.2), opacity=1
        ).next_to(
            self.baseline, UP, buff=0
        ).align_to(
            self.baseline, RIGHT
        ).shift(
            0.125 * LEFT
        )

        self.Htext = MyTex(
            r'H',
            font_size=60,
        ).next_to(self.Hbar, DOWN)
        self.Ttext = MyTex(
            r'T',
            font_size=60,
            color=sol.BASE03
        ).next_to(self.Tbar, DOWN)

        self.Hplabel = MyMathTex(
            plabel,
            font_size=40
        ).set_color_by_tex(
            plabel, color
        ).next_to(self.Hbar, UP)
        self.Tplabel = MyMathTex(
            r'{{1-}}'+plabel,
            font_size=40
        ).set_color_by_tex(
            plabel,color
        ).next_to(self.Tbar, UP)

        self.coinlabel = MyTex(
            label,
            font_size=60,
            color=color
        ).next_to(self.baseline, UP).shift(4.25*UP)

        self.add(self.baseline, self.Hbar, self.Tbar, self.Htext, self.Ttext, self.Hplabel, self.Tplabel, self.coinlabel)

    def transform(self):
        self.baseline.set_opacity(0)
        self.Tplabel.set_opacity(0)
        self.coinlabel.shift(0.5*UP)
        self.Hbar.shift(0.5*DOWN + 0.5*RIGHT)
        self.Tbar.next_to(self.Hbar, UP, buff=0)
        self.Htext.next_to(self.Hbar, DOWN, buff=0).shift(0.75*UP)
        self.Ttext.next_to(self.Tbar, UP, buff=0).shift(0.75*DOWN)
        self.Hplabel.next_to(self.Hbar, LEFT).align_to(self.Hbar, UP).shift(0.1*UP)

class CoinFlipExample(Scene):
    def construct(self):
        coin1 = CoinBarChart(0.7, label='$\mu_p$', plabel='p', color=sol.MAGENTA).shift(2*LEFT + 2.5*DOWN) #5.75
        coin2 = CoinBarChart(0.4, label='$\mu_q$', plabel='q', color=sol.VIOLET).shift(2*RIGHT + 2.5*DOWN) #3

        definition1 = MyTex(
            r'\textbf{Definition 1}',
            font_size=70
        ).move_to(2.75*UP + 2.75*RIGHT)

        dtv = MyMathTex(
            r'\mathrm{d_{TV}}({{\cmup}}, {{\cmuq}})'
        ).next_to(definition1, DOWN).align_to(definition1, LEFT).shift(0.5*DOWN + 1.75*LEFT)

        formula1a = MyMathTex(
            r'= \frac{1}{2} \sum_{{{\cx}} \in \{H, T\}} |{{\cmup}}({{\cx}}) - {{\cmuq}}({{\cx}})|'
        ).next_to(dtv, DOWN).align_to(dtv, LEFT).shift(0.25*RIGHT)

        formula1b = MyMathTex(
            r'= \frac{1}{2} \big(|{{\cp}} - {{\cq}}| + |(1-{{\cp}}) - (1-{{\cq}})|\big)'
        ).next_to(formula1a, DOWN).align_to(formula1a, LEFT)

        formula1c = MyMathTex(
            r'= {{\cp}}-{{\cq}}'
        ).next_to(formula1b, DOWN).align_to(formula1a, LEFT).shift(0.5*DOWN)

        definition2 = MyTex(
            r'\textbf{Definition 2}',
            font_size=70
        ).move_to(2.75*UP + 2.75*RIGHT)

        formula2a = MyMathTex(
            r'= \max_{{{\cA}} \subseteq \{H,T\}} |{{\cmup}}({{\cA}}) - {{\cmuq}}({{\cA}})|'
        ).next_to(dtv, DOWN).align_to(dtv, LEFT).shift(RIGHT + 0.25*DOWN)

        formula2b = MyMathTex(
            r'\geq |{{\cmup}}({{ \{H\} }}) - {{\cmuq}}({{ \{H\} }})|'
        ).next_to(formula2a, DOWN).align_to(formula2a, LEFT).shift(0.25*DOWN).set_color_by_tex(r'H', sol.YELLOW)

        formula2c = MyMathTex(
            r'= {{\cp}}-{{\cq}}'
        ).next_to(formula2b, DOWN).align_to(formula2a, LEFT).shift(0.625*DOWN)

        definition3 = MyTex(
            r'\textbf{Definition 3}',
            font_size=70
        ).move_to(2.75*UP + 2.75*RIGHT)

        formula3a = MyMathTex(
            r'= \min_{\substack{ {{\cX_p}} \sim {{\cmup}} \\ {{\cX_q}} \sim {{\cmuq}} } } \mathbb{P}[{{\cX_p}} \neq {{\cX_q}}]'
        ).next_to(dtv, DOWN).align_to(dtv, LEFT).shift(0.25*RIGHT + 0.25*DOWN)

        formula3b = MyMathTex(
            r'\leq \P[{{\cX_p}} \neq {{\cX_q}}]'
        ).next_to(formula3a, DOWN).shift(0.5*DOWN).align_to(formula3a, LEFT)

        formula3c = MyMathTex(
            r'\text{(where } & {{\cX_p}} \sim {{\cmup}} \\ \text{ and } & {{\cX_q}} \sim {{\cmuq}} \\ \text{ are } & \text{independent)}',
            font_size=40
        ).next_to(formula3b, RIGHT).shift(0.5*RIGHT)

        formula3d = MyMathTex(
            r'= {{\cp}}(1-{{\cq}}) + (1-{{\cp}}){{\cq}}'
        ).next_to(formula3c, DOWN).align_to(formula3a, LEFT).shift(0.25*DOWN)

        uniformbar = Rectangle(height=5, width=0.5, stroke_width=0)
        uniformbar.set_fill(sol.BASE1, opacity=1).align_to(coin1.Hbar, DOWN).shift(0.5*DOWN+4.35*LEFT)
        topline = Line(ORIGIN, 0.5*RIGHT, color=sol.BASE02).next_to(uniformbar, DOWN, buff=0)
        bottomline = Line(ORIGIN, 0.5*RIGHT, color=sol.BASE02).next_to(uniformbar, UP, buff=0)
        topnum = DecimalNumber(1, color=sol.BASE03, num_decimal_places=0).next_to(uniformbar, UP)
        bottomnum = DecimalNumber(0, color=sol.BASE03, num_decimal_places=0).next_to(uniformbar, DOWN)
        uniformtext = MyTex(
            r'Random Number',
            font_size=60
        ).rotate(PI/2).next_to(uniformbar, LEFT).shift(1.2*LEFT)
        randomnumberBar = Group(uniformbar, topline, bottomline, topnum, bottomnum)

        resultbar = Rectangle(height=5, width=1.75, stroke_width=0.5, color=sol.BASE02, z_index=2)
        resultbar.set_fill(sol.BASE2, opacity=1).align_to(coin1.Hbar, DOWN).shift(0.5*DOWN+2*RIGHT)
        HHbar = Rectangle(height=0.4*5, width=1.75, stroke_width=0.5, color=sol.BASE02, z_index=4)
        HHbar.set_fill(sol.BASE1, opacity=1).next_to(resultbar, DOWN).align_to(resultbar, DOWN)
        HTbar = Rectangle(height=(0.7-0.4)*5, width=1.75, stroke_width=0.5, color=sol.BASE02, z_index=4)
        HTbar.set_fill(sol.BASE1, opacity=1).next_to(HHbar, UP, buff=0)
        TTbar = Rectangle(height=(1-0.7)*5, width=1.75, stroke_width=0.5, color=sol.BASE02, z_index=4)
        TTbar.set_fill(sol.BASE1, opacity=1).next_to(HTbar, UP, buff=0)

        resultTT = MyTex(
            r'({{T}},{{T}})',
            font_size=60
        ).next_to(TTbar, ORIGIN).set_z_index(3).set_color_by_tex(r'T', sol.YELLOW)
        resultHH = MyTex(
            r'({{H}},{{H}})',
            font_size=60
        ).next_to(HHbar, ORIGIN).set_z_index(3).set_color_by_tex(r'H', sol.YELLOW)
        resultHT = MyTex(
            r'({{H}},{{T}})',
            font_size=60
        ).next_to(HTbar, ORIGIN).set_z_index(3).set_color_by_tex(r'H', sol.YELLOW).set_color_by_tex(r'T', sol.YELLOW)

        resultbar.add(resultHH, resultHT, resultTT, HHbar, HTbar, TTbar)
        resulttext = MyMathTex(
            r'({{\cX_p}}, {{\cX_q}})',
            font_size=60,
            z_index=3
        ).next_to(resultbar, UP).shift(0.1*UP)
        resultbar.add(resulttext)

        randomnumber = ValueTracker(0.5)
        randomnumberPoint = Dot(color=sol.BASE03, radius=0.125)
        randomnumberPoint.add_updater(
            lambda x : x.move_to(uniformbar.get_bottom()).shift(5 * randomnumber.get_value() * UP)
        )
        randomnumberText = DecimalNumber(randomnumber.get_value(), color=sol.BASE03)
        randomnumberText.add_updater(
            lambda x : x.next_to(randomnumberPoint, LEFT).set_value(randomnumber.get_value())
        )

        #xpPoint = Group(Dot(color=sol.BASE02, radius=0.12, z_index=5), Dot(color=sol.YELLOW, z_index=10))
        xpPoint = RoundedRectangle(
            width=0.5,
            height=0.25,
            color=sol.BASE02,
            corner_radius=0.125,
            z_index=5
        ).set_fill(
            sol.YELLOW,
            opacity=1
        ).move_to(coin1.Hbar.get_bottom()).shift(5*randomnumber.get_value()*UP)

        xpPoint.add_updater(
            lambda x : x.move_to(coin1.Hbar.get_bottom()).shift(5 * randomnumber.get_value() * UP)
        )

        xpText = MyMathTex(r'{{\cX_p}} = {{H}}' if randomnumber.get_value() < 0.7 else r'{{\cX_p}} = {{T}}').set_color_by_tex(r'H', sol.YELLOW).set_color_by_tex(r'T', sol.YELLOW).next_to(xpPoint, RIGHT)

        #xqPoint = Group(Dot(color=sol.BASE02, radius=0.12, z_index=5), Dot(color=sol.YELLOW, z_index=10))
        xqPoint = RoundedRectangle(
            width=0.5,
            height=0.25,
            color=sol.BASE02,
            corner_radius=0.125,
            z_index=5
        ).set_fill(
            sol.YELLOW,
            opacity=1
        ).move_to(coin2.Hbar.get_bottom()).shift(5*randomnumber.get_value()*UP)
        xqPoint.add_updater(
            lambda x : x.move_to(coin2.Hbar.get_bottom()).shift(5 * randomnumber.get_value() * UP)
        )
        randomnumberLine = Line(randomnumberPoint.get_center(), xpPoint.get_center(), color=sol.BASE02, stroke_width=1, z_index=1)
        randomnumberLine.add_updater(
            lambda x : x.put_start_and_end_on(randomnumberPoint.get_center(), xpPoint.get_center())
        )

        def rerandomize():
            randomnumber.set_value(random())
            self.update_mobjects(0)

        disagreebrace = Brace(HTbar, RIGHT, color=sol.BASE03)
        disagreeprob1 = MyMathTex(
            r'\mathbb{P}[{{\cX_p}} \neq {{\cX_q}}]',
            font_size = 60
        )
        disagreeprob2 = MyMathTex(
            r'={{\cp}}-{{\cq}}',
            font_size=60
        ).next_to(disagreeprob1, DOWN).shift(0.125*RIGHT)
        disagreeprob = Group(disagreeprob1, disagreeprob2)
        disagreeprob.next_to(disagreebrace)

        self.play(
            FadeIn(coin1, shift=RIGHT),
            FadeIn(coin2, shift=LEFT)
        )
        self.play(
            coin1.animate.shift(3.75 * LEFT),
            coin2.animate.shift(5*LEFT)
        )
        self.play(FadeIn(definition1, shift=DOWN))
        self.play(FadeIn(dtv, scale=0.75))
        self.play(FadeIn(formula1a, shift=LEFT))
        self.play(FadeIn(formula1b, shift=LEFT))
        self.play(FadeIn(formula1c, shift=LEFT))
        self.play(FadeOut(formula1a, formula1b, formula1c, scale=0.75))
        self.play(Transform(definition1, definition2))
        self.play(FadeIn(formula2a, shift=LEFT))
        self.play(FadeIn(formula2b, shift=LEFT))
        self.play(FadeIn(formula2c, shift=LEFT))
        self.play(FadeOut(formula2a, formula2b, formula2c, scale=0.75))
        self.play(Transform(definition1, definition3))
        self.play(FadeIn(formula3a, shift=LEFT))
        self.play(FadeIn(formula3b, shift=LEFT))
        self.play(FadeIn(formula3c, scale=0.75))
        self.play(FadeIn(formula3d, shift=LEFT))
        self.play(FadeOut(definition1, dtv, formula3a, formula3b, formula3c, formula3d, shift=3.25*RIGHT),
                  FadeOut(coin2, shift=3.25*RIGHT), coin1.animate.shift(3.25*RIGHT))
        coin2.shift(2.5*RIGHT)
        coin2.transform()
        self.play(coin1.animate.transform())
        self.play(FadeIn(randomnumberBar, scale=0.75))
        self.play(
            FadeIn(randomnumberPoint, scale=0.75),
            FadeIn(randomnumberText, scale=0.75),
            FadeIn(uniformtext, shift=RIGHT)
        )
        self.play(
            FadeIn(xpPoint, scale=0.75),
            Create(randomnumberLine)
        )

        self.play(
            FadeIn(xpText, scale=0.75)
        )

        xpText.add_updater(
            lambda x : x.become(MyMathTex(r'{{\cX_p}} = {{H}}' if randomnumber.get_value() < 0.7 else r'{{\cX_p}} = {{T}}').set_color_by_tex(r'H', sol.YELLOW).set_color_by_tex(r'T', sol.YELLOW)).next_to(xpPoint, RIGHT)
        )
        
        self.wait()
        rerandomize()
        self.wait()
        rerandomize()
        self.wait()
        xpText.clear_updaters()
        randomnumberLine.clear_updaters()

        #TODO: fix lots of this stuff

        self.play(
            FadeIn(coin2, shift=2*LEFT),
            FadeOut(xpText, scale=0.75),
            FadeIn(xqPoint, scale=0.75),
            randomnumberLine.animate.put_start_and_end_on(randomnumberPoint.get_center(), xqPoint.get_center())
        )

        self.play(
            FadeIn(HHbar, HTbar, TTbar, resulttext)
        )

        randomnumberLine.add_updater(
            lambda x : x.put_start_and_end_on(randomnumberPoint.get_center(), randomnumberPoint.get_center() + 6 * RIGHT)
        )

        HHbar.add_updater(
            lambda x : x.set_fill(sol.BASE1, opacity=0 if randomnumber.get_value() < 0.4 else 1)
        )
        HTbar.add_updater(
            lambda x : x.set_fill(sol.BASE1, opacity=0 if randomnumber.get_value() >= 0.4 and randomnumber.get_value() < 0.7 else 1)
        )
        TTbar.add_updater(
            lambda x : x.set_fill(sol.BASE1, opacity=0 if randomnumber.get_value() >= 0.7 else 1)
        )


        self.add(resultbar)
        self.play(randomnumber.animate.set_value(0.9))
        self.play(FadeIn(disagreebrace, disagreeprob))
        self.wait()
        rerandomize()
        self.wait(0.5)
        rerandomize()
        self.wait(0.5)
        rerandomize()
        self.wait(0.5)
        rerandomize()
        self.wait(0.5)
        rerandomize()
        self.wait(0.5)
        rerandomize()
        self.wait(0.5)
        rerandomize()
        self.wait(1)