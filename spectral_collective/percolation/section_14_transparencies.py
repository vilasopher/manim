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
            r'\text{for any } {{ \ell }} \in \mathbb{N}',
            color = sol.BASE03
        ).next_to(t2, RIGHT).set_color_by_tex(r'\ell', sol.GREEN)
        t4 = MathTex(
            r'o \leftrightarrow \ell',
            color = sol.BASE03
        ).next_to(t3, RIGHT).set_color_by_tex(r'\ell', sol.GREEN)

        t = Group(t1, t2, t3, t4).move_to(2 * UP)

        s1 = MathTex(
            r'\mathbb{P}_{{p}} [ {{ o \leftrightarrow \infty }} ]',
            color = sol.BASE03
        ).set_color_by_tex(r'p', sol.RED)
        s2 = MathTex(
            r'\leq',
            color = sol.BASE03
        ).next_to(s1, RIGHT)
        s3 = MathTex(
            r'\mathbb{P}_{{p}} [ {{ o \leftrightarrow \ell }} ]',
            color = sol.BASE03
        ).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'\ell', sol.GREEN).next_to(s3, RIGHT)

        s = Group(s1, s2, s3).move_to(2 * UP)

