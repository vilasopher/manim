from manim import *
import solarized as sol
from numpy.random import random, seed
from sharedclasses import *

seed(0)

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
        exampletext = MyTex(
            r'\textbf{Example:} \\ coin flips',
            font_size=80
        ).shift(4.5*LEFT + 2*UP)

        pbiggerqtext = MyMathTex(
            r'\text{Assumption:} \\ {{\cp}} \geq {{\cq}} \quad \; \;',
            font_size=70
        ).shift(4.5*LEFT + 1.5*DOWN)

        mupqobfuscation = Rectangle(
            width=10, height=1,
            color=sol.BASE3, stroke_width=0,
            z_index=10
        ).set_fill(sol.BASE3, opacity=1).shift(2.5*UP + 4*RIGHT)

        coin1 = CoinBarChart(0.7, label='$\mu_p$', plabel='p', color=sol.MAGENTA).shift(0*LEFT + 2.5*DOWN) #5.75, 2
        coin2 = CoinBarChart(0.4, label='$\mu_q$', plabel='q', color=sol.VIOLET).shift(4*RIGHT + 2.5*DOWN) #3, 2

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

        formula2bprime = MyMathTex(
            r'\geq |{{\cmup}}({{ \cA }}) - {{\cmuq}}({{ \cA }})|'
        ).next_to(formula2a, DOWN).align_to(formula2a, LEFT).shift(0.25*DOWN)

        formula2extratext = MyTex(
            r'(for any particular event {{$\cA$}})',
            font_size=45
        ).next_to(formula2bprime, DOWN).shift(1.5*RIGHT)

        formula2b = MyMathTex(
            r'\geq |{{\cmup}}({{ \{H\} }}) - {{\cmuq}}({{ \{H\} }})|'
        ).next_to(formula2a, DOWN).align_to(formula2a, LEFT).shift(0.25*DOWN).set_color_by_tex(r'H', sol.YELLOW)

        formula2c = MyMathTex(
            r'= {{\cp}}-{{\cq}}'
        ).next_to(formula2b, DOWN).align_to(formula2a, LEFT).shift(0.625*DOWN)

        optimaltext = MyTex(
            r'so {{$\{ H \}$}} is an \\ optimal event',
            font_size=60
        ).next_to(formula2c, RIGHT).shift(0.5*DOWN+1*RIGHT).set_color_by_tex(r'H', sol.YELLOW)
        optimalbox = SurroundingRectangle(
            optimaltext, color=sol.BASE01, corner_radius=0.1, buff=MED_SMALL_BUFF
        ).set_fill(sol.BASE2, opacity=1)
        optimal = Group(optimalbox, optimaltext)

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

        formula3e = MyMathTex(
            r'> {{\cp}} - {{\cq}}',
            font_size=55
        ).next_to(formula3d, RIGHT).shift(0.05*DOWN + 0.1*RIGHT)

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

        randomnumber = ValueTracker(0.2327)
        randomnumberPoint = Dot(color=sol.BASE03, radius=0.125).move_to(uniformbar.get_bottom()).shift(5*randomnumber.get_value() * UP)
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

        xpText = MyMathTex(r'{{\cX_p}} = {{H}}' if randomnumber.get_value() < 0.7 else r'{{\cX_p}} = {{T}}').set_color_by_tex(r'H', sol.YELLOW).set_color_by_tex(r'T', sol.YELLOW)

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

        table = Table(
            [[r'{{\cp}} {{\cq}}', r'(1-{{\cp}}) {{\cq}}'],
            [r'{{\cp}} (1-{{\cq}})', r'(1-{{\cp}}) (1 - {{\cq}})']],
            row_labels=[MyTex(r'H'), MyTex(r'T')],
            col_labels=[MyTex(r'H'), MyTex(r'T')],
            top_left_entry=VGroup(MyMathTex(r'\cX_q').shift(0.3*(DOWN+LEFT)), MyMathTex(r'\cX_p').shift(0.3*(UP+RIGHT))),
            include_outer_lines=True,
            include_background_rectangle=True,
            background_rectangle_color=sol.BASE2,
            v_buff=0.45,
            h_buff=0.25,
            line_config={"color" : sol.BASE01},
            element_to_mobject=MyMathTex,
            element_to_mobject_config={"color" : sol.BASE03, "font_size" : 30}
        )
        table.add(Line(table.get_cell((1,1)).get_corner(UL), table.get_cell((1,1)).get_corner(DR), color=sol.BASE01))
        table.shift(4*LEFT + 0.5*DOWN)
        tablelabel = Tex(
            r'\textbf{independent} \\ \textbf{coupling}',
            color=sol.YELLOW,
            font_size=60
        ).next_to(table, UP, buff=MED_LARGE_BUFF)
        tablesuboptimal = Tex(
            r'\textbf{\emph{not optimal!}}',
            color=PURE_RED,
            font_size=65
        ).next_to(table, DOWN, buff=MED_LARGE_BUFF)

        disagreebox1 = SurroundingRectangle(
            table.get_cell((2,3)), color=sol.FOREST_GREEN, corner_radius=0.1
        ).set_fill(sol.FOREST_GREEN, opacity=0.25)
        disagreebox2 = SurroundingRectangle(
            table.get_cell((3,2)), color=sol.FOREST_GREEN, corner_radius=0.1
        ).set_fill(sol.FOREST_GREEN, opacity=0.25)

        takeawaytext = MyTex(
            r'\textbf{Takeaway:} good couplings generally arise \\\
                when you can simulate two distributions \\\
                using the same source of randomness.',
            font_size=62,
        ).set_z_index(10)

        takeawaybox = SurroundingRectangle(
            takeawaytext, color=sol.BASE01, buff=MED_SMALL_BUFF, corner_radius=0.1, z_index=9
        ).set_fill(sol.BASE2, opacity=1)

        takeawayobfuscation = Rectangle(
            width=20, height=15, color=sol.BASE3
        ).set_fill(sol.BASE3, opacity=0.80).set_z_index(8)

        takeaway = Group(takeawayobfuscation, takeawaybox, takeawaytext)

        whatisacoupling1 = MyTex(
            r'What is this?',
            font_size=45
        ).next_to(formula3a, DOWN).shift(0.25*DOWN + 0.25*LEFT)
        whatisacouplingarrow = Arrow(
            whatisacoupling1.get_corner(UP+RIGHT) + 0.25*LEFT,
            formula3a[6].get_corner(DOWN + RIGHT) + 0.1*DOWN+0.5*RIGHT,
            color=sol.BASE1
        )
        whatisacoupling2 = MyTex(
            r'A way to flip both coins at once.',
            font_size=45
        ).next_to(whatisacoupling1, DOWN).align_to(whatisacoupling1, LEFT)
        whatisacoupling3 = MyMathTex(
            r'&\text{For instance,} \\ &\text{we could flip them independently.}',
            font_size=45
        ).next_to(whatisacoupling2, DOWN).shift(0.25*DOWN).align_to(whatisacoupling1, LEFT)

        goal = MyTex(
            r'\textbf{Goal:} compute the total variation distance \\\
                between two different (possibly unfair) coin flip \\\
                distributions, using all three definitions.',
            font_size=60
        ).shift(1.5*DOWN)

        self.add(mupqobfuscation)

        self.wait(5)

        #7:51:30
        self.play(FadeIn(exampletext, shift=DOWN+RIGHT))

        self.wait()
        
        #7:53:30
        self.play(Write(goal))

        self.wait(9)

        #8:03:30
        self.play(
            FadeOut(goal, shift=9*LEFT),
            FadeIn(coin1, shift=9*LEFT)
        )

        self.wait(2.5)

        #8:07:00
        self.play(FadeIn(coin2, shift=4*LEFT))

        self.wait(2.5)

        #8:10:30
        self.play(FadeIn(pbiggerqtext, scale=0.75))

        self.wait(3.5)

        #8:15:00
        self.play(FadeOut(mupqobfuscation))

        self.wait(4.5)

        #8:18:30
        self.play(
            FadeOut(exampletext, shift=5.75*LEFT),
            FadeOut(pbiggerqtext, shift=5.75*LEFT),
            coin1.animate.shift(5.75 * LEFT),
            coin2.animate.shift(7*LEFT)
        )

        #8:19:30
        self.play(FadeIn(definition1, shift=DOWN))

        #8:20:30
        self.play(FadeIn(Group(dtv, formula1a), scale=0.75))

        self.wait(2)

        #8:23:30
        self.play(FadeIn(formula1b, shift=LEFT))

        self.wait(5.5)

        #8:29:00
        self.play(FadeIn(formula1c, shift=LEFT))

        self.wait(2.5)

        #8:32:30
        self.play(
            FadeOut(formula1a, formula1b, formula1c, scale=0.75),
            Transform(definition1, definition2),
            run_time=0.5
        )

        #8:33:00
        self.play(FadeIn(formula2a, shift=LEFT))

        self.wait(0.5)

        #8:34:30
        self.play(
            FadeIn(formula2bprime, shift=LEFT),
            FadeIn(formula2extratext, shift=LEFT)
        )

        self.wait(3)

        #8:38:30
        self.play(
            TransformMatchingTex(formula2bprime, formula2b),
            FadeOut(formula2extratext, shift=RIGHT)
        )

        self.wait(10)

        #8:49:30
        self.play(FadeIn(formula2c, shift=LEFT))

        self.wait(5.5)

        #8:56:00
        self.play(FadeIn(optimal, scale=0.75))

        self.wait()

        #9:00:30
        self.play(
            FadeOut(formula2a, formula2b, formula2c, optimal, scale=0.75),
            Transform(definition1, definition3),
            run_time=0.5
        )

        #9:01:00
        self.play(FadeIn(formula3a, shift=LEFT))

        #9:03:00
        self.play(
            FadeIn(whatisacoupling1, scale=0.75),
            GrowArrow(whatisacouplingarrow)
        )

        #9:08:00
        self.play(FadeIn(whatisacoupling2, shift=UP))

        #9:12:00
        self.play(FadeIn(whatisacoupling3, shift=UP))

        #9:15:30
        self.play(
            FadeOut(Group(coin1, coin2), scale=0.75),
            FadeIn(table, shift=UP),
            FadeIn(tablelabel, shift=DOWN)
        )

        #9:28:00 
        self.play(FadeOut(Group(whatisacoupling1, whatisacoupling2, whatisacoupling3, whatisacouplingarrow), scale=0.75))

        #9:29:00
        self.play(FadeIn(formula3b, shift=LEFT))

        #9:30:00
        self.play(FadeIn(formula3c, scale=0.75))

        #9:38:00
        self.play(
            LaggedStart(
                FadeIn(disagreebox1, scale=1.25),
                FadeIn(disagreebox2, scale=1.25)
            ),
            run_time=1
        )

        #9:40:00 
        self.play(
            FadeIn(formula3d, shift=LEFT),
            FadeOut(disagreebox1, scale=1.25),
            FadeOut(disagreebox2, scale=1.25)
        )

        #9:47:00
        self.play(FadeIn(formula3e, scale=0.75))

        #9:52:00
        self.play(FadeIn(tablesuboptimal, shift=UP))

        coin1.shift(5.75*RIGHT)
        coin2.shift(2.5*RIGHT)
        coin2.transform()

        #9:56:30
        self.play(
            FadeOut(definition1, dtv, formula3a, formula3b, formula3c, formula3d, formula3e, shift=5*RIGHT),
            FadeOut(table, tablelabel, tablesuboptimal, shift=5*RIGHT),
            FadeIn(randomnumberBar, shift=5*RIGHT)
        )

        #9:58:30
        self.play(
            FadeIn(randomnumberPoint, scale=0.75),
            FadeIn(randomnumberText, scale=0.75),
            FadeIn(uniformtext, shift=RIGHT)
        )

        for _ in range(3):
            self.play(
                randomnumber.animate.set_value(random()*0.95+0.025),
                run_time=0.5
            )
            self.wait(0.5)
        
        self.play(
            randomnumber.animate.set_value(0.23),
            run_time=0.5
        )
        self.wait(0.5)

        #10:02:30
        self.play(FadeIn(coin1, scale=0.75))

        #10:03:30
        self.play(coin1.animate.transform().shift(2.5*LEFT))

        xpPoint.update()
        xpText.next_to(xpPoint, RIGHT).shift(0.1*RIGHT + 0.05*DOWN)

        #10:04:30
        self.play(
            FadeIn(xpPoint, scale=0.75),
            Create(randomnumberLine),
            FadeIn(xpText, scale=0.75)
        )

        xpText.add_updater(
            lambda x : x.become(MyMathTex(r'{{\cX_p}} = {{H}}' if randomnumber.get_value() < 0.7 else r'{{\cX_p}} = {{T}}').set_color_by_tex(r'H', sol.YELLOW).set_color_by_tex(r'T', sol.YELLOW)).next_to(xpPoint, RIGHT).shift(0.1*RIGHT+0.05*DOWN)
        )

        self.wait(2)

        #10:07:30
        self.play(randomnumber.animate.set_value(0.79))
        
        self.wait(0.5)

        #10:09:00
        for _ in range(6):
            self.play(
                randomnumber.animate.set_value(random()*0.95+0.025),
                run_time=0.5
            )
            self.wait(0.5)
        
        self.play(
            randomnumber.animate.set_value(0.46),
            run_time=0.5
        )
        self.wait(0.5)

        xpText.clear_updaters()
        randomnumberLine.clear_updaters()
        xqPoint.update()

        #10:16:00
        self.play(
            FadeIn(coin2, shift=2*LEFT),
            FadeOut(xpText, scale=0.75),
            FadeIn(xqPoint, scale=0.75),
            randomnumberLine.animate.put_start_and_end_on(randomnumberPoint.get_center(), xqPoint.get_center())
        )

        #10:17:00
        self.play(
            FadeIn(Group(HHbar, HTbar, TTbar, resulttext), shift=LEFT),
            randomnumberLine.animate.put_start_and_end_on(randomnumberPoint.get_center(), randomnumberPoint.get_center() + 6*RIGHT)
        )

        self.add(resultbar)

        #10:18:00
        self.play(
            HTbar.animate.set_fill(sol.BASE1, opacity=0)
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

        randomnumberLine.add_updater(
            lambda x : x.put_start_and_end_on(randomnumberPoint.get_center(), randomnumberPoint.get_center() + 6*RIGHT)
        )

        self.wait(0.5)

        #10:19:30
        for _ in range(41-19):
            self.play(
                randomnumber.animate.set_value(random()*0.95+0.025),
                run_time=0.5
            )
            self.wait(0.5)

        #10:41:30 -- rerandomizations ending up in HH

        for _ in range(46-41):
            self.play(
                randomnumber.animate.set_value(random()*0.35+0.025),
                run_time=0.5
            )
            self.wait(0.5)

        #10:46:30 -- rerandomizations ending up in TT

        for _ in range(51-46):
            self.play(
                randomnumber.animate.set_value(random()*0.25+0.725),
                run_time=0.5
            )
            self.wait(0.5)

        #10:51:30 -- rerandomizations ending up in HT

        for _ in range(56-51):
            self.play(
                randomnumber.animate.set_value(random()*0.25+0.725),
                run_time=0.5
            )
            self.wait(0.5)

        #10:56:30 -- all rerandomizations

        for _ in range(30):
            self.play(
                randomnumber.animate.set_value(random()*0.95 + 0.025),
                run_time=0.5
            )
            self.wait(0.5)

        #11:21:00 -- end


class CoinFlipTransparencies(Scene):
    def construct(self):
        coin1 = CoinBarChart(0.7, label='$\mu_p$', plabel='p', color=sol.MAGENTA).shift(0*LEFT + 2.5*DOWN) #5.75, 2
        resultbar = Rectangle(height=5, width=1.75, stroke_width=0.5, color=sol.BASE02, z_index=2)
        resultbar.set_fill(sol.BASE2, opacity=1).align_to(coin1.Hbar, DOWN).shift(0.5*DOWN+2*RIGHT)
        HHbar = Rectangle(height=0.4*5, width=1.75, stroke_width=0.5, color=sol.BASE02, z_index=4)
        HHbar.set_fill(sol.BASE1, opacity=1).next_to(resultbar, DOWN).align_to(resultbar, DOWN)
        HTbar = Rectangle(height=(0.7-0.4)*5, width=1.75, stroke_width=0.5, color=sol.BASE02, z_index=4)
        HTbar.set_fill(sol.BASE1, opacity=1).next_to(HHbar, UP, buff=0)

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

        takeawaytext = MyTex(
            r'\textbf{Takeaway:} good couplings generally arise \\\
                when you can simulate two distributions \\\
                using the same source of randomness.',
            font_size=62,
        ).set_z_index(10)

        takeawaybox = SurroundingRectangle(
            takeawaytext, color=sol.BASE01, buff=MED_SMALL_BUFF, corner_radius=0.1, z_index=9
        ).set_fill(sol.BASE2, opacity=1)

        takeawayobfuscation = Rectangle(
            width=20, height=15, color=sol.BASE3
        ).set_fill(sol.BASE3, opacity=0.80).set_z_index(8)

        takeaway = Group(takeawayobfuscation, takeawaybox, takeawaytext)

        #10:56:00
        self.play(FadeIn(disagreebrace, disagreeprob))
        
        self.wait(13)

        #11:10:00
        self.play(FadeIn(takeaway, scale=0.75))

        self.wait(15)