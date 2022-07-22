from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import ValueSlider

config.background_opacity = 0

class Slider(Scene):
    def construct(self):
        p = ValueTracker(0.5)

        slider = ValueSlider(z_index = 2)
        self.add(slider)

        self.wait()

        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        ivalues = [ 6, 7, 9, 10, 11, 8, 5, 3, 2,
                    1, 4, 6, 8, 10, 11,
                    9, 5, 7, 3 ]

        for i in ivalues:
            self.play(p.animate.set_value(i/12), run_time=0.5)
            self.wait(2.5)

        self.wait(0.5)

class PpDefinition(Scene):
    def construct(self):
        Pp = MathTex(
            r'&\mathbb{P}_ {{ p }} [A] \phantom{= \text{the probability that}} \\',
            r'&\phantom{\text{event } A \text{ occurs in Bernoulli}} \\',
            r'&\phantom{\text{percolation with parameter } p}',
            color=sol.BASE03
        )
        eq = MathTex(
            r'&\phantom{\mathbb{P}_p[A]} = \text{the probability that} \\',
            r'&\text{event } A \text{ occurs in Bernoulli} \\',
            r'&\text{percolation with parameter } {{ p }}',
            color=sol.BASE03
        ).shift(0.81 * LEFT)
        Pp.align_to(eq, UP + LEFT)
        Pp.set_color_by_tex(r'p', sol.RED)
        Pp.set_color_by_tex(r'[', sol.BASE03)
        eq.set_color_by_tex(r'p', sol.RED)
        eq.set_color_by_tex(r'a', sol.BASE03)
        tbox = TranslucentBox(eq)
        self.add(tbox, Pp, eq)
        self.wait(5)
        self.play(Indicate(Pp))
        self.wait(15)
