from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from more_graphs import HPGraph
from glitch import Glitch, GlitchEdges, GlitchPercolate
import random

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
        random.seed(3)
        g = self.pipe_system(24, 14, 0.3)
        g .percolate()
        self.add(g)

        water_color = rgb_to_color([0,0.5,1])
        
        self.play(g.animate.highlight_subgraph([(0,0)], [], node_default_color=water_color))
        self.wait()

        self.play(g.percolation_flow_animation((0,0), water_color), run_time = 5)
        self.wait(3)

        self.play(GlitchEdges(g, intensity=0.05), run_time=0.25)

class PumpIn1(PipeSystemAbstract):
    def construct(self):
        g = self.pipe_system(24, 14, 0.3)
        g .percolate()
        self.add(g)

        self.play(GlitchEdges(g, intensity=0.05), run_time=0.25)
        self.wait(0.5)

        water_color = rgb_to_color([0,0.5,1])
        self.play(g.percolation_flow_animation((0,0), water_color), run_time = 3)
        self.wait(0.5)

        self.play(GlitchEdges(g, intensity=0.05), run_time=0.25)

class PumpIn2(PumpIn1):
    pass

class PumpIn3(PumpIn1):
    pass

class PumpIn4(PumpIn1):
    pass
