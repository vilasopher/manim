from manim import *
import random
from cluster_image import ClusterImage

class Helper:
    def helper(self, n):
        random.seed(n)

        p = ValueTracker(0)

        c = ClusterImage((720,1280), p=p.get_value())
        self.add(c)

        c.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.play(
            p.animate.set_value(1),
            rate_func = rate_functions.linear,
            run_time = 10
        )

class h0(Scene, Helper):
    def construct(self):
        self.helper(0)

class h1(Scene, Helper):
    def construct(self):
        self.helper(1)

class h2(Scene, Helper):
    def construct(self):
        self.helper(2)

class h3(Scene, Helper):
    def construct(self):
        self.helper(3)

class h4(Scene, Helper):
    def construct(self):
        self.helper(4)

class h5(Scene, Helper):
    def construct(self):
        self.helper(5)

class h6(Scene, Helper):
    def construct(self):
        self.helper(6)

class h7(Scene, Helper):
    def construct(self):
        self.helper(7)

class h8(Scene, Helper):
    def construct(self):
        self.helper(8)

class h9(Scene, Helper):
    def construct(self):
        self.helper(9)

class h10(Scene, Helper):
    def construct(self):
        self.helper(10)

class h11(Scene, Helper):
    def construct(self):
        self.helper(11)

class h12(Scene, Helper):
    def construct(self):
        self.helper(12)

class h13(Scene, Helper):
    def construct(self):
        self.helper(13)
        
class h14(Scene, Helper):
    def construct(self):
        self.helper(14)

class h15(Scene, Helper):
    def construct(self):
        self.helper(15)

class h16(Scene, Helper):
    def construct(self):
        self.helper(16)

class h17(Scene, Helper):
    def construct(self):
        self.helper(17)

class h18(Scene, Helper):
    def construct(self):
        self.helper(18)

class h19(Scene, Helper):
    def construct(self):
        self.helper(19)
