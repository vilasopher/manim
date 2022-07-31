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
        g = HPGrid.from_grid((8, 5), 0.95)
        g.highlight_root((2,2))

        self.add(g)
        self.wait(8.5)
        self.play(GlitchEdges(g, intensity=0.03), run_time=0.5)

class Percolated(Scene):
    def construct(self):
        random.seed(0)

        g = HPGrid.from_grid((8,5), 0.95)
        g.percolate()
        g.dramatically_highlight_ball((2, 2))
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
                color = sol.GREEN,
                node_colors = {(2, 2) : sol.ROOT}
            ), run_time = 1
        )
        
        self.play(
            g.animate.highlight_subgraph(
                path[7:],
                node_default_color = sol.HIGHLIGHT_NODE,
                edge_default_color = sol.HIGHLIGHT_EDGE,
                node_colors = {(5, 0) : sol.GREEN}
            ), run_time = 1
        )

        self.wait(50 - 17)

        for j in range(7):
            self.play(Indicate(safe_edge(g, (path[j], path[j+1]))), run_time=0.5)

        self.wait(20)


class UnPercolated(Scene):
    def construct(self):
        g = HPGrid.from_grid((8,5), 0.95)
        g.highlight_root((2,2))

        for v in g.vertices:
            g[v].set(z_index = 2)

        self.add(g)

        self.wait(20)

        self.play(Indicate(safe_edge(g, ((2,2),(2,3)))))
        self.play(Indicate(safe_edge(g, ((2,2),(1,2)))))
        self.play(Indicate(safe_edge(g, ((2,2),(2,1)))))

        self.play(
            g.animate.highlight_subgraph(
                [(3, 2)],
                [((2,2), (3,2))], 
                node_default_color = sol.GREEN,
                edge_default_color = sol.GREEN
            )
        )

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

            excluded = [ path[i-1], path[i+1] ]
            tries = [
                (path[i], tuple_add(path[i], de))
                for de in des if tuple_add(path[i], de) not in excluded
            ]

            self.play(Indicate(safe_edge(g, tries[0])), run_time=1 if i == 1 else 0.5)
            self.play(Indicate(safe_edge(g, tries[1])), run_time=1 if i == 1 else 0.5)

            self.play(
                g.animate.highlight_subgraph(
                    [path[i+1]],
                    [(path[i], path[i+1])], 
                    node_default_color = sol.GREEN,
                    edge_default_color = sol.GREEN
                ), run_time= 1 if i == 1 else 0.5
            )

        self.wait(3)

        self.play(
            g.animate.highlight_subgraph(
                path,
                node_default_color = sol.NODE,
                edge_default_color = sol.EDGE,
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

        self.play(
            g.animate.highlight_path(
                badpath,
                color = sol.GREEN,
                node_colors = { (2,2) : sol.ROOT }
            ), run_time = 3
        )

        self.wait(0.5)

        self.play(
            g.animate.highlight_subgraph(
                badpath,
                node_default_color = sol.NODE,
                edge_default_color = sol.EDGE,
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

        self.play(
            g.animate.highlight_path(
                goodpath,
                color = sol.GREEN,
                node_colors = { (2,2) : sol.ROOT }
            ), run_time = 3
        )

        self.wait(50)
