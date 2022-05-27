from manim import *
from more_graphs import HPGraph
import grid as gr
import networkx as nx
import solarized as sol
from random import seed
from glitch import GlitchEdges

seed(0)

def convert_edge(u,v):
    if u[0] == v[0]:
        return (
            (2 * u[0] - 1, u[1] + v[1]),
            (2 * u[0] + 1, u[1] + v[1])
        )
    elif u[1] == u[1]:
        return (
            (u[0] + v[0], 2 * u[1] - 1),
            (u[0] + v[0], 2 * u[1] + 1)
        )

class Duality(VGroup):
    def __init__(self, shape=(8,5), scale=0.95):
        primal_nodes, primal_edges = gr.grid_nodes_edges(*shape)
        nxprimal = nx.Graph()
        nxprimal.add_nodes_from(primal_nodes)
        nxprimal.add_edges_from(primal_edges)

        self.primal = HPGraph.from_networkx(
            nxprimal,
            layout=gr.grid_layout(*shape, scale=scale),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )

        dual_nodes, dual_edges = gr.dual_nodes_edges(*shape)
        nxdual = nx.Graph()
        nxdual.add_nodes_from(dual_nodes)
        nxdual.add_edges_from(dual_edges)

        self.dual = HPGraph.from_networkx(
            nxdual,
            layout=gr.dual_layout(*shape, scale=scale),
            vertex_config = sol.DUAL_VERTEX_CONFIG,
            edge_config = sol.DUAL_EDGE_CONFIG
        )

        super().__init__(self.primal, self.dual)

    def percolate(self, p=0.5):
        primal_closed_edges = self.primal.random_edge_set(p)
        primal_open_edges = [ e for e in self.primal.edges
                              if e not in primal_closed_edges ]
        dual_closed_edges = [ convert_edge(*e) for e in primal_open_edges ]

        return (
            self.primal.remove_edges(*primal_closed_edges),
            self.dual.remove_edges(*dual_closed_edges)
        )

    @override_animate(percolate)
    def _percolate_animation(self, p=0.5, animation=FadeOut, **kwargs):
        primal_closed_edges = self.primal.random_edge_set(p)
        primal_open_edges = [ e for e in self.primal.edges
                              if e not in primal_closed_edges ]
        dual_closed_edges = [ convert_edge(*e) for e in primal_open_edges ]

        primalmobjects, dualmobjects = self.percolate(p)

        return AnimationGroup(
            AnimationGroup(*(animation(m, **kwargs) for m in primalmobjects)),
            AnimationGroup(*(animation(m, **kwargs) for m in dualmobjects))
        )

class DualityTest(Scene):
    def construct(self):
        d = Duality()

        self.add(d)
        self.wait()

        self.play(
            GlitchEdges(d.primal, out=True),
            GlitchEdges(d.dual, out=True),
            run_time=0.25
        )

        d = Duality()
        d.percolate()

        self.play(
            GlitchEdges(d.primal),
            GlitchEdges(d.dual),
            run_time=0.05
        )

        self.wait(3)

        self.play(
            GlitchEdges(d.primal, out=True),
            GlitchEdges(d.dual, out=True),
            run_time=0.05
        )

        d = Duality()

        self.play(
            GlitchEdges(d.primal, out=True),
            GlitchEdges(d.dual, out=True),
            run_time=0.2
        )

        d = Duality()
        d.percolate()

        self.play(
            GlitchEdges(d.primal),
            GlitchEdges(d.dual),
            run_time=0.05
        )

        self.wait(3)

        self.play(
            GlitchEdges(d.primal, out=True),
            GlitchEdges(d.dual, out=True),
            run_time=0.05
        )

        d = Duality()

        self.play(
            GlitchEdges(d.primal, out=True),
            GlitchEdges(d.dual, out=True),
            run_time=0.2
        )

        d = Duality()
        d.percolate()

        self.play(
            GlitchEdges(d.primal),
            GlitchEdges(d.dual),
            run_time=0.05
        )

        self.wait(3)
