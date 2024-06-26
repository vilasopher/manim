from manim import *
from youngdiagrams import *
import numpy.random as ra

class DotTest(Scene):
    def construct(self):
        l1 = Line(LEFT, ORIGIN, color=sol.RED)
        l2 = Line(ORIGIN, UP, color=sol.RED)
        d = Dot(ORIGIN, radius=0.0175, color=sol.RED, )
        self.add(l1, l2, d)

class TileTest(Scene):
    def construct(self):
        t = Tile(3)
        self.add(t)

        self.play(t.animate.shift(3*RIGHT))
        self.wait()

class YDTest(Scene):
    def construct(self):
        yd = YoungDiagram(ra.random(size=1000))
        self.add(yd)
        self.wait()
        yd.set_unit(0.5)
        yd.redraw()
        self.wait()
        yd.highlight_first_row()
        yd.set_unit(0.1)
        yd.redraw()
        self.wait()
        yd.set_unit(0.05)
        yd.redraw()
        self.wait()

class Test(Scene):
    def construct(self):
        a = Circle()
        self.play(Create(a))

class TextTest(Scene):
    def construct(self):
        t = Text('a^2 + b^2 = c^2')
        self.play(Write(t))
        
class TexTest(Scene):
    def construct(self):
        t = MathTex('a^2 + b^2 = c^2')
        self.play(Write(t))

class RadiusTest(Scene):
    def construct(self):
        d = Dot(radius=1)

        self.add(d)
        self.wait()
        d.scale(2)
        self.wait()
        d.scale(2 / d.width)
        self.wait()

class RemoveTest(Scene):
    def construct(self):
        self.c = Circle()
        self.x = ValueTracker(0)


        self.add(self.c)

        def tick(dt):
            self.c.become(Circle().shift(self.x.get_value()*RIGHT))
    
        self.add_updater(tick)

        self.play(self.x.animate.set_value(3))

class LineTest(Scene):
    def construct(self):
        l = Line(ORIGIN, ORIGIN)
        l.put_start_and_end_on(ORIGIN, ORIGIN)
        self.add(l)
