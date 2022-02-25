from manim import Graph, Create, override_animate, FadeOut, AnimationGroup
from random import random
import networkx as nx
import solarized as sol

class HighlightableGraph(Graph):
    @staticmethod
    def from_networkx(nxgraph: nx.classes.graph.Graph, **kwargs) -> "HighlightableGraph":
        return HighlightableGraph(list(nxgraph.nodes), list(nxgraph.edges), **kwargs)

    def edges_spanned_by(self, nodes):
        return [e for (e, _) in self.edges.items() if e[0] in nodes and e[1] in nodes ]

    def highlight_subgraph(
        self,
        nodes,
        edges = None,
        node_colors = {},
        edge_colors = {}
    ):
        if edges == None:
            edges = self.edges_spanned_by(nodes)

        for n in nodes:
            self[n].set_color(node_colors.get(n, sol.HIGHLIGHT_NODE))

        for e in edges:
            self.edges[e].set_color(edge_colors.get(e, sol.HIGHLIGHT_EDGE))

    @override_animate(highlight_subgraph)
    def _highlight_subgraph_animation(
        self,
        nodes,
        edges = None,
        node_colors = {},
        edge_colors = {},
        **kwargs
    ):
        if edges == None:
            edges = self.edges_spanned_by(nodes)

        nodegroup = AnimationGroup(
            *(self[n].animate.set_color(node_colors.get(n, sol.HIGHLIGHT_NODE))
                for n in nodes)
        )

        edgegroup = AnimationGroup(
            *(self.edges[e].animate.set_color(edge_colors.get(e, sol.HIGHLIGHT_EDGE))
                for e in edges)
        )

        return AnimationGroup(nodegroup, edgegroup)
        
    def ball(self, root, radius):
        return set().union(
            *(nx.descendants_at_distance(self._graph, root, d)
            for d in range(radius+1))
        )

    def highlight_ball(self, root, radius):
        self.highlight_subgraph(self.ball(root, radius), node_colors = { root : sol.ROOT })

    @override_animate(highlight_ball)
    def _highlight_ball_animation(self, root, radius, **kwargs):
        return self._highlight_subgraph_animation(
            self.ball(root, radius),
            node_colors = { root : sol.ROOT },
            **kwargs
        )

class PercolatingGraph(Graph):
    @staticmethod
    def from_networkx(nxgraph: nx.classes.graph.Graph, **kwargs) -> "PercolatingGraph":
        return PercolatingGraph(list(nxgraph.nodes), list(nxgraph.edges), **kwargs)

    def random_edge_set(self, p=0.5):
        return [ e for (e, _) in self.edges.items() if random() > p ]

    def percolate(self, p=0.5):
        return self.remove_edges(*self.random_edge_set())

    @override_animate(percolate)
    def _percolate_animation(self, p=0.5, animation=FadeOut, **kwargs):
        edges_to_remove = self.random_edge_set(p)

        mobjects = [self.edges.pop(e) for e in edges_to_remove]
        self._graph.remove_edges_from(edges_to_remove)

        return AnimationGroup(
            *(animation(mobj, **kwargs) for mobj in mobjects), group=self
        )

class HPGraph(HighlightableGraph, PercolatingGraph):
    @staticmethod
    def from_networkx(nxgraph: nx.classes.graph.Graph, **kwargs) -> "HPGraph":
        return HPGraph(list(nxgraph.nodes), list(nxgraph.edges), **kwargs)
