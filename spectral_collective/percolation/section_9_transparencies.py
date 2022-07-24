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
