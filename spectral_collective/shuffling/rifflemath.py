from manim import *
import solarized as sol
from sharedclasses import *

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

        self.play(FadeIn(title, scale=0.75))
        self.play(FadeIn(stmt1, shift=LEFT))
        self.play(FadeIn(stmt2, shift=LEFT))
        self.play(
            FadeIn(reform, scale=0.75),
            FadeIn(arrow1, shift=RIGHT, scale=0.75)
        )
        self.play(
            FadeIn(birthdaymobject, scale=0.75)
        )
        self.wait(5)


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
        entropy[0][1].set_color(sol.FOREST_GREEN)
        entropy[0][5].set_color(sol.FOREST_GREEN)

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
    
        self.play(FadeIn(implication, shift=DOWN))
        self.play(FadeIn(unionbound, scale=0.75))
        self.play(
            FadeIn(energy, shift=0.25*LEFT),
            Create(arrow1),
            FadeIn(brace1, shift=0.05*UP)
        )
        self.play(
            FadeIn(entropy, shift=0.25*LEFT),
            Create(arrow2),
            FadeIn(brace2, shift=0.05*UP)
        )
        self.play(FadeIn(dbound1, scale=0.75))
        self.play(TransformMatchingTex(dbound1,dbound2))
        self.remove(dbound1)
        self.add(dbound2)
        self.play(
            FadeOut(dbound2, shift=dbound3.get_right() - dbound2.get_right()),
            FadeIn(dbound3, shift=dbound3.get_right() - dbound2.get_right())
        )
        self.play(
            dbound3.animate.shift(4.75*LEFT),
            FadeIn(tbound, shift=4.75*LEFT),
            FadeIn(arrow3, shift=0.5*DOWN, scale=0.75)
        )
        self.wait(5)
