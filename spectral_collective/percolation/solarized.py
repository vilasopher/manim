from manim import rgb_to_color, config, average_color
from numpy import array

def _r2c(a,b,c):
    return rgb_to_color([a/255, b/255, c/255])

all_colors_rgb = array([
    [0,43,54],
    [7,54,66],
    [88,110,117],
    [101,123,131],
    [131,148,150],
    [147,161,161],
    [238,232,213],
    [253,246,227],
    [181,137,0],
    [203,75,22],
    [220,50,47],
    [211,54,130],
    [108,113,196],
    [38,139,210],
    [42,161,152],
    [133,153,0]
])

background_colors_rgb = array([
    [0,43,54],
    [7,54,66],
    [88,110,117],
    [101,123,131],
    [131,148,150],
    [147,161,161],
    [238,232,213],
    [253,246,227]
])

foreground_colors_rgb = array([
    [181,137,0],
    [203,75,22],
    [220,50,47],
    [211,54,130],
    [108,113,196],
    [38,139,210],
    [42,161,152],
    [133,153,0]
])

BASE03  = _r2c(0,43,54)
BASE02  = _r2c(7,54,66)
BASE01  = _r2c(88,110,117)
BASE00  = _r2c(101,123,131)
BASE0   = _r2c(131,148,150)
BASE1   = _r2c(147,161,161)
BASE2   = _r2c(238,232,213)
BASE3   = _r2c(253,246,227)
YELLOW  = _r2c(181,137,0)
ORANGE  = _r2c(203,75,22)
RED     = _r2c(220,50,47)
MAGENTA = _r2c(211,54,130)
VIOLET  = _r2c(108,113,196)
BLUE    = _r2c(38,139,210)
CYAN    = _r2c(42,161,152)
GREEN   = _r2c(133,153,0)
FOREST_GREEN = _r2c(40, 190, 15)

NODE = BASE02
EDGE = BASE01

LIGHT_NODE = BASE0
LIGHT_EDGE = BASE1

ROOT = RED
HIGHLIGHT_NODE = BASE03
HIGHLIGHT_EDGE = BASE02

UNHIGHLIGHT_NODE = BASE2
UNHIGHLIGHT_EDGE = BASE2

VERTEX_CONFIG = { 'fill_color' : NODE }
EDGE_CONFIG = { 'stroke_color' : EDGE }

DUAL_VERTEX_CONFIG = { 'fill_color' : BLUE }
DUAL_EDGE_CONFIG = { 'stroke_color' : CYAN }

LIGHT_VERTEX_CONFIG = { 'fill_color' : LIGHT_NODE }
LIGHT_EDGE_CONFIG = { 'stroke_color' : LIGHT_EDGE }

VERY_LIGHT_VERTEX_CONFIG = { 'fill_color' : BASE2 }
VERY_LIGHT_EDGE_CONFIG = { 'stroke_color' : BASE2 }

DUAL_LIGHT_VERTEX_CONFIG = { 'fill_color' : average_color(BASE3, BASE3, BASE3, BASE3, BLUE) }
DUAL_LIGHT_EDGE_CONFIG = { 'stroke_color' : average_color(BASE3, BASE3, BASE3, BASE3, CYAN) }

config.background_color = BASE3
