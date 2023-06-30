from manim import *

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
