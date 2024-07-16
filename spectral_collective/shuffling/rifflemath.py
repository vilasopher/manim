from manim import *
import solarized as sol

tt = TexTemplate()
tt.add_to_preamble(r'\usepackage{amsfonts}')
tt.add_to_preamble(r'\usepackage{amsmath}')
tt.add_to_preamble(r'\usepackage{xcolor}')
tt.add_to_preamble(r'\addtolength{\jot}{-0.35em}')
tt.add_to_preamble(r'\renewcommand{\P}{\mathbb{P}}')
tt.add_to_preamble(r'\newcommand{\coloredt}{t}')
tt.add_to_preamble(r'\newcommand{\coloredn}{n}')
tt.add_to_preamble(r'\newcommand{\coloredeps}{\varepsilon}')

class BirthdayProblem(Scene):
    def construct(self):

        title = MathTex(
            r'&\text{How many shuffles until every} \\\
            &\text{card has a unique number?}',
            color=sol.BASE03,
            font_size=60,
            tex_template=tt
        ).shift(2.65*UP + 1.75*LEFT)

        stmt1 = MathTex(
            r'\bullet &\text{ after } {{\coloredt}} \text{ shuffles, each card has a uniformly} \\\
                &\text{ random binary number with } {{\coloredt}} \text{ bits.}',
            color=sol.BASE03,
            tex_template=tt
        ).next_to(title, DOWN).align_to(title,LEFT).shift(0.5*DOWN+0.5*RIGHT).set_color_by_tex(r'\coloredt',sol.BLUE)

        stmt2 = MathTex(
            r'\bullet &\text{ there are } 2^{{\coloredt}} \text{ such binary numbers.}',
            color=sol.BASE03,
            tex_template=tt
        ).next_to(stmt1, DOWN).align_to(stmt1,LEFT).set_color_by_tex(r'\coloredt',sol.BLUE)

        reform = MathTex(
            r'&\text{If we sample } {{\coloredn}} \text{ items (with replacement) } \\\
            &\text{from } 2^{{\coloredt}} \text{ possibilities, what is the probability } \\\
            &\text{that there is a duplicate somewhere?}',
            color=sol.BASE03,
            font_size=60,
            tex_template=tt
        ).next_to(stmt2, DOWN).align_to(title,LEFT).shift(0.5*DOWN).set_color_by_tex(r'\coloredt',sol.BLUE).set_color_by_tex(r'\coloredn',sol.FOREST_GREEN)

        arrow1 = CurvedDoubleArrow([-6,2,0],[-6,-1.5,0],color=sol.BASE1)

        arrow2 = CurvedArrow([6,1.95,0],[5.75,-1.75,0],color=sol.BASE01, radius=-6)

        birthdaytext = MathTex(
            r'&\textbf{Birthday} \\\ &\textbf{Problem}',
            color=sol.BASE03,
            font_size=70,
            tex_template=tt
        ).shift(2.85*UP+5.05*RIGHT)

        birthdaybox = SurroundingRectangle(
            birthdaytext, color=sol.BASE01, buff=MED_SMALL_BUFF
        ).set_fill(sol.BASE2, opacity=1)

        birthdaymobject = Group(arrow2, birthdaybox, birthdaytext)

        self.add(title, stmt1, stmt2, reform, arrow1, arrow2, birthdaymobject)


class Arithmetic(Scene):
    def construct(self):
        
        implication = MathTex(
            r'\text{there is a duplicate} \Rightarrow \substack{\text{there are two distinct cards, } C_1 \\ \text{and } C_2, \text{ with the same number}}',
            color=sol.BASE03,
            tex_template=tt
        ).shift(3*UP)

        unionbound = MathTex(
            r'\P[\text{there is a duplicate}] \leq \sum_{\substack{C_1, C_2 \\ \text{distinct cards}}} \P\Big[\substack{C_1 \text{ and } C_2 \text{ have}\\ \text{the same number}}\Big]',
            color=sol.BASE03,
            tex_template=tt
        ).shift(UP)

        energy = MathTex(
            r'1 \over 2^{{\coloredt}}',
            color=sol.BASE03,
            tex_template=tt,
            font_size=36
        ).set_color_by_tex(r'\coloredt', sol.BLUE).shift(4.75*RIGHT)

        brace1 = BraceBetweenPoints([2,1,0],[6,1,0], color=sol.BASE1)
        arrow1 = CurvedArrow(4.5*RIGHT, 4*RIGHT+0.5*UP, color=sol.BASE1, radius=-0.5, tip_shape=StealthTip, tip_length=0.1)

        entropy = MathTex(
            r'\binom{n}{2} \leq \frac{n^2}{2}',
            color=sol.BASE03,
            tex_template=tt,
            font_size=36
        ).shift(2.25*RIGHT + 0.7*DOWN)
        entropy[0][1].set_color(sol.FOREST_GREEN)
        entropy[0][5].set_color(sol.FOREST_GREEN)

        brace2 = BraceBetweenPoints([-0.5,0.3,0],[2.2,0.3,0],color=sol.BASE1)
        arrow2 = CurvedArrow([1.35, -0.7, 0], [0.85, -0.2, 0], color=sol.BASE1, radius=-0.5, tip_shape=StealthTip, tip_length=0.1)

        dbound1 = MathTex(
            r'{{ \P[ }} \text{there is a duplicate} {{ ] }} {{ \leq }} { {{\coloredn}}^2 \over 2^{{{\coloredt}} + 1} }',
            color=sol.BASE03,
            tex_template=tt,
        ).set_color_by_tex(r'\coloredt', sol.BLUE).set_color_by_tex(r'\coloredn', sol.FOREST_GREEN).shift(2.5*DOWN)

        dbound2 = MathTex(
            r"{{ \P[ }} \text{decks don't align after } {{\coloredt}} \text{ shuffles} {{ ] }} {{ \leq }} { {{\coloredn}}^2 \over 2^{{{\coloredt}} + 1} }",
            color=sol.BASE03,
            tex_template=tt,
        ).set_color_by_tex(r'\coloredt', sol.BLUE).set_color_by_tex(r'\coloredn', sol.FOREST_GREEN).shift(2.5*DOWN).align_to(dbound1,RIGHT)

        dbound3 = MathTex(
            r'\mathrm{d}^\mathrm{riffle}_{ {{\coloredn}} } ({{\coloredt}}) {{ \leq }} { {{\coloredn}}^2 \over 2^{{{\coloredt}} + 1} }',
            color=sol.BASE03,
            tex_template=tt
        ).set_color_by_tex(r'\coloredt', sol.BLUE).set_color_by_tex(r'\coloredn', sol.FOREST_GREEN).shift(2.5*DOWN).align_to(dbound1,RIGHT)

        tbound = MathTex(
            r'\tau^\mathrm{riffle}_{ {{\coloredn}} } ({{\coloredeps}}) \leq 2 \log_2({{\coloredn}}) + \log_2\Big( { 1 \over {{\coloredeps}} } \Big) - 1',
            color=sol.BASE03,
            tex_template=tt
        ).set_color_by_tex(r'\coloredn', sol.FOREST_GREEN).set_color_by_tex(r'\coloredeps', sol.RED).shift(2.5*DOWN + 2.5*RIGHT)

        arrow3 = CurvedDoubleArrow([-4.45, -2.25, 0], [0.65, -2.25, 0], color=sol.BASE1, radius=-2.65)
    
        self.add(implication, unionbound, energy, brace1, arrow1, entropy, brace2, arrow2, dbound1)

        self.play(TransformMatchingTex(dbound1,dbound2))
        self.remove(dbound1)
        self.add(dbound2)
        self.play(
            FadeOut(dbound2),
            FadeIn(dbound3)
        )
        self.play(
            dbound3.animate.shift(6.25*LEFT),
            FadeIn(tbound, shift=6.25*LEFT)
        )
        self.play(FadeIn(arrow3, shift=0.5*DOWN))
        self.wait(10)
