from manim import *
import canopy_tree as ct
import highlight_ball as hb
from math import log

class GrowTree(Scene):
    def construct(self):
        g = ct.treeball(1)
        g.change_layout(ct.show_treeball(1, scaling=2.5))
        self.play(Create(g))

        nodes = ['a','b','c']
        for i in range(5):
            nodes, edges = ct.treeball_nodes_edges_next_layer(nodes)

            layout = ct.show_treeball(i+3, scaling=2.5 - 0.5 * log(i+1) , shrink_parameter=(2/3) - 0.01 * i)

            self.play(g.animate.add_vertices(*nodes, positions=layout),
                      g.animate.add_edges(*edges))

            if i < 4:
                layout = ct.show_treeball(i+3, scaling=2.5 - 0.5 * log(i+2) , shrink_parameter=(2/3) - 0.01 * i - 0.01)
                self.play(g.animate.change_layout(layout))

        self.wait()

        nodes, edges = hb.ball(g, 'ababab', 5)
        self.play(hb.HighlightSubgraph(g, nodes, edges))
        self.wait()

        canopy_layout = ct.show_canopy(6)
        self.play(g.animate.change_layout(canopy_layout))
        self.wait()

