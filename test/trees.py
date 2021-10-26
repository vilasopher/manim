from manim import *
import newballs
import networkx as nx

class TreeScene(Scene):
    def construct(self):
        nxgraph = nx.balanced_tree(3,4)
        g = Graph.from_networkx(nxgraph)

        self.play(Create(g))
        self.play(g.animate.change_layout("tree", root_vertex=0))
        self.wait()
