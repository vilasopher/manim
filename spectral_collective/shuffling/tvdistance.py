from manim import *
import solarized as sol
from numpy.random import random

tt = TexTemplate()
tt.add_to_preamble(r'\usepackage{amsfonts}')
tt.add_to_preamble(r'\usepackage{amsmath}')
tt.add_to_preamble(r'\usepackage{xcolor}')
tt.add_to_preamble(r'\addtolength{\jot}{-0.35em}')
tt.add_to_preamble(r'\renewcommand{\P}{\mathbb{P}}')
tt.add_to_preamble(r'\newcommand{\coloredt}{t}')
tt.add_to_preamble(r'\newcommand{\coloredn}{n}')
tt.add_to_preamble(r'\newcommand{\coloredeps}{\varepsilon}')


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

def MyMathTex(text, color=sol.BASE03, **kwargs):
    return MathTex(
        text,
        color=color,
        tex_template=tt,
        **kwargs
    ).set_color_by_tex(
        r'\mu_1', sol.CRIMSON_RED
    ).set_color_by_tex(
        r'\mu_2', sol.ROYAL_BLUE
    ).set_color_by_tex(
        r'\coloredeps', sol.FOREST_GREEN
    )

def MyTex(text, color=sol.BASE03, **kwargs):
    return Tex(
        text,
        color=color,
        tex_template=tt,
        **kwargs
    ).set_color_by_tex(
        r'\mu_1', sol.CRIMSON_RED
    ).set_color_by_tex(
        r'\mu_2', sol.ROYAL_BLUE
    ).set_color_by_tex(
        r'\coloredeps', sol.FOREST_GREEN
    )

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

class DiaconisTable(Scene):
    def construct(self):
        self.add(diaconistable)

class Equivalence(Scene):
    def construct(self):
        text1 = MyTex(
            r'How close are we to perfect randomness?',
            font_size=60
        ).shift(2*UP)

        text2 = MyTex(
            r'What is the \emph{distance} between the uniform distribution \\ and the distribution of arrangements after {{$\coloredt$}} shuffles?',
            font_size=50
        ).shift(2*DOWN)

        arrow = DoubleArrow([0,1.5,0],[0,-1.3,0],color=sol.BASE1)

        self.play(FadeIn(text1, scale=0.75))
        self.play(Write(text2))
        self.play(FadeIn(arrow, scale=0.75))


class Notations(Scene):
    def construct(self):
        notation = MyTex(
            r'\textbf{Notation}',
            font_size=70
        ).shift(3.25*UP + 5*LEFT)

        muomega = MyTex(
            r'$\mu$ denotes a \emph{probability distribution} on an \emph{outcome space} $\Omega$'
        ).shift(2.25*UP)

        omegalabeltext = MyTex(
            r'e.g. the set of all possible \\ arrangements of a deck of cards',
            font_size=40
        ).shift(3.25*RIGHT + 1.15*UP)

        omegalabelbox = SurroundingRectangle(
            omegalabeltext, color=sol.BASE01, corner_radius=0.05
        ).set_fill(sol.BASE2, opacity=1)

        omegalabelline = Line(
            muomega.get_corner(DOWN+RIGHT) + 0.05*DOWN + 0.5*LEFT,
            muomega.get_corner(DOWN+RIGHT) + 0.05*DOWN + 3.6*LEFT,
            color=sol.BASE01
        )

        omegalabelcurve = Line(
            omegalabelbox.get_top() + RIGHT,
            omegalabelline.get_center(),
            color=sol.BASE01
        )

        omegalabel = Group(omegalabelcurve, omegalabelline, omegalabelbox, omegalabeltext)


        mulabeltext = MyTex(
            r'determines how likely each \\ possible outcome in $\Omega$ is',
            font_size=40
        ).shift(3*LEFT + 1.15*UP)

        mulabelbox = SurroundingRectangle(
            mulabeltext, color=sol.BASE01, corner_radius=0.05
        ).set_fill(sol.BASE2, opacity=1)

        mulabelline = Line(
            muomega.get_corner(DOWN+LEFT) + 0.05*DOWN + 2.6*RIGHT,
            muomega.get_corner(DOWN+LEFT) + 0.05*DOWN + 7.6*RIGHT,
            color=sol.BASE01
        )

        mulabelcurve = Line(
            mulabelbox.get_top() + RIGHT,
            mulabelline.get_center(),
            color=sol.BASE01
        )

        mulabel = Group(mulabelcurve, mulabelline, mulabelbox, mulabeltext)

        example = MyTex(
            r'\textbf{Examples}',
            font_size=70
        ).align_to(notation, LEFT).shift(0.5*DOWN)

        exomegatext = MyTex(
            r'\bigg(with $\Omega = \bigg\{ \qquad, \qquad, \qquad, \qquad, \qquad, \qquad \bigg\}$ \bigg)',
            font_size=40
        ).next_to(example, RIGHT).shift(0.5*RIGHT)

        arrangements = Group(
            ThreeCardStack([1,2,3]).scale(0.5),
            ThreeCardStack([2,1,3]).scale(0.5),
            ThreeCardStack([2,3,1]).scale(0.5),
            ThreeCardStack([1,3,2]).scale(0.5),
            ThreeCardStack([3,1,2]).scale(0.5),
            ThreeCardStack([3,2,1]).scale(0.5)
        ).arrange().shift(0.5*DOWN+2.875*RIGHT)

        exomega = Group(exomegatext, arrangements)

        ex1 = MyMathTex(
            r'\bullet & \text{ if } \mu \text{ is the uniform} \\\
            & \text{ distribution on } \Omega, \\\
            & \qquad {\textstyle \mu(x) = \frac{1}{6}} \\\
            & \text{ for each } x \in \Omega.'
        ).shift(2.5*DOWN + 4.25*LEFT)

        ex2text = MyMathTex(
            r"\bullet & \text{ if } \mu \text{ is the distribution after one} \\\
                & \text{ top-to-random shuffle,} \\\
                & \quad {\textstyle \mu(\quad) = \mu(\quad) = \mu(\quad) = \frac{1}{3}}, \text{ and} \\\
                & \quad {\textstyle \mu(\quad) = \mu(\quad) = \mu(\quad) = 0}"
        ).align_to(ex1, UP).shift(2.75*RIGHT)

        ex2arrangements1 = Group(
            ThreeCardStack([1,2,3]).scale(0.275),
            ThreeCardStack([2,1,3]).scale(0.275),
            ThreeCardStack([2,3,1]).scale(0.275),
        ).arrange(buff=1.42).shift(2.85*DOWN + 2.175*RIGHT)

        ex2arrangements2 = Group(
            ThreeCardStack([1,3,2]).scale(0.275),
            ThreeCardStack([3,1,2]).scale(0.275),
            ThreeCardStack([3,2,1]).scale(0.275),
        ).arrange(buff=1.42).shift(3.43*DOWN + 2.175*RIGHT)

        ex2 = Group(ex2text, ex2arrangements1, ex2arrangements2)

        self.play(FadeIn(notation, shift=DOWN+RIGHT))
        self.play(FadeIn(muomega, scale=0.75))
        self.play(FadeIn(omegalabel, shift=LEFT))
        self.play(FadeIn(mulabel, shift=RIGHT))
        self.play(FadeIn(example, scale=0.75))
        self.play(
            FadeIn(exomega, shift=LEFT),
            FadeIn(ex1, shift=LEFT)
        )
        self.play(FadeIn(ex2, shift=LEFT))


class TVDefinition(Scene):
    def construct(self):
        headertext = MyTex(
            r'Let {{$\mu_1$}} and {{$\mu_2$}} be two probability distributions\\\
                on the same outcome space $\Omega$.',
        ).shift(3*UP)

        def1text = MyMathTex(
            r'\textbf{Definition 1: } \mathrm{d_{TV}}({{\mu_1}}, {{\mu_2}}) = \frac{1}{2} \sum_{ {{x}} \in \Omega} |{{\mu_1}}({{x}}) - {{\mu_2}}({{x}})|',
            font_size=55
        ).shift(1.25*UP).set_color_by_tex(r'x', sol.FOREST_GREEN).set_color_by_tex(r'D', sol.BASE03)

        def2text = MyMathTex(
            r'\textbf{Definition 2: } \mathrm{d_{TV}}({{\mu_1}},{{\mu_2}}) = \max_{ {{A}} \subseteq \Omega} | {{\mu_1}}({{A}}) - {{\mu_2}}({{A}}) |',
            font_size=55
        ).next_to(def1text, DOWN).align_to(def1text, LEFT).shift(0.25*DOWN).set_color_by_tex(r'A', sol.FOREST_GREEN)

        def3text = MyMathTex(
            r'\textbf{Definition 3: } \mathrm{d_{TV}}({{\mu_1}}, {{\mu_2}}) = \min_{\substack{ {{X_1}} \sim {{\mu_1}} \\ {{X_2}} \sim {{\mu_2}} }} \mathbb{P}[{{X_1}} \neq {{X_2}}]',
            font_size=55
        ).next_to(def2text, DOWN).align_to(def1text, LEFT).shift(0.5*DOWN).set_color_by_tex(r'X_1', sol.FOREST_GREEN).set_color_by_tex(r'X_2', sol.FOREST_GREEN)

        nametext = MyTex(
            r"``Total Variation Distance''",
            font_size=80
        ).shift(0.5*DOWN)

        eventtext1 = MyTex(
            r'$A$ is an event \\ $\Leftrightarrow A \subseteq \Omega$',
            font_size=40
        ).shift(5*LEFT+1.75*DOWN)

        eventtext2 = MyMathTex(
            r'\mu(A) = \sum_{x \in A} \mu(x)',
            font_size=40
        ).next_to(eventtext1, DOWN).shift(0.25*DOWN)

        extext1 = MyMathTex(
            r'\text{e.g. } {{A}} = \{ x \in \Omega : \text{card } 2 \text{ is above card } 3 \}',
            font_size=40
        ).shift(2*RIGHT + 1.5*DOWN).set_color_by_tex(r'A', sol.FOREST_GREEN)

        extext2 = MyMathTex(
            r'\textstyle \bullet \text{ if } {{\mu_1}} \text{ is uniform, then } {{\mu_1}}({{A}}) = \frac{1}{2}',
            font_size=40
        ).next_to(extext1, DOWN).align_to(extext1, LEFT).set_color_by_tex(r'A', sol.FOREST_GREEN)

        extext3 = MyMathTex(
            r'\textstyle \bullet &\text{ if } {{\mu_2}} \text{ is the distribution after one} \\ \textstyle &\text{ top-to-random shuffle, then } {{\mu_2}}({{A}}) = 1',
            font_size=40
        ).next_to(extext2, DOWN).align_to(extext1, LEFT).set_color_by_tex(r'A', sol.FOREST_GREEN)

        extext4 = MyMathTex(
            r'\Rightarrow \mathrm{d_{TV}}({{\mu_1}},{{\mu_2}}) \geq \frac{1}{2}'
        ).next_to(Group(extext1,extext2,extext3), RIGHT).shift(4*LEFT)

        exbrace = Brace(Group(extext1, extext2, extext3), RIGHT, color=sol.BASE03).shift(4.5*LEFT)

        popupbox = Rectangle(color=sol.BASE01, height=7, width=13).set_fill(sol.BASE2, opacity=1)

        randomvars = MyTex(
            r'\textbf{Random Variables 101}',
            font_size=60
        ).align_to(popupbox, UP + LEFT).shift(0.5*(DOWN + RIGHT))

        rvtext1 = MyTex(
            r'\textbullet{} A \emph{random variable} is a random outcome $X \in \Omega$.'
        ).next_to(randomvars, DOWN).align_to(randomvars, LEFT).shift(0.25*DOWN + 0.5*RIGHT)

        rvtext2 = MyMathTex(
            r'\bullet & \text{ } X \sim \mu \text{ means that } X \text{ has distribution } \mu, \\ &\text{ i.e. } \mu(x) = \P[X = x] \text{ for each fixed } x \in \Omega.'
        ).next_to(rvtext1, DOWN).align_to(rvtext1, LEFT)

        rvtext3 = MyTex(
            r'\emph{different random variables may} \\ \emph{have the same distribution}'
        ).next_to(rvtext2, DOWN)
        rvtext3.shift([-rvtext3.get_center()[0], -0.15, 0])

        rvextext = MyMathTex(
            r'\textstyle &\textbf{Example:} \text{ flip a fair coin } 5 \text{ times. Let } X \text{ be the number of} \\\
              \textstyle &\text{ heads, and let } Y \text{ be the number of tails. Then } X \text{ and } Y \\\
              \textstyle &\text{ have the same distribution } \mu = \mathrm{Binomial}(5,\tfrac{1}{2}), \text{ but } X \neq Y.',
            font_size=45
        ).next_to(rvtext3, DOWN).align_to(randomvars, LEFT).shift(0.3*DOWN + 0.1*LEFT)

        couplingtext = MyTex(
            r"``coupling''"
        ).next_to(def3text, DOWN).shift(LEFT + 0.25*UP)

        couplingarrow = Arrow(
            couplingtext.get_right(),
            def3text[5].get_left()+0.25*DOWN,
            color=sol.BASE1,
            tip_shape=StealthTip
        )

        self.play(FadeIn(headertext, shift=DOWN))

        self.play(FadeIn(def1text, scale=0.75))
        self.play(Wiggle(Group(def1text[5][0], def1text[6][0:2])))
        self.play(Wiggle(Group(def1text[6][2], def1text[7:])))
        self.play(Wiggle(def1text[4][-1]))
        self.play(Wiggle(Group(def1text[4][-4:-1])))
        self.play(Wiggle(Group(def1text[0][-4:], def1text[1:4], def1text[4][0])))
        self.play(Write(nametext))
        self.play(Wiggle(Group(def1text[0][-3:-1])))

        self.play(FadeOut(nametext, shift=DOWN))
        self.play(FadeIn(def2text, scale=0.75))
        self.play(FadeIn(eventtext1, shift=RIGHT))
        self.play(FadeIn(eventtext2, shift=RIGHT))
        self.play(FadeIn(extext1, scale=0.75))
        self.play(FadeIn(extext2, shift=LEFT))
        self.play(FadeIn(extext3, shift=LEFT))
        self.play(
            FadeOut(Group(eventtext1, eventtext2), shift=4.5*LEFT),
            extext1.animate.shift(4.5*LEFT),
            extext2.animate.shift(4.5*LEFT),
            extext3.animate.shift(4.5*LEFT),
            FadeIn(Group(exbrace, extext4), shift=4.5*LEFT)
        )
        self.play(
            FadeOut(Group(extext1, extext2, extext3, extext4, exbrace), shift=14*LEFT),
            FadeIn(diaconistable, shift=14*LEFT)
        )

        self.play(FadeIn(Group(popupbox, randomvars), scale=0.75))
        self.play(FadeIn(rvtext1, shift=LEFT)) 
        self.play(FadeIn(rvtext2, shift=LEFT))
        self.play(FadeIn(rvtext3, scale=0.75))
        self.play(FadeIn(rvextext, scale=0.75))
        self.remove(diaconistable)
        self.play(FadeOut(Group(popupbox, randomvars, rvtext1, rvtext2, rvtext3, rvextext), scale=0.75))
        self.play(FadeIn(def3text, scale=0.75))
        self.play(Write(couplingtext), FadeIn(couplingarrow, scale=0.75))

        self.wait(5)