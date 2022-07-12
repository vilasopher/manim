from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from more_graphs import HPCCGraph
from glitch import Glitch, GlitchEdges, GlitchPercolate
import random

class ParameterSamples(Scene):
    def construct(self):
        random.seed(0)

        nodes, edges = gr.grid_nodes_edges(24, 14)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        slider = ValueSlider(1/11, z_index = 2)
        self.add(slider)

        ivalues = [ 6, 7, 9, 10, 11, 8, 5, 3, 2,
                    1, 4, 6, 8, 10, 11,
                    9, 5, 7, 3 ]

        for i in ivalues:
            g = HPCCGraph.from_networkx(
                nxgraph,
                layout=gr.grid_layout(24, 14, scale=0.3)
            )

            g.set_p(i/12)
            self.play(
                GlitchEdges(g),
                # slider.animate.set_p((i+1)/11), THIS NEEDS TO GO IN TRANSPARENCIES
                run_time=0.25
            )
            self.wait(2.5)
            self.play(GlitchEdges(g), run_time=0.25)
