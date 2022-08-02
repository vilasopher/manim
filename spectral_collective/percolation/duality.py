from manim import *
from more_graphs import HPGraph
import grid as gr
import networkx as nx
import solarized as sol
from random import seed
from glitch import GlitchEdges

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

def z2add(u, v):
    return (u[0] + v[0], u[1] + v[1])

def boundary(primal_graph, o):
    c = nx.node_connected_component(primal_graph, o)

    q = [o]
    seen = []

    boundary = []

    while q:
        v = q.pop()
        seen.append(v)
        for diff in [(0,1),(0,-1),(1,0),(-1,0)]:
            u = z2add(v,diff)
            if u in c and u not in seen:
                q.append(u)
            elif u not in c:
                boundary.append(convert_edge(u,v))

    return boundary

def circuit_around_origin(primal_graph, dual_graph, shape, o):
    b = boundary(primal_graph, o)
    s = dual_graph.edge_subgraph(b).copy()

    for i in range(2 * shape[0]):
        j = shape[0] - i 
        if convert_edge((j-1+o[0],o[1]), (j+o[0],o[1])) in b or convert_edge((j+o[0],o[1]), (j-1+o[0],o[1])) in b:
            s.remove_edge((2*(j+o[0])-1,2*o[1]-1), (2*(j+o[0])-1,2*o[1]+1))
            return [(2*(j+o[0])-1,2*o[1]-1)] + nx.shortest_path(s, source=(2*(j+o[0])-1,2*o[1]+1), target=(2*(j+o[0])-1,2*o[1]-1))

class Duality(VGroup):
    def __init__(
        self,
        shape=(8,5),
        scale=0.95,
        primal_vertex_config = sol.VERTEX_CONFIG,
        primal_edge_config = sol.EDGE_CONFIG,
        dual_vertex_config = sol.DUAL_VERTEX_CONFIG,
        dual_edge_config = sol.DUAL_EDGE_CONFIG
    ):
        self.shape = shape
        self.scale = scale

        self.primal = HPGraph.from_grid(
            self.shape,
            scale=self.scale,
            vertex_config = primal_vertex_config,
            edge_config = primal_edge_config
        )

        dual_nodes, dual_edges = gr.dual_nodes_edges(*self.shape)
        nxdual = nx.Graph()
        nxdual.add_nodes_from(dual_nodes)
        nxdual.add_edges_from(dual_edges)

        self.dual = HPGraph.from_networkx(
            nxdual,
            layout=gr.dual_layout(*self.shape, scale=self.scale),
            vertex_config = dual_vertex_config,
            edge_config = dual_edge_config
        )

        super().__init__(self.dual, self.primal)

    def hide_dual(self):
        self.dual.shift(self.scale * 0.5 * (LEFT + DOWN))

    def reveal_dual(self):
        self.dual.shift(self.scale * 0.5 * (RIGHT + UP))

    def highlight_circuit_around_origin(self, origin = (0,0)):
        path = self.primal.path_to_boundary_from(origin)

        if len(path) == 0:
            circuit = circuit_around_origin(
                self.primal._graph, 
                self.dual._graph,
                self.shape,
                origin
            )
            self.dual.highlight_path(circuit, color = sol.FOREST_GREEN)

    def dramatically_highlight_circuit_around_origin(self, origin = (0,0)):
        path = self.primal.path_to_boundary_from(origin)

        if len(path) == 0:
            circuit = circuit_around_origin(
                self.primal._graph, 
                self.dual._graph,
                self.shape,
                origin
            )
            self.dual.highlight_path(circuit, color = sol.FOREST_GREEN)
            self.dual.unhighlight_complement(
                circuit,
                self.dual.path_edges(circuit),
                node_default_color = sol.DUAL_LIGHT_NODE,
                edge_default_color = sol.DUAL_LIGHT_EDGE
            )

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

class CircuitTest(Scene):
    def construct(self):
        d = Duality((24,14), 0.3)
        d.percolate(0.45)
        d.primal.dramatically_highlight_ball((0,0), root_scale_factor = 1.5)
        d.highlight_circuit_around_origin()
        self.add(d)

class HideRevealTest(Scene):
    def construct(self):
        d = Duality()

        self.add(d)
        self.wait()
        self.play(d.animate.hide_dual())
        self.wait()
        self.play(d.animate.reveal_dual())
        self.wait()

class DualityTest(Scene):
    def construct(self):
        d = Duality()
        d.hide_dual()

        self.add(d)

        self.wait()
        self.play(d.animate.reveal_dual())
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

        self.wait()

class ReRandomizeTest(Scene):
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
