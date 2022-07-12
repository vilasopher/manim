from manim import *
import random
from cluster_image import ClusterImage
from value_slider import ValueSlider
import numpy as np

def interp(alpha):
    return np.sqrt((1 - np.cos(2 * np.pi * alpha)) / 2)

def almost_linear(alpha):
    return interp(alpha) * alpha + (1 - interp(alpha)) * (1 - np.cos(np.pi * alpha)) / 2

class SpoilerBackgroundAbstract(Scene):
    def abstract_construct(self, start, end, run_time=10):
        random.seed(1) # good ones: 1 = green, 2 = blue

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
            rate_func = almost_linear,
            run_time = 10
        )

class SpoilerBackground0(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(0, 1, run_time=20)

class SpoilerBackground1BACKWARDS(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(1, 0)

class SpoilerBackground2(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(0, 3/4)

class SpoilerBackground3BACKWARDS(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(3/4, 1/4)

class SpoilerBackground4(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(1/4, 5/8)

class SpoilerBackground5BACKWARDS(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(5/8, 3/8)

class SpoilerBackground6(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(3/8, 9/16)

class SpoilerBackground7BACKWARDS(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(9/16, 7/16)

class SpoilerBackground8(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(7/16, 17/32)

class SpoilerBackground9BACKWARDS(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(17/32, 15/32)

class SpoilerBackground10(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(15/32, 33/64)

class SpoilerBackground11BACKWARDS(SpoilerBackgroundAbstract):
    def construct(self):
        self.abstract_construct(33/64, 31/64)
