from manim import *
import solarized as sol
from sharedclasses import *

class ModelTransparencies(Scene):
    def construct(self):
        #TODO
        box = RoundedRectangle(
            color=sol.BASE01, width=13, height=3, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75).shift(2*DOWN)

        cut = MyTex(
            r'\textbf{Cut the deck}',
            font_size=55
        ).align_to(box, UP+LEFT).shift(0.25*(DOWN+RIGHT))

        riffle = MyTex(
            r'\textbf{Riffle the halves together}',
            font_size=55
        ).align_to(box, UP+RIGHT).shift(0.25*(DOWN+LEFT))

        binomial = MyMathTex(
            r'&\text{size of the top half} \\ &\;\; \sim \mathrm{Binomial}({{\cn}}, \tfrac{1}{2})'
        ).next_to(cut, DOWN).align_to(cut, LEFT).shift(0.25*RIGHT)

        binomialexplanation = MyMathTex(
            r'(\text{\emph{pretty close to }} {{\cn}} / 2)'
        ).next_to(binomial, DOWN).align_to(cut, LEFT)

        choice = MyTex(
            r'place a card down from a half \\ with probability proporitional to the \\ number of cards left in that half',
            font_size=43
        ).next_to(riffle, DOWN).align_to(riffle, RIGHT).shift(0.25*LEFT)

        uniform = MyTex(
            r'choose a uniformly random \\ interleaving of the two halves',
        ).next_to(cut, DOWN).align_to(riffle, RIGHT).shift(0.25*LEFT)

        reverse = MyTex(
            r'\textbf{Reverse shuffle:} put a uniformly random subset on top.'
        ).align_to(box, DOWN).shift(0.15*UP)

        #18:19:00
        self.play(FadeIn(box, scale=0.75))

        self.wait()
        
        #18:21:00
        self.play(FadeIn(cut, shift=0.5*(UP+LEFT)))
        
        self.wait(1.5)

        #18:23:30
        self.play(FadeIn(riffle, shift=0.5*(UP+RIGHT)))

        self.wait(6.5)

        #18:31:00
        self.play(FadeIn(binomial, scale=0.75))

        self.wait(11)

        #18:43:00
        self.play(FadeIn(binomialexplanation, scale=0.75))

        self.wait(18)

        #19:02:00
        self.play(FadeIn(choice, scale=0.75))

        self.wait(11.5)

        #19:14:30
        self.play(FadeTransform(choice, uniform))

        self.remove(choice)
        self.add(uniform)

        self.wait(8.5)

        #19:24:00
        self.play(
            FadeOut(binomialexplanation, scale=0.25),
            FadeIn(reverse, scale=0.5, shift=3*LEFT)
        )

        self.wait(10) #7.5

        #19:32:30
        self.play(
            FadeOut(box, cut, riffle, binomial, uniform, reverse, scale=0.75),
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
        ).shift(5.5*LEFT)
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
                    r'\text{Chosen subset: } {{\textbf{' + r'} \varheart}},{{\textbf{'.join(s) + r'} \varheart}}'
                ).set_color_by_tex(r'\varheart', sol.CRIMSON_RED)
                for s in [
                    ['A','2','6'],
                    ['2','3'],
                    ['A','3','4','6'],
                    ['A','5','6'],
                    ['A','3','5']
                ]
            ]
        ]

        self.add(perfbox, perf, unshbox, unsh, topbox, top)

        self.wait()

        #20:07:00
        self.play(FadeIn(seeds[0], scale=0.75), run_time=0.5)

        self.wait(4.5)

        #20:12:00
        self.play(
            FadeOut(seeds[0], shift=0.75*UP),
            FadeIn(seeds[1], shift=0.75*UP),
            run_time=0.5
        )
        
        self.wait(4.5)

        #20:17:00
        self.play(
            FadeOut(seeds[1], shift=0.75*UP),
            FadeIn(seeds[2], shift=0.75*UP),
            run_time=0.5
        )

        self.wait(5.5)

        #20:23:00
        self.play(
            FadeOut(seeds[2], shift=0.75*UP),
            FadeIn(seeds[3], shift=0.75*UP),
            run_time=0.5
        )

        self.wait(6)

        #20:29:30
        self.play(
            FadeOut(seeds[3], shift=0.75*UP),
            FadeIn(seeds[4], shift=0.75*UP),
            run_time=0.5
        )

        self.wait(10)

class NumberTransparencies(Scene):
    def construct(self):
        perf = MyTex(
            r'perfectly \\ random'
        ).shift(UP + 5.5*RIGHT)
        perfbox = SurroundingRectangle(
            perf, color=sol.BASE01, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75)

        unsh = MyTex(
            r'unshuffled'
        ).shift(DOWN).align_to(perf, LEFT)
        unshbox = SurroundingRectangle(
            unsh, color=sol.BASE01, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75)

        top = MyMathTex(
            r'\xleftarrow{\text{top}}'
        ).shift(5.5*LEFT + 0.25*LEFT)
        topbox = SurroundingRectangle(
            top, color=sol.BASE01, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=0.75)

        numbers1 = [
            Group(
                SurroundingRectangle(
                    x,
                    color=sol.BASE02,
                    corner_radius=0.1
                ).set_fill(sol.BASE2, opacity=0.85),
                x
            ) for x in [
                MyMathTex(
                    num,
                    font_size=60
                ).shift(pos * RIGHT + 0.25*LEFT).set_z_index(5)
                for (num,pos) in [
                    (r'\texttt{0}', -3.2),
                    (r'\texttt{1}', -1.9),
                    (r'\texttt{2}', -0.5),
                    (r'\texttt{2}', 0.9),
                    (r'\texttt{3}', 2.3),
                    (r'\texttt{3}', 3.7)
                ]
            ]
        ]

        numbers2 = [
            Group(
                SurroundingRectangle(
                    x,
                    color=sol.BASE02,
                    corner_radius=0.1
                ).set_fill(GREEN if b else RED, opacity=1),
                x
            ) for (x,b) in [
                (MyMathTex(
                    num,
                    font_size=60
                ).shift(pos * RIGHT + 0.75*LEFT + 0.25*DOWN), b)
                for (num,pos, b) in [
                    (r'\texttt{1}', -3.2, True),
                    (r'\texttt{3}', -1.9, False),
                    (r'\texttt{3}', -0.5, False),
                    (r'\texttt{4}', 0.9, True),
                    (r'\texttt{6}', 2.3, False),
                    (r'\texttt{6}', 3.7, False)
                ]
            ]
        ]

        numbers3 = [
            Group(
                SurroundingRectangle(
                    x,
                    color=sol.BASE02,
                    corner_radius=0.1
                ).set_fill(GREEN if b else RED, opacity=1),
                x
            ) for (x,b) in [
                (MyMathTex(
                    num,
                    font_size=60
                ).shift(pos * RIGHT + 0.25*LEFT + 0.25*DOWN), b)
                for (num,pos, b) in [
                    (r'\texttt{1}', -3.2, True),
                    (r'\texttt{3}', -1.9, False),
                    (r'\texttt{3}', -0.5, False),
                    (r'\texttt{6}', 0.9, True),
                    (r'\texttt{12}', 2.3, True),
                    (r'\texttt{14}', 3.7, True)
                ]
            ]
        ]

        numbers4 = [
            Group(
                SurroundingRectangle(
                    x,
                    color=sol.BASE02,
                    corner_radius=0.1
                ).set_fill(GREEN if b else RED, opacity=1),
                x
            ) for (x,b) in [
                (MyMathTex(
                    num,
                    font_size=60
                ).shift(pos * RIGHT + 0.25*LEFT + 0.25*DOWN), b)
                for (num,pos, b) in [
                    (r'\texttt{3}', -3.2, True),
                    (r'\texttt{6}', -1.9, True),
                    (r'\texttt{12}', -0.5, True),
                    (r'\texttt{17}', 0.9, True),
                    (r'\texttt{19}', 2.3, True),
                    (r'\texttt{30}', 3.7, True)
                ]
            ]
        ]
        
        self.add(perfbox, perf, unshbox, unsh, topbox, top)

        self.wait(25)
        
        #21:01:00
        self.play(
            LaggedStart(
                *(FadeIn(n, scale=0.75) for n in numbers1),
                lag_ratio=1/3
            ),
            run_time=2
        )

        self.wait(1)

        #21:04:00
        self.play(
            LaggedStart(
                *(Wiggle(n) for n in numbers1),
                lag_ratio=1/6
            ),
            run_time=3
        )

        self.wait(9)

        #21:16:00
        self.play(
            LaggedStart(
                numbers1[0][0].animate.set_fill(GREEN, opacity=1),
                numbers1[1][0].animate.set_fill(GREEN, opacity=1),
                lag_ratio=0.5
            ),
            run_time=1.5
        )

        self.wait(5.5)

        #21:23:00
        self.play(
            LaggedStart(
                AnimationGroup(
                    numbers1[2][0].animate.set_fill(RED, opacity=1),
                    numbers1[3][0].animate.set_fill(RED, opacity=1)
                ),
                AnimationGroup(
                    numbers1[4][0].animate.set_fill(RED, opacity=1),
                    numbers1[5][0].animate.set_fill(RED, opacity=1)
                ),
                lag_ratio=0.5
            ),
            run_time=1.5
        )

        self.wait(5.5)

        #21:30:00
        self.play(
            *(FadeOut(n, scale=0.75) for n in numbers1),
            run_time=0.5
        )

        self.wait(2.25)

        #21:32:45
        self.play(
            *(FadeIn(n, scale=0.75) for n in numbers2),
            run_time=0.25
        )
        self.wait(0.5)

        #21:33:30
        self.play(
            *(FadeOut(n, scale=0.75) for n in numbers2),
            run_time=0.25
        )

        self.wait(1.75)

        #21:35:30
        self.play(
            *(FadeIn(n, scale=0.75) for n in numbers3),
            run_time=0.25
        )
        self.wait(0.25)

        #21:36:00
        self.play(
            *(FadeOut(n, scale=0.75) for n in numbers3),
            run_time=0.25
        )

        self.wait(1.75)

        #21:38:00
        self.play(
            *(FadeIn(n, scale=0.75) for n in numbers4),
            run_time=0.5
        )

        self.wait(10)

class BirthdayProblem(Scene):
    def construct(self):

        title = MyMathTex(
            r'&\text{How many shuffles until every} \\\
            &\text{card has a unique number?}',
            font_size=60,
        ).shift(2.65*UP + 1.75*LEFT)

        stmt1 = MyMathTex(
            r'\bullet &\text{ after } {{\ct}} \text{ shuffles, each card has a uniformly} \\\
                &\text{ random binary number with } {{\ct}} \text{ bits.}'
        ).next_to(title, DOWN).align_to(title,LEFT).shift(0.5*DOWN+0.5*RIGHT)

        stmt2 = MyMathTex(
            r'\bullet &\text{ there are } 2^{{\ct}} \text{ such binary nubers.}'
        ).next_to(stmt1, DOWN).align_to(stmt1,LEFT)

        reform = MyMathTex(
            r'&\text{If we sample } {{\cn}} \text{ items (with replacement) } \\\
            &\text{from } 2^{{\ct}} \text{ possibilities, what is the probability } \\\
            &\text{that there is a duplicate somewhere?}',
            font_size=60,
        ).next_to(stmt2, DOWN).align_to(title,LEFT).shift(0.5*DOWN)

        arrow1 = CurvedDoubleArrow([-6,2,0],[-6,-1.5,0],color=sol.BASE1)

        arrow2 = CurvedArrow([6,1.95,0],[5.75,-1.75,0],color=sol.BASE01, radius=-6)

        birthdaytext = MyMathTex(
            r'&\textbf{Birthday} \\\ &\textbf{Problem}',
            font_size=70,
        ).shift(2.85*UP+5.05*RIGHT)

        birthdaybox = SurroundingRectangle(
            birthdaytext, color=sol.BASE01, buff=MED_SMALL_BUFF, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=1)

        birthdaymobject = Group(arrow2, birthdaybox, birthdaytext)

        #21:12:30
        self.play(FadeIn(title, scale=0.75))

        self.wait(1.5)

        #21:15:00
        self.play(FadeIn(stmt1, shift=LEFT))

        self.wait(6)

        #21:22:00
        self.play(FadeIn(stmt2, shift=LEFT))

        self.wait(3.5)

        #21:26:30
        self.play(
            FadeIn(reform, scale=0.75),
            FadeIn(arrow1, shift=RIGHT, scale=0.75)
        )

        self.wait(8)

        #21:35:30
        self.play(
            FadeIn(birthdaymobject, scale=0.75)
        )

        self.wait(10)


class Arithmetic(Scene):
    def construct(self):
        
        implication = MyMathTex(
            r'\text{there is a duplicate} \Rightarrow \substack{\text{there are two distinct cards, } C_1 \\ \text{and } C_2, \text{ with the same number}}'
        ).shift(3*UP)

        unionbound = MyMathTex(
            r'\P[\text{there is a duplicate}] \leq \sum_{\substack{C_1, C_2 \\ \text{distinct cards}}} \P\Big[\substack{C_1 \text{ and } C_2 \text{ have}\\ \text{the same number}}\Big]'
        ).shift(UP)

        energy = MyMathTex(
            r'1 \over 2^{{\ct}}',
            font_size=36
        ).shift(4.75*RIGHT)

        brace1 = BraceBetweenPoints([2,1,0],[6,1,0], color=sol.BASE1)
        arrow1 = CurvedArrow(4.5*RIGHT, 4*RIGHT+0.5*UP, color=sol.BASE1, radius=-0.5, tip_shape=StealthTip, tip_length=0.1)

        entropy = MyMathTex(
            r'\binom{n}{2} \leq \frac{n^2}{2}',
            font_size=36
        ).shift(2.25*RIGHT + 0.7*DOWN)
        entropy[0][1].set_color(sol.GREEN)
        entropy[0][5].set_color(sol.GREEN)

        brace2 = BraceBetweenPoints([-0.5,0.3,0],[2.2,0.3,0],color=sol.BASE1)
        arrow2 = CurvedArrow([1.35, -0.7, 0], [0.85, -0.2, 0], color=sol.BASE1, radius=-0.5, tip_shape=StealthTip, tip_length=0.1)

        dbound1 = MyMathTex(
            r'{{ \P[ }} \text{there is a duplicate} {{ \text{ after } }} {{\ct}} {{ \text{ shuffles} }} {{ ] }} {{ \leq }} { {{\cn}}^2 \over 2^{{{\ct}} + 1} }'
        ).shift(2.5*DOWN)

        dbound2 = MyMathTex(
            r"{{ \P[ }} \text{decks don't align} {{ \text{ after } }} {{\ct}} {{ \text{ shuffles} }} {{ ] }} {{ \leq }} { {{\cn}}^2 \over 2^{{{\ct}} + 1} }"
        ).shift(2.5*DOWN).align_to(dbound1,RIGHT)

        dbound3 = MyMathTex(
            r'\mathrm{d}^\text{riffle}_{ {{\cn}} } ({{\ct}}) {{ \leq }} { {{\cn}}^2 \over 2^{{{\ct}} + 1} }'
        ).shift(2.5*DOWN)

        tbound = MyMathTex(
            r'\textstyle \tau^\text{riffle}_{ {{\cn}} } ({{\ceps}}) \leq 2 \log_2({{\cn}}) + \log_2\big( { 1 \over {{\ceps}} } \big) - 1'
        ).shift(2.5*DOWN + 2.5*RIGHT)

        #arrow3 = CurvedDoubleArrow([-4.45, -2.25, 0], [0.65, -2.25, 0], color=sol.BASE1, radius=-2.65)
        arrow3 = CubicBezier(
            [-4.45, -2.15, 0],
            [-4.45, -0.5, 0],
            [0.75, -0.45, 0],
            [0.75, -2.1, 0],
            color=sol.BASE1
        )
        arrow3.add(ArrowTriangleFilledTip(color=sol.BASE1, width=0.2, length=0.2).rotate(PI/2).move_to(arrow3.get_start()))
        arrow3.add(ArrowTriangleFilledTip(color=sol.BASE1, width=0.2, length=0.2).rotate(PI/2).move_to(arrow3.get_end()))

        fiftytwo1 = MyMathTex(r'\tau^\text{riffle}_{ {{ 52 }} } ( {{ 50\% }} )', font_size=60).set_color_by_tex(r'52', sol.GREEN).set_color_by_tex(r'50', sol.RED)
        fiftytwo2 = MyMathTex(r'{{\leq}} 2 \log_2( {{52}} ) + \log_2 \bigg( { 1 \over {{0.5}} } \bigg) - 1', font_size=60).set_color_by_tex(r'52', sol.GREEN).set_color_by_tex(r'0.5', sol.RED).next_to(fiftytwo1, RIGHT)
        fiftytwo3 = MyMathTex(r'{{\leq}} 11.40088...', font_size=60)
        fiftytwo4 = MyMathTex(r'{{\leq}} 12', font_size=60)

        Group(fiftytwo1, fiftytwo2).move_to(ORIGIN).shift(UP)
        fiftytwo3.next_to(fiftytwo1, RIGHT)
        fiftytwo4.next_to(fiftytwo1, RIGHT)

        overlay1 = SurroundingRectangle(
            Group(diaconistable[13], diaconistable[14]),
            color=sol.FOREST_GREEN,
            corner_radius=0.1
        ).set_fill(sol.FOREST_GREEN, opacity=0.25)

        justUBtext = MyTex(
            r'just an upper bound...',
            font_size=55
        ).shift(2.5*RIGHT + 0.25*DOWN)

        justUBarrow = Arrow(justUBtext.get_top(), 2*UP, color=sol.BASE1)

        #21:43:30
        self.play(FadeIn(implication, shift=DOWN))

        self.wait(4.5)

        #21:49:00
        self.play(FadeIn(unionbound, scale=0.75))

        self.wait(15)

        #22:05:00
        self.play(
            FadeIn(energy, shift=0.25*LEFT),
            Create(arrow1),
            FadeIn(brace1, shift=0.05*UP)
        )

        self.wait(3)

        #22:09:00
        self.play(
            FadeIn(entropy, shift=0.25*LEFT),
            Create(arrow2),
            FadeIn(brace2, shift=0.05*UP)
        )

        self.wait(5)

        #21:15:00
        self.play(FadeIn(dbound1, scale=0.75))

        self.wait(6.5)

        #22:22:30
        self.play(TransformMatchingTex(dbound1,dbound2))

        self.remove(dbound1)
        self.add(dbound2)

        self.wait(6)

        #22:29:30
        self.play(
            FadeOut(dbound2, shift=dbound3.get_right() - dbound2.get_right()),
            FadeIn(dbound3, shift=dbound3.get_right() - dbound2.get_right())
        )

        self.wait(5.5)

        #22:36:00
        self.play(
            dbound3.animate.shift(4.75*LEFT),
            FadeIn(tbound, shift=4.75*LEFT),
            FadeIn(arrow3, shift=0.5*DOWN, scale=0.75)
        )

        self.wait(9)

        #22:46:00
        self.play(
            tbound.animate.move_to(2.5*UP),
            FadeOut(Group(implication, unionbound, energy, arrow1, brace1, entropy, arrow2, brace2, dbound3, arrow3), shift=5*UP + 2.5*LEFT)
        )

        self.wait(0.5)

        #22:47:30
        self.play(FadeIn(fiftytwo1, scale=0.75))

        self.wait(0.5)

        #22:49:00
        self.play(FadeIn(fiftytwo2, shift=LEFT))

        self.wait(4.5)

        #22:54:30
        self.play(
            FadeOut(fiftytwo2),
            FadeIn(fiftytwo3)
        )

        self.wait()

        #22:56:30
        self.play(
            FadeOut(fiftytwo3),
            FadeIn(fiftytwo4)
        )

        self.wait(1.5)

        #22:59:00
        self.play(FadeIn(diaconistable, shift=UP))

        #23:00:00
        self.play(FadeIn(overlay1, scale=1.25))

        self.wait(3.5)

        #23:04:30
        self.play(
            FadeIn(justUBtext, scale=0.75),
            GrowArrow(justUBarrow)
        )

        self.wait(10)
