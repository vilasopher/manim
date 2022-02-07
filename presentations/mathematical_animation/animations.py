from manim import *

class A1(Scene):
    def construct(self):
        c = Circle()
        self.add(c)

class A2(Scene):
    def construct(self):
        c = Circle()
        s = Square()

        s.next_to(c)
        self.add(c,s)

class A3(Scene):
    def construct(self):
        c = Circle()
        s = Square()

        self.play(Create(c))
        self.wait()
        self.play(Transform(c,s))
        self.wait()

class A4(Scene):
    def construct(self):
        t = MathTex(
            r'\mathbb{Z} / 2 \mathbb{Z}'
            r'\otimes'
            r'\mathbb{Z} / 3 \mathbb{Z}'
            r'\cong 0',
            font_size = 100
        )

        self.play(Write(t))
        self.wait()

class A5(Scene):
    def construct(self):
        t1 = MathTex(r'{{a^2}} + {{b^2}} = {{c^2}}')
        t2 = MathTex(r'{{a^2}} = {{c^2}} - {{b^2}}')

        self.play(Write(t1))
        self.wait()
        self.play(TransformMatchingTex(t1,t2))
        self.wait()

class A6(Scene):
    def construct(self):
        c = Circle()
        
        self.play(Create(c))
        self.wait()
        self.play(c.animate.set_fill(RED, opacity=1))
        self.wait()

class A7(Scene):
    def construct(self):
        
