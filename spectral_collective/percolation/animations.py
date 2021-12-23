from manim import *
import grid as gr
from percolating_graph import PercolatingGraph
import networkx as nx

class Percolate(Scene):
    def construct():

        nodes, edges = gr.grid_nodes_edges(5)
        nxgraph = nx.Graph(nodes, edges)
        pg = PercolatingGraph.from_networkx(nxgraph, layout=gr.grid_layout(5))

        self.add(pg)

class Test(Scene):
    def construct():

        circle = Circle()
        self.add(circle)

