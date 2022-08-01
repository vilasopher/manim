from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from more_graphs import PercolatingGraph, HPGrid
from glitch import Glitch, GlitchEdges, GlitchPercolate
from duality import Duality
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
