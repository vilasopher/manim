from manim import *
import solarized as sol

tt = TexTemplate()
tt.add_to_preamble(r'\usepackage{amsfonts}')
tt.add_to_preamble(r'\usepackage{amsmath}')
tt.add_to_preamble(r'\usepackage{amssymb}')
tt.add_to_preamble(r'\usepackage{xcolor}')
tt.add_to_preamble(r'\addtolength{\jot}{-0.35em}')
tt.add_to_preamble(r'\renewcommand{\P}{\mathbb{P}}')
tt.add_to_preamble(r'\newcommand{\cmuone}{\mu_1}')
tt.add_to_preamble(r'\newcommand{\cmutwo}{\mu_2}')
tt.add_to_preamble(r'\newcommand{\ct}{t}')
tt.add_to_preamble(r'\newcommand{\cn}{n}')
tt.add_to_preamble(r'\newcommand{\ceps}{\varepsilon}')
tt.add_to_preamble(r'\newcommand{\cx}{x}')
tt.add_to_preamble(r'\newcommand{\cX}{X}')
tt.add_to_preamble(r'\newcommand{\cA}{A}')

def MyMathTex(text, color=sol.BASE03, **kwargs):
    return MathTex(
        text,
        color=color,
        tex_template=tt,
        **kwargs
    ).set_color_by_tex(
        r'\cmuone', sol.MAGENTA
    ).set_color_by_tex(
        r'\cmutwo', sol.VIOLET
    ).set_color_by_tex(
        r'\cn', sol.FOREST_GREEN
    ).set_color_by_tex(
        r'\ceps', sol.CRIMSON_RED
    ).set_color_by_tex(
        r'\ct', sol.ROYAL_BLUE
    ).set_color_by_tex(
        r'\cx', sol.YELLOW
    ).set_color_by_tex(
        r'\cA', sol.YELLOW
    ).set_color_by_tex(
        r'\cX', sol.YELLOW
    )

def MyTex(text, color=sol.BASE03, **kwargs):
    return Tex(
        text,
        color=color,
        tex_template=tt,
        **kwargs
    ).set_color_by_tex(
        r'\cmuone', sol.MAGENTA
    ).set_color_by_tex(
        r'\cmutwo', sol.VIOLET
    ).set_color_by_tex(
        r'\cn', sol.FOREST_GREEN
    ).set_color_by_tex(
        r'\ceps', sol.CRIMSON_RED
    ).set_color_by_tex(
        r'\ct', sol.ROYAL_BLUE
    ).set_color_by_tex(
        r'\cx', sol.YELLOW
    ).set_color_by_tex(
        r'\cA', sol.YELLOW
    ).set_color_by_tex(
        r'\cX', sol.YELLOW
    )


class ThreeCardStack(Group):
    def __init__(self, permutation, z_index=1, **kwargs):
        super().__init__(z_index=1, **kwargs)

        cards = [ Rectangle(color=sol.BASE02, height=0.5, width=1.5, stroke_width=2) for i in range(3) ]

        cards[0].set_fill(sol.CRIMSON_RED, opacity=1)
        cards[1].set_fill(sol.ROYAL_BLUE, opacity=1)
        cards[2].set_fill(sol.FOREST_GREEN, opacity=1)

        for i in range(3):
            cards[i].add(MathTex(rf'\mathbf{{{i+1}}}', color=sol.BASE3).next_to(cards[i], ORIGIN))

        a, b, c = (i-1 for i in permutation)

        cards[b].move_to(ORIGIN)
        cards[a].next_to(cards[b], UP, buff=0)
        cards[c].next_to(cards[b], DOWN, buff=0)

        self.occlusion = Square(color=sol.BASE2, stroke_width=0, side_length=1.55)
        self.occlusion.set_fill(sol.BASE2, opacity=0)
        self.opacity=0

        self.add(*cards)
        self.add(self.occlusion)

    def set_percentage(self, percentage):
        self.occlusion.set_fill(sol.BASE2, opacity=1-np.power(percentage,1/4))

diaconistable = Table(
    [[r"\large number of \\ riffle shuffles", r"\huge 1", r"\huge 2", r"\huge 3", r"\huge 4", r"\huge 5", r"\huge 6", r"\huge 7", r"\huge 8", r"\huge 9", r"\huge 10"],
     [r"\large distance from \\ perfect randomness", r"100\%", r"100\%", r"100\%", r"100\%", r"92.4\%", r"61.4\%", r"33.4\%", r"16.7\%", r"8.5\%", r"4.3\%"]],
     include_outer_lines=True,
     include_background_rectangle=True,
     background_rectangle_color=sol.BASE2,
     v_buff=0.25,
     h_buff=0.25,
     line_config={"color" : sol.BASE01},
     element_to_mobject=MyTex,
     element_to_mobject_config={"color" : sol.BASE03, "font_size" : 30}
).shift(2.5*DOWN)