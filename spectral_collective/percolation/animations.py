from manim import *
import grid as gr
from more_graphs import HPGraph
import networkx as nx
from random import random
import solarized as sol

class Percolate(Scene):
    def construct(self):
        nodes, edges = gr.grid_nodes_edges(15, 8)

        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        g = HPGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(15, 8),
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.LIGHT_EDGE_CONFIG
        )

        self.add(g)
        self.wait()

        self.play(g.animate.percolate(0.6))
        self.wait()

        self.play(g.animate.dramatically_highlight_ball((0,0), 3))
        self.wait()
