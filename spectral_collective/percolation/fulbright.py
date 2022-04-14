from manim import *
from more_graphs import HPCCGraph, PercolatingGraph
from value_slider import ValueSlider
from cluster_image import ClusterImage
import grid as gr
import networkx as nx
import random
import solarized as sol


# spoiler for the talk
class Spoiler(Scene):
    def construct(self):
        random.seed(1)

        p = ValueTracker(0.45)

        c = ClusterImage((540,960), p=p.get_value())
        self.add(c)

        c.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.play(
            p.animate.set_value(0.55),
            rate_func = rate_functions.linear,
            run_time = 10
        )

# just show the grid
class PipeSystem(Scene):
    def construct(self):
        nodes, edges = gr.grid_nodes_edges(8, 5)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        g = Graph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(8, 5, scale=0.95),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )

        self.add(g)

# explain how each edge independently flips a coin
class DeletingPipes(Scene):
    def construct(self):
        random.seed(0)

        nodes, edges = gr.grid_nodes_edges(8, 5)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        g = Graph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(8, 5, scale=0.95),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )

        self.add(g)

        counter = 1
        minslow = 20
        maxslow = 100

        time = 1/30

        for e in g.edges:
            if random.random() > 0.5:
                self.play(
                    Indicate(g.edges[e]),
                    FadeOut(g.edges[e]),
                    run_time=time
                )
            else:
                self.play(
                    Indicate(g.edges[e]),
                    run_time=time
                )

            counter += 1

            if counter > minslow:
                time = 1/3

            if counter > maxslow:
                time = 1/30

# resample the percolation a few times
class DeletingPipesResamples(Scene):
    def construct(self):
        random.seed(0)

        nodes, edges = gr.grid_nodes_edges(24, 14)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        for _ in range(5):
            g = PercolatingGraph.from_networkx(
                nxgraph,
                layout=gr.grid_layout(24, 14, scale=0.3),
                vertex_config = sol.VERTEX_CONFIG,
                edge_config = sol.EDGE_CONFIG
            )

            g.percolate(0.5)
            self.play(FadeIn(g), run_time=0.25)
            self.wait(2)
            self.play(FadeOut(g), run_time=0.25)

# show different colored liquids "flowing" into the different
# connected components of a single instance of percolation
class PercolationFlow(Scene):
    def construct(self):
        pass

# now show the colored graphs more, but resample a few times
class PercolationFlowResamples(Scene):
    def construct(self):
        random.seed(0)

        nodes, edges = gr.grid_nodes_edges(24, 14)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        for _ in range(10):
            g = HPCCGraph.from_networkx(
                nxgraph,
                layout=gr.grid_layout(24, 14, scale=0.3),
                vertex_config = sol.VERTEX_CONFIG,
                edge_config = sol.EDGE_CONFIG
            )

            g.set_p(0.5)
            self.play(FadeIn(g), run_time=0.25)
            self.wait(2)
            self.play(FadeOut(g), run_time=0.25)

# introduce the parameter, and sample a few graphs at a few
# different values of p
class Parameter(Scene):
    def construct(self):
        random.seed(0)

        nodes, edges = gr.grid_nodes_edges(24, 14)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        slider = ValueSlider(0.91, z_index = 2)
        self.add(slider)

        for i in range(10):
            g = HPCCGraph.from_networkx(
                nxgraph,
                layout=gr.grid_layout(24, 14, scale=0.3),
                vertex_config = sol.VERTEX_CONFIG,
                edge_config = sol.EDGE_CONFIG
            )

            g.set_p((i+1)/11)
            self.play(
                FadeIn(g),
                slider.animate.set_p((i+1)/11),
                run_time=0.25
            )
            self.wait(2)
            self.play(FadeOut(g), run_time=0.25)

# begin explaining the coupling
class CouplingExplanation(Scene):
    def construct(self):
        pass

# demonstrate the coupling on a small example
class CouplingDemonstration(Scene):
    def construct(self):
        random.seed(0)

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

# show a coupled cluster thing but on a large Manim Graph object
# also, remove the visible numbers on the edges
class MidResCoupling(Scene):
    def construct(self):
        pass

# remove the edges altogether, this is now a pixel picture
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

# this is only the critical region
class HighResCouplingCritical(Scene):
    def construct(self):
        random.seed(0)

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
