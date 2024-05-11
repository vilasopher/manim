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
        ).next_to(uniformbar, UP).shift(0.5*LEFT+0.125*UP)
        uniformtext1 = Tex(
            r'Random',
            color=sol.BASE03
        ).next_to(uniformtext2, UP, buff=0.25).align_to(uniformtext2, LEFT)
        uniformbar.add(topline, bottomline, topnum, bottomnum, uniformtext1, uniformtext2)

        resultbar = Rectangle(height=5, width=1.25, stroke_width=0)
        resultbar.set_fill(sol.BASE02, opacity=1).align_to(coin1.Hbar, DOWN).shift(0.5*DOWN+4*RIGHT)
        disagreebar = Rectangle(height=(0.7-0.4)*5, width=1.25, stroke_width=0)
        disagreebar.set_fill(sol.BASE01, opacity=0.5).align_to(coin1.Hbar, UP).shift(0.5*DOWN+4*RIGHT)
        resultbar.add(disagreebar)
        resultTT1 = Tex(
            r'\textbf{T}',
            color=sol.RED,
            font_size=60
        ).align_to(resultbar, UP + LEFT).shift(0.1*(DOWN+RIGHT))
        resultTT2 = Tex(
            r'\textbf{T}',
            color=sol.BLUE,
            font_size=60
        ).align_to(resultbar, UP + RIGHT).shift(0.1*(DOWN+LEFT))
        resultbar.add(resultTT1, resultTT2)
        resultHH1 = Tex(
            r'\textbf{H}',
            color=sol.RED,
            font_size=60
        ).align_to(resultbar, DOWN + LEFT).shift(0.1*(UP+RIGHT))
        resultHH2 = Tex(
            r'\textbf{H}',
            color=sol.BLUE,
            font_size=60
        ).align_to(resultbar, DOWN + RIGHT).shift(0.1*(UP+LEFT))
        resultbar.add(resultHH1, resultHH2)
        resultHT1 = Tex(
            r'\textbf{H}',
            color=sol.RED,
            font_size=60
        ).next_to(disagreebar, LEFT).align_to(disagreebar, LEFT).shift(0.1*RIGHT)
        resultHT2 = Tex(
            r'\textbf{T}',
            color=sol.BLUE,
            font_size=60
        ).next_to(disagreebar, RIGHT).align_to(resultbar, RIGHT).shift(0.1*LEFT)
        resultbar.add(resultHT1, resultHT2)
        resulttext = Tex(
            r'Result',
            color = sol.BASE03,
            font_size=60
        ).next_to(resultbar, UP).shift(0.1*UP)
        resultbar.add(resulttext)

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
                  FadeOut(coin2, shift=3.75*RIGHT), coin1.animate.shift(3.75*RIGHT))
        coin2.shift(3.75*RIGHT)
        coin2.transform()
        self.play(coin1.animate.transform())
        self.play(FadeIn(uniformbar))
        self.play(FadeIn(coin2))
        self.play(FadeIn(resultbar))
        self.wait()