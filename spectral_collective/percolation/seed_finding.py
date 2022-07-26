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
            run_time = 5
        )

class h20(Scene, Helper):
    def construct(self):
        self.helper(20)

class h21(Scene, Helper):
    def construct(self):
        self.helper(21)

class h22(Scene, Helper):
    def construct(self):
        self.helper(22)

class h23(Scene, Helper):
    def construct(self):
        self.helper(23)

class h24(Scene, Helper):
    def construct(self):
        self.helper(24)

class h25(Scene, Helper):
    def construct(self):
        self.helper(25)

class h26(Scene, Helper):
    def construct(self):
        self.helper(26)

class h27(Scene, Helper):
    def construct(self):
        self.helper(27)

class h28(Scene, Helper):
    def construct(self):
        self.helper(28)

class h29(Scene, Helper):
    def construct(self):
        self.helper(29)

class h30(Scene, Helper):
    def construct(self):
        self.helper(30)

class h31(Scene, Helper):
    def construct(self):
        self.helper(31)

class h32(Scene, Helper):
    def construct(self):
        self.helper(32)

class h33(Scene, Helper):
    def construct(self):
        self.helper(33)
        
class h34(Scene, Helper):
    def construct(self):
        self.helper(34)

class h35(Scene, Helper):
    def construct(self):
        self.helper(35)

class h36(Scene, Helper):
    def construct(self):
        self.helper(36)

class h37(Scene, Helper):
    def construct(self):
        self.helper(37)

class h38(Scene, Helper):
    def construct(self):
        self.helper(38)

class h39(Scene, Helper):
    def construct(self):
        self.helper(39)

class h40(Scene, Helper):
    def construct(self):
        self.helper(40)

class h41(Scene, Helper):
    def construct(self):
        self.helper(41)

class h42(Scene, Helper):
    def construct(self):
        self.helper(42)

class h43(Scene, Helper):
    def construct(self):
        self.helper(43)

class h44(Scene, Helper):
    def construct(self):
        self.helper(44)

class h45(Scene, Helper):
    def construct(self):
        self.helper(45)

class h46(Scene, Helper):
    def construct(self):
        self.helper(46)

class h47(Scene, Helper):
    def construct(self):
        self.helper(47)

class h48(Scene, Helper):
    def construct(self):
        self.helper(48)

class h49(Scene, Helper):
    def construct(self):
        self.helper(49)

class h50(Scene, Helper):
    def construct(self):
        self.helper(50)

class h51(Scene, Helper):
    def construct(self):
        self.helper(51)

class h52(Scene, Helper):
    def construct(self):
        self.helper(52)

class h53(Scene, Helper):
    def construct(self):
        self.helper(53)
        
class h54(Scene, Helper):
    def construct(self):
        self.helper(54)

class h55(Scene, Helper):
    def construct(self):
        self.helper(55)

class h56(Scene, Helper):
    def construct(self):
        self.helper(56)

class h57(Scene, Helper):
    def construct(self):
        self.helper(57)

class h58(Scene, Helper):
    def construct(self):
        self.helper(58)

class h59(Scene, Helper):
    def construct(self):
        self.helper(59)
