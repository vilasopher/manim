from manim import *
from cluster_image import ClusterImage
import grid as gr
import networkx as nx
import random
import solarized as sol

class CriticalZoomOut(Scene):
    def construct(self):
        random.seed(0)

        c = ClusterImage((2160,3840), p=0.5)

        h = ValueTracker(24)

        c.add_updater(
            lambda s : s.set(height=h.get_value())
        )

        self.add(c)

        self.play(
            h.animate.set_value(8),
            rate_func = rate_functions.linear,
            run_time = 5
        )

class CZO_OneCluster(Scene):
    def construct(self):
        random.seed(1)

        c = ClusterImage((540,960), p=0.5)

        c.highlight_biggest_cluster(sol.BASE03, bg_color=sol.BASE3)

        self.add(c)

        return

        h = ValueTracker(24)

        c.add_updater(
            lambda s : s.set_height(h.get_value())
        )

        self.add(c)

        self.play(
            h.animate.set_value(8),
            rate_func = rate_functions.linear,
            run_time = 5
        )

