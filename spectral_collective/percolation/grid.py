from manim import RIGHT, UP, ORIGIN

def grid_nodes_edges(width, height=None):
    if height == None:
        height = width

    nodes = [ (a,b) for a in range(-width,width+1) for b in range(-height,height+1) ]
    edges = [ (v,w) for v in nodes for w in nodes if abs(v[0]-w[0]) + abs(v[1]-w[1]) == 1 ]
    return nodes, edges

def grid_layer_nodes_edges(width, height=None):
    if height == None:
        height = width

    allnodes, alledges = grid_nodes_edges(width, height)
    nodes = [ v for v in allnodes if abs(v[0]) == width or abs(v[1]) == height ]
    edges = [ e for e in alledges if e[0] in nodes or e[1] in nodes ]
    return nodes, edges

def grid_boundary(thickness, width, height=None):
    if height == None:
        height = width

    allnodes, alledges = grid_nodes_edges(width, height)
    nodes = [ v for v in allnodes if abs(v[0]) > (width-thickness) or abs(v[1]) > (height-thickness) ]
    edges = [ e for e in alledges if e[0] in nodes and e[1] in nodes ]
    return nodes, edges

def grid_position(v, scale=0.5):
    return scale * (v[0] * RIGHT + v[1] * UP)

def grid_layout(width, height=None, shift=ORIGIN, **kwargs):
    nodes, _ = grid_nodes_edges(width, height)
    return { v : shift + grid_position(v,**kwargs) for v in nodes }

def dual_nodes_edges(width, height=None):
    if height == None:
        height = width

    nodes = [ (2 * a + 1, 2 * b + 1)
              for a in range(-width-1,width+1)
              for b in range(-height-1,height+1) ]
    edges = [ (v,w) for v in nodes for w in nodes 
              if abs(v[0]-w[0]) + abs(v[1]-w[1]) == 2 ]
    return nodes, edges

def dual_position(v, scale=0.5):
    return scale * 0.5 * (v[0] * RIGHT + v[1] * UP)

def dual_layout(width, height=None, shift=ORIGIN, **kwargs):
    nodes, _ = dual_nodes_edges(width, height)
    return { v : shift + dual_position(v,**kwargs) for v in nodes }
