from manim import *

def grid_nodes_edges(radius):
    nodes = [ (a,b) for a in range(-radius,radius+1) for b in range(-radius,radius+1) ]
    edges = [ (v,w) for v in nodes for w in nodes if abs(v[0]-w[0]) + abs(v[1]-w[1]) == 1 ]
    return nodes, edges

def grid_layer_nodes_edges(radius):
    allnodes, alledges = grid_nodes_edges(radius)
    nodes = [ v for v in allnodes if abs(v[0]) == radius or abs(v[1]) == radius ]
    edges = [ e for e in alledges if e[0] in nodes or e[1] in nodes ]
    return nodes, edges

def grid_boundary(radius, thickness):
    allnodes, alledges = grid_nodes_edges(radius)
    nodes = [ v for v in allnodes if abs(v[0]) > (radius-thickness) or abs(v[1]) > (radius-thickness) ]
    edges = [ e for e in alledges if e[0] in nodes and e[1] in nodes ]
    return nodes, edges

def grid_position(v, scale=0.5):
    return scale * (v[0] * RIGHT + v[1] * UP)

def grid_layout(radius, **kwargs):
    nodes, _ = grid_nodes_edges(radius)
    return { v : grid_position(v,**kwargs) for v in nodes }
