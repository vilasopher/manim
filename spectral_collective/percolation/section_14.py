from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from more_graphs import PercolatingGraph, HPGrid
from glitch import Glitch, GlitchEdges, GlitchPercolate
import random

def safe_edge(g, e):
    return g.edges[e] if e in g.edges else g.edges[(e[1], e[0])]

class PrePercolated(Scene):
    def construct(self):
        g = HPGrid.from_grid(
            (8, 5),
            0.95,
            vertex_config = {'fill_color' : sol.BASE00},
            edge_config = {'stroke_color' : sol.BASE1}
        )
        g.highlight_root((2,2))

        self.add(g)
        self.wait(8.5)
        self.play(GlitchEdges(g, intensity=0.03), run_time=0.5)

class Percolated(Scene):
    def construct(self):
        random.seed(0)

        g = HPGrid.from_grid(
            (8, 5),
            0.95,
            vertex_config = {'fill_color' : sol.BASE00},
            edge_config = {'stroke_color' : sol.BASE1}
        )
        g.percolate()
        g.highlight_root((2,2))
        g.unhighlight_complement_ball((2, 2))
        self.add(g)

        self.play(GlitchEdges(g, intensity=0.03), run_time=0.5)

        path = [
            (2, 2),
            (3, 2),
            (3, 3),
            (4, 3),
            (4, 2),
            (5, 2),
            (5, 1),
            (5, 0),
            (5, -1),
            (6, -1),
            (7, -1),
            (8, -1)
        ]

        self.wait()

        self.play(
            g.animate.highlight_path(path, node_colors = {(2, 2) : sol.ROOT}),
            run_time = 2
        )

        self.wait(3)

        self.play(
            g.animate.highlight_path(
                path[:8],
                color = sol.FOREST_GREEN,
                node_colors = {(2, 2) : sol.ROOT}
            ), run_time = 1
        )
        
        self.play(
            g.animate.highlight_subgraph(
                path[7:],
                node_default_color = sol.BASE00,
                edge_default_color = sol.BASE1,
                node_colors = {(5, 0) : sol.FOREST_GREEN}
            ), run_time = 1
        )

        self.wait(50 - 17)

        for j in range(7):
            self.play(Indicate(safe_edge(g, (path[j], path[j+1]))), run_time=0.5)

        self.wait(20)


class UnPercolated(Scene):
    def construct(self):
        g = HPGrid.from_grid(
            (8,5),
            0.95,
            vertex_config = {'fill_color' : sol.BASE2},
            edge_config = {'stroke_color' : sol.BASE2}
        )
        g.highlight_root((2,2))

        for v in g.vertices:
            g[v].set(z_index = 2)

        self.add(g)

        self.wait(20)

        self.play(
            Indicate(safe_edge(g, ((2,2),(2,3)))),
            Indicate(safe_edge(g, ((2,2),(1,2)))),
            Indicate(safe_edge(g, ((2,2),(2,1)))),
            Indicate(safe_edge(g, ((2,2),(3,2)))),
            run_time = 2
        )

        self.play(
            g.animate.highlight_subgraph(
                [(3, 2)],
                [((2,2), (3,2))], 
                node_default_color = sol.FOREST_GREEN,
                edge_default_color = sol.FOREST_GREEN
            )
        )

        self.wait()

        path = [
            (2, 2),
            (3, 2),
            (3, 3),
            (4, 3),
            (4, 2),
            (5, 2),
            (5, 1),
            (5, 0),
        ]

        des = [ (0, -1), (1, 0), (0, 1), (-1, 0) ] 

        def tuple_add(u,v):
            return (u[0]+v[0], u[1]+v[1])

        for i in range(1, len(path)-1):

            excluded = path[:i]
            tries = [
                (path[i], tuple_add(path[i], de))
                for de in des if tuple_add(path[i], de) not in excluded
            ]

            self.play(
                *(
                    Indicate(safe_edge(g, t))
                    for t in tries
                ),
                run_time = 2 if i == 1 else 1
            )

            self.play(
                g.animate.highlight_subgraph(
                    [path[i+1]],
                    [(path[i], path[i+1])], 
                    node_default_color = sol.FOREST_GREEN,
                    edge_default_color = sol.FOREST_GREEN
                ), run_time= 1 if i == 1 else 0.5
            )

        self.wait(2)

        self.play(
            g.animate.highlight_subgraph(
                path,
                node_default_color = sol.BASE2,
                edge_default_color = sol.BASE2,
                node_colors = { (2,2) : sol.ROOT }
            ), run_time = 0.5
        )

        badpath = [
            (2, 2),
            (3, 2),
            (4, 2),
            (5, 2),
            (5, 1),
            (4, 1),
            (4, 2),
            (4, 3)
        ]

        for i in range(len(badpath) - 1):
            g.highlight_subgraph(
                [badpath[i+1]],
                [(badpath[i],badpath[i+1])],
                node_default_color = sol.FOREST_GREEN,
                edge_default_color = sol.FOREST_GREEN
            )
            self.wait(0.4)

        self.wait(0.7)

        self.play(
            g.animate.highlight_subgraph(
                badpath,
                node_default_color = sol.BASE2,
                edge_default_color = sol.BASE2,
                node_colors = { (2,2) : sol.ROOT }
            ), run_time = 0.5
        )

        goodpath = [
            (2, 2),
            (3, 2),
            (3, 1),
            (4, 1),
            (4, 0),
            (5, 0),
            (6, 0),
            (6, -1)
        ]

        for i in range(len(goodpath) - 1):
            g.highlight_subgraph(
                [goodpath[i+1]],
                [(goodpath[i],goodpath[i+1])],
                node_default_color = sol.FOREST_GREEN,
                edge_default_color = sol.FOREST_GREEN
            )
            self.wait(0.4)

        self.wait(50)
