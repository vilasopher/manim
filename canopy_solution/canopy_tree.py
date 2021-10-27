from manim import *
import networkx as nx
from random import random

def tree_ball_nodes_edges(r):
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

def treeball(r):
    nodes, edges = rtb_ne(r)
    nxgraph = nx.Graph()
    nxgraph.add_nodes_from(nodes)
    nxgraph.add_edges_from(edges)
    return Graph.from_networkx(nxgraph)


# gives the positions for vertices in a nice representation of the canopy tree
# centered around a point at height 'height' from a leaf ('height=0' <-> leaf)
# assumes representation by a 3-regular tree ball of depth r
# make sure r >> 0 for this to work
def showcanopy(
        r,
        height=0,
        horizontal_scaling=1,
        vertical_scaling=1,
        spine_scaling=2,
        vertical_offset=0,
        offscreen_distance=20):

    spine = [ ('ab'*r)[:r-k] for k in range(r) ] 
    positions = { spine[s] : horizontal_scaling * spine_scaling * s * RIGHT for s in range(r) }

    layer = []
    for v in spine[1:]:
        layer.append(v + 'c')
        positions[v + 'c'] = positions[v] + vertical_scaling * DOWN

    for k in range(r):
        newlayer = []

        for v in layer[2**k:]:
            children = [ v + x for x in 'abc' if v[-1] != x ]
            newlayer.extend(children)

            positions[children[0]] = positions[v] + vertical_scaling * DOWN + (1/3**(k+1)) * horizontal_scaling * LEFT
            positions[children[1]] = positions[v] + vertical_scaling * DOWN + (1/3**(k+1)) * horizontal_scaling * RIGHT

        layer = newlayer

    allvertices, _ = treeball_nodes_edges
    offscreen_positions = { v : (offscreen_distance + random()) * RIGHT for v in allvertices if v not in positions.keys() }
    positions.update(offscreen_positions)

    return { v : positions[v] + horizontal_scaling * height * LEFT + vertical_offset * UP for v in positions.keys() }
