from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import ValueSlider

config.background_opacity = 0

class SliderSmall(Scene):
    def slide(self, p, to, time):
        self.play(
            p.animate.set_value(to),
            run_time = time,
            rate_func = rate_functions.linear
        )

    def construct(self):
        p = ValueTracker(0)

        slider = ValueSlider(p=0, z_index = 2)

        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )
        self.add(slider)

        self.wait()

        self.slide(p, 1, 6)
        self.slide(p, 0, 6)
        self.slide(p, 1, 18)
        self.slide(p, 1/2, 6)
        
        self.wait(21.5 + 11)

        self.slide(p, 0, 6)
        self.slide(p, 1, 12)
        self.slide(p, 0, 12)
        self.slide(p, 1, 12)

class SliderMedium(Scene):
    def slide(self, p, to, time):
        self.play(
            p.animate.set_value(to),
            run_time = time,
            rate_func = rate_functions.linear
        )

    def construct(self):
        p = ValueTracker(0)

        slider = ValueSlider(p=0, z_index = 2)

        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.add(slider)
        self.wait()

        self.slide(p, 1, 9)
        self.slide(p, 0, 9)

class Definition(Scene):
    def construct(self):
        equiv = MathTex(
            r'\Leftrightarrow',
            color=sol.BASE03
        ).rotate(PI/2)
        text1 = MathTex(
            r'\text{an edge is in the graph at parameter } {{p}}',
            color=sol.BASE03
        ).next_to(equiv, UP)
        text2 = MathTex(
            r'\text{the number at that potential edge is} < {{p}}',
            color=sol.BASE03
        ).next_to(equiv, DOWN)
        text1.set_color_by_tex(r'p', sol.RED)
        text1.set_color_by_tex(r'a', sol.BASE03)
        text2.set_color_by_tex(r'p', sol.RED)
        text2.set_color_by_tex(r'a', sol.BASE03)
        text1.shift(0.81 * LEFT)
        text2.shift(0.81 * LEFT)
        equiv.shift(0.81 * LEFT)
        t = Group(text1, text2, equiv)
        tbox = TranslucentBox(t)
        self.add(tbox, t)

class Equivalence(Scene):
    def construct(self):
        p = MathTex(r'= \; {{ p }} \; = ', color=sol.BASE03).shift(0.81 * LEFT)
        text1 = MathTex(
            r'\mathbb{P}[\text{a uniform random number between } 0 \text{ and } 1 \text{ is} < {{ p }} ]',
            color = sol.BASE03
        ).next_to(p, UP)
        text2 = MathTex(
            r'\mathbb{P}_{{ p }} [\text{an edge is open}]',
            color=sol.BASE03
        ).next_to(p, DOWN)
        p.set_color_by_tex(r'p', sol.RED)
        p.set_color_by_tex(r'=', sol.BASE03)
        text1.set_color_by_tex(r'p', sol.RED)
        text1.set_color_by_tex(r'a', sol.BASE03)
        text2.set_color_by_tex(r'p', sol.RED)
        text2.set_color_by_tex(r'a', sol.BASE03)
        t = Group(p, text1, text2)
        tbox = TranslucentBox(t)
        self.add(tbox, t)

class MonotoneUniformCouplingForeground(Scene):
    def construct(self):
        mc = MathTex(
            r'{{ \text{Monotone} }} {{ \text{ Coupling} }}',
            color=sol.BASE03,
            font_size = 100,
            z_index = 2
        ).shift(0.81 * LEFT)
        mtbox = TranslucentBox(mc)

        uc = MathTex(
            r'{{ \text{Uniform} }} {{ \text{ Coupling} }}',
            color=sol.BASE03,
            font_size = 100,
            z_index = 2
        ).shift(0.81* LEFT)
        utbox = TranslucentBox(uc)

        self.add(mc)
        self.wait(10)
        self.play(TransformMatchingTex(mc, uc))
        self.wait(10)

class MonotoneUniformCouplingBackground(Scene):
    def construct(self):
        mc = MathTex(
            r'{{ \text{Monotone} }} {{ \text{ Coupling} }}',
            color=sol.BASE03,
            font_size = 100,
            z_index = 2
        ).shift(0.81 * LEFT)
        mtbox = TranslucentBox(mc)

        uc = MathTex(
            r'{{ \text{Uniform} }} {{ \text{ Coupling} }}',
            color=sol.BASE03,
            font_size = 100,
            z_index = 2
        ).shift(0.81* LEFT)
        utbox = TranslucentBox(uc)

        self.add(mtbox)
        self.wait(10)
        self.play(Transform(mtbox, utbox))
        self.wait(10)
