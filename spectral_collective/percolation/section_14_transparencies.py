from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import CriticalValueSlider
import math

config.background_opacity = 0

class Lemma(Scene):
    def construct(self):
        tex = MathTex(
            r'\textbf{Lemma: } {{ p_c }} > 0.',
            color = sol.BASE03
        ).set_color_by_tex(r'p_c', sol.BLUE).move_to(5 * LEFT + 3.5 * UP)

        self.add(TranslucentBox(tex), tex)

class PurpleTex(Scene):
    def construct(self):
        t1 = MathTex(
            r'o \leftrightarrow \infty',
            color = sol.BASE03
        )
        t2 = MathTex(
            r'\Rightarrow',
            color = sol.BASE03
        ).next_to(t1, RIGHT)
        t3 = MathTex(
            r'\text{for any } {{ \ell }} \in \mathbb{N},',
            color = sol.BASE03
        ).next_to(t2, RIGHT).set_color_by_tex(r'\ell', sol.GREEN)
        t4 = MathTex(
            r'o \leftrightarrow {{ \ell }}',
            color = sol.BASE03
        ).next_to(t3, RIGHT).set_color_by_tex(r'\ell', sol.GREEN).align_to(t3, UP)

        t = Group(t1, t2, t3, t4).move_to(2 * UP + 3.2 * LEFT)

        s1 = MathTex(
            r'\mathbb{P}_{{p}} [ {{ o \leftrightarrow \infty }} ]',
            color = sol.BASE03
        ).set_color_by_tex(r'p', sol.RED)
        s2 = MathTex(
            r'\leq',
            color = sol.BASE03
        ).next_to(s1, RIGHT)
        s3 = MathTex(
            r'\mathbb{P}_{{p}} [ {{ o \leftrightarrow }} {{ \ell }} ]',
            color = sol.BASE03
        ).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'\ell', sol.GREEN).next_to(s2, RIGHT)

        s = Group(s1, s2, s3).move_to(2 * UP + 3.2 * LEFT)

        self.play(FadeIn(t1))
        self.wait(2)
        self.play(FadeIn(t2), run_time=0.5)
        self.play(FadeIn(t3))
        self.wait(0.5)
        self.play(FadeIn(t4))
        self.wait(3)
        self.play(Indicate(t4))
        self.wait(5)
        self.play(
            TransformMatchingTex(t1, s1),
            TransformMatchingTex(t2, s2),
            FadeOut(t3),
            TransformMatchingTex(t4, s3)
        )
        self.wait(6)
        self.play(Indicate(s3))
        self.wait(10)

class PurpleTexBox(Scene):
    def construct(self):
        t1 = MathTex(
            r'o \leftrightarrow \infty',
            color = sol.BASE03
        )
        t2 = MathTex(
            r'\Rightarrow',
            color = sol.BASE03
        ).next_to(t1, RIGHT)
        t3 = MathTex(
            r'\text{for any } {{ \ell }} \in \mathbb{N},',
            color = sol.BASE03
        ).next_to(t2, RIGHT).set_color_by_tex(r'\ell', sol.GREEN)
        t4 = MathTex(
            r'o \leftrightarrow {{ \ell }}',
            color = sol.BASE03
        ).next_to(t3, RIGHT).set_color_by_tex(r'\ell', sol.GREEN).align_to(t3, UP)

        t = Group(t1, t2, t3, t4).move_to(2 * UP + 3.2 * LEFT)

        s1 = MathTex(
            r'\mathbb{P}_{{p}} [ {{ o \leftrightarrow \infty }} ]',
            color = sol.BASE03
        ).set_color_by_tex(r'p', sol.RED)
        s2 = MathTex(
            r'\leq',
            color = sol.BASE03
        ).next_to(s1, RIGHT)
        s3 = MathTex(
            r'\mathbb{P}_{{p}} [ {{ o \leftrightarrow }} {{ \ell }} ]',
            color = sol.BASE03
        ).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'\ell', sol.GREEN).next_to(s2, RIGHT)

        s = Group(s1, s2, s3).move_to(2 * UP + 3.2 * LEFT)

        tbox = TranslucentBox(t1)
        self.add(tbox)

        self.wait()
        self.wait(2)
        self.play(Transform(tbox, TranslucentBox(t1, t2)), run_time=0.5)
        self.play(Transform(tbox, TranslucentBox(t1, t2, t3)))
        self.wait(0.5)
        self.play(Transform(tbox, TranslucentBox(t1, t2, t3, t4)))
        self.wait(3)
        self.wait()
        self.wait(5)
        self.play(Transform(tbox, TranslucentBox(s1, s2, s3)))
        self.wait(6)
        self.wait()
        self.wait(10)

class BlueTex(Scene):
    def construct(self):
        t1 = MathTex(
            r'\mathbb{P}_{{p}} [ o \leftrightarrow {{ \ell }} ]',
            color = sol.BASE03
        ).set_color_by_tex(r'\ell', sol.GREEN).set_color_by_tex(r'p', sol.RED)
        t2 = MathTex(
            r'\leq',
            color = sol.BASE03
        ).next_to(t1, RIGHT)
        t3 = MathTex(
            r'\sum_{\substack{ {{ \gamma }} \text{ a path} \\ \text{of length } {{\ell}} }}',
            color = sol.BASE03
        ).set_color_by_tex(r'\gamma', sol.GREEN).set_color_by_tex(r'\ell', sol.GREEN).next_to(t2, RIGHT).shift(0.3 * LEFT)
        t4 = MathTex(
            r'\mathbb{P}_{{p}} [ {{\gamma}} \text{ is all open} ]',
            color = sol.BASE03
        ).set_color_by_tex(r'\gamma', sol.GREEN).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'o', sol.BASE03).next_to(t3, RIGHT).shift(0.5 * LEFT)
        t3.shift(0.35 * DOWN)

        t = Group(t1, t2, t3, t4).move_to(2 * LEFT)

        s4 = MathTex(
            r'{{p}}^{{\ell}}',
            color=sol.GREEN
        ).set_color_by_tex(r'p', sol.RED).next_to(t2, RIGHT).shift(1.2 * RIGHT + 0.1 * UP)
        
        s3 = MathTex(
            r'\cdot \, \# \{ \text{paths of length } {{\ell}}\}',
            color = sol.BASE03
        ).set_color_by_tex(r'\ell', sol.GREEN).next_to(t2, RIGHT).shift(0.5 * RIGHT)

        self.play(FadeIn(t1))
        self.wait(1.5)
        self.play(FadeIn(t2))
        self.play(FadeIn(t3))
        self.play(FadeIn(t4))
        self.wait(5)
        self.play(Indicate(t4))
        self.wait(2)
        self.play(TransformMatchingTex(t4, s4))
        self.wait(10)
        self.play(
            TransformMatchingTex(t3, s3),
            s4.animate.shift(1.2 * LEFT + 0.05 * DOWN)
        )
        self.wait(10)

class BlueTexBox(Scene):
    def construct(self):
        t1 = MathTex(
            r'\mathbb{P}_{{p}} [ o \leftrightarrow {{ \ell }} ]',
            color = sol.BASE03
        ).set_color_by_tex(r'\ell', sol.GREEN).set_color_by_tex(r'p', sol.RED)
        t2 = MathTex(
            r'\leq',
            color = sol.BASE03
        ).next_to(t1, RIGHT)
        t3 = MathTex(
            r'\sum_{\substack{ {{ \gamma }} \text{ a path} \\ \text{of length } {{\ell}} }}',
            color = sol.BASE03
        ).set_color_by_tex(r'\gamma', sol.GREEN).set_color_by_tex(r'\ell', sol.GREEN).next_to(t2, RIGHT).shift(0.3 * LEFT)
        t4 = MathTex(
            r'\mathbb{P}_{{p}} [ {{\gamma}} \text{ is all open} ]',
            color = sol.BASE03
        ).set_color_by_tex(r'\gamma', sol.GREEN).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'o', sol.BASE03).next_to(t3, RIGHT).shift(0.5 * LEFT)
        t3.shift(0.35 * DOWN)

        t = Group(t1, t2, t3, t4).move_to(2 * LEFT)

        s4 = MathTex(
            r'{{p}}^{{\ell}}',
            color=sol.GREEN
        ).set_color_by_tex(r'p', sol.RED).next_to(t2, RIGHT).shift(1.2 * RIGHT + 0.1 * UP)
        
        s3 = MathTex(
            r'\cdot \, \# \{ \text{paths of length } {{\ell}}\}',
            color = sol.BASE03
        ).set_color_by_tex(r'\ell', sol.GREEN).next_to(t2, RIGHT).shift(0.5 * RIGHT)

        tbox = TranslucentBox(t1)
        self.add(tbox)
        self.wait()
        self.wait(1.5)
        self.play(Transform(tbox, TranslucentBox(t1, t2)))
        self.play(Transform(tbox, TranslucentBox(t1, t2, t3)))
        self.play(Transform(tbox, TranslucentBox(t1, t2, t3, t4)))
        self.wait(5)
        self.wait()
        self.wait(2)
        self.play(Transform(tbox, TranslucentBox(t1, t2, t3, s4)))
        self.wait(10)
        s4.shift(1.2 * LEFT + 0.05 * DOWN)
        self.play(Transform(tbox, TranslucentBox(t1, t2, s3, s4)))
        self.wait(10)

class GreenTex(Scene):
    def construct(self):
        t1 = MathTex(
            r'\# \{ \text{paths of length } {{\ell}}\}',
            color = sol.BASE03
        ).set_color_by_tex(r'\ell', sol.GREEN)
        t2 = MathTex(
            r'\leq',
            color = sol.BASE03
        ).next_to(t1, RIGHT)
        t3 = MathTex(
            r'4 \cdot 3^{ {{ \ell }} - 1}',
            color = sol.BASE03
        ).set_color_by_tex(r'\ell', sol.GREEN).next_to(t2, RIGHT).shift(0.075 * UP)

        t = Group(t1, t2, t3).move_to(2.3 * LEFT + 1.3 * DOWN)

        self.play(FadeIn(t1))
        self.wait()
        self.play(FadeIn(t2))
        self.play(Write(t3))
        self.wait(10)

class GreenTexBox(Scene):
    def construct(self):
        t1 = MathTex(
            r'\# \{ \text{paths of length } {{\ell}}\}',
            color = sol.BASE03
        ).set_color_by_tex(r'\ell', sol.GREEN)
        t2 = MathTex(
            r'\leq',
            color = sol.BASE03
        ).next_to(t1, RIGHT)
        t3 = MathTex(
            r'4 \cdot 3^{ {{ \ell }} - 1}',
            color = sol.BASE03
        ).set_color_by_tex(r'\ell', sol.GREEN).next_to(t2, RIGHT).shift(0.075 * UP)

        t = Group(t1, t2, t3).move_to(2.3 * LEFT + 1.3 * DOWN)

        tbox = TranslucentBox(t1)
        self.add(tbox)

        self.wait()
        self.wait()
        self.play(Transform(tbox, TranslucentBox(t1, t2)))
        self.play(Transform(tbox, TranslucentBox(t1, t2, t3)))
        self.wait(10)
