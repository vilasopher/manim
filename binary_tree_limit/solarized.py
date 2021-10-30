from manim import rgb_to_color, config

def _r2c(a,b,c):
    return rgb_to_color([a/255, b/255, c/255])

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

NODE = BASE02
EDGE = BASE01

ROOT = RED
HIGHLIGHT_NODE = BLUE
HIGHLIGHT_EDGE = BLUE

VERTEX_CONFIG = { 'fill_color' : NODE }
EDGE_CONFIG = { 'stroke_color' : EDGE }

config.background_color = BASE3
