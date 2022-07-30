from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import CriticalValueSlider, ValueSlider
import math

config.background_opacity = 0

####################################################

lemma = MathTex(
    r'\textbf{Lemma: } {{ p_c }} < 1.',
    color = sol.BASE03
).set_color_by_tex(r'p_c', sol.BLUE).move_to(4.75 * LEFT + 3.25 * UP)

temp = TexTemplate()
temp.add_to_preamble(r'\usepackage{stackengine}')
temp.add_to_preamble(r'\usepackage{mathtools}')
temp.add_to_preamble(r'\newcommand\oo{\stackMath\mathbin{\stackinset{c}{0ex}{c}{0ex}{o}{\bigcirc}}}')

####################################################

definitionleft = MathTex(
    r'\oo_{{\ell}} \coloneqq',
    color=sol.BASE03,
    tex_template=temp
).set_color_by_tex(r'\ell', sol.GREEN)
definitionleft.next_to(lemma, RIGHT).align_to(lemma, UP).shift(2 * RIGHT)

definitiontop = MathTex(
    r'\text{the event that a length-} {{ \ell }}',
    color=sol.BASE03,
    font_size=36
).set_color_by_tex(r'\ell', sol.GREEN)
definitionbot = MathTex(
    r'\text{dual circuit encircles } o',
    color = sol.BASE03,
    font_size=36
).next_to(definitiontop, DOWN).align_to(definitiontop, LEFT).shift(0.2 * UP)
definitionright = Group(definitiontop, definitionbot).next_to(definitionleft, RIGHT).shift(0.05 * UP)

definition = Group(definitionleft, definitionright)

####################################################

bound1_A = MathTex(
    r'\mathbb{P}_{{p}}[\oo_{{\ell}}] \leq',
    color = sol.BASE03,
    tex_template = temp
).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'\ell', sol.GREEN).next_to(lemma, DOWN).align_to(lemma, LEFT).shift(1 * DOWN + 0.5 * RIGHT)

bound1_B = MathTex(
    r'\sum_{\substack{ {{ \gamma }} \text{ a circuit} \\ \text{of length } {{\ell}} }}',
    color = sol.BASE03
).set_color_by_tex(r'\gamma', sol.GREEN).set_color_by_tex(r'\ell', sol.GREEN).next_to(bound1_A, RIGHT).shift(0.35 * DOWN + 0.3 * LEFT)

bound1_C = MathTex(
    r'\mathbb{P}_{{p}}[{{\gamma}} \text{ is all open}]',
    color = sol.BASE03
).set_color_by_tex(r'\gamma', sol.GREEN).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'o', sol.BASE03).next_to(bound1_B, RIGHT).shift(0.35 * UP + 0.3 * LEFT)

bound1_C2 = MathTex(
    r'(1-{{p}})^{{\ell}}',
    color = sol.BASE03
).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'\ell', sol.GREEN).next_to(bound1_B, RIGHT).shift(0.4 * UP + 0.3 * LEFT)

bound1_C3 = MathTex(
    r'(1-{{p}})^{{\ell}}',
    color = sol.BASE03
).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'\ell', sol.GREEN).next_to(bound1_A, RIGHT).shift(0.05 * UP)

bound1_B3 = MathTex(
    r'\cdot \, \# \{\text{length-}{{\ell}} \text{ circuits around } o\}',
    color = sol.BASE03
).set_color_by_tex(r'\ell', sol.GREEN).next_to(bound1_C3, RIGHT).shift(0.05 * DOWN)

####################################################

bound2_A = MathTex(
    r'\# \{\text{length-}{{\ell}} \text{ circuits around } o\}',
    color = sol.BASE03
).set_color_by_tex(r'\ell', sol.GREEN).next_to(lemma, DOWN).align_to(lemma, LEFT).shift(0.5 * RIGHT + 3 * DOWN)

bound2_B = MathTex(
    r'\leq { {{\ell}} \over 2 } \cdot 3^{{{\ell}} - 1}',
    color = sol.BASE03
).set_color_by_tex(r'\ell', sol.GREEN).next_to(bound2_A, RIGHT)

bound2_C = MathTex(
    r'\leq {{\ell}} \cdot 3^{{\ell}}',
    color = sol.BASE03
).set_color_by_tex(r'\ell', sol.GREEN).next_to(bound2_B, RIGHT).shift(0.02 * UP)

####################################################

bound3_A = MathTex(
    r'\mathbb{P}_{{p}}[\oo_{{\ell}}] \leq {{(1-}}{{p}}{{)}}^{{\ell}} \cdot {{\ell}} \cdot {{3}}^{{\ell}}',
    color = sol.BASE03,
    tex_template = temp
).set_color_by_tex(r'\ell', sol.GREEN).set_color_by_tex(r'p', sol.RED).next_to(lemma, DOWN).align_to(lemma, LEFT).shift(0.5 * RIGHT + 5 * DOWN)

bound3_A2 = MathTex(
    r'\mathbb{P}_{{p}}[\oo_{{\ell}}] \leq {{\ell}} \cdot ({{3}} \, {{(1-}}{{p}}{{)}})^{{\ell}}',
    color = sol.BASE03,
    tex_template = temp
).set_color_by_tex(r'\ell', sol.GREEN).set_color_by_tex(r'p', sol.RED).next_to(lemma, DOWN).align_to(lemma, LEFT).shift(0.5 * RIGHT + 5 * DOWN)

bound3_A3 = MathTex(
    r'\mathbb{P}_{{p}}[\oo_{{\ell}}] \leq {{\ell}} \cdot ({{3}} \, {{(1-}}{{p}}{{)}})^{{\ell}}',
    color = sol.BASE03,
    tex_template = temp
).set_color_by_tex(r'\ell', sol.GREEN).set_color_by_tex(r'p', sol.RED).next_to(lemma, DOWN).align_to(lemma, LEFT).shift(0.5 * RIGHT + 0.75 * DOWN)

####################################################

definitionleft2 = MathTex(
    r'\oo_{\geq {{N}}} \coloneqq',
    color=sol.BASE03,
    tex_template=temp
).set_color_by_tex(r'N', sol.VIOLET)
definitionleft2.next_to(lemma, RIGHT).align_to(lemma, UP).shift(2 * RIGHT)

definitiontop2 = MathTex(
    r'\text{the event that a dual circuit of}',
    color=sol.BASE03,
    font_size=36
)
definitionbot2 = MathTex(
    r'\text{length at least } {{N}} \text{ encircles } o',
    color = sol.BASE03,
    font_size=36
).set_color_by_tex(r'N', sol.VIOLET).next_to(definitiontop2, DOWN).align_to(definitiontop2, LEFT).shift(0.2 * UP)
definitionright2 = Group(definitiontop2, definitionbot2).next_to(definitionleft2, RIGHT).shift(0.05 * UP)

definition2 = Group(definitionleft2, definitionright2)

####################################################

sum_equality = MathTex(
    r'\mathbb{P}_{{p}}[\oo _ { \geq {{N \hspace{0cm} }} } ] {{=}} \sum_{ {{\ell}} = \hspace{0em} {{N}} }^\infty {{ \mathbb{P} }}_{{p}}[\oo_{{\ell \hspace{0em} }}]',
    color = sol.BASE03,
    tex_template = temp
).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'0em', sol.GREEN).set_color_by_tex(r'\infty', sol.VIOLET).set_color_by_tex(r'0cm', sol.VIOLET).next_to(bound3_A3, RIGHT).shift(RIGHT + 0.05 * DOWN)

####################################################

bound4_A = MathTex(
    r'{\mathbb{P}_{{p}}[\oo _ { \geq {{N \hspace{0cm} }} } ] {{\leq}} \sum_{ {{\ell}} = \hspace{0em} {{N}} }^\infty {{\ell \hspace{0em} }} \cdot (3 \, (1 - {{p}}))^{{\ell \hspace{0em} }}',
    color = sol.BASE03,
    tex_template = temp
).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'0em', sol.GREEN).set_color_by_tex(r'\infty', sol.VIOLET).set_color_by_tex(r'0cm', sol.VIOLET).next_to(lemma, DOWN).align_to(lemma, LEFT).shift(0.5 * RIGHT + 2.25 * DOWN)

bound4_B = MathTex(
    r'\text{converges}',
    color = sol.BASE03
).next_to(bound4_A, RIGHT).shift(0.5 * RIGHT)

bound4_B2 = MathTex(
    r'\to 0 \text{ as } {{N}} \to \infty',
    color = sol.BASE03
).set_color_by_tex(r'N', sol.VIOLET).next_to(bound4_A, RIGHT).shift(0.1 * UP)

bound4_C = MathTex(
    r'{{ (\text{if } }} 1 - {{p}} < 1 {{ / 3 ) }}',
    color = sol.BASE03
).set_color_by_tex(r'p', sol.RED).next_to(bound4_B, RIGHT).shift(0.05 * UP)

bound4_C2 = MathTex(
    r'{{ (\text{if } }} {{p}} > 2 {{ / 3 ) }}',
    color = sol.BASE03
).set_color_by_tex(r'p', sol.RED).next_to(bound4_B2, RIGHT).shift(0.05 * DOWN)

####################################################

bound5_A = MathTex(
    r'\text{for } {{p}} > 2/3,',
    color = sol.BASE03
).set_color_by_tex(r'p', sol.RED).next_to(lemma, DOWN).align_to(lemma, LEFT).shift(0.5 * RIGHT + 4.5 * DOWN)

bound5_B = MathTex(
    r'\text{and large enough } {{N}},',
    color = sol.BASE03
).set_color_by_tex(r'N', sol.VIOLET).next_to(bound5_A, RIGHT)

bound5_C = MathTex(
    r'\mathbb{P}_{{p}}[\oo_{\geq {{N}}}] < 1,',
    color = sol.BASE03,
    tex_template = temp
).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'N', sol.VIOLET).next_to(bound5_B, RIGHT)

bound5_D = MathTex(
    r'\text{so} \quad \mathbb{P}_{{p}}[\text{not } \oo_{\geq {{N}}}] = 1 - \mathbb{P}_{{p}}[\oo_{\geq {{N}}}] > 0.',
    color = sol.BASE03,
    tex_template = temp
).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'N', sol.VIOLET).next_to(bound5_C, DOWN).align_to(bound5_C, RIGHT).shift(0.15 * DOWN)

####################################################

class BlueTex(Scene):
    def construct(self):
        #self.add(lemma, definition, bound1_A, bound1_B3, bound1_C3, bound2_A, bound2_B, bound2_C, bound3_A2)
        #self.add(lemma, definition2, bound3_A3, sum_equality, bound4_A, bound4_B, bound4_C, bound5_A, bound5_B, bound5_C)

        self.add(lemma)
        self.wait()

        self.play(FadeIn(definition))
        self.wait(5)

        self.play(FadeIn(bound1_A))
        self.play(FadeIn(bound1_B))
        self.play(FadeIn(bound1_C))

        self.wait(4)

        self.play(Indicate(bound1_C))

        self.wait(2)

        self.play(TransformMatchingTex(bound1_C, bound1_C2))

        self.wait(4)

        self.play(
            TransformMatchingTex(bound1_B, bound1_B3),
            TransformMatchingTex(bound1_C2, bound1_C3)
        )

        self.wait(37)

        self.play(FadeIn(bound2_A))
        self.play(FadeIn(bound2_B))
        self.play(FadeIn(bound2_C))

        self.wait(10)

        self.play(FadeIn(bound3_A))
        self.wait(2)
        self.play(TransformMatchingTex(bound3_A, bound3_A2))
        self.wait(1)

        self.play(
            FadeOut(bound1_A),
            FadeOut(bound1_B3),
            FadeOut(bound1_C3),
            FadeOut(bound2_A),
            FadeOut(bound2_B),
            FadeOut(bound2_C)
        )

        self.play(TransformMatchingTex(bound3_A2, bound3_A3))
        self.wait(6)

        self.play(
            FadeOut(definition),
            FadeIn(definition2)
        )

        self.wait(2)

        self.play(FadeIn(sum_equality))

        self.wait(1)

        self.play(FadeIn(bound4_A))

        self.wait(5)

        self.play(FadeIn(bound4_B))
        self.play(FadeIn(bound4_C))

        self.wait(2)

        self.play(TransformMatchingTex(bound4_C, bound4_C2))

        self.wait(8)

        self.play(TransformMatchingTex(bound4_B, bound4_B2))

        self.wait(3)

        self.play(FadeIn(bound5_A))

        self.wait(1)

        self.play(FadeIn(bound5_B))

        self.wait(1)

        self.play(FadeIn(bound5_C))

        self.wait(8)

        self.play(Write(bound5_D))

        self.wait(10)

class BlueTexDefBoxIn(Scene):
    def construct(self):
        self.add(TranslucentBox(definition))

class BlueTexB1BoxIn(Scene):
    def construct(self):
        self.add(TranslucentBox(bound1_A))

class BlueTexB2BoxIn(Scene):
    def construct(self):
        self.add(TranslucentBox(bound2_A))

class BlueTexB3BoxIn(Scene):
    def construct(self):
        self.add(TranslucentBox(bound3_A))

class BlueTexBoxesOut(Scene):
    def construct(self):
        self.add(TranslucentBox(bound1_A, bound1_B3, bound1_C3))
        self.add(TranslucentBox(bound2_A, bound2_B, bound2_C))

class BlueTexSEQBoxIn(Scene):
    def construct(self):
        self.add(TranslucentBox(sum_equality))

class BlueTexB4BoxIn(Scene):
    def construct(self):
        self.add(TranslucentBox(bound4_A))

class BlueTexB5BoxIn(Scene):
    def construct(self):
        self.add(TranslucentBox(bound5_A))

class BlueTexBox(Scene):
    def construct(self):
        self.add(TranslucentBox(lemma))
        self.wait()

        #self.play(FadeIn(definition)) TODO
        self.wait()
        tdef = TranslucentBox(definition)
        self.add(tdef)
        self.wait(5)

        #self.play(FadeIn(bound1_A)) TODO
        self.wait()
        t1 = TranslucentBox(bound1_A)
        self.add(t1)
        self.play(Transform(t1, TranslucentBox(bound1_A, bound1_B)))
        self.play(Transform(t1, TranslucentBox(bound1_A, bound1_B, bound1_C)))

        self.wait(7)

        self.play(Transform(t1, TranslucentBox(bound1_A, bound1_B, bound1_C2)))

        self.wait(4)

        self.play(Transform(t1, TranslucentBox(bound1_A, bound1_B3, bound1_C3)))

        self.wait(37)

        #self.play(FadeIn(bound2_A)) TODO
        self.wait()
        t2 = TranslucentBox(bound2_A)
        self.add(t2)
        self.play(Transform(t2, TranslucentBox(bound2_A, bound2_B)))
        self.play(Transform(t2, TranslucentBox(bound2_A, bound2_B, bound2_C)))

        self.wait(10)

        #self.play(FadeIn(bound3_A)) TODO
        self.wait()
        t3 = TranslucentBox(bound3_A)
        self.add(t3)
        self.wait(2)
        self.play(Transform(t3, TranslucentBox(bound3_A2)))
        self.wait(1)

        self.remove(t1, t2)
        self.wait()
        #self.play(
        #    FadeOut(bound1_A),
        #    FadeOut(bound1_B3),
        #    FadeOut(bound1_C3),
        #    FadeOut(bound2_A),
        #    FadeOut(bound2_B),
        #    FadeOut(bound2_C)
        #) TODO

        self.play(Transform(t3, TranslucentBox(bound3_A3)))
        self.wait(6)

        self.play(Transform(tdef, TranslucentBox(definition2)))

        self.wait(2)

        #self.play(FadeIn(sum_equality)) TODO
        self.wait()
        tseq = TranslucentBox(sum_equality)
        self.add(tseq)

        self.wait(1)

        #self.play(FadeIn(bound4_A)) TODO
        self.wait()
        t4 = TranslucentBox(bound4_A)
        self.add(t4)

        self.wait(5)

        self.play(Transform(t4, TranslucentBox(bound4_A, bound4_B)))
        self.play(Transform(t4, TranslucentBox(bound4_A, bound4_B, bound4_C)))

        self.wait(2)

        self.play(Transform(t4, TranslucentBox(bound4_A, bound4_B, bound4_C2)))

        self.wait(8)

        self.play(Transform(t4, TranslucentBox(bound4_A, bound4_B2, bound4_C2)))

        self.wait(3)

        #self.play(FadeIn(bound5_A)) TODO
        self.wait()
        t5 = TranslucentBox(bound5_A)
        self.add(t5)

        self.wait(1)

        self.play(Transform(t5, TranslucentBox(bound5_A, bound5_B)))

        self.wait(1)

        self.play(Transform(t5, TranslucentBox(bound5_A, bound5_B, bound5_C)))

        self.wait(8)

        self.play(Transform(t5, TranslucentBox(bound5_A, bound5_B, bound5_C, bound5_D)))

        self.wait(10)
