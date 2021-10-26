from manim import *
from math import floor
import networkx as nx

def adjacent(g: Graph, v, w):
    if v not in g.vertices or w not in g.vertices:
        raise Exception("adjacent: vertex does not exist in graph")

    return (v,w) in g.edges or (w,v) in g.edges


# counts distance between two vertices of a graph
# returns -1 if the two vertices are in different connected components
def vertex_distance(g: Graph, v, w, recursion_depth=0):
    if v not in g.vertices or w not in g.vertices:
        raise Exception("vertex_distance: vertex does not exist in graph")

    if recursion_depth > len(g.vertices):
        return -1

    if v == w:
        return 0
    elif adjacent(g,v,w):
        return 1
    else:
        neighbor_distances = [vertex_distance(g, x, w, recursion_depth + 1) for x in g.vertices if adjacent(g,v,x)]

        finite_neighbor_distances = [d for d in neighbor_distances if d > -1]

        if len(finite_neighbor_distances) == 0:
            return -1
        else:
            return min(finite_neighbor_distances) + 1


# distance between a vertex and an edge
# this is 1 if e contains v
# returns -1 if v and e are in different connected components
def edge_distance(g: Graph, v, e):
    if not adjacent(g, *e):
        raise Exception("edge_distance: edge does not exist in graph")

    return max(vertex_distance(g,v,e[0]), vertex_distance(g,v,e[1]))


# highlight the ball of radius r around v in g
class HighlightBall(Animation):
    def __init__(self, g: Graph, v, r, root_color=ORANGE, highlight_color=RED, **kwargs):
        super().__init__(g, **kwargs)
        self.v = v
        self.r = r+1
        self.root_color = root_color
        self.highlight_color = highlight_color

        # confusing: maybe there is a better way to do this
        # the list in position d should hold all vertices at distance d from v
        self.vertices_at_distance = [[] for d in range(len(g.vertices)+1)]
        self.edges_at_distance = [[] for d in range(len(g.vertices)+1)]

        for w in g.vertices:
            d = vertex_distance(g,v,w)
            self.vertices_at_distance[d].append(w)

        for e in g.edges:
            d = edge_distance(g,v,e)
            self.edges_at_distance[d].append(e)

        self.original_vertex_colors = {w : g[w].get_color() for w in g.vertices}
        self.original_edge_colors = {e : g.edges[e].get_color() for e in g.edges}
            
    def interpolate_mobject(self, alpha: float) -> None:
        if floor(alpha * self.r) == 0:
            self.mobject[self.v].set_color(interpolate_color(self.original_vertex_colors[self.v], self.root_color, alpha * self.r))
        else:
            for w in self.vertices_at_distance[floor(alpha * self.r)]:
                self.mobject[w].set_color(interpolate_color(self.original_vertex_colors[w], self.highlight_color, alpha * self.r - floor(alpha * self.r)))

        for e in self.edges_at_distance[floor(alpha * self.r)]:
            self.mobject.edges[e].set_color(interpolate_color(self.original_edge_colors[e], self.highlight_color, alpha * self.r - floor(alpha * self.r)))

###############################################################################

nxgraph = nx.erdos_renyi_graph(14,0.5)

class balltest(Scene):
    def construct(self):
        g = Graph.from_networkx(nxgraph, layout="spring", layout_scale=3.5)
        self.play(Create(g))
        self.play(HighlightBall(g,1,3))
        self.wait()
