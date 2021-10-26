from manim import *
from math import floor
import networkx as nx

# gives the r-ball around vertex v in graph g
# nodes[d] is a list of nodes at distance d from v
# edges[d] is a list of edges at max distance d from v
def ball(g: Graph, v, r):
    nodes = [nx.descendants_at_distance(g._graph, v, d) for d in range(r+1)]
    edges = [[]]

    for d in range(1, r+1):
        forward = [(u,w) for u in nodes[d-1] for w in nodes[d] if (u,w) in g.edges]
        backward = [(u,w) for u in nodes[d] for w in nodes[d-1] if (u,w) in g.edges]
        internal = [(u,w) for u in nodes[d] for w in nodes[d] if (u,w) in g.edges]
        edges.append(forward + backward + internal)

    return nodes, edges


# highlight a subgraph given by a selection of nodes and edges
# nodes[d] should be the dth collection of vertices to highlight
# edges[d] should be the dth collection of edges to highlight
# highlight_color[d] is the color of the dth collection of nodes and edges
class HighlightSubgraph(Animation):
    def __init__(self, g: Graph, nodes, edges, highlight_color=[ORANGE,RED], **kwargs):
        super().__init__(g, **kwargs)
        self.length = max(len(nodes), len(edges))

        self.nodes = nodes + ([[]] * (self.length - len(nodes)))
        self.edges = edges + ([[]] * (self.length - len(nodes)))
        self.highlight_color = highlight_color + ([highlight_color[-1]] * (self.length - len(highlight_color)))

        
    def interpolate_mobject(self, alpha: float) -> None:
        index = floor(alpha * self.length)
        theta = alpha * self.length - index

        if index < self.length:
            for w in self.nodes[index]:
                new_color = interpolate_color(self.mobject.vertices[w].get_color(), self.highlight_color[index], theta)
                self.mobject.vertices[w].set_color(new_color)

            for e in self.edges[index]:
                new_color = interpolate_color(self.mobject.edges[e].get_color(), self.highlight_color[index], theta)
                self.mobject.edges[e].set_color(new_color)

        if index > 0:
            for w in self.nodes[index-1]:
                self.mobject.vertices[w].set_color(self.highlight_color[index-1])
            for e in self.edges[index-1]:
                self.mobject.edges[e].set_color(self.highlight_color[index-1])
