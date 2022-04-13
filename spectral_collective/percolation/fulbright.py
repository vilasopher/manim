from manim import *
from more_graphs import HPCCGraph
import grid as gr
import networkx as nx
import random
import solarized as sol

class CouplingExplanation(Scene):
    def construct(self):

        nodes, edges = gr.grid_nodes_edges(8, 5)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        g = HPCCGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(8, 5, scale=0.95)
        )

        coupling = g.coupling

        bg = Graph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(8, 5, scale=0.95),
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.VERY_LIGHT_EDGE_CONFIG
        )

        self.add(bg, g)

        nums = {}

        for r, e in coupling:
            nums[e] = DecimalNumber(
                    r,
                    font_size=20,
                    z_index=1
                )
            nums[e].color = BLACK
            nums[e].next_to(bg.edges[e], ORIGIN)
            self.add(nums[e])

        n = 20
        for i in range(n):
            self.play(g.animate.set_p((i+1)/n), run_time=0.25)
            self.wait(0.25)
