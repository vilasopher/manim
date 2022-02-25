from manim import *
import grid as gr
from more_graphs import HPGraph
import networkx as nx
from random import random, seed
import solarized as sol

seed(1)

class Percolate(Scene):
    def construct(self):
        nodes, edges = gr.grid_nodes_edges(24, 14)

        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        g = HPGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(24, 14, scale=0.3),
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.LIGHT_EDGE_CONFIG
        )

        self.add(g)
        self.wait()

        self.play(g.animate.percolate(0.505))
        self.wait()

        self.play(g.animate.dramatically_highlight_ball((0,0)))
        self.wait()
