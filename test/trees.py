from manim import *
import newballs
import networkx as nx

def rtb_ne(d, r):
    if r == 1:
        nodes = ['', 'a', 'b', 'c']
        edges = [('', 'a'), ('', 'b'), ('', 'c')]
        return nodes, edges
    else:
        nodes, edges = rtb_ne(d,r-1)
        maxlength = max([len(v) for v in nodes])
        outernodes = [v for v in nodes if len(v) == maxlength] 

        newnodes = [v + x for v in outernodes for x in 'abc' if v[-1] != x]
        newedges = [(v, v+x) for v in outernodes for x in 'abc' if v[-1] != x]

        return nodes + newnodes, edges + newedges


def regulartreeball(d, r):
    nodes, edges = rtb_ne(d,r)
    nxgraph = nx.Graph()
    nxgraph.add_nodes_from(nodes)
    nxgraph.add_edges_from(edges)
    return Graph.from_networkx(nxgraph)


class TreeScene(Scene):
    def construct(self):
        g = regulartreeball(3,4)
        h = regulartreeball(3,6)

        g.change_layout("kamada_kawai")
        h.change_layout("kamada_kawai", layout_scale=3)

        nodes, edges = newballs.ball(h, 'abab', 3)

        flatn = [v for l in nodes for v in l]
        flate = [e for l in edges for e in l]

        compn = [[v for v in h.vertices if v not in flatn]]
        compe = [[e for e in h.edges if e not in flate]]

        self.play(Create(h))
        self.play(newballs.HighlightSubgraph(h, nodes, edges))
        self.play(newballs.HighlightSubgraph(h, compn, compe, highlight_color=[BLUE]))
        self.wait()
