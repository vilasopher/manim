from manim import *
from math import log, floor, sqrt

def binary_tree_position(vertex, horizontal_shrink=1/2, vertical_shrink=2.1/3, horizontal_scale=6, vertical_scale=3):
    if vertex == 0:
        return ORIGIN
    else:
        parent = (vertex - 1) // 2
        parent_pos = binary_tree_position(parent, horizontal_shrink, vertical_shrink, horizontal_scale, vertical_scale)

        layer = floor(log(vertex+1,2))
        down_part = vertical_scale * (vertical_shrink ** layer) * DOWN

        if vertex % 2 == 1:
            return parent_pos + down_part + horizontal_scale * (horizontal_shrink ** layer) * LEFT
        else:
            return parent_pos + down_part + horizontal_scale * (horizontal_shrink ** layer) * RIGHT


def binary_tree_layout(depth, shift=2*UP, **kwargs):
    return { v : shift + binary_tree_position(v, **kwargs) for v in range(2 ** (depth+1) - 1) }


def binary_tree_layer(depth):
    nodes = [ v for v in range(2 ** (depth+1) - 1) if v not in range(2 ** depth - 1) ]
    edges = [ ((v - 1) // 2, v) for v in nodes ]
    return nodes, edges


def canopy_tree_position(vertex, depth, horizontal_scale=2, vertical_scale=1, horizontal_shrink=1/2, vertical_shrink=2.1/3):
    if vertex in [ 2 ** i - 1 for i in range(depth+1) ]:
        return log(vertex + 1, 2) * horizontal_scale * LEFT

    if vertex in [ 2 ** i for i in range(1,depth+1) ]:
        return (log(vertex, 2) - 1) * horizontal_scale * LEFT + vertical_scale * DOWN

    parent = (vertex - 1) // 2
    parent_pos = canopy_tree_position(parent, depth, horizontal_scale, vertical_scale, horizontal_shrink, vertical_shrink)

    for i in range(depth):
        if vertex % (2 ** (depth - i)) >= (2 ** (depth - i - 1) - 1) and vertex > (2 ** (depth - i)):
            if vertex % 2 == 1:
                return parent_pos + vertical_scale * (vertical_shrink ** (depth - i)) * DOWN + horizontal_scale * (horizontal_shrink ** (depth - i)) * LEFT
            else:
                return parent_pos + vertical_scale * (vertical_shrink ** (depth - i)) * DOWN + horizontal_scale * (horizontal_shrink ** (depth - i)) * RIGHT


def canopy_tree_layout(depth, height=0, vertical_shift=ORIGIN, horizontal_scale=2, **kwargs):
    shift = vertical_shift + (depth-height) * horizontal_scale * RIGHT
    return { v : shift + canopy_tree_position(v, depth, horizontal_scale, **kwargs) for v in range(2 ** (depth+1) - 1) }



