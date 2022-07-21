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
    pass #TODO

class MonotoneCoupling(Scene):
    pass #TODO

class UniformCoupling(Scene):
    pass #TODO
