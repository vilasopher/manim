from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import ValueSlider

config.background_opacity = 0

def interp(alpha):
    return np.sqrt((1 - np.cos(2 * np.pi * alpha)) / 2)

def almost_linear(alpha):
    return interp(alpha) * alpha + (1 - interp(alpha)) * (1 - np.cos(np.pi * alpha)) / 2

class ForegroundAbstract(Scene):
    def abstract_construct(self, start, end, run_time=10):
        p = ValueTracker(start)

        slider = ValueSlider(z_index = 2)
        self.add(slider)

        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.play(
            p.animate.set_value(end),
            rate_func = almost_linear,
            run_time = 10
        )

class Foreground0(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(0, 1, run_time=20)

class Foreground1(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(1, 0)

class Foreground2(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(0, 3/4)

class Foreground3(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(3/4, 1/4)

class Foreground4(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(1/4, 5/8)

class Foreground5(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(5/8, 3/8)

class Foreground6(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(3/8, 9/16)

class Foreground7(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(9/16, 7/16)

class Foreground8(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(7/16, 17/32)

class Foreground9(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(17/32, 15/32)

class Foreground10(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(15/32, 33/64)

class Foreground11(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(33/64, 31/64)
