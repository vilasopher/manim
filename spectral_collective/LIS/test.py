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