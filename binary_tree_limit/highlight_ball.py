from manim import *
from math import floor
import networkx as nx
import solarized as sol

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
    def __init__(self,
            g: Graph,
            nodes, # list of lists of nodes, in order of highlighting
            edges, # list of lists of edges, in order of highlighting
            node_highlight_color=[sol.YELLOW],
            edge_highlight_color=[sol.YELLOW],
            slow=False,
            **kwargs):

        super().__init__(g, **kwargs)

        self.length = max(len(nodes), len(edges))
        self.slow = slow

        self.nodes = nodes + ([[]] * (self.length - len(nodes)))
        self.edges = edges + ([[]] * (self.length - len(edges)))
        self.node_highlight_color = node_highlight_color + ([node_highlight_color[-1]] * (self.length - len(node_highlight_color)))
        self.edge_highlight_color = edge_highlight_color + ([edge_highlight_color[-1]] * (self.length - len(edge_highlight_color)))

    def interpolate_mobject_fast(self, alpha: float) -> None:
        for index in range(self.length):
            for w in self.nodes[index]:
                new_color = interpolate_color(self.mobject.vertices[w].get_color(), self.node_highlight_color[index], alpha)
                self.mobject.vertices[w].set_color(new_color)

            for e in self.edges[index]:
                new_color = interpolate_color(self.mobject.edges[e].get_color(), self.edge_highlight_color[index], alpha)
                self.mobject.edges[e].set_color(new_color)
        
    def interpolate_mobject_slow(self, alpha: float) -> None:
        index = floor(alpha * self.length)
        theta = alpha * self.length - index

        if index < self.length:
            for w in self.nodes[index]:
                new_color = interpolate_color(self.mobject.vertices[w].get_color(), self.node_highlight_color[index], theta)
                self.mobject.vertices[w].set_color(new_color)

                # TODO: figure out this bug with the labels
                if w in self.mobject._labels.keys():
                    self.mobject._labels[w].set_color(WHITE)
                    say(bad)

            for e in self.edges[index]:
                new_color = interpolate_color(self.mobject.edges[e].get_color(), self.edge_highlight_color[index], theta)
                self.mobject.edges[e].set_color(new_color)

        for prev in range(index):
            for w in self.nodes[prev]:
                self.mobject.vertices[w].set_color(self.node_highlight_color[prev])

                if w in self.mobject._labels.keys():
                    self.mobject._labels[w].set_color(WHITE)
                    say(bad)

            for e in self.edges[prev]:
                self.mobject.edges[e].set_color(self.edge_highlight_color[prev])

    def interpolate_mobject(self, alpha: float) -> None:
        if self.slow:
            self.interpolate_mobject_slow(alpha)
        else:
            self.interpolate_mobject_fast(alpha)


# highlights a ball around a vertex, and un-highlights everything else
def HighlightBall(
        g: Graph,
        v, # the vertex to serve as the root
        r, # the radius of the ball to highlight
        root_highlight_color=sol.ROOT,
        node_highlight_color=sol.HIGHLIGHT_NODE,
        edge_highlight_color=sol.HIGHLIGHT_EDGE,
        run_time=0.99,
        fade_run_time=0.01,
        slow=False,
        fadeout=True,
        **kwargs):

    if fadeout == False:
        run_time = 1

    ballnodes, balledges = ball(g,v,r)

    ball_anim = HighlightSubgraph(g,
                                  ballnodes,
                                  balledges,
                                  node_highlight_color=[root_highlight_color, node_highlight_color],
                                  edge_highlight_color=[edge_highlight_color],
                                  run_time = run_time,
                                  slow=slow,
                                  **kwargs)

    if fadeout:
        flatnodes = [ w for ws in ballnodes for w in ws ]
        flatedges = [ e for es in balledges for e in es ] 

        fadenodes = [[w] for w in flatnodes ]
        fadeedges = [[e] for e in flatedges ]

        fadenodecolors = [ g[w].get_color() for w in flatnodes ]
        fadeedgecolors = [ g.edges[e].get_color() for e in flatedges ] + [ sol.EDGE ]

        fade_anim = HighlightSubgraph(g,
                                       fadenodes,
                                       fadeedges,
                                       node_highlight_color=fadenodecolors,
                                       edge_highlight_color=fadeedgecolors,
                                       run_time = fade_run_time,
                                       slow=False,
                                       **kwargs)

        return Succession(ball_anim, fade_anim)
    else:
        return ball_anim


# unhighlight everything
def UnHighlight(
        g: Graph,
        node_base_color=sol.NODE,
        edge_base_color=sol.EDGE,
        **kwargs):

    return HighlightSubgraph(g,
                             [g.vertices],
                             [g.edges],
                             node_highlight_color=[node_base_color],
                             edge_highlight_color=[edge_base_color],
                             **kwargs)
