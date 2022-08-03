from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import ValueSlider

config.background_opacity = 0

def interp(alpha):
    return np.sqrt((1 - np.cos(2 * np.pi * alpha)) / 2)

def almost_linear(alpha):
    return interp(alpha) * alpha + (1 - interp(alpha)) * (1 - np.cos(np.pi * alpha)) / 2

class SliderForward(Scene):
    def construct(self):
        p = ValueTracker(0)
        v = ValueSlider(p.get_value())
        v.add_updater(
            lambda s : s.set_p(p.get_value())
        )
        self.add(v)

        self.play(
            p.animate.set_value(1),
            run_time=10,
            rate_func=almost_linear
        )

class SliderBackward(Scene):
    def construct(self):
        p = ValueTracker(1)
        v = ValueSlider(p.get_value())
        v.add_updater(
            lambda s : s.set_p(p.get_value())
        )
        self.add(v)

        self.play(
            p.animate.set_value(0),
            run_time=10,
            rate_func=almost_linear
        )


class ThreeDCaption(Scene):
    def construct(self):
        tex1 = Tex(r'Exploring a cluster in near-critical', color=sol.BASE03, font_size=33)
        tex2 = Tex(r'percolation on the cubic lattice.', color=sol.BASE03, font_size=33)
        tex2.next_to(tex1, DOWN).align_to(tex1, LEFT).shift(0.1 * RIGHT + 0.2 * UP)
        t = Group(tex1, tex2).move_to(3.2 * UP + 4.05 * LEFT)
        self.add(TranslucentBox(t, margin=0.15), t)

class ThreeDPC(Scene):
    def construct(self):
        tex1 = Tex(r'critical parameter $= 0.24881...$', font_size=35, color=sol.BASE03)
        tex2 = Tex(r'(from numerical simulations)', color=sol.BASE03, font_size=33)
        tex2.next_to(tex1, DOWN).shift(0.2 * UP)
        t = Group(tex1, tex2).move_to(3.15 * UP + 4.15 * RIGHT)
        self.add(TranslucentBox(t, margin=0.15), t)
