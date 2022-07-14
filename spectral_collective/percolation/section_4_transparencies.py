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
