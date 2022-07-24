from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from more_graphs import HPCCGraph, HPGraph
from glitch import Glitch, GlitchEdges, GlitchPercolate
import random
import binary_tree as bt

def interp(alpha):
    return np.sqrt((1 - np.cos(2 * np.pi * alpha)) / 2)

def almost_linear(alpha):
    return interp(alpha) * alpha + (1 - interp(alpha)) * (1 - np.cos(np.pi * alpha)) / 2

class BinaryTreeCouplingAbstract(Scene):
    def construct_abstract(self, start, end, run_time=10):
        random.seed(10) #1, 5, 7

        nxgraph = nx.balanced_tree(2,8)
        g = HPCCGraph.from_networkx(
            nxgraph,
            vertex_config=sol.VERTEX_CONFIG,
            edge_config=sol.EDGE_CONFIG,
            layout=bt.binary_tree_layout(
                8, 
                shift=3.5*UP,
                horizontal_scale=10.2,
                vertical_scale=3.45
            )
        )

        p = ValueTracker(start if start < end else end)
        g.set_p(p.get_value())
        g.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.add(g)

        self.play(
            p.animate.set_value(end if start < end else start),
            run_time=run_time,
            rate_func=almost_linear
        )

class BinaryTreeCoupling(BinaryTreeCouplingAbstract):
    def construct(self):
        self.construct_abstract(0,1,10)
