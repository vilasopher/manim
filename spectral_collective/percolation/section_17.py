from manim import *
import random
from cluster_image import ClusterImage, ClusterReveal
from value_slider import ValueSlider
from duality import Duality
from glitch import GlitchEdges
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

#config.background_color = sol.BASE03
class ThankYou(Scene):
    def construct(self):
        ty = Tex(r'Thanks for Watching!', color = sol.BASE3, font_size = 120)
        self.add(ty)

class Outro(Scene):
    def construct(self):
        ty = ImageMobject('ThankYou.png')
        ty.set(height = 8, z_index = -1)
        self.add(ty)

        random.seed(0)
        np.random.seed(0)

        p = ValueTracker(0)
        self.add(p)

        c = ClusterReveal(
            (720, 1280),
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


class DualityBackgroundTransition(Scene):
    def construct(self):
        g = Duality(
            primal_vertex_config = sol.VERY_LIGHT_VERTEX_CONFIG,
            primal_edge_config = sol.VERY_LIGHT_EDGE_CONFIG,
            dual_vertex_config = sol.DUAL_LIGHT_VERTEX_CONFIG,
            dual_edge_config = sol.DUAL_LIGHT_EDGE_CONFIG
        )
        self.play(
            GlitchEdges(g.primal, intensity=0.03, simple=True),
            GlitchEdges(g.dual, intensity=0.03, simple=True),
            run_time=0.5
        )

class DualityBackground0(Scene):
    def construct(self):
        g = Duality(
            primal_vertex_config = sol.VERY_LIGHT_VERTEX_CONFIG,
            primal_edge_config = sol.VERY_LIGHT_EDGE_CONFIG,
            dual_vertex_config = sol.DUAL_LIGHT_VERTEX_CONFIG,
            dual_edge_config = sol.DUAL_LIGHT_EDGE_CONFIG
        )
        g.percolate()
        self.play(
            GlitchEdges(g.primal, intensity=0.03, simple=True),
            GlitchEdges(g.dual, intensity=0.03, simple=True), 
            run_time=0.25
        )
        self.wait(6)
        self.play(
            GlitchEdges(g.primal, intensity=0.03, simple=True),
            GlitchEdges(g.dual, intensity=0.03, simple=True), 
            run_time=0.25
        )

class DualityBackground1(DualityBackground0):
    pass

class DualityBackground2(DualityBackground0):
    pass

class DualityBackground3(DualityBackground0):
    pass

class DualityBackground4(DualityBackground0):
    pass

class DualityBackground5(DualityBackground0):
    pass

class DualityBackground6(DualityBackground0):
    pass

class DualityBackground7(DualityBackground0):
    pass

class DualityBackground8(DualityBackground0):
    pass

class DualityBackground9(DualityBackground0):
    pass
