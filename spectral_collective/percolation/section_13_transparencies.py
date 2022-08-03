from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import CriticalValueSlider
from glitch import Glitch
from math import sqrt

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
            finala.animate.shift(2.5 * UP)
        )
        self.wait(27)
        self.play(
            finala.animate.shift(3.5 * UP),
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
        self.play(tbox.animate.shift(2.5 * UP))
        self.wait(27)
        self.play(tbox.animate.shift(3.5 * UP))

class PcDefinition(Scene):
    def construct(self):
        tmp = TexTemplate()
        tmp.add_to_preamble(r'\usepackage{mathtools}')
        d = MathTex(
            r'{{p_c}} \coloneqq \sup \, \{ {{p}} \in [0, 1] : \mathbb{P}_{{p}}[o \leftrightarrow \infty] = 0 \}',
            color=sol.BASE03,
            tex_template=tmp
        ).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'p_c', sol.BLUE).set_color_by_tex(r's', sol.BASE03).move_to(2.5*UP)
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

        thm = Group(thm1, thm2, thm3).move_to(2.5 * UP + 3.5 * UP)
        tbox = TranslucentBox(thm)

        self.play(
            tbox.animate.shift(3.5 * DOWN),
            thm.animate.shift(3.5 * DOWN)
        )
        self.wait(1.5)

        self.play(Indicate(thm2))
        self.play(Indicate(thm3))

        self.wait(3.3)

        self.play(Indicate(thm1c), run_time=3)

        self.wait(10)

def theta(pc, p):
    if p < pc or pc == 1:
        return 0
    else:
        return (sqrt((p - pc)/(1 - pc) + 1/3) - sqrt(1/3)) / (sqrt(1 + 1/3) - sqrt(1/3))

class Plot(Scene):
    def construct(self):
        ax = Axes(
            x_range = [0, 1, 1],
            y_range = [0, 1, 1],
            x_length = 10,
            y_length = 3,
            axis_config = {'color' : sol.BASE03},
            tips=False
        )

        pc = ValueTracker(0.5)

        plt = ax.plot(
            lambda p : theta(pc.get_value(), p),
            x_range = [0, 1, 0.005],
            color=sol.BASE02,
            discontinuities=[pc.get_value()],
            use_smoothing=False
        )

        plt.add_updater(
            lambda s : s.become(
                ax.plot(
                    lambda p : theta(pc.get_value(), p),
                    x_range = [0, 1, 0.005],
                    color=sol.BASE02,
                    discontinuities=[pc.get_value()],
                    use_smoothing=False
                )
            )
        )

        pt0 = Dot(ax.coords_to_point(0,0), color=sol.BASE02, radius=0.05)
        pt1 = Dot(ax.coords_to_point(1,1), color=sol.BASE02, radius=0.05)

        lab = ax.get_axis_labels(
            x_label = MathTex(r'p', color=sol.RED),
            y_label = MathTex(
                r'\mathbb{P}_{{p}}[o \leftrightarrow \infty]',
                color=sol.BASE03
            ).set_color_by_tex(r'p', sol.RED)
        )


        plot = Group(ax, plt, pt0, pt1, lab).move_to(DOWN)

        crit = Square(
            0.1 / sqrt(2),
            color=sol.BLUE
        ).rotate(PI/4).set_fill(
            sol.BLUE,
            opacity=1
        ).move_to(ax.coords_to_point(pc.get_value(), 0))

        crit.add_updater(
            lambda s : s.move_to(ax.coords_to_point(pc.get_value(), 0))
        )

        pctex = MathTex(r'p_c', color=sol.BLUE).next_to(crit, DOWN)

        pctex.add_updater(
            lambda s : s.next_to(crit, DOWN)
        )

        pcrit = Group(crit, pctex)

        tbox = TranslucentBox(plot, pcrit)

        self.add(tbox, ax, lab)

        self.wait()

        self.play(
            Create(plt),
            FadeIn(pt0),
            FadeIn(pt1),
            run_time=2
        )

        self.wait(25)

        self.play(FadeIn(pcrit))

        self.wait(16.5)

        self.play(pc.animate.set_value(0))
        self.play(pc.animate.set_value(1), run_time=2)

        self.wait(2)
        self.play(pc.animate.set_value(0), run_time=2)
        self.wait(2)
        self.play(pc.animate.set_value(1), run_time=2)
        self.wait(2)
        self.play(pc.animate.set_value(0), run_time=2)
        self.wait(2)
        self.play(pc.animate.set_value(1), run_time=2)
        self.wait(2)
        self.play(pc.animate.set_value(0), run_time=2)
        self.wait(2)
        self.play(pc.animate.set_value(1), run_time=2)
        self.wait(2)
        self.play(pc.animate.set_value(0), run_time=2)
        self.wait(2)
        self.play(pc.animate.set_value(1), run_time=2)

occlusion_top = Rectangle(height=4, width=15, color = sol.BASE3).set_fill(sol.BASE3, opacity=1).move_to(4 * UP)
occlusion_bottom = Rectangle(height=2, width=15, color = sol.BASE3).set_fill(sol.BASE3, opacity=1).move_to(4 * DOWN)
occlusion_left = Rectangle(height=9, width=8, color = sol.BASE3).set_fill(sol.BASE3, opacity=1).move_to(7 * LEFT)
occlusion_right = Rectangle(height=9, width=2, color = sol.BASE3).set_fill(sol.BASE3, opacity=1).move_to(7 * RIGHT)
occlusion_frame = Rectangle(height=5, width=9, color = sol.BASE0).move_to(1.5 * RIGHT + 0.5 * DOWN)
occlusion = Group(occlusion_top, occlusion_bottom, occlusion_left, occlusion_right, occlusion_frame)

translucent_occlusion_text = Rectangle(height = 1.5, width=14, color = sol.BASE3).set_fill(sol.BASE3, opacity=0.9).move_to(3 * UP)
translucent_occlusion_f = Rectangle(height = 2, width=3.5, color = sol.BASE3).set_fill(sol.BASE3, opacity=0.9).move_to(5 * LEFT)
translucent_occlusion_frame = Rectangle(height=5, width=9, color=sol.BASE2).move_to(1.5 * RIGHT + 0.5 * DOWN)
trocl = Group(translucent_occlusion_text, translucent_occlusion_f, translucent_occlusion_frame)


class Function(Scene):
    def construct(self):
        self.add(occlusion)

        t = Tex(
            r'Uniform Coupling $\Leftrightarrow$ random \emph{function} $\mathbf{f} : [0, 1] \to \{$graphs$\}$',
            color = sol.BASE03
        ).move_to(3 * UP)

        self.add(t)

        f = MathTex(
            r'\mathbf{f}( \quad \; \; ) =',
            color = sol.BASE03,
            font_size = 70
        ).move_to(4.65 * LEFT + 0.5 * DOWN)

        pd = DecimalNumber(0.5, color = sol.BASE03, font_size = 70).next_to(f, RIGHT).shift(2.45 * LEFT)

        p = ValueTracker(0.5)

        pd.add_updater(
            lambda s : s.set_value(p.get_value())
        )

        self.add(f, p, pd)


        self.play(p.animate.set_value(1), run_time=2, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(0), run_time=4, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(1), run_time=4, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(0.5), run_time=2, rate_func=rate_functions.linear)

        self.wait(2.5)

        self.play(Glitch(f))

        self.wait(2 + 2/3)

        self.play(Glitch(f))
        
        self.wait(2 + 2/3)

        self.play(Glitch(f))

        self.wait(2 + 2/3)

        self.play(Glitch(f))

        self.wait(1.5)

        self.play(p.animate.set_value(0), run_time=3, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(1), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(2/3), run_time=2, rate_func=rate_functions.linear)
        self.play(
            p.animate.set_value(1/3),
            FadeIn(trocl),
            run_time=2,
            rate_func=rate_functions.linear
        )
        self.play(p.animate.set_value(0), run_time=2, rate_func=rate_functions.linear)

        self.play(p.animate.set_value(1), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(0), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(1), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(0), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(1), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(0), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(1), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(0), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(1), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(0), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(1), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(0), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(1), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(0), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(1), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(0), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(1), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(0), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(1), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(0), run_time=6, rate_func=rate_functions.linear)
        self.play(p.animate.set_value(1), run_time=6, rate_func=rate_functions.linear)
