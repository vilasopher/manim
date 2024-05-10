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

        baseline = Line(color=sol.BASE03, z_index=1, start=1*LEFT, end=1*RIGHT)
        Hbar = Rectangle(
            height=p*5, width=0.75, stroke_width=0
        ).set_fill(
            interpolate_color(color, sol.BASE03, 0.2), opacity=1
        ).next_to(
            baseline, UP, buff=0
        ).align_to(
            baseline, LEFT
        ).shift(
            0.125 * RIGHT
        )
        Tbar = Rectangle(
            height=(1-p)*5, width=0.75, stroke_width=0
        ).set_fill(
            interpolate_color(color, sol.BASE3, 0.2), opacity=1
        ).next_to(
            baseline, UP, buff=0
        ).align_to(
            baseline, RIGHT
        ).shift(
            0.125 * LEFT
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
            plabel, color=sol.BASE03, font_size=40
        ).set_color_by_tex(
            plabel, color
        ).next_to(Hbar, UP)
        Tplabel = MathTex(
            r'{{1-}}'+plabel, color=sol.BASE03, font_size=40
        ).set_color_by_tex(
            plabel,color
        ).next_to(Tbar, UP)

        coinlabel = Tex(
            r'\textbf{'+label+r'}',
            font_size=60,
            color=color
        ).next_to(baseline, UP).shift(4.25*UP)

        self.add(baseline, Hbar, Tbar, Htext, Ttext, Hplabel, Tplabel, coinlabel)

class CoinFlipExample(Scene):
    def construct(self):
        coin1 = CoinBarChart(0.7, label='Coin 1', plabel='p', color=sol.RED).shift(5.75*LEFT + 2.5*DOWN)
        coin2 = CoinBarChart(0.4, label='Coin 2', plabel='q', color=sol.BLUE).shift(3*LEFT + 2.5*DOWN)

        definition1 = Tex(
            r'\textbf{Definition 1}',
            color=sol.BASE03,
            font_size=70
        ).move_to(2.5*UP + 2.75*RIGHT)

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
        ).move_to(2.5*UP + 2.75*RIGHT)

        formula2a = MathTex(
            r'= \max_{A \subseteq \{H,T\}} |{{C_1}}(A) - {{C_2}}(A)|',
            color=sol.BASE03,
            font_size=50
        ).next_to(dtv, DOWN).align_to(dtv, LEFT).shift(0.25*RIGHT).set_color_by_tex(r'C_1', sol.RED).set_color_by_tex(r'C_2', sol.BLUE).shift(0.25*DOWN)

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

        self.add(coin1, coin2, definition1, dtv, formula2a, formula2b, formula2c)