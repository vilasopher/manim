from manim import Graph, Create, override_animate
from random import random
import networkx as nx

class PercolatingGraph(Graph):
    def __init__(self, nodes, edges, **kwargs) -> None:
        super().__init__(nodes, edges, **kwargs)

    def percolate(self, p=0.5):
        edges_to_remove = [ e for (e, _) in self.edges.items() if random() > p ]
        return self.remove_edges(*edges_to_remove)

    # TODO: the remove edges thing isn't even working in animation
    @override_animate(percolate)
    def _percolate_animation(self, p=0.5, *args, anim_args=None, **kwargs):
        edges_to_remove = [ e for (e, _) in self.edges.items() if random() > p ]
        return self.animate.remove_edges(*edges_to_remove, *args, anim_args, **kwargs)

    @staticmethod
    def from_networkx(nxgraph: nx.classes.graph.Graph, **kwargs) -> "PercolatingGraph":
        return PercolatingGraph(list(nxgraph.nodes), list(nxgraph.edges), **kwargs)
