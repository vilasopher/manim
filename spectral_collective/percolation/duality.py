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

DIRECTIONS = [(0,2), (-2,0), (0,-2), (2,0)]
MY_UP = (0,2)
MY_LEFT = (-2,0)
MY_DOWN = (0,-2)
MY_RIGHT = (2,0)

def turn_left(u,v):
    return (-v, u)

def turn_right(u,v):
    return (v, -u)

def turn_back(u,v):
    return (-u,-v)

def edgeQ(graph, u, v):
    return (u,v) in graph.edges or (v,u) in graph.edges

def z2add(u, v):
    return (u[0] + v[0], u[1] + v[1])

def longest_winding_path(dual, start):
    path = [start]
    directions = []
    current_dir = MY_RIGHT

    excluded_nodes = []

    print('called, start=',start)

    while len(path) > 0:
        current_dir = turn_left(*current_dir)
        next_node = z2add(path[-1], current_dir)
        
        success = False

        for _ in range(3):
            if next_node in excluded_nodes or not edgeQ(dual, path[-1], next_node):
                current_dir = turn_right(*current_dir)
                next_node = z2add(path[-1], current_dir)
            elif next_node in path:
                i = path.index(next_node)
                path = path[:i+1]
                directions = directions[:i]
                excluded_nodes.append(next_node)
                break
            else:
                path.append(next_node)
                directions.append(current_dir)
                success = True
                break

        if not success:
            excluded_nodes.append(path.pop())

            if len(path) > 0:
                current_dir = directions.pop()
            else:
                return []

        if success and path[-1] == start:
            return path

        print(len(path))

    return []

def circuit_around_origin(dual):
    for i in range(len(dual)):
        if (2 * i + 1, -1) not in dual.vertices:
            return []
        elif edgeQ(dual, (2 * i + 1, -1), (2 * i + 1, 1)):
            path = longest_winding_path(dual, (2 * i + 1, -1))
            if len(path) > 0:
                return path

class Duality(VGroup):
    def __init__(self, shape=(8,5), scale=0.95):
        self.scale = scale

        self.primal = HPGraph.from_grid(shape, scale=self.scale)

        dual_nodes, dual_edges = gr.dual_nodes_edges(*shape)
        nxdual = nx.Graph()
        nxdual.add_nodes_from(dual_nodes)
        nxdual.add_edges_from(dual_edges)

        self.dual = HPGraph.from_networkx(
            nxdual,
            layout=gr.dual_layout(*shape, scale=self.scale),
            vertex_config = sol.DUAL_VERTEX_CONFIG,
            edge_config = sol.DUAL_EDGE_CONFIG
        )

        super().__init__(self.dual, self.primal)

    def hide_dual(self):
        self.dual.shift(self.scale * 0.5 * (LEFT + DOWN))

    def reveal_dual(self):
        self.dual.shift(self.scale * 0.5 * (RIGHT + UP))

    def highlight_circuit_around_origin(self):
        path = self.primal.path_to_boundary_from((0,0))

        if len(path) == 0:
            circuit = circuit_around_origin(self.dual)
            self.dual.highlight_path(circuit)

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
