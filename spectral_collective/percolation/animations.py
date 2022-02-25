from manim import *
import grid as gr
from more_graphs import HPGraph
import networkx as nx
from random import random, seed
import solarized as sol

class Percolate(Scene):
    def construct(self):
        seed(0)

        nodes, edges = gr.grid_nodes_edges(24, 14)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        n = 500

        for i in range(n):
            g = HPGraph.from_networkx(
                nxgraph,
                layout=gr.grid_layout(24, 14, scale=0.3),
                vertex_config = sol.LIGHT_VERTEX_CONFIG,
                edge_config = sol.LIGHT_EDGE_CONFIG
            )

            if i == 0:
                self.play(Create(g))
                self.wait()
            else:
                self.add(g)

            g.percolate((i+1)/(n+1))
            g.dramatically_highlight_ball((0,0))

            self.wait(0.1)
            self.clear()

class Coupling(Scene):
    def construct(self):
        seed(2)

        nodes, edges = gr.grid_nodes_edges(24, 14)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        g = HPGraph.from_networkx(nxgraph)
        coupling = g.generate_coupling()

        n = 300

        for i in range(n):
            g = HPGraph.from_networkx(
                nxgraph,
                layout = gr.grid_layout(24, 14, scale=0.3),
                vertex_config = sol.LIGHT_VERTEX_CONFIG,
                edge_config = sol.LIGHT_EDGE_CONFIG
            )

            g.coupled_percolate(coupling, (i+1)/(n+1))
            g.dramatically_highlight_ball((0,0))

            self.add(g)
            self.wait(1/30)
            self.clear()

class Test(Scene):
    def construct(self):
        g = HPGraph(
            [1,2,3],
            [(1,2),(2,3),(3,1)],
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )

        self.play(FadeIn(g))
        self.wait()

        self.play(g.animate.percolate(1/4))
        self.wait()

        self.play(FadeOut(g))
        self.wait()
