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

        self.wait(5)


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

        self.Htext = Tex(
            r'H',
            font_size=60,
            color=sol.BASE03
        ).next_to(self.Hbar, DOWN)
        self.Ttext = Tex(
            r'T',
            font_size=60,
            color=sol.BASE03
        ).next_to(self.Tbar, DOWN)

        self.Hplabel = MathTex(
            plabel, color=sol.BASE03, font_size=40
        ).set_color_by_tex(
            plabel, color
        ).next_to(self.Hbar, UP)
        self.Tplabel = MathTex(
            r'{{1-}}'+plabel, color=sol.BASE03, font_size=40
        ).set_color_by_tex(
            plabel,color
        ).next_to(self.Tbar, UP)

        self.coinlabel = Tex(
            r'\textbf{'+label+r'}',
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
        self.Hplabel.next_to(self.Hbar, RIGHT).align_to(self.Hbar, UP).shift(0.1*UP)

class CoinFlipExample(Scene):
    def construct(self):
        coin1 = CoinBarChart(0.7, label='Coin 1', plabel='p', color=sol.RED).shift(2*LEFT + 2.5*DOWN) #5.75
        coin2 = CoinBarChart(0.4, label='Coin 2', plabel='q', color=sol.BLUE).shift(2*RIGHT + 2.5*DOWN) #3

        definition1 = Tex(
            r'\textbf{Definition 1}',
            color=sol.BASE03,
            font_size=70
        ).move_to(2.75*UP + 2.75*RIGHT)

        dtv = MathTex(
            r'\mathrm{d_{TV}}({{C_1}}, {{C_2}})',
            color=sol.BASE03,
            font_size=50
        ).next_to(definition1, DOWN).align_to(definition1, LEFT).shift(0.5*DOWN + 1.75*LEFT).set_color_by_tex(r'C_1', sol.RED).set_color_by_tex(r'C_2', sol.BLUE)

        formula1a = MathTex(
            r'= \frac{1}{2} \sum_{x \in \{H, T\}} |{{C_1}}(x) - {{C_2}}(x)|',
            color=sol.BASE03,
            font_size=50
        ).next_to(dtv, DOWN).align_to(dtv, LEFT).shift(0.25*RIGHT).set_color_by_tex(r'C_1', sol.RED).set_color_by_tex(r'C_2', sol.BLUE)

        formula1b = MathTex(
            r'= \frac{1}{2} \big(|{{p}} - {{q}}| + |(1-{{p}}) - (1-{{q}})|\big)',
            color=sol.BASE03,
            font_size=50
        ).next_to(formula1a, DOWN).align_to(formula1a, LEFT).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'q', sol.BLUE)

        formula1c = MathTex(
            r'= {{p}}-{{q}}',
            color=sol.BASE03,
            font_size=50
        ).next_to(formula1b, DOWN).align_to(formula1a, LEFT).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'q', sol.BLUE)

        definition2 = Tex(
            r'\textbf{Definition 2}',
            color=sol.BASE03,
            font_size=70
        ).move_to(2.75*UP + 2.75*RIGHT)

        formula2a = MathTex(
            r'= \max_{A \subseteq \{H,T\}} |{{C_1}}(A) - {{C_2}}(A)|',
            color=sol.BASE03,
            font_size=50
        ).next_to(dtv, DOWN).align_to(dtv, LEFT).shift(RIGHT).set_color_by_tex(r'C_1', sol.RED).set_color_by_tex(r'C_2', sol.BLUE).shift(0.25*DOWN)

        formula2b = MathTex(
            r'\geq |{{C_1}}(\{H\}) - {{C_2}}(\{H\})|',
            color=sol.BASE03,
            font_size=50
        ).next_to(formula2a, DOWN).align_to(formula2a, LEFT).set_color_by_tex(r'C_1', sol.RED).set_color_by_tex(r'C_2', sol.BLUE).shift(0.25*DOWN)

        formula2c = MathTex(
            r'= {{p}}-{{q}}',
            color=sol.BASE03,
            font_size=50
        ).next_to(formula2b, DOWN).align_to(formula2a, LEFT).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'q', sol.BLUE).shift(0.25*DOWN)

        definition3 = Tex(
            r'\textbf{Definition 3}',
            color=sol.BASE03,
            font_size=70
        ).move_to(2.75*UP + 2.75*RIGHT)

        formula3a = MathTex(
            r'= \min_{\substack{X \sim {{C_1}} \\ Y \sim {{C_2}}}} \mathbb{P}[X \neq Y]',
            color=sol.BASE03,
            font_size=50
        ).next_to(dtv, DOWN).align_to(dtv, LEFT).shift(0.25*RIGHT).set_color_by_tex(r'C_1', sol.RED).set_color_by_tex(r'C_2', sol.BLUE).shift(0.25*DOWN)

        formula3b = MathTex(
            r'\leq',
            color=sol.BASE03,
            font_size=50
        ).next_to(formula3a, DOWN).shift(0.5*DOWN).align_to(formula3a, LEFT).set_color_by_tex(r'Coin 1', sol.RED).set_color_by_tex(r'Coin 2', sol.BLUE).shift(0.25*DOWN)

        formula3c = MathTex(
            r'\quad \text{Probability that when {{Coin 1}} is}',
            color=sol.BASE03,
            font_size=40
        ).next_to(formula3a, DOWN).align_to(formula3a, LEFT).shift(0.75*RIGHT+0.1*UP).set_color_by_tex(r'Coin 1', sol.RED).set_color_by_tex(r'Coin 2', sol.BLUE).shift(0.25*DOWN)

        formula3d = MathTex(
            r'\quad \text{flipped independently from {{Coin 2}}}',
            color=sol.BASE03,
            font_size=40
        ).next_to(formula3c, DOWN).align_to(formula3c, LEFT).shift(0.25*UP).set_color_by_tex(r'Coin 1', sol.RED).set_color_by_tex(r'Coin 2', sol.BLUE).shift(0.25*DOWN)

        formula3e = MathTex(
            r'\quad \text{the coins come up on different sides}',
            color=sol.BASE03,
            font_size=40
        ).next_to(formula3d, DOWN).align_to(formula3c, LEFT).shift(0.25*UP).set_color_by_tex(r'Coin 1', sol.RED).set_color_by_tex(r'Coin 2', sol.BLUE).shift(0.25*DOWN)

        formula3f = MathTex(
            r'= {{p}}(1-{{q}}) + (1-{{p}}){{q}}',
            color=sol.BASE03,
            font_size=50
        ).next_to(formula3e, DOWN).align_to(formula3a, LEFT).shift(0.25*UP).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'q', sol.BLUE).shift(0.25*DOWN)

        uniformbar = Rectangle(height=5, width=0.5, stroke_width=0)
        uniformbar.set_fill(sol.BASE1, opacity=1).align_to(coin1.Hbar, DOWN).shift(0.5*DOWN+4.75*LEFT)
        topline = Line(ORIGIN, 0.5*RIGHT, color=sol.BASE02).next_to(uniformbar, DOWN, buff=0)
        bottomline = Line(ORIGIN, 0.5*RIGHT, color=sol.BASE02).next_to(uniformbar, UP, buff=0)
        topnum = DecimalNumber(1, color=sol.BASE03, num_decimal_places=0).next_to(uniformbar, RIGHT).align_to(uniformbar, UP).shift(0.125*UP)
        bottomnum = DecimalNumber(0, color=sol.BASE03, num_decimal_places=0).next_to(uniformbar, RIGHT).align_to(uniformbar, DOWN).shift(0.125*DOWN)
        uniformtext2 = Tex(
            r'Number',
            color=sol.BASE03
        ).next_to(uniformbar, UP).shift(0.65*LEFT+0.125*UP)
        uniformtext1 = Tex(
            r'Random',
            color=sol.BASE03
        ).next_to(uniformtext2, UP, buff=0.25).align_to(uniformtext2, LEFT)
        randomnumberBar = Group(uniformbar, topline, bottomline, topnum, bottomnum, uniformtext1, uniformtext2)

        resultbar = Rectangle(height=5, width=1.25, stroke_width=0.5, color=sol.BASE02, z_index=2)
        resultbar.set_fill(sol.BASE2, opacity=1).align_to(coin1.Hbar, DOWN).shift(0.5*DOWN+2.5*RIGHT)
        HHbar = Rectangle(height=0.4*5, width=1.25, stroke_width=0.5, color=sol.BASE02, z_index=4)
        HHbar.set_fill(sol.BASE1, opacity=1).next_to(resultbar, DOWN).align_to(resultbar, DOWN)
        HTbar = Rectangle(height=(0.7-0.4)*5, width=1.25, stroke_width=0.5, color=sol.BASE02, z_index=4)
        HTbar.set_fill(sol.BASE1, opacity=1).next_to(HHbar, UP, buff=0)
        TTbar = Rectangle(height=(1-0.7)*5, width=1.25, stroke_width=0.5, color=sol.BASE02, z_index=4)
        TTbar.set_fill(sol.BASE1, opacity=1).next_to(HTbar, UP, buff=0)

        resultTT1 = Tex(
            r'\textbf{T}',
            color=sol.RED,
            font_size=60
        ).align_to(TTbar, UP + LEFT).shift(0.1*(DOWN+RIGHT)).set_z_index(3)
        resultTT2 = Tex(
            r'\textbf{T}',
            color=sol.BLUE,
            font_size=60
        ).align_to(TTbar, UP + RIGHT).shift(0.1*(DOWN+LEFT)).set_z_index(3)
        resultHH1 = Tex(
            r'\textbf{H}',
            color=sol.RED,
            font_size=60
        ).align_to(HHbar, DOWN + LEFT).shift(0.1*UP+0.05*RIGHT).set_z_index(3)
        resultHH2 = Tex(
            r'\textbf{H}',
            color=sol.BLUE,
            font_size=60
        ).align_to(HHbar, DOWN + RIGHT).shift(0.1*UP+0.05*LEFT).set_z_index(3)
        resultHT1 = Tex(
            r'\textbf{H}',
            color=sol.RED,
            font_size=60
        ).next_to(HTbar, LEFT).align_to(HTbar, LEFT).shift(0.075*RIGHT).set_z_index(3)
        resultHT2 = Tex(
            r'\textbf{T}',
            color=sol.BLUE,
            font_size=60
        ).next_to(HTbar, RIGHT).align_to(HTbar, RIGHT).shift(0.1*LEFT).set_z_index(3)

        resultbar.add(resultHH1, resultHH2, resultHT1, resultHT2, resultTT1, resultTT2, HHbar, HTbar, TTbar)
        resulttext = Tex(
            r'Result',
            color = sol.BASE03,
            font_size=60,
            z_index=3
        ).next_to(resultbar, UP).shift(0.1*UP + 0.25*RIGHT)
        resultbar.add(resulttext)

        randomnumber = ValueTracker(0.5)
        randomnumberPoint = Dot(color=sol.BASE03)
        randomnumberPoint.add_updater(
            lambda x : x.next_to(uniformbar, DOWN, buff=0).shift(5 * randomnumber.get_value() * UP)
        )
        randomnumberText = DecimalNumber(randomnumber.get_value(), color=sol.BASE03)
        randomnumberText.add_updater(
            lambda x : x.next_to(randomnumberPoint, LEFT).set_value(randomnumber.get_value())
        )
        randomnumberLine = Line(randomnumberPoint.get_midpoint(), randomnumberPoint.get_midpoint() + 7 * RIGHT, color=sol.BASE02, stroke_width=0.5, z_index=1)
        randomnumberLine.add_updater(
            lambda x : x.put_start_and_end_on(randomnumberPoint.get_midpoint(), randomnumberPoint.get_midpoint() + 7 * RIGHT)
        )

        disagreebrace = Brace(HTbar, RIGHT, color=sol.BASE03)
        disagreeprob1 = MathTex(
            r'\mathbb{P}[X \neq Y]',
            font_size = 60,
            color=sol.BASE03
        )
        disagreeprob2 = MathTex(
            r'={{p}}-{{q}}',
            font_size=60,
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'q', sol.BLUE).next_to(disagreeprob1, DOWN).shift(0.125*RIGHT)
        disagreeprob = Group(disagreeprob1, disagreeprob2)
        disagreeprob.next_to(disagreebrace)

        self.play(FadeIn(coin1), FadeIn(coin2))
        self.play(coin1.animate.shift(3.75 * LEFT), coin2.animate.shift(5*LEFT))
        self.play(FadeIn(definition1))
        self.play(FadeIn(dtv))
        self.play(FadeIn(formula1a))
        self.play(FadeIn(formula1b))
        self.play(FadeIn(formula1c))
        self.play(FadeOut(formula1a, formula1b, formula1c))
        self.play(Transform(definition1, definition2))
        self.play(FadeIn(formula2a))
        self.play(FadeIn(formula2b))
        self.play(FadeIn(formula2c))
        self.play(FadeOut(formula2a, formula2b, formula2c))
        self.play(Transform(definition1, definition3))
        self.play(FadeIn(formula3a))
        self.play(FadeIn(formula3b, formula3c, formula3d, formula3e))
        self.play(FadeIn(formula3f))
        self.play(FadeOut(definition1, dtv, formula3a, formula3b, formula3c, formula3d, formula3e, formula3f),
                  FadeOut(coin2, shift=3*RIGHT), coin1.animate.shift(3*RIGHT))
        coin2.shift(3*RIGHT)
        coin2.transform()
        self.play(coin1.animate.transform())
        self.play(FadeIn(randomnumberBar, randomnumberPoint, randomnumberText, randomnumberLine))
        self.play(FadeIn(coin2))
        self.play(FadeIn(HHbar, HTbar, TTbar, resulttext))

        HHbar.add_updater(
            lambda x : x.set_fill(sol.BASE1, opacity=0.25 if randomnumber.get_value() < 0.4 else 1)
        )
        HTbar.add_updater(
            lambda x : x.set_fill(sol.BASE1, opacity=0.25 if randomnumber.get_value() >= 0.4 and randomnumber.get_value() < 0.7 else 1)
        )
        TTbar.add_updater(
            lambda x : x.set_fill(sol.BASE1, opacity=0.25 if randomnumber.get_value() >= 0.7 else 1)
        )

        def rerandomize():
            randomnumber.set_value(random())
            self.update_mobjects(0)

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