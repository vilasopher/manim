from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from glitch import Glitch, GlitchEdges
import random

class PipeSystemAbstract(Scene):
    def pipe_system(self, width, height, scale):
        nodes, edges = gr.grid_nodes_edges(width, height)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        return Graph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(width, height, scale=scale),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )

class PipeSystem0(PipeSystemAbstract):
    def construct(self):
        pass

class PipeSystem1(PipeSystemAbstract):
    def construct(self):
         g = self.pipe_system(8,5,0.95)
         self.play(FadeIn(g))

class PipeSystem2(PipeSystemAbstract):
    def construct(self):
        g = self.pipe_system(8,5,0.95)
        self.add(g)

class DeletingEdges(PipeSystemAbstract, MovingCameraScene):
    def construct(self):
        g = self.pipe_system(8,5,0.95)
        self.add(g)

        for v in g.vertices:
            g[v].set(z_index = 2)

        self.camera.frame.save_state()

        e = g.edges[((-3,-2),(-2,-2))]
        self.play(self.camera.frame.animate.scale(0.15).move_to(e))
        self.wait()

        self.play(Glitch(e, intensity=0.02, out=True))
        g.remove_edges(((-3,-2), (-2,-2)))
        self.wait()

        e = g.edges[((-2,-2),(-1,-2))]
        self.play(self.camera.frame.animate.move_to(e))
        self.wait()
 
        self.play(Glitch(e, intensity=0.02, out=False))
        #g.remove_edges(((-2,-2), (-1,-2)))
        self.wait()

        e = g.edges[((-1,-2),(-1,-1))]
        self.play(self.camera.frame.animate.move_to(e))
        self.wait()

        self.play(Glitch(e, intensity=0.02, out=False))
        #g.remove_edges(((-1,-2), (-1,-1)))
        self.wait()

        self.play(self.camera.frame.animate.restore())
        self.wait()

        randomedgelist = list(g.edges)
        random.shuffle(randomedgelist)

        self.play(
            LaggedStart(
                *(
                    Glitch(
                        g.edges[x],
                        intensity=0.02,
                        out = True if random.random() < 1/2 else False
                    ) for x in randomedgelist
                ),
                lag_ratio = 0.005
            )
        )
        self.wait()


