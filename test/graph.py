from manim import *

class MovingVertices(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1,2), (2,3), (3,4), (1,3), (1,4)]
        g = Graph(vertices, edges)

        self.play(Create(g))
        self.wait()

        self.play(g[1].animate.move_to([1,1,0]),
                  g[2].animate.move_to([-1,1,0]),
                  g[3].animate.move_to([1,-1,0]),
                  g[4].animate.move_to([-1,-1,0]))
        self.wait()

        h = Graph(vertices, edges, layout="spring")

        self.play(Transform(g,h))
        self.wait()

        vertices = [1,2,3,4,5]
        edges = [(1,2),(2,3),(3,4),(1,3),(1,4),(1,5)]

        f = Graph(vertices, edges, layout="spring")

        self.play(Transform(g,f))
        self.wait()


class AddingVertices(Scene):
    def construct(self):
        vertices = [1,2,3,4]
        edges = [(1,2),(2,3),(3,4),(1,4)]

        g = Graph(vertices, edges)

        text = Text(str(g._layout), font_size=14)
        
        self.play(Create(g))
        self.play(Create(text))
        self.wait()

        self.play(g.animate.add_edges((1,6),(2,5),edge_config={
                (1,6) : {"stroke_color": RED},
                (2,5) : {"stroke_color": BLUE}
                }))
        self.wait()



