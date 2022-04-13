from manim import *
from cluster_image import ClusterImage
from more_graphs import ClusterGraph, HPCGraph
import grid as gr
import networkx as nx
import random
import solarized as sol

random.seed(0)

class ClusterGraphTest(Scene):
    def construct(self):

        nodes, edges = gr.grid_nodes_edges(3, 3)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)


        g = HPCGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(3, 3),
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.LIGHT_EDGE_CONFIG
        )

        g.percolate(0.4)
        self.add(g)
        self.wait(0.5)

        g.initialize_color_dicts()

        self.play(g.animate.update_colors())
        self.wait(0.5)

        self.play(g.animate.add_edges(((0,0), (0,-1))))
        self.wait(0.5)




class ClusterImageTest(Scene):
    def construct(self):
        p = ValueTracker(0)

        c = ClusterImage((540,960), p=p.get_value())
        self.add(c)

        ptex = MathTex('p', color=BLACK)
        line = UnitInterval(color=BLACK)
        self.add(ptex, line)
        return

        self.wait(1/30)

        for i in range(300):
            c.update_clusters((i+1)/300)
            self.wait(1/30)

