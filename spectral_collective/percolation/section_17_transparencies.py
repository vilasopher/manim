from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import CriticalValueSlider, ValueSlider
import math
from numpy import sqrt

config.background_opacity = 0

#################################################

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

thm = Group(thm1, thm2, thm3).move_to(2 * UP)
thmbox = TranslucentBox(thm)
thmgp = Group(thmbox, thm)

#################################################

pcbound = MathTex(
    r'1/3 \leq {{ p_c }} \leq 2/3',
    color = sol.BASE03,
    font_size = 80
).set_color_by_tex(r'p_c', sol.BLUE).shift(DOWN)

pceq = MathTex(
    r'\text{To prove that } {{ p_c }} = 1/2...',
    color = sol.BASE03,
    font_size = 80
).set_color_by_tex(r'p_c', sol.BLUE).shift(2.75 * UP)

#################################################

tex1 = Tex(
    r'In most cases,',
    color = sol.BASE03
)

tex2 = Tex(
    r'primal percolation is large (has an infinite cluster)',
    color = sol.BASE03
).next_to(tex1, DOWN)

tex3 = MathTex(
    r'\Leftrightarrow',
    color = sol.BASE03
).next_to(tex2, DOWN)

tex4 = Tex(
    r'dual percolation is small (has no infinite cluster)',
    color = sol.BASE03
).next_to(tex3, DOWN)

tex = Group(tex1, tex2, tex3, tex4).move_to(DOWN)

#################################################

#config.background_opacity = 1
class Test(Scene):
    def construct(self):
        #self.add(thm, pcbound)
        self.add(pceq, tex)

#################################################

class Theorem(Scene):
    def construct(self):
        thmgp.shift(4 * UP)
        self.add(thmgp)
        self.play(thmgp.animate.shift(4 * DOWN))
        self.wait(19)
        self.play(thmgp.animate.shift(4 * UP))

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

        primal = ax.plot(
            lambda p : theta(pc.get_value(), p),
            x_range = [0, 1, 0.005],
            color=sol.BASE02,
            discontinuities=[pc.get_value()],
            use_smoothing=False
        )

        dual = ax.plot(
            lambda p : theta(pc.get_value(), 1-p),
            x_range = [0, 1, 0.005],
            color = sol.CYAN,
            discontinuities=[1-pc.get_value()],
            use_smoothing=False
        )

        primal.add_updater(
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

        dual.add_updater(
            lambda s : s.become(
                ax.plot(
                    lambda p : theta(pc.get_value(), 1-p),
                    x_range = [0, 1, 0.005],
                    color = sol.CYAN,
                    discontinuities=[1-pc.get_value()],
                    use_smoothing=False
                )
            )
        )

        ppt0 = Dot(ax.coords_to_point(0,0), color=sol.BASE02, radius=0.05)
        ppt1 = Dot(ax.coords_to_point(1,1), color=sol.BASE02, radius=0.05)

        dpt0 = Dot(ax.coords_to_point(0,1), color=sol.CYAN, radius=0.05)
        dpt1 = Dot(ax.coords_to_point(1,0), color=sol.CYAN, radius=0.05)

        lab = ax.get_axis_labels(
            x_label = MathTex(r'p', color=sol.RED),
            y_label = MathTex(
                r'\mathbb{P}_{1-{{p}}} [o \leftrightarrow \infty] {{\qquad \qquad \qquad \qquad \quad}} ',
                r'\mathbb{P \hspace{0em} }_{{p}} \hspace{0em} [o \leftrightarrow \infty]',
                color = sol.CYAN
            ).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'0', sol.BASE02)
        )

        plot = Group(
            ax,
            primal,
            dual,
            ppt0,
            ppt1,
            dpt0,
            dpt1,
            lab,
        ).move_to(0.5 * DOWN)

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


        brace = BraceBetweenPoints(
            ax.coords_to_point(1/3,0),
            ax.coords_to_point(2/3,0),
            color = sol.BASE03
        ).shift(0.1 * UP)
        largebracelabel = Tex(r'both are large', color=sol.BASE03, font_size=33).next_to(brace, DOWN).shift(0.1 * UP)
        smallbracelabel = Tex(r'both are small', color=sol.BASE03, font_size=33).next_to(brace, DOWN).shift(0.1 * UP)

        tbox = TranslucentBox(plot, pcrit, brace, largebracelabel, smallbracelabel)

        self.add(tbox, ax)

        self.wait(5)

        self.play(
            LaggedStart(
                AnimationGroup(Create(primal), Create(ppt0), Create(ppt1)),
                AnimationGroup(Create(dual), Create(dpt0), Create(dpt1)),
                AnimationGroup(FadeIn(lab), Create(crit), FadeIn(pctex))
            ),
            run_time = 1.5
        )

        self.wait(0.5)

        self.play(pc.animate.set_value(1/3))

        self.wait(2.5)

        self.play(
            FadeIn(brace),
            FadeIn(largebracelabel)
        )

        self.wait(3.5)

        self.play(
            FadeOut(brace),
            FadeOut(largebracelabel),
            run_time = 0.5
        )

        self.play(pc.animate.set_value(2/3))

        self.wait(2.5)

        self.play(
            FadeIn(brace),
            FadeIn(smallbracelabel)
        )

        self.wait(3)

        self.play(
            FadeOut(brace),
            FadeOut(smallbracelabel),
            run_time = 0.5
        )

        self.play(pc.animate.set_value(1/2))

        self.wait(10)
