from manim import *
from cluster_image import ClusterImage, StaticPercolationImage
import grid as gr
import networkx as nx
import random
import solarized as sol
import PIL

class CriticalZoomOut(Scene):
    def konstrakta(self, onecluster = False, p=0.5, time = 30, zoom = 8):
        c = StaticPercolationImage(
            (540 * zoom, 960 * zoom),
            p=p,
            onecluster=onecluster
        )

        h = ValueTracker(8 * 4 * zoom)

        c.add_updater(
            lambda s : s.set(height=h.get_value())
        )

        self.add(c)

        self.play(
            h.animate.set_value(8),
            rate_func = rate_functions.ease_out_quad,
            run_time = time
        )

    def construct(self):
        random.seed(0)
        self.konstrakta(onecluster=False)

class CZO_OneCluster(CriticalZoomOut):
    def construct(self):
        random.seed(1)
        self.konstrakta(onecluster=True, p=0.525)

class CZO_IMAGE(Scene):
    def construct(self):
        PIL.Image.MAX_IMAGE_PIXELS = 3686400000
        img = ImageMobject('huge/allclusters_shape=(14400, 25600)_seed=3_parameter=0.5.png')
        img.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])

        h = ValueTracker(80)

        img.add_updater(
            lambda s : s.set(height=h.get_value())
        )

        self.add(img)

        self.play(
            h.animate.set_value(8),
            rate_func = rate_functions.ease_out_quad,
            run_time = 30
        )
