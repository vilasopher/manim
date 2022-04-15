from manim import *
from more_graphs import HPCCGraph, PercolatingGraph, HPGraph
from value_slider import ValueSlider
from cluster_image import ClusterImage
import grid as gr
import networkx as nx
import random
import solarized as sol


# spoiler for the talk
class Spoiler(Scene):
    def construct(self):
        random.seed(4)

        p = ValueTracker(0.40)

        c = ClusterImage((540,960), p=p.get_value())

        c.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.add(c)

        self.play(
            p.animate.set_value(0.55),
            rate_func = rate_functions.linear,
            run_time = 5
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

# show different colored liquids "flowing" into one connected component
class PercolationFlowSingle(Scene):
    def construct(self):
        random.seed(3)

        nodes, edges = gr.grid_nodes_edges(24, 14)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        g = HPGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(24, 14, scale=0.3),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )

        g.percolate()
        self.add(g)
        self.wait()

        water_color = rgb_to_color([0,0.1,1])

        self.play(g.animate.highlight_subgraph([(0,0)], [], node_default_color=water_color))
        self.wait()

        self.play(g.percolation_flow_animation((0,0), water_color), run_time = 5)
        self.wait(3)

        self.play(
            g.animate.highlight_subgraph(
                g.vertices,
                g.edges,
                node_default_color = sol.NODE,
                edge_default_color = sol.EDGE
            )
        )

def random_color():
    c = rgb_to_color([random.randint(0,255)/255 for _ in range(3)])

    while c == sol.NODE:
        c = rgb_to_color([random.randint(0,255)/255 for _ in range(3)])

    return c

# flow colors into all the other components
class PercolationFlowMultiple(Scene):
    def construct(self):
        random.seed(3)

        nodes, edges = gr.grid_nodes_edges(24, 14)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        g = HPGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(24, 14, scale=0.3),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )

        water_color = rgb_to_color([0,0.1,1])

        g.percolate()
        g.highlight_subgraph(
            g.ball((0,0)),
            node_default_color=water_color,
            edge_default_color=water_color
        )
        self.add(g)
        self.wait()

        self.play(
            g.percolation_flow_animation((8,-4), rgb_to_color([0.1,0.9,0.1])),
            run_time = 2
        )

        self.play(
            g.percolation_flow_animation((7,2), rgb_to_color([1,0,0.1])),
            run_time = 2
        )

        self.play(
            g.percolation_flow_animation((-21,-11), rgb_to_color([0.9,0,0.5])),
            run_time = 1.5
        )

        self.play(
            g.percolation_flow_animation((18,-10), rgb_to_color([0.8,0.4,0])),
            run_time = 1.5
        )

        self.play(
            g.percolation_flow_animation((-2,-3), rgb_to_color([0.5,0.5,0.1])),
            run_time = 1.5
        )

        vs = list(g.vertices)

        trycount = 0
        clustercount = 0
        while trycount < 1000:
            v = random.choice(vs)

            trycount = 0
            while trycount < 1000 and g.vertices[v].color != sol.NODE:
                v = random.choice(vs)
                trycount += 1

            if trycount < 1000:
                clustercount += 1
                col = random_color()
                self.play(
                    g.percolation_flow_animation(v, col),
                    run_time = 100 / (clustercount+10) ** 2
                )

        self.wait()


# now show the colored graphs more, but resample a few times
class PercolationFlowResamples(Scene):
    def construct(self):
        random.seed(1)

        nodes, edges = gr.grid_nodes_edges(24, 14)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        for _ in range(10):
            g = HPCCGraph.from_networkx(
                nxgraph,
                layout=gr.grid_layout(24, 14, scale=0.3)
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
                layout=gr.grid_layout(24, 14, scale=0.3)
            )

            g.set_p((i+1)/11)
            self.play(
                FadeIn(g),
                slider.animate.set_p((i+1)/11),
                run_time=0.25
            )
            self.wait(2)
            self.play(FadeOut(g), run_time=0.25)

# begin explaining the coupling, introducing the numbering
class CouplingNumbering(Scene):
    def construct(self):
        random.seed(7)

        nodes, edges = gr.grid_nodes_edges(3, 2)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        g = HPCCGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(3, 2, scale=2.5)
        )

        coupling = list(g.coupling)

        coupling = [ ((i+1)/59, c[1]) for i, c in enumerate(coupling) ]

        g.coupling = coupling

        bg = Graph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(5, 3, scale=2.5),
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.VERY_LIGHT_EDGE_CONFIG
        )

        self.add(bg, g)

        p = ValueTracker(0)

        slider = ValueSlider(p=0, opacity=0.95, bar_color=sol.BASE1, z_index = 2)
        self.add(slider)
        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.wait()

        nums = {}

        for r, e in coupling:
            nums[e] = DecimalNumber(
                    r,
                    font_size=40,
                    z_index=1
                )
            nums[e].color = BLACK
            nums[e].next_to(bg.edges[e], ORIGIN)

        self.play(LaggedStart(*(Write(nums[e]) for r, e in coupling)), run_time=5)
        self.wait()

# explain how the coupling works and how the colors are updated
class CouplingUnionFind(Scene):
    def construct(self):
        random.seed(7)

        nodes, edges = gr.grid_nodes_edges(3, 2)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        g = HPCCGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(3, 2, scale=2.5)
        )

        coupling = list(g.coupling)

        coupling = [ ((i+1)/59, c[1]) for i, c in enumerate(coupling) ]

        g.coupling = coupling

        bg = Graph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(3, 2, scale=2.5),
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.VERY_LIGHT_EDGE_CONFIG
        )

        self.add(bg, g)

        p = ValueTracker(0)

        slider = ValueSlider(p=0, opacity=0.95, bar_color=sol.BASE1, z_index = 2)
        self.add(slider)
        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        nums = {}

        for r, e in coupling:
            nums[e] = DecimalNumber(
                    r,
                    font_size=40,
                    z_index=1
                )
            nums[e].color = BLACK
            nums[e].next_to(bg.edges[e], ORIGIN)
            self.add(nums[e])

        self.wait()

        prev_r = 0
        for r, e in list(coupling):
            self.play(
                g.animate.set_p(r),
                p.animate.set_value(r),
                run_time = 20 * (r - prev_r),
                rate_func = rate_functions.linear
            )
            prev_r = r

        if prev_r < 1:
            self.play(
                g.animate.set_p(1),
                p.animate.set_value(1),
                run_time = 20 * (1 - prev_r),
                rate_func = rate_functions.linear
            )

        self.wait()

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

        slider = ValueSlider(opacity=0.95, bar_color=sol.BASE1, z_index = 2)
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
        random.seed(1)

        nodes, edges = gr.grid_nodes_edges(24, 14)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        g = HPCCGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(24, 14, scale=0.3)
        )
        
        self.add(g)

        slider = ValueSlider(0, z_index = 2)
        self.add(slider)

        p = ValueTracker(0)

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

        p = ValueTracker(0.4)

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
