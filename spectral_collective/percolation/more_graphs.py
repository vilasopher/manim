from manim import *
#Graph, Create, override_animate, FadeIn, FadeOut, AnimationGroup, rgb_to_color
from random import random, randint
import networkx as nx
import solarized as sol
from union_find import UnionFind

class HighlightableGraph(Graph):
    @classmethod
    def from_networkx(cls, nxgraph: nx.classes.graph.Graph, **kwargs):
        return cls(list(nxgraph.nodes), list(nxgraph.edges), **kwargs)

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
    @classmethod
    def from_networkx(cls, nxgraph: nx.classes.graph.Graph, **kwargs):
        return cls(list(nxgraph.nodes), list(nxgraph.edges), **kwargs)

    def random_edge_set(self, p=0.5):
        return [ e for e in self.edges if random() > p ]

    def percolate(self, p=0.5):
        return self.remove_edges(*self.random_edge_set(p))

    @override_animate(percolate)
    def _percolate_animation(self, p=0.5, animation=FadeOut, **kwargs):
        mobjects = self.percolate(p)
        return AnimationGroup(*(animation(mobj, **kwargs) for mobj in mobjects))

    def generate_coupling(self):
        return { e : random() for e in self.edges }

    def coupled_percolate(self, coupling, p=0.5):
        return self.remove_edges(*(e for e in self.edges if coupling[e] > p))

    @override_animate(coupled_percolate)
    def _coupled_percolate_animation(self, coupling, p=0.5, animation=FadeOut, **kwargs):
        mobjects = self.coupled_percolate(coupling, p)
        return AnimationGroup(*(animation(mobj, **kwargs) for mobj in mobjects))

def completely_random(*args):
    return [randint(0,255)/255 for _ in range(3)]

class ClusterGraph(Graph):
    @classmethod
    def from_networkx(cls, nxgraph: nx.classes.graph.Graph, **kwargs):
        return cls(list(nxgraph.nodes), list(nxgraph.edges), **kwargs)

    def __init__(self, *args, color_picker=completely_random, **kwargs):
        super().__init__(*args, **kwargs)

        self.clusters = UnionFind(self.vertices)
        self.vertex_colors = { v : rgb_to_color(color_picker()) for v in self.vertices }
        self.edge_colors = None

    def initialize_color_dicts(self):
        for e in self.edges:
            self.clusters.union(e[0], e[1])

        self._update_color_dicts()

    def update_colors(self):
        for v in self.vertices:
            self.vertices[v].set_color(self.vertex_colors[v])

        for e in self.edges:
            self.edges[e].set_color(self.edge_colors[e])

    def _update_color_dicts(self):
        for v in self.vertices:
            w = self.clusters.find(v)
            self.vertex_colors[v] = self.vertex_colors[w]

        self.edge_colors = { e : self.vertex_colors[e[0]] for e in self.edges }

    def add_edges(self, *edges):
        super().add_edges(*edges)

        for e in edges:
            self.clusters.union(e[0], e[1])

        self._update_color_dicts()
        self.update_colors()

    @override_animate(add_edges)
    def _add_edges_animation(self, *edges, animation=Create, **kwargs):
        for e in edges:
            self.clusters.union(e[0], e[1])

        mobjects = super().add_edges(*edges)

        self._update_color_dicts()

        return AnimationGroup(
                AnimationGroup(
                    *(animation(mobj, **kwargs) for mobj in mobjects)
                ),
                self.animate.update_colors().build()
            )

class HPGraph(HighlightableGraph, PercolatingGraph):
    pass

class HPCGraph(HPGraph, ClusterGraph):
    pass
