from manim import *
import solarized as sol

class BirthdayProblem(Scene):
    def construct(self):
        tt = TexTemplate()
        tt.add_to_preamble(r'\addtolength{\jot}{-0.35em}')
        tt.add_to_preamble(r'\newcommand{\coloredt}{t}')
        tt.add_to_preamble(r'\newcommand{\coloredn}{n}')
        tt.add_to_preamble(r'\newcommand{\coloredeps}{\varepsilon}')

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
