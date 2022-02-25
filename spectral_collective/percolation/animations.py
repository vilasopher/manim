from manim import *
import grid as gr
from percolating_graph import HPGraph
import networkx as nx
from random import random
import solarized as sol

class Percolate(Scene):
    def construct(self):
        nodes, edges = gr.grid_nodes_edges(10, 5)

        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        g = HPGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(10, 5),
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.LIGHT_EDGE_CONFIG
        )

        self.add(g)
        self.wait()

        self.play(g.animate.percolate(0.5))
        self.wait()

        self.play(g.animate.highlight_ball((0,0), 4))
        self.wait()

class Test(Scene):
    def construct(self):
        g = Graph([1,2,3], [(1,2),(2,3),(3,1)])
        self.play(Create(g))
        self.wait()
        self.play(g.animate.remove_edges((1,2),(3,2), anim_args = { "animation" : FadeOut} ))
        self.wait()
