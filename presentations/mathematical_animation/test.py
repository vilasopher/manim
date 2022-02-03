from manim import *

class Test1(Scene):
    def construct(self):

        squares = [ Square() for _ in range(5) ]

        for i in range(5):
            squares[i].move_to(3 * i * RIGHT + 6 * LEFT)

        self.add(*squares)
        self.wait()
        self.play(ShowSubmobjectsOneByOne(squares))

class Test2(Scene):
    def construct(self):
        
        arcs = [ LightArc(lambda t : [-3 * np.cos(t), (2 + 0.01 *c) * np.sin(t) - 1, 0],
                          t_range=[0, PI, 0.01]) for c in range(100) ]

        self.play(ShowSubmobjectsOneByOne(arcs))

class Test3(Scene):
    def construct(self):
        tex1 = MathTex(
            r"{ \sin \theta_a \over {{v_a}} }=",
            r"{ {{\sin \theta_w}} \over v_w }"
        )
        tex2 = MathTex(
            r"{ \sin \theta_a \over {{\sin \theta_w}} }=",
            r"{ {{v_a}} \over v_w }"
        )
        self.play(FadeIn(tex1))
        self.wait(0.5)
        self.play(TransformMatchingTex(tex1,tex2))
        self.wait(0.5)

class Test4(Scene):
        def construct(self):
            tex = MathTex(r"{a}=",
                    r"{b}")
            self.play(Write(tex))
