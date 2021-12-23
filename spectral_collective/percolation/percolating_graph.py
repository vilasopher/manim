from manim import Graph, Create, override_animate
from random import random
import networkx as nx

class PercolatingGraph(Graph):
    def __init__(self, nodes, edges, **kwargs) -> None:
        super().__init__(self, nodes, edges, **kwargs)

    def percolate(self, parameter=0.5):
        edges_to_remove = [ e for e in self.edges if random() > parameter ]
        self.remove_edges(edges_to_remove)

    @override_animate(percolate)
    def _percolate_animation(self, parameter=0.5, *args, anim_args=None, **kwargs):
        edges_to_remove = [ e for e in self.edges if random() > parameter ]
        return self.animate.remove_edges(edges_to_remove)

    @staticmethod
    def from_networkx(nxgraph: nx.classes.graph.Graph, **kwargs) -> "PercolatingGraph":
        return PercolatingGraph(list(nxgraph.nodes), list(nxgraph.edges))
