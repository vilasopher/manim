from manim import *
from cluster_image import ClusterImage, StaticPercolationImage
import grid as gr
import networkx as nx
import random
import solarized as sol

class CriticalZoomOut(Scene):
    def konstrakta(self, onecluster = False, time = 5, shape = (2160, 3840)):
        c = StaticPercolationImage(shape, p=0.5)
        
        if onecluster:
            c.highlight_biggest_cluster(sol.BASE03, bg_color=sol.BASE3)

        h = ValueTracker(24)

        c.add_updater(
            lambda s : s.set(height=h.get_value())
        )

        self.add(c)

        self.play(
            h.animate.set_value(8),
            rate_func = rate_functions.linear,
            run_time = time
        )

    def constructor(self):
        random.seed(0)
        self.konstrakta(onecluster=False)

class CZO_OneCluster(CriticalZoomOut):
    def construct(self):
        random.seed(1)
        self.konstrakta(onecluster=True)
