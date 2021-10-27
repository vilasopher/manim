from manim import *
import newballs
import networkx as nx
from random import random

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


# show the canopy tree, rooted at a leaf
# assumes representation by a 3-regular tree ball of depth r
# make sure r >> 0 for this to work
def oldshowcanopy(r):
    spine = [ ('ab'*r)[:r-k] for k in range(r) ]

    positions = { spine[s] : s * RIGHT for s in range(r) }

    layer = spine

    for k in range(r):
        newlayer = []
        init = init + (1 - (1 / 4**k)) * RIGHT + DOWN
        step = (1 / 2**k) * RIGHT

        for j in layer:
            if len(j) < r and len(j) > 0:
                newlayer = newlayer + [ j + x for x in 'abc' if j[-1] != x and j + x not in positions.keys()]

        newpositions = { newlayer[s] : init + s * step for s in range(len(newlayer)) }

        positions.update(newpositions)
        layer = newlayer

    allvertices, _ = rtb_ne(3,r)
    finalpositions = { v : 100 * RIGHT + random() * RIGHT + random() * UP for v in allvertices if v not in positions.keys() }

    positions.update(finalpositions)

    return positions


def showcanopy(r):
    spine = [ ('ab'*r)[:r-k] for k in range(r) ] 
    positions = { spine[s] : 2 * s * RIGHT for s in range(r) }

    layer = []
    for v in spine[1:]:
        layer.append(v + 'c')
        positions[v + 'c'] = positions[v] + DOWN

    for k in range(r):
        newlayer = []

        for v in layer[2**k:]:
            children = [ v + x for x in 'abc' if v[-1] != x ]
            newlayer.extend(children)

            positions[children[0]] = positions[v] + DOWN + (1/3**(k+1)) * LEFT
            positions[children[1]] = positions[v] + DOWN + (1/3**(k+1)) * RIGHT

        layer = newlayer

    allvertices, _ = rtb_ne(3,r)
    finalpositions = { v : 20 * RIGHT + random() * RIGHT + random() * UP for v in allvertices if v not in positions.keys() }

    positions.update(finalpositions)
    return positions


class TreeScene(Scene):
    def construct(self):
        g = regulartreeball(3,4)
        h = regulartreeball(3,6)

        g.change_layout("kamada_kawai", layout_scale=4)
        h.change_layout("kamada_kawai", layout_scale=3)

        nodes, edges = newballs.ball(h, 'ababab', 5)

        flatn = [v for l in nodes for v in l]
        flate = [e for l in edges for e in l]

        compn = [[v for v in h.vertices if v not in flatn]]
        compe = [[e for e in h.edges if e not in flate]]

        self.play(Create(h))
        self.play(newballs.HighlightSubgraph(h, nodes, edges))
        self.play(newballs.HighlightSubgraph(h, compn, compe, highlight_color=[GRAY]))
        self.wait()

        self.play(h.animate.change_layout(showcanopy(6), layout_scale=3))
        self.wait()
