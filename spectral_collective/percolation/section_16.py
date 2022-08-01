from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from more_graphs import PercolatingGraph, HPGrid
from glitch import Glitch, GlitchEdges, GlitchPercolate
from duality import Duality
import random


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

        g.primal.highlight_root((-4,-2))

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

        g.primal.highlight_path(
            path,
            color = average_color(sol.BASE3, sol.ORANGE),
            node_colors = { (-4,-2) : sol.RED }
        )

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
            (9, -5)
        ]

        g.dual.highlight_path(toobigcircuit, color = sol.FOREST_GREEN)

        self.add(g)
