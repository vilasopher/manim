from manim import *
import networkx as nx
from random import random
from math import sqrt

def treeball_nodes_edges(r):
    if r == 1:
        nodes = ['', 'a', 'b', 'c']
        edges = [('', 'a'), ('', 'b'), ('', 'c')]
        return nodes, edges
    else:
        nodes, edges = treeball_nodes_edges(r-1)
        maxlength = max([len(v) for v in nodes])
        outernodes = [v for v in nodes if len(v) == maxlength] 

        newnodes = [v + x for v in outernodes for x in 'abc' if v[-1] != x]
        newedges = [(v, v+x) for v in outernodes for x in 'abc' if v[-1] != x]

        return nodes + newnodes, edges + newedges

def treeball_nodes_edges_next_layer(previous_layer):
    newnodes = [v + x for v in previous_layer for x in 'abc' if v[-1] != x]
    newedges = [(v, v+x) for v in previous_layer for x in 'abc' if v[-1] != x]
    return newnodes, newedges

def treeball(r):
    nodes, edges = treeball_nodes_edges(r)
    nxgraph = nx.Graph()
    nxgraph.add_nodes_from(nodes)
    nxgraph.add_edges_from(edges)
    return Graph.from_networkx(nxgraph)


BRANCHING_DIRECTION = {
        'a' : LEFT,
        'b' : (1/2) * RIGHT + (sqrt(3)/2) * UP,
        'c' : (1/2) * RIGHT + (sqrt(3)/2) * DOWN
        }

def treeball_vertex_position(v, scaling=1, shrink_parameter=2/3, shrink_function=None):
    if shrink_function == None:
        shrink_function = lambda i : shrink_parameter ** i 

    pos = ORIGIN
    
    for i in range(len(v)):
        pos = pos + (-1)**i * shrink_function(i) * BRANCHING_DIRECTION[v[i]]

    return pos * scaling

# nice embedding of a treeball
def show_treeball(r, scaling=1, shrink_parameter=2/3, shrink_function=None):
    allvertices, _ = treeball_nodes_edges(r)

    return { v : treeball_vertex_position(v, scaling=scaling, shrink_parameter=shrink_parameter, shrink_function=shrink_function) for v in allvertices }

# gives the positions for vertices in a nice picture of the canopy tree
# centered around a point at height 'height' from a leaf ('height=0' <-> leaf)
# assumes representation by a 3-regular tree ball of depth r
# make sure r >> 0 for this to work
def show_canopy(
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

    allvertices, _ = treeball_nodes_edges(r)
    offscreen_positions = { v : (offscreen_distance + random()) * RIGHT for v in allvertices if v not in positions.keys() }
    positions.update(offscreen_positions)

    return { v : positions[v] + horizontal_scaling * height * LEFT + vertical_offset * UP for v in positions.keys() }
