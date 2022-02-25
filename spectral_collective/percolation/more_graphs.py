from manim import Graph, Create, override_animate, FadeOut, AnimationGroup
from random import random
import networkx as nx
import solarized as sol

class HighlightableGraph(Graph):
    @staticmethod
    def from_networkx(nxgraph: nx.classes.graph.Graph, **kwargs) -> "HighlightableGraph":
        return HighlightableGraph(list(nxgraph.nodes), list(nxgraph.edges), **kwargs)

    def edges_spanned_by(self, nodes):
        return [e for e in self.edges if e[0] in nodes and e[1] in nodes ]
    
    def highlight_subgraph(
        self,
        nodes,
        edges = None,
        node_colors = {},
        node_default_color = sol.HIGHLIGHT_NODE,
        edge_colors = {},
        edge_default_color = sol.HIGHLIGHT_EDGE
    ):
        if edges == None:
            edges = self.edges_spanned_by(nodes)

        for n in nodes:
            self[n].set_color(node_colors.get(n, node_default_color))

        for e in edges:
            self.edges[e].set_color(edge_colors.get(e, edge_default_color))

    @override_animate(highlight_subgraph)
    def _highlight_subgraph_animation(
        self,
        nodes,
        edges = None,
        node_colors = {},
        node_default_color = sol.HIGHLIGHT_NODE,
        edge_colors = {},
        edge_default_color = sol.HIGHLIGHT_EDGE,
        **kwargs
    ):
        if edges == None:
            edges = self.edges_spanned_by(nodes)

        nodegroup = AnimationGroup(
            *(self[n].animate.set_color(node_colors.get(n, node_default_color))
                for n in nodes)
        )

        edgegroup = AnimationGroup(
            *(self.edges[e].animate.set_color(edge_colors.get(e, edge_default_color))
                for e in edges)
        )

        return AnimationGroup(nodegroup, edgegroup)

    def complement_nodes_edges(self, nodes, edges):
        complement_nodes = [ n for n in self.vertices if not n in nodes ]
        complement_edges = [ e for e in self.edges if not e in edges ]
        return complement_nodes, complement_edges

    def unhighlight_complement(self, nodes, edges=None, **kwargs):
        if edges == None:
            edges = self.edges_spanned_by(nodes)

        complement_nodes, complement_edges = self.complement_nodes_edges(nodes, edges)

        self.highlight_subgraph(
            complement_nodes,
            complement_edges, 
            node_default_color = sol.UNHIGHLIGHT_NODE,
            edge_default_color = sol.UNHIGHLIGHT_EDGE,
            **kwargs
        )

    @override_animate(unhighlight_complement)
    def _unhighlight_complement_animation(self, nodes, edges=None, **kwargs):
        if edges == None:
            edges = self.edges_spanned_by(nodes)

        complement_nodes, complement_edges = self.complement_nodes_edges(nodes, edges)

        return self._highlight_subgraph_animation(
            complement_nodes,
            complement_edges,
            node_default_color = sol.UNHIGHLIGHT_NODE,
            edge_default_color = sol.UNHIGHLIGHT_EDGE,
            **kwargs
        )

    def ball(self, root, radius=None):
        bfs = nx.bfs_edges(self._graph, source=root, depth_limit=radius)
        return [root] + [v for u, v in bfs]

    def highlight_ball(self, root, radius=None):
        self.highlight_subgraph(self.ball(root, radius), node_colors = { root : sol.ROOT })

    @override_animate(highlight_ball)
    def _highlight_ball_animation(self, root, radius=None, **kwargs):
        return self._highlight_subgraph_animation(
            self.ball(root, radius),
            node_colors = { root : sol.ROOT },
            **kwargs
        )

    def unhighlight_complement_ball(self, root, radius=None):
        self.unhighlight_complement(self.ball(root, radius))

    @override_animate(unhighlight_complement_ball)
    def _unhighlight_complement_ball_animation(self, root, radius=None, **kwargs):
        return self._unhighlight_complement_animation(self.ball(root, radius), **kwargs)

    def dramatically_highlight_ball(self, root, radius=None):
        self.highlight_ball(root, radius)
        self.unhighlight_complement_ball(root, radius)

    @override_animate(dramatically_highlight_ball)
    def _dramatically_highlight_ball_animation(self, root, radius=None, **kwargs):
        return AnimationGroup(
            self._highlight_ball_animation(root, radius, **kwargs),
            self._unhighlight_complement_ball_animation(root, radius, **kwargs)
        )

class PercolatingGraph(Graph):
    @staticmethod
    def from_networkx(nxgraph: nx.classes.graph.Graph, **kwargs) -> "PercolatingGraph":
        return PercolatingGraph(list(nxgraph.nodes), list(nxgraph.edges), **kwargs)

    def random_edge_set(self, p=0.5):
        return [ e for e in self.edges if random() > p ]

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
