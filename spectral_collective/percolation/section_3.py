from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from more_graphs import HPCCGraph, HPGraph
from glitch import Glitch, GlitchEdges, GlitchPercolate
import random

WATER_COLOR = rgb_to_color([0,0.5,1])

class PipeSystemAbstract(Scene):
    def pipe_system(self, width, height, scale):
        nodes, edges = gr.grid_nodes_edges(width, height)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        return HPGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(width, height, scale=scale),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )

class GlitchingPipeSystem(PipeSystemAbstract):
    def construct(self):
        g = self.pipe_system(24,14,0.3)
        self.play(GlitchEdges(g, intensity=0.05), run_time=0.5)

class GlitchInPipeSystem1(PipeSystemAbstract):
    def construct(self):
        g = self.pipe_system(24,14,0.3)
        g.percolate()
        self.play(GlitchEdges(g, intensity=0.05), run_time=0.25)
        self.wait(2.5)
        self.play(GlitchEdges(g, intensity=0.05), run_time=0.25)

class GlitchInPipeSystem2(GlitchInPipeSystem1):
    pass

class GlitchInPipeSystem3(GlitchInPipeSystem1):
    pass

class GlitchInPipeSystemFinal(PipeSystemAbstract):
    def construct(self):
        random.seed(3)
        g = self.pipe_system(24,14,0.3)
        g.percolate()
        self.play(GlitchEdges(g, intensity=0.05), run_time=0.25)
        self.wait(5)

class PumpInInitial(PipeSystemAbstract):
    def construct(self):
        random.seed(5)
        g = self.pipe_system(24, 14, 0.3)
        g .percolate()
        self.add(g)

        self.play(g.animate.highlight_subgraph([(0,0)], [], node_default_color=WATER_COLOR))
        self.wait()

        self.play(g.percolation_flow_animation((0,0), WATER_COLOR), run_time = 5)
        self.wait(3)

        self.play(GlitchEdges(g, intensity=0.05), run_time=0.25)

class PumpIn1(PipeSystemAbstract):
    def construct(self):
        g = self.pipe_system(24, 14, 0.3)
        g .percolate()
        self.add(g)

        self.play(GlitchEdges(g, intensity=0.05), run_time=0.25)
        self.wait(0.5)

        self.play(g.percolation_flow_animation((0,0), WATER_COLOR), run_time = 3)
        self.wait(0.5)

        self.play(GlitchEdges(g, intensity=0.05), run_time=0.25)

class PumpIn2(PumpIn1):
    pass

class PumpIn3(PumpIn1):
    pass

class PumpIn4(PumpIn1):
    pass

def random_color():
    c = rgb_to_color([random.randint(0,255)/255 for _ in range(3)])

    while c == sol.NODE:
        c = rgb_to_color([random.randint(0,255)/255 for _ in range(3)])

    return c

class PumpInMultiple(PipeSystemAbstract): #LENGTH: 35.25
    def construct(self):
        random.seed(3)
        g = self.pipe_system(24, 14, 0.3)
        g.percolate()

        self.play(GlitchEdges(g, intensity=0.05), run_time=0.25)
        self.wait(0.5)

        self.play(g.percolation_flow_animation((0,0), WATER_COLOR), run_time = 3)
        self.wait(2.5)

        # 6.75
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
        random.shuffle(vs)

        clustercount = 0

        for v in vs:
            if g.vertices[v].color == sol.NODE:
                col = random_color()
                self.play(
                    g.percolation_flow_animation(v, col),
                    run_time = 100 / (clustercount+10) ** 2
                )
                clustercount += 1

        return

        self.wait(10)

        self.play(GlitchEdges(g, intensity=0.05), run_time=0.25)

class ColoredAbstract(Scene):
    def pipe_system(self, width, height, scale):
        nodes, edges = gr.grid_nodes_edges(width, height)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        return HPCCGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(width, height, scale=scale),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )

class Colored1(ColoredAbstract):
    def construct(self):
        g = self.pipe_system(24,14,0.3)
        g.set_p(0.5)
        self.play(GlitchEdges(g, intensity=0.05), run_time=0.25)
        self.wait(2.5)
        self.play(GlitchEdges(g, intensity=0.05), run_time=0.25)

class Colored2(Colored1):
    pass

class Colored3(Colored1):
    pass

class Colored4(Colored1):
    pass

class Colored5(Colored1):
    pass

class Colored6(Colored1):
    pass

class Colored7(Colored1):
    pass

class Colored8(Colored1):
    pass

class Colored9(Colored1):
    pass
