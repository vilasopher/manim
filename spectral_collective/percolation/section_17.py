from manim import *
import random
from cluster_image import ClusterImage, ClusterReveal
from value_slider import ValueSlider
import solarized as sol
import numpy as np

class SeedTest(Scene):
    def construct(self):
        random.seed(0)
        np.random.seed(0)
        c = ClusterImage((720, 1280))
        c.set_p(1)
        self.add(c)
        print(c.get_TL_color())

config.background_color = sol.BASE03
class ThankYou(Scene):
    def construct(self):
        ty = Tex(r'Thanks for Watching!', color = sol.BASE3, font_size = 120)
        self.add(ty)

class Outro(Scene):
    def construct(self):
        ty = ImageMobject('ThankYou.png')
        random.seed(0)
        np.random.seed(0)

        p = ValueTracker(0)
        self.add(p)

        c = ClusterReveal(
            (720, 1280),
            ty,
            [82, 67, 161]
        )
        c.add_updater(
            lambda s : c.set_p(p.get_value())
        )
        self.add(c)

        self.play(
            p.animate.set_value(1),
            run_time=40,
            rate_func = rate_functions.linear
        )
