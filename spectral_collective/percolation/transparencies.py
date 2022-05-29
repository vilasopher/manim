from manim import *
import solarized as sol
from value_slider import ValueSlider, CriticalValueSlider

config.background_opacity = 0

class TransparencyTest(Scene):
    def construct(self):
        slider = CriticalValueSlider(0.75)

        bg = Rectangle(width=11.5, height=7, color=sol.BASE2)
        bg.set_fill(sol.BASE3, opacity=0.95)
        bg.move_to(0.6111111 * LEFT)

        self.add(slider, bg)

        self.wait()
        self.play(slider.animate.add_crit())
        self.wait()

