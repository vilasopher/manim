from manim import *
import random
from cluster_image import ClusterImage
from value_slider import ValueSlider
import numpy as np

def interp(alpha):
    return np.sqrt((1 - np.cos(2 * np.pi * alpha)) / 2)

def almost_linear(alpha):
    return interp(alpha) * alpha + (1 - interp(alpha)) * (1 - np.cos(np.pi * alpha)) / 2

class BackgroundCritical(Scene):
    def construct(self)
        random.seed(50) # good ones: 1 = green, 2 = blue
        c = ClusterImage((720,1280), 0.5)
        self.add(c)

class BackgroundAbstract(Scene):
    def abstract_construct(self, start, end, time=10):
        random.seed(50) # good ones: 1 = green, 2 = blue

        p = ValueTracker(start if start < end else end)

        c = ClusterImage((720,1280), p=p.get_value())
        self.add(c)

        c.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.play(
            p.animate.set_value(end if start < end else start),
            rate_func = almost_linear,
            run_time = time
        )

class BackgroundFullForwards(BackgroundAbstract):
    def construct(self):
        self.construct_abstract(0, 1)

class REVERSEDBackgroundFullBackwards(BackgroundAbstract):
    def construct(self):
        self.construct_abstract(1, 0)

class BackgroundZeroToHalf(BackgroundAbstract):
    def construct(self):
        self.construct_abstract(0, 1/2, time=5)

class REVERSEDBackgroundHalfToZero(BackgroundAbstract):
    def construct(self):
        self.construct_abstract(1/2, 0, time=5)

class BackgroundHalfToOne(BackgroundAbstract):
    def construct(self):
        self.construct_abstract(1/2, 1, time=5)

class REVERSEDBackgroundToOneToHalf(BackgroundAbstract):
    def construct(self):
        self.construct_abstract(1, 1/2, time=5)
