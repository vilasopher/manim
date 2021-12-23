from manim import *
import grid as gr
from percolating_graph import PercolatingGraph
import networkx as nx
from random import random

class Percolate(Scene):
    def construct(self):
        nodes, edges = gr.grid_nodes_edges(5)

        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        pg = PercolatingGraph.from_networkx(nxgraph, layout=gr.grid_layout(5))

        self.play(Create(pg))

        edges_to_remove = [ e for e, _ in pg.edges.items() if random() > 0.9]

        self.play(pg.animate.remove_edges(*edges_to_remove), run_time=3)


class Test(Scene):
    def construct(self):
        g = Graph([1,2], [(1,2)])
        self.play(Create(g))
        self.play(g.animate.remove_edges((1,2)))
        self.wait()
