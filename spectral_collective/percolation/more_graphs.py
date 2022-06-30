from manim import *
#Graph, Create, override_animate, FadeIn, FadeOut, AnimationGroup, rgb_to_color
from random import random, randint, shuffle
import networkx as nx
import solarized as sol
from union_find import UnionFind
import grid as gr

class HighlightableGraph(Graph):
    @classmethod
    def from_networkx(cls, nxgraph: nx.classes.graph.Graph, **kwargs):
        return cls(list(nxgraph.nodes), list(nxgraph.edges), **kwargs)

    def edges_spanned_by(self, nodes):
        return [e for e in self.edges if e[0] in nodes and e[1] in nodes ]

    def safe_edge(self, e):
        if e in self.edges:
            return e
        elif (e[1], e[0]) in self.edges:
            return (e[1], e[0])
        else:
            raise Exception('no such edge')

    def path_edges(self, p):
        return [self.safe_edge((p[i],p[i+1])) for i in range(len(p)-1)]

    def highlight_subgraph(
        self,
        nodes,
        edges = None,
        node_colors = {},
        node_default_color = sol.HIGHLIGHT_NODE,
        edge_colors = {},
        edge_default_color = sol.HIGHLIGHT_EDGE,
        nodes_to_scale = [],
        scale_factor = 2,
        **kwargs
    ):
        if edges == None:
            edges = self.edges_spanned_by(nodes)

        for n in nodes:
            self[n].set_color(node_colors.get(n, node_default_color))

        for n in nodes_to_scale:
            self[n].scale(scale_factor)

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
        nodes_to_scale = [],
        scale_factor = 2,
        **kwargs
    ):
        if edges == None:
            edges = self.edges_spanned_by(nodes)

        nodegroup = AnimationGroup(
            *(self[n].animate.set_color(node_colors.get(n, node_default_color))
                for n in nodes if n not in nodes_to_scale)
        )

        scalegroup = AnimationGroup(*(
            self[n].animate.set_color(
                node_colors.get(n, node_default_color)
            ).scale(scale_factor)
            for n in nodes_to_scale
        ))

        edgegroup = AnimationGroup(
            *(self.edges[e].animate.set_color(edge_colors.get(e, edge_default_color))
                for e in edges)
        )

        return AnimationGroup(nodegroup, scalegroup, edgegroup)

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

    def highlight_ball(self, root, radius=None, root_scale_factor=2):
        self.highlight_subgraph(self.ball(root, radius), node_colors = { root : sol.ROOT })
        self[root].scale(root_scale_factor)

    @override_animate(highlight_ball)
    def _highlight_ball_animation(self, root, radius=None, root_scale_factor=2, **kwargs):
        return AnimationGroup(
            self._highlight_subgraph_animation(
                self.ball(root, radius),
                node_colors = { root : sol.ROOT },
                nodes_to_scale = [root],
                scale_factor = root_scale_factor,
                **kwargs
            )
        )

    def unhighlight_complement_ball(self, root, radius=None, **kwargs):
        self.unhighlight_complement(self.ball(root, radius), **kwargs)

    @override_animate(unhighlight_complement_ball)
    def _unhighlight_complement_ball_animation(self, root, radius=None, **kwargs):
        return self._unhighlight_complement_animation(self.ball(root, radius), **kwargs)

    def dramatically_highlight_ball(self, root, radius=None, **kwargs):
        self.highlight_ball(root, radius, **kwargs)
        self.unhighlight_complement_ball(root, radius, **kwargs)

    @override_animate(dramatically_highlight_ball)
    def _dramatically_highlight_ball_animation(self, root, radius=None, **kwargs):
        return AnimationGroup(
            self._highlight_ball_animation(root, radius, **kwargs),
            self._unhighlight_complement_ball_animation(root, radius, **kwargs)
        )

    def longest_path_from(self, root):
        bfs = nx.bfs_tree(self._graph, source=root)
        return nx.dag_longest_path(bfs)

    def highlight_path(self, path, color=sol.ORANGE, **kwargs):
        self.highlight_subgraph(
            path,
            edges = self.path_edges(path),
            node_default_color = color,
            edge_default_color = color,
            **kwargs
        )

    @override_animate(highlight_path)
    def _highlight_path_animation(self, path, color=sol.ORANGE, **kwargs):
        return LaggedStart(*(
            self._highlight_subgraph_animation(
                path[i:i+2],
                node_default_color=color,
                edge_default_color=color,
                **kwargs
            ) for i in range(len(path) - 2)), **kwargs
        )

    def highlight_longest_path_from(self, root, color=sol.ORANGE, length=None):
        path = self.longest_path_from(root)
        if length != None:
            path = path[0:length+2]
        self.highlight_path(path, color=color, node_colors={ root : sol.ROOT })

    @override_animate(highlight_longest_path_from)
    def _highlight_longest_path_from_animation(
        self,
        root,
        color=sol.ORANGE,
        length=None,
        **kwargs
    ):

        path = self.longest_path_from(root)
        if length != None:
            path = path[0:length+2]

        return self._highlight_path_animation(
            path,
            color=color, 
            node_colors={ root : sol.ROOT },
            **kwargs
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

        self.clusters = UnionFind(list(self.vertices))
        self.vertex_colors = { v : rgb_to_color(color_picker()) for v in self.vertices }
        self.edge_colors = None

    def initialize_color_dicts(self):
        for e in self.edges:
            self.clusters.union(*e)

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
            self.clusters.union(*e)

        self._update_color_dicts()
        self.update_colors()

    @override_animate(add_edges)
    def _add_edges_animation(self, *edges, animation=Create, **kwargs):
        for e in edges:
            self.clusters.union(*e)

        mobjects = super().add_edges(*edges)

        self._update_color_dicts()

        return AnimationGroup(
                AnimationGroup(
                    *(animation(mobj, **kwargs) for mobj in mobjects)
                ),
                self.animate.update_colors().build()
            )

class CoupledClusterGraph(ClusterGraph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.coupling = sorted([ (random(), e) for e in self.edges ])
        self.remove_edges(*self.edges)
        self.initialize_color_dicts()
        self.update_colors()

    def set_p(self, p):
        edges_to_add = []

        while len(self.coupling) > 0 and self.coupling[0][0] < p:
            r, e = self.coupling.pop(0)
            edges_to_add.append(e)

        self.add_edges(*edges_to_add)

    @override_animate(set_p)
    def _set_p_animation(self, p, *edges, animation=Create, **kwargs):
        edges_to_add = []

        while len(self.coupling) > 0 and self.coupling[0][0] < p:
            r, e = self.coupling.pop(0)

            s0 = self.clusters.size(e[0])
            s1 = self.clusters.size(e[1])

            if s0 < s1 or (s0 == s1 and random() < 0.5):
                edges_to_add.append((e[1], e[0]))
            else:
                edges_to_add.append(e)

        return self._add_edges_animation(*edges_to_add, animation=animation, **kwargs)

# good shape/scale combinations:
# (24,14) 0.3
# (8,5)   0.95
# (3,2)   2.5
class GridableGraph(HighlightableGraph):
    @classmethod
    def from_grid(cls, shape, scale, **kwargs):
        nodes, edges = gr.grid_nodes_edges(*shape)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        if 'vertex_config' not in kwargs:
            kwargs['vertex_config'] = sol.VERTEX_CONFIG

        if 'edge_config' not in kwargs:
            kwargs['edge_config'] = sol.EDGE_CONFIG

        return cls.from_networkx(
            nxgraph,
            layout=gr.grid_layout(*shape, scale=scale),
            **kwargs
        ).set(gridshape=shape, gridscale=scale)

    def path_to_boundary_from(self, root):
        if not (hasattr(self, 'gridshape') and hasattr(self, 'gridscale')):
            raise Exception("trying to get path offscreen in a non-grid graph")

        paths = nx.shortest_path(self._graph, source=root)

        boundary_nodes = [
            (a,b) for (a,b) in self.vertices
            if abs(a) == self.gridshape[0] or abs(b) == self.gridshape[1]
        ]

        shuffle(boundary_nodes)

        for b in boundary_nodes:
            if b in paths:
                return paths[b]

        return []

    def highlight_path_to_boundary_from(self, root, **kwargs):
        p = self.path_to_boundary_from(root)
        self.highlight_path(p, node_colors = { root : sol.ROOT }, **kwargs)

    @override_animate(highlight_path_to_boundary_from)
    def _highlight_path_to_boundary_from_animation(self, root, **kwargs):
        p = self.path_to_boundary_from(root)
        return self._highlight_path_animation(
            p,
            node_colors = { root : sol.ROOT },
            **kwargs
        )

    def path_of_length_from(self, root, length):
        p = self.path_to_boundary_from(root)

        if len(p) < length+2:
            return p
        
        if len(p) > 0:
            return p[0:length+2]

        p = self.longest_path_from(root)

        if len(p) >= length+2:
            return p[0:length+2]

        return []

    def highlight_path_of_length_from(self, root, length, **kwargs):
        p = self.path_of_length_from(root, length)
        self.highlight_path(p, node_colors = { root : sol.ROOT }, **kwargs)

    @override_animate(highlight_path_of_length_from)
    def _highlight_path_of_length_from_animation(self, root, length, **kwargs):
        p = self.path_of_length_from(root, length)
        return self._highlight_path_animation(
            p,
            node_colors = { root : sol.ROOT },
            **kwargs
        )

class HPGraph(GridableGraph, PercolatingGraph):
    def correct_orientation(self, edge):
        if edge in self.edges:
            return edge
        else:
            return (edge[1], edge[0])

    def percolation_flow_animation(self, source, color, **kwargs):
        bfs = nx.edge_bfs(self._graph, source)

        return LaggedStart(
            self._highlight_subgraph_animation(
                [source],
                node_default_color = color,
                **kwargs
            ),
            *(
                self._highlight_subgraph_animation(
                    e, 
                    [self.correct_orientation(e)],
                    node_default_color = color,
                    edge_default_color = color,
                    **kwargs
                )
                for e in bfs
            )
        )

class HPCGraph(HPGraph, ClusterGraph):
    pass

class HPCCGraph(HPGraph, CoupledClusterGraph):
    pass
