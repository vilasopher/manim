from manim import *

class Test(Scene):
    def construct(self):
        sw=30
        r = Rectangle(stroke_width=sw, height=2.0 + sw/100, width=4.0 + sw/100)
        r2 = Rectangle(color=BLUE, height=2.0, width=4.0)
        c = Circle()

        r.move_to(2 * RIGHT + UP)
        r2.move_to(2 * RIGHT + UP)


        self.add(c,r,r2)
        self.play(c.animate.move_to(3*RIGHT))
        self.wait()
