from manim import *
import random
from cluster_image import ClusterImage
from value_slider import ValueSlider
import numpy as np

class FirstFrameBackground(Scene):
    def construct(self):
        random.seed(2)
        c = ClusterImage((720,1280), 1)
        self.add(c)

def interp(alpha):
    return np.sqrt((1 - np.cos(2 * np.pi * alpha)) / 2)

def almost_linear(alpha):
    return interp(alpha) * alpha + (1 - interp(alpha)) * (1 - np.cos(np.pi * alpha)) / 2

class BackgroundAbstract(Scene):
    def abstract_construct(self, start, end):
        random.seed(2) # good ones: 1 = green, 2 = blue

        p = ValueTracker(start if start < end else end)

        c = ClusterImage((720,1280), p=p.get_value())
        self.add(c)

        slider = ValueSlider(z_index = 2)
        #self.add(slider) TODO

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

class Background0(BackgroundAbstract):
    def construct(self):
        self.abstract_construct(0, 1)

class REVERSEDBackground1(BackgroundAbstract):
    def construct(self):
        self.abstract_construct(0, 1)

class Background2(BackgroundAbstract):
    def construct(self):
        self.abstract_construct(0, 3/4)

class REVERSEDBackground3(BackgroundAbstract):
    def construct(self):
        self.abstract_construct(3/4, 1/4)

class Background4(BackgroundAbstract):
    def construct(self):
        self.abstract_construct(1/4, 5/8)

class REVERSEDBackground5(BackgroundAbstract):
    def construct(self):
        self.abstract_construct(5/8, 3/8)

class Background6(BackgroundAbstract):
    def construct(self):
        self.abstract_construct(3/8, 9/16)

class REVERSEDBackground7(BackgroundAbstract):
    def construct(self):
        self.abstract_construct(9/16, 7/16)
