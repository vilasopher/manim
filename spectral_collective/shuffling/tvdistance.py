from manim import *
import solarized as sol

class TVDefinition(Scene):
    def construct(self):
        headertext = Tex(
            r'Let $\mu$ and $\lambda$ be probability distributions on $\Omega$, \\'
            r'the set of possible outcomes.',
            color=sol.BASE03
        ).shift(2*UP)

        def1text = MathTex(
            r'\textbf{Definition 1: } \mathrm{d_{TV}}(\mu, \lambda) = \frac{1}{2} \sum_{x \in \Omega} |\mu(x) - \lambda(x)|',
            color=sol.BASE03
        ).next_to(headertext, DOWN).align_to(headertext, LEFT)

        def2text = MathTex(
            r'\textbf{Definition 2: } \mathrm{d_{TV}}(\mu,\lambda) = \max_{A \subseteq \Omega} |\mu(A) - \lambda(A)|',
            color=sol.BASE03
        ).next_to(def1text, DOWN).align_to(headertext, LEFT)

        def3text = MathTex(
            r'\textbf{Definition 3: } \mathrm{d_{TV}}(\mu, \lambda) = \min_{\substack{X \sim \mu \\ Y \sim \lambda}} \mathbb{P}[X \neq Y]',
            color=sol.BASE03
        ).next_to(def2text, DOWN).align_to(headertext, LEFT)

        self.add(headertext, def1text, def2text, def3text)

class CoinBarChart(Group):
    def __init__(self, p, label=r'Coin', plabel=r'p', color=sol.RED):
        super().__init__()

        baseline = Line(color=sol.BASE03, z_index=1, start=1.5*LEFT, end=1.5*RIGHT)
        Hbar = Rectangle(
            height=p*4, width=1, stroke_width=0
        ).set_fill(
            interpolate_color(color, sol.BASE03, 0.2), opacity=1
        ).next_to(
            baseline, UP, buff=0
        ).align_to(
            baseline, LEFT
        ).shift(
            0.25 * RIGHT
        )
        Tbar = Rectangle(
            height=(1-p)*4, width=1, stroke_width=0
        ).set_fill(
            interpolate_color(color, sol.BASE3, 0.2), opacity=1
        ).next_to(
            baseline, UP, buff=0
        ).align_to(
            baseline, RIGHT
        ).shift(
            0.25 * LEFT
        )

        Htext = Tex(
            r'H',
            font_size=60,
            color=sol.BASE03
        ).next_to(Hbar, DOWN)
        Ttext = Tex(
            r'T',
            font_size=60,
            color=sol.BASE03
        ).next_to(Tbar, DOWN)

        Hplabel = MathTex(
            plabel, color=sol.BASE03
        ).set_color_by_tex(
            plabel, color
        ).next_to(Hbar, UP)
        Tplabel = MathTex(
            r'{{1-}}'+plabel, color=sol.BASE03
        ).set_color_by_tex(
            plabel,color
        ).next_to(Tbar, UP)

        coinlabel = Tex(
            r'\textbf{'+label+r'}',
            font_size=80,
            color=color
        ).next_to(baseline, UP).shift(3.75*UP)

        self.add(baseline, Hbar, Tbar, Htext, Ttext, Hplabel, Tplabel, coinlabel)

class CoinFlipExample(Scene):
    def construct(self):
        coin1 = CoinBarChart(0.7, label='Coin 1', plabel='p', color=sol.RED).shift(4.5*LEFT + 2*DOWN)
        coin2 = CoinBarChart(0.4, label='Coin 2', plabel='q', color=sol.BLUE).shift(2*DOWN)

        self.add(coin1, coin2)