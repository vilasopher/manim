from manim import *
from more_graphs import HPCCGraph
from value_slider import ValueSlider
from cluster_image import ClusterImage
import grid as gr
import networkx as nx
import random
import solarized as sol

random.seed(0)

class CouplingDemonstration(Scene):
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

        p = ValueTracker(0)

        slider = ValueSlider(z_index = 2)
        self.add(slider)

        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        g.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.play(
            p.animate.set_value(1),
            rate_func=rate_functions.linear,
            run_time=10
        )

class HighResCoupling(Scene):
    def construct(self):
        p = ValueTracker(0)

        c = ClusterImage((540,960), p=p.get_value())
        self.add(c)

        slider = ValueSlider(z_index = 2)
        self.add(slider)

        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        c.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.play(
            p.animate.set_value(1),
            rate_func = rate_functions.linear,
            run_time = 10
        )

class HighResCouplingCritical(Scene):
    def construct(self):
        p = ValueTracker(0.45)

        c = ClusterImage((540,960), p=p.get_value())
        self.add(c)

        slider = ValueSlider(z_index = 2)
        self.add(slider)

        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        c.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.play(
            p.animate.set_value(0.55),
            rate_func = rate_functions.linear,
            run_time = 10
        )
