from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import CriticalValueSlider
import math

config.background_opacity = 0

class IncreasingTex(Scene):
    def construct(self):
        t1a = MathTex(
            r'\text{If } {{ p_1 }} < {{ p_2 }},',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED)
        t1b = MathTex(r'\text{ then}', color=sol.BASE03).next_to(t1a, RIGHT)
        t1 = Group(t1a, t1b)

        t2a = MathTex(
            r'{{ o \leftrightarrow \infty }} {{ \text{ in } \mathbf{f}( }} {{ {p_1} }} {{ ) }}',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED)
        t2b = MathTex(
            r'\Rightarrow',
            color=sol.BASE03
        ).next_to(t2a, RIGHT)
        t2c = MathTex(
            r'{{ o \leftrightarrow \infty }} {{ \text{ in } \mathbf{f}( }} {{ {p_2} }} {{ ) }}',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED).next_to(t2b, RIGHT)

        t2 = Group(t2a, t2b, t2c).next_to(t1, DOWN)

        t3a = MathTex(
            r'{{ \mathbb{P} }} {{ [ }} {{ o \leftrightarrow \infty }} {{ \text{ in } \mathbf{f}( }} {{ {p_1} }} {{ ) }} {{ ] }}',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED)
        t3b = MathTex(
            r'\leq',
            color=sol.BASE03
        ).next_to(t3a, RIGHT)
        t3c = MathTex(
            r'{{ \mathbb{P} }} {{ [ }} {{ o \leftrightarrow \infty }} {{ \text{ in } \mathbf{f}( }} {{ {p_2} }} {{ ) }} {{ ] }} ',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED).next_to(t3b, RIGHT)

        t3 = Group(t3a, t3b, t3c).next_to(t1, DOWN)

        t4a = MathTex(
            r'{{ \mathbb{P} }} _ {{ {p_1} }} {{ [ }}  {{ o \leftrightarrow \infty }} {{ ] }}',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED).next_to(t3b, LEFT)
        t4c = MathTex(
            r'{{ \mathbb{P} }} _ {{ {p_2} }} {{ [ }}  {{ o \leftrightarrow \infty }} {{ ] }}',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED).next_to(t3b, RIGHT)

        t4 = Group(t4a, t4c)

        a = Group(t1, t2, t3, t4).move_to(ORIGIN)

        finala = Group(t1, t4, t3b)

        self.add(t1a)
        self.wait(2)
        self.play(FadeIn(t1b), FadeIn(t2a))
        self.wait(3)
        self.play(FadeIn(t2b), FadeIn(t2c))
        self.wait(4.5)
        self.play(
            TransformMatchingTex(t2a, t3a),
            TransformMatchingTex(t2b, t3b),
            TransformMatchingTex(t2c, t3c)
        )
        self.wait(12)
        self.play(
            TransformMatchingTex(t3a, t4a),
            TransformMatchingTex(t3c, t4c)
        )
        self.wait(7)
        self.play(
            finala.animate.shift(2 * UP)
        )
        self.wait(27)
        self.play(
            finala.animate.shift(4 * UP),
        )

class IncreasingTexBox(Scene):
    def construct(self):
        t1a = MathTex(
            r'\text{If } {{ p_1 }} < {{ p_2 }},',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED)
        t1b = MathTex(r'\text{ then}', color=sol.BASE03).next_to(t1a, RIGHT)
        t1 = Group(t1a, t1b)

        t2a = MathTex(
            r'{{ o \leftrightarrow \infty }} {{ \text{ in } \mathbf{f}( }} {{ {p_1} }} {{ ) }}',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED)
        t2b = MathTex(
            r'\Rightarrow',
            color=sol.BASE03
        ).next_to(t2a, RIGHT)
        t2c = MathTex(
            r'{{ o \leftrightarrow \infty }} {{ \text{ in } \mathbf{f}( }} {{ {p_2} }} {{ ) }}',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED).next_to(t2b, RIGHT)

        t2 = Group(t2a, t2b, t2c).next_to(t1, DOWN)

        t3a = MathTex(
            r'{{ \mathbb{P} }} {{ [ }} {{ o \leftrightarrow \infty }} {{ \text{ in } \mathbf{f}( }} {{ {p_1} }} {{ ) }} {{ ] }}',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED)
        t3b = MathTex(
            r'\leq',
            color=sol.BASE03
        ).next_to(t3a, RIGHT)
        t3c = MathTex(
            r'{{ \mathbb{P} }} {{ [ }} {{ o \leftrightarrow \infty }} {{ \text{ in } \mathbf{f}( }} {{ {p_2} }} {{ ) }} {{ ] }} ',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED).next_to(t3b, RIGHT)

        t3 = Group(t3a, t3b, t3c).next_to(t1, DOWN)

        t4a = MathTex(
            r'{{ \mathbb{P} }} _ {{ {p_1} }} {{ [ }}  {{ o \leftrightarrow \infty }} {{ ] }}',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED).next_to(t3b, LEFT)
        t4c = MathTex(
            r'{{ \mathbb{P} }} _ {{ {p_2} }} {{ [ }}  {{ o \leftrightarrow \infty }} {{ ] }}',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED).next_to(t3b, RIGHT)

        t4 = Group(t4a, t4c)

        a = Group(t1, t2, t3, t4).move_to(ORIGIN)

        tbox = TranslucentBox(t1a)
        self.add(tbox)
        self.wait(2)
        self.play(Transform(tbox, TranslucentBox(t1, t2a)))
        self.wait(3)
        self.play(Transform(tbox, TranslucentBox(t1, t2)))
        self.wait(4.5)
        self.play(Transform(tbox, TranslucentBox(t1, t3)))
        self.wait(12)
        self.play(Transform(tbox, TranslucentBox(t1, t3b, t4)))
        self.wait(7)
        self.play(tbox.animate.shift(2 * UP))
        self.wait(27)
        self.play(tbox.animate.shift(4 * UP))

class PcDefinition(Scene):
    def construct(self):
        tmp = TexTemplate()
        tmp.add_to_preamble(r'\usepackage{mathtools}')
        d = MathTex(
            r'{{p_c}} \coloneqq \sup \, \{ {{p}} \in [0, 1] : \mathbb{P}_{{p}}[o \leftrightarrow \infty] = 0 \}',
            color=sol.BASE03,
            tex_template=tmp
        ).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'p_c', sol.BLUE).set_color_by_tex(r's', sol.BASE03).move_to(2*UP)
        td = TranslucentBox(d)

        self.add(td, d)

class Theorem(Scene):
    def construct(self):
        thm1a = MathTex(r'\textbf{Theorem: }', color=sol.BASE03)
        thm1b = MathTex(r'\text{there exists }', color=sol.BASE03).next_to(thm1a, RIGHT)
        thm1c = MathTex(r'{{p_c}} \in (0,1)', color=sol.BASE03).next_to(thm1b, RIGHT)
        thm1c.set_color_by_tex(r'p_c', sol.BLUE)
        thm1d = MathTex(r'\text{ such that}', color=sol.BASE03).next_to(thm1c, RIGHT)

        thm1 = Group(thm1a, thm1b, thm1c, thm1d)

        thm2a = MathTex(r'\text{for } {{p}} < {{p_c}} \text{, }', color=sol.BASE03)
        thm2a.set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'p_c', sol.BLUE)
        thm2b = MathTex(r'\mathbb{P}_{{p}}[o \leftrightarrow \infty] = 0', color=sol.BASE03).next_to(thm2a, RIGHT)
        thm2b.set_color_by_tex(r'p', sol.RED)
        thm2c = MathTex(r'\text{, and}', color=sol.BASE03).next_to(thm2b, RIGHT).shift(0.15 * LEFT)

        thm2 = Group(thm2a, thm2b, thm2c).next_to(thm1, DOWN).align_to(thm1, LEFT).shift(RIGHT)
    
        thm3a = MathTex(r'\text{for } {{p}} > {{p_c}} \text{, }', color=sol.BASE03)
        thm3a.set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'p_c', sol.BLUE)
        thm3b = MathTex(r'\mathbb{P}_{{p}}[o \leftrightarrow \infty] > 0 \text{.}', color=sol.BASE03).next_to(thm3a, RIGHT)
        thm3b.set_color_by_tex(r'p', sol.RED)

        thm3 = Group(thm3a, thm3b).next_to(thm2, DOWN).align_to(thm2, LEFT)

        thm = Group(thm1, thm2, thm3).move_to(2.5 * UP + 4 * UP)
        tbox = TranslucentBox(thm)

        self.play(
            tbox.animate.shift(4 * DOWN),
            thm.animate.shift(4 * DOWN)
        )
        self.wait(1.5)

        self.play(Indicate(thm2))
        self.play(Indicate(thm3))

        self.wait(3.3)

        self.play(Indicate(thm1c), run_time=3)

        self.wait(10)

def theta(pc, p):
    if p <= pc:
        return 0
    else:
        if pc == 1:
            return 1
        else:
            return math.sqrt((p - pc)/(1 - pc))

class Plot(Scene):
    def construct(self):
        ax = Axes(
            x_range = [0, 1, 1],
            y_range = [0, 1, 1],
            x_length = 8,
            y_length = 4,
            axis_config = {"color" : sol.BASE03},
            tips=False
        )

        pc = ValueTracker(0.9)

        theta_below = ax.plot(
            lambda p : theta(pc.get_value(), p),
            t_range = [0, pc.get_value()],
            color=sol.BASE02,
            discontinuities=[pc.get_value()]
        )

        theta_above = ax.plot(
            lambda p : theta(pc.get_value(), p),
            t_range = [pc.get_value(), 1],
            color=sol.BASE02,
            discontinuities=[pc.get_value()]
        )

        theta_below.add_updater(
            lambda s : s.become(
                ax.plot(
                    lambda p : theta(pc.get_value(), p),
                    t_range = [0, pc.get_value()],
                    color=sol.BASE02,
                    discontinuities=[pc.get_value()]
                )
            )
        )

        theta_above.add_updater(
            lambda s : s.become(
                ax.plot(
                    lambda p : theta(pc.get_value(), p),
                    t_range = [pc.get_value(), 1],
                    color=sol.BASE02,
                    discontinuities=[pc.get_value()]
                )
            )
        )

        plot = Group(ax, theta_below, theta_above)
        tbox = TranslucentBox(plot)
        self.add(tbox, plot)

        self.wait()
        self.play(pc.animate.set_value(0.1), run_time=5)
        self.wait()
