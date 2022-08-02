from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from more_graphs import PercolatingGraph, HPGrid
from glitch import Glitch, GlitchEdges, GlitchPercolate
from duality import Duality, convert_edge
import random

def safe_edge(g, e):
    return g.edges[e] if e in g.edges else g.edges[(e[1], e[0])]

class NumberOfCircuits(Scene):
    def construct(self):
        g = Duality(
            (8,5),
            0.95,
            primal_vertex_config = sol.VERY_LIGHT_VERTEX_CONFIG,
            primal_edge_config = sol.VERY_LIGHT_EDGE_CONFIG,
            dual_vertex_config = sol.DUAL_LIGHT_VERTEX_CONFIG,
            dual_edge_config = sol.DUAL_LIGHT_EDGE_CONFIG
        )

        g.primal[(-4,-2)].set(z_index = 3)

        g.primal.highlight_root((-4,-2))

        self.add(g)

        self.wait(10)

        path = [
            (-4, -2),
            (-3, -2),
            (-2, -2),
            (-1, -2),
            (0, -2),
            (1, -2),
            (2, -2),
            (3, -2),
            (4, -2)
        ]

        p = Graph(
            vertices = path,
            edges = [(path[i],path[i+1]) for i in range(len(path)-1)],
            vertex_config = {'fill_color' : average_color(sol.BASE3, sol.ORANGE)},
            edge_config = {'stroke_color' : average_color(sol.BASE3, sol.ORANGE)},
            layout = gr.grid_layout(8,5,scale=0.95)
        )
        for v in p.vertices:
            p[v].set(z_index = 2)
        for e in p.edges:
            p.edges[e].set(z_index = 2)

        self.play(FadeIn(p))

        brace = BraceBetweenPoints(
            p[(-4,-2)].get_center(),
            p[(4,-2)].get_center(),
            color = sol.BASE03,
            z_index = 3
        ).shift(0.5 * DOWN)

        label = MathTex(r'{{\ell}} / 2', color = sol.BASE03).set_color_by_tex(r'\ell', sol.FOREST_GREEN)
        label.next_to(brace, DOWN)
        label.set(z_index = 3)

        self.play(
            FadeIn(brace, shift=UP),
            FadeIn(label, shift=UP)
        )

        self.wait(4)

        toobigcircuit = [
            (9, -5),
            (9, -3),
            (7, -3),
            (5, -3),
            (3, -3),
            (1, -3),
            (-1, -3),
            (-3, -3),
            (-5, -3),
            (-7, -3),
            (-9, -3),
            (-9, -5),
            (-7, -5),
            (-5, -5),
            (-3, -5),
            (-1, -5),
            (1, -5),
            (3, -5),
            (5, -5),
            (7, -5),
        ]

        tbc = Graph(
            vertices = toobigcircuit,
            edges = [(toobigcircuit[i-1],toobigcircuit[i]) for i in range(len(toobigcircuit))],
            vertex_config = {'fill_color' : sol.FOREST_GREEN},
            edge_config = {'stroke_color' : sol.FOREST_GREEN},
            layout = gr.dual_layout(8,5,scale=0.95)
        )
        for v in tbc.vertices:
            tbc[v].set(z_index = 2)
        for e in tbc.edges:
            tbc.edges[e].set(z_index = 2)

        self.play(FadeIn(tbc[toobigcircuit[-1]]), run_time=0.25)
        for i in range(len(toobigcircuit)):
            if i < len(toobigcircuit)-1:
                self.play(
                    FadeIn(tbc.edges[(toobigcircuit[i-1],toobigcircuit[i])]),
                    FadeIn(tbc[toobigcircuit[i]]),
                    run_time=0.25
                )
            else:
                self.play(
                    FadeIn(tbc.edges[(toobigcircuit[i-1],toobigcircuit[i])]),
                    run_time=0.25
                )

        self.wait(2.75)
        self.play(FadeOut(tbc))
        self.wait()

        circuit = [
            (-3, -3),
            (-5, -3),
            (-7, -3),
            (-9, -3),
            (-11, -3),
            (-13, -3),
            (-13, -5),
            (-13, -7),
            (-11, -7),
            (-11, -5),
            (-9, -5),
            (-9, -7),
            (-7, -7),
            (-5, -7),
            (-3, -7),
            (-3, -5)
        ]

        c = Graph(
            vertices = circuit,
            edges = [(circuit[i-1],circuit[i]) for i in range(len(circuit))],
            vertex_config = {'fill_color' : sol.FOREST_GREEN},
            edge_config = {'stroke_color' : sol.FOREST_GREEN},
            layout = gr.dual_layout(8,5,scale=0.95)
        )
        for v in c.vertices:
            c[v].set(z_index = 2)
        for e in c.edges:
            c.edges[e].set(z_index = 2)

        self.play(
            FadeIn(c.edges[((-3,-5),(-3,-3))]),
            FadeIn(c[(-3,-3)]),
            FadeIn(c[(-3,-5)])
        )

        self.wait()

        des = [ (0, -2), (2, 0), (0, 2), (-2, 0) ] 

        def tuple_add(u,v):
            return (u[0]+v[0], u[1]+v[1])

        for i in range(len(circuit)-1):
            visited = circuit[:i]

            tries = [
                (circuit[i], tuple_add(circuit[i], de))
                for de in des if tuple_add(circuit[i], de) not in visited
            ]

            self.play(
                *(
                    Indicate(safe_edge(g.dual, t))
                    for t in tries
                ),
                run_time = 2 if i == 0 else 1
            )

            if i < len(circuit)-2:
                self.play(
                    FadeIn(c.edges[(circuit[i],circuit[i+1])]),
                    FadeIn(c[circuit[i+1]]),
                    run_time= 1 if i == 0 else 0.5
                )
            else:
                self.play(
                    FadeIn(c.edges[(circuit[i],circuit[i+1])]),
                    run_time=0.5
                )



        self.wait(30)

class BigCircuit(Scene):
    def construct(self):
        random.seed(12)
        g = Duality((24, 14), 0.3)
        g.percolate(0.5)

        self.play(
            GlitchEdges(g.primal, intensity=0.04),
            GlitchEdges(g.dual, intensity=0.04),
            run_time = 0.25
        )

        self.wait(0.75)

        self.play(
            g.primal.animate.dramatically_highlight_ball(
                (0,0),
                root_scale_factor = 1.5
            )
        )

        self.wait(1.5)

        self.play(
            g.animate.dramatically_highlight_circuit_around_origin()
        )

        self.wait(50)

class HugeCircuit(Scene):
    def construct(self):
        random.seed(20)
        g = Duality(
            (24, 14),
            0.3,
            primal_vertex_config = sol.VERY_LIGHT_VERTEX_CONFIG,
            primal_edge_config = sol.VERY_LIGHT_EDGE_CONFIG,
            dual_vertex_config = sol.DUAL_LIGHT_VERTEX_CONFIG,
            dual_edge_config = sol.DUAL_LIGHT_EDGE_CONFIG
        )
        g.percolate(0.5)

        bad_edges = [ 
            ((5,-13), (5,-12)),
            ((7,-13), (7,-12)),
            ((10,-13), (10,-12))
        ]

        g.primal.remove_edges(*bad_edges)
        g.dual.add_edges(*(convert_edge(*e) for e in bad_edges))

        g.primal.highlight_root((0,0), scale_factor=1.5)
        g.highlight_circuit_around_origin()

        self.add(g)

class BigBox(Scene):
    def construct(self):
        random.seed(14)
        g = Duality(
            (24, 14),
            0.3,
            primal_vertex_config = sol.VERY_LIGHT_VERTEX_CONFIG,
            primal_edge_config = sol.VERY_LIGHT_EDGE_CONFIG,
            dual_vertex_config = sol.DUAL_LIGHT_VERTEX_CONFIG,
            dual_edge_config = sol.DUAL_LIGHT_EDGE_CONFIG
        )
        g.percolate(0.5)
        g.primal.highlight_root((14,4), scale_factor = 1.5)

        self.add(g)

        boxcorners = [
            (14+8, 4+8),
            (14-8, 4+8),
            (14-8, 4-8),
            (14+8, 4-8)
        ]

        side1 = [ (14+8-i, 4+8) for i in range(16) ]
        side2 = [ (14-8, 4+8-i) for i in range(16) ]
        side3 = [ (14-8+i, 4-8) for i in range(16) ]
        side4 = [ (14+8, 4-8+i) for i in range(16) ]

        box = side1 + side2 + side3 + side4
        box_edges = [
            (u,v) for u in box for v in box
            if np.abs(u[0]-v[0]) + np.abs(u[1]-v[1]) == 1
        ]

        b = Graph(
            box,
            box_edges,
            vertex_config = { 'fill_color' : sol.VIOLET },
            edge_config = { 'stroke_color' : sol.VIOLET },
            layout = gr.grid_layout(24, 14, scale=0.3)
        )
        for v in b.vertices:
            b[v].set(z_index = 2)
        for e in b.edges:
            b.edges[e].set(z_index = 2)

        self.add(b)

        self.wait(15)

        box_to_infinity = [
            (6, -1),
            (5, -1),
            (4, -1),
            (3, -1),
            (2, -1),
            (1, -1),
            (1, 0),
            (0, 0),
            (0, -1),
            (-1, -1),
            (-2, -1),
            (-2, -2),
            (-3, -2),
            (-4, -2),
            (-5, -2),
            (-5, -1),
            (-6, -1),
            (-7, -1),
            (-8, -1),
            (-8, -2),
            (-8, -3),
            (-8, -4),
            (-8, -5),
            (-9, -5),
            (-10, -5),
            (-10, -6),
            (-11, -6),
            (-11, -7),
            (-11, -8),
            (-10, -8),
            (-10, -9),
            (-11, -9),
            (-11, -10),
            (-12, -10),
            (-12, -11),
            (-12, -12),
            (-11, -12),
            (-10, -12),
            (-9, -12),
            (-8, -12),
            (-8, -13),
            (-8, -14)
        ]
        
        self.play(
            g.primal.animate.highlight_path(
                box_to_infinity,
                node_default_color=sol.HIGHLIGHT_NODE,
                edge_default_color=sol.HIGHLIGHT_EDGE
            ),
            run_time = 5
        )
        self.wait(4.5)

        box_interior_vertices = [
            (i, j)
            for i in range(14-8,14+8+1)
            for j in range(4-8,4+8-1)
        ]

        box_interior_edges = [
            (u,(u[0]+d[0], u[1]+d[1]))
            for u in box_interior_vertices
            for d in [(1,0),(0,1)]
            if u[0]+d[0] <= 14+8 and u[1]+d[1] <= 4+8
        ]

        self.play(
            Glitch(
                Group(
                    *(
                        g.primal.edges[g.primal.safe_edge(e)]
                        for e in box_interior_edges
                        if e in g.primal.edges
                    )
                ),
                intensity = 0.04,
                simple = True
            ),
            run_time = 1
        )

        g.primal.add_edges(
            *(
                e for e in box_interior_edges
                if e not in g.primal.edges
            )
        )
        g.dual.remove_edges(
            *(
                convert_edge(*e) for e in box_interior_edges
                if convert_edge(*e) in g.dual.edges
            )
        )
        g.primal.highlight_subgraph(
            box_interior_vertices,
            node_colors = { (14,4) : sol.RED },
        )

        self.play(
            Glitch(
                Group(
                    *(
                        g.primal.edges[g.primal.safe_edge(e)]
                        for e in box_interior_edges
                    )
                ),
                intensity = 0.04
            ),
            run_time = 1
        )

        self.wait(25.5)
        
        origin_to_box = [
            (14, 4),
            (13, 4),
            (13, 3),
            (12, 3),
            (12, 2),
            (11, 2),
            (11, 1),
            (10, 1),
            (10, 0),
            (9, 0),
            (9, -1),
            (8, -1),
            (7, -1)
        ]

        origin_to_infinity = origin_to_box + box_to_infinity

        self.play(g.primal.animate.highlight_path(origin_to_infinity))

        self.wait(30)
