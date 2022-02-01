from manim import *
from light_arc import LightArc

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

