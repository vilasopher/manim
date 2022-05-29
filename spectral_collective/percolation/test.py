from manim import *
from cluster_image import ClusterImage
from more_graphs import ClusterGraph, HPCGraph, HPCCGraph, PercolatingGraph, HPGraph
from value_slider import ValueSlider
import grid as gr
import networkx as nx
import random
import solarized as sol
from glitch import Glitch, GlitchEdges

#random.seed(0)

class CoupledClusterGraphTest(Scene):
    def construct(self):

        nodes, edges = gr.grid_nodes_edges(24, 14)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        g = HPCCGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(24, 14, scale=0.3),
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.LIGHT_EDGE_CONFIG
        )

        self.add(g)
        self.wait(0.5)

        n = 20

        for i in range(n):
            self.play(g.animate.set_p((i+1)/n), run_time=0.25)
            self.wait(0.25)

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

        self.play(g.animate.add_edges(
            ((0,0), (0,-1)),
            ((1,2), (1,3))
            ))
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


class GlitchyPercolationTest(Scene):
    def construct(self):
        random.seed(0)

        nodes, edges = gr.grid_nodes_edges(24, 14)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        h = Graph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(24, 14, scale=0.3),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )

        g = HPCCGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(24, 14, scale=0.3),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )
        g.set_p(0.5)

        self.add(g)
        self.wait(3)
        self.play(Glitch(g, intensity=0.03, out=True), run_time=0.05)
        self.play(Glitch(h, intensity=0.03, out=True), run_time=0.25)

        g = HPCCGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(24, 14, scale=0.3),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )
        g.set_p(0.5)

        self.play(Glitch(g, intensity=0.03), run_time=0.05)
        self.wait(3)

class HighResCoupling(Scene):
    def construct(self):
        random.seed(0)

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

class OpacityTest(Scene):
    def construct(self):
        c = Line([-1,-1,0],[1,1,0])
        self.add(c)
        self.wait()
        c.set_opacity(0.5)
        self.wait()

class PathTest(Scene):
    def construct(self):
        nodes, edges = gr.grid_nodes_edges(24, 14)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        h = HPGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(24, 14, scale=0.3),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )

        h.percolate(0.501)
        self.add(h)
        self.wait()
        self.play(h.animate.dramatically_highlight_ball((0,0)))
        self.wait()
        self.play(h.animate.highlight_longest_path_from((0,0)))
        self.wait()

class GridPathTest(Scene):
    def construct(self):

        h = HPGraph.from_grid((24,14),0.3)

        h.percolate(0.501)
        h.dramatically_highlight_ball((0,0))
        self.add(h)
        self.wait()
        self.play(h.animate.highlight_path_of_length_from((0,0), 10))
        self.wait()
