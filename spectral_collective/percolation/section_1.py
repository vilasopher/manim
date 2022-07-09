from manim import *
import random
from cluster_image import ClusterImage
from value_slider import ValueSlider

class SpoilerBackgroundAbstract(Scene):
    def abstract_construct(self, start, end):
        random.seed(2) # good ones: 1 = green, 2 = blue

        p = ValueTracker(start if start < end else end)

        c = ClusterImage((720,1280), p=p.get_value())
        self.add(c)

        slider = ValueSlider(z_index = 2)
        self.add(slider)

        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        c.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.play(
            p.animate.set_value(end if start < end else start),
            rate_func = rate_functions.linear,
            run_time = 10
        )

class SpoilerBackground1(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(0, 1)

class SpoilerBackground2(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(0, 3/4)

class SpoilerBackground3(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(3/4, 1/4)

class SpoilerBackground4(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(1/4, 5/8)

class SpoilerBackground5(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(5/8, 3/8)

class SpoilerBackground6(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(3/8, 9/16)

class SpoilerBackground7(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(9/16, 7/16)
