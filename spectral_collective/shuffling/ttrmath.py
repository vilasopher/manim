from manim import *
import solarized as sol

def MyTex(text, color=sol.BASE03, **kwargs):
    return MathTex(
        text,
        color=color,
        tex_template=tt,
        **kwargs
    ).set_color_by_tex(
        r'\coloredt', sol.BLUE
    ).set_color_by_tex(
        r'\coloredn', sol.FOREST_GREEN
    ).set_color_by_tex(
        r'\coloredeps', sol.RED
    )

tt = TexTemplate()
tt.add_to_preamble(r'\usepackage{amsfonts}')
tt.add_to_preamble(r'\usepackage{amsmath}')
tt.add_to_preamble(r'\usepackage{xcolor}')
tt.add_to_preamble(r'\addtolength{\jot}{-0.35em}')
tt.add_to_preamble(r'\renewcommand{\P}{\mathbb{P}}')
tt.add_to_preamble(r'\newcommand{\coloredt}{t}')
tt.add_to_preamble(r'\newcommand{\coloredn}{n}')
tt.add_to_preamble(r'\newcommand{\coloredeps}{\varepsilon}')

class Coupon(Scene):
    def construct(self):
        goal = MyTex(
            r"\mathrm{d}^\text{random-to-top}_{ {{\coloredn}} } ({{\coloredt}}) \leq \P[\text{decks don't align after } {{\coloredt}} \text{ shuffles}]",
        ).shift(2.75*UP)

        item1 = MyTex(
            r'\bullet \text{ after a card is chosen, its position is the same in both decks}',
            font_size=45
        ).shift(1.5*UP)

        item2 = MyTex(
            r'\bullet \text{ decks will align after every card is chosen at least once.}',
            font_size=45
        ).shift(0.75*UP).align_to(item1, LEFT)

        reduction = MyTex(
            r'\mathrm{d}^\text{random-to-top}_{ {{\coloredn}} } ({{\coloredt}}) \leq \P[\text{not every card is among the } {{\coloredt}} \text{ choices}]',
        ).shift(0.5*DOWN)

        ccptext = MyTex(
            r'\textbf{Coupon} \\ \textbf{Collector} \\ \textbf{Problem}',
            font_size=60
        ).shift(2.5*DOWN+3.5*RIGHT)

        ccpbox = SurroundingRectangle(
            ccptext, color=sol.BASE01, buff=MED_SMALL_BUFF
        ).set_fill(sol.BASE2, opacity=1)

        ccparrow = CurvedArrow(ccpbox.get_right(), reduction.get_corner(DOWN+RIGHT) + 0.1*(RIGHT+DOWN), color=sol.BASE01)

        ccp = Group(ccparrow, ccpbox, ccptext)
        
        expectation = MyTex(
            r'&\text{expected number of trials } {{\coloredt}} \\\
                &\text{before all } {{\coloredn}} \text{ cards are chosen} \\\
                &\text{is approximately } {{\coloredn}} \log({{\coloredn}})',
            font_size=45,
            color=sol.BASE03
        ).shift(2.5*DOWN + 2.25*LEFT)

        bigccpbox = SurroundingRectangle(
            Group(ccptext, expectation),
            color=sol.BASE01, buff=MED_SMALL_BUFF
        ).set_fill(sol.BASE2, opacity=1)

        self.add(goal, item1, item2, reduction, ccp)

        self.play(
            Transform(ccpbox, bigccpbox),
            FadeIn(expectation, shift=bigccpbox.get_left() - ccpbox.get_left(), scale=0.25)
        )

        self.wait()