from manim import *

class GraphProblem(Scene):
    def construct(self):
        vertices = [1,2,3,4]
        edges = [(1,2),(2,3),(3,4)]

        g = Graph(vertices, edges)

        self.play(Create(g))
        self.play(g.animate.change_layout())
        self.wait()

        arrow = Arrow(start=LEFT, end=g[1])

        self.play(Create(arrow))
        self.wait()

class GraphProblem2(Scene):
    def construct(self):
        vertices = [1,2,3]
        edges = [(1,2),(2,3)]

        g = Graph(vertices, edges)

        self.play(Create(g))
        #self.play(g.animate.add_vertices(4, positions={4 : LEFT * 2}),
        #          g.animate.add_edges((2,4)))
        self.wait()

        self.play(g[2].animate.move_to(RIGHT))
        self.wait()
