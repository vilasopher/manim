from manim import *
import random
from cluster_image import ClusterImage
from value_slider import ValueSlider
import numpy as np

class SeedTest(Scene):
    def construct(self):
        random.seed(0)
        c = ClusterImage((100, 200))
        c.set_p(1)
        self.add(c)
        print(c.get_TL_color())

class Outro(Scene):
    def construct(self):
        outro_image = 
        random.seed(0)

        p = ValueTracker(0)
        self.add(p)

        c = ClusterImage((100, 200))
        c.add_updater(
            lambda s : 
