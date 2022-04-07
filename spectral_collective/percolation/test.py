from manim import *
from cluster_image import ClusterImage
import random

random.seed(0)

class Test(Scene):
    def construct(self):
        a = ImageMobject(np.uint8([[[0,255,0],[255,0,0]],
                                   [[255,100,0],[200,0,100]]]))
        a.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        a.height = 8
        self.add(a)

        self.wait()
        a.pixel_array[(0,0,0)] = 100
        self.wait()

class ClusterTest(Scene):
    def construct(self):
        p = ValueTracker(0)

        c = ClusterImage((540,960), p=p.get_value())
        self.add(c)

        ptex = MathTex('p', color=BLACK)
        line = UnitInterval(color=BLACK)
        self.add(ptex, line)
        return

        self.wait(1/30)

        for i in range(300):
            c.update_clusters((i+1)/300)
            self.wait(1/30)

