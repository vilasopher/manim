from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from more_graphs import PercolatingGraph, HPGraph, HPGrid
from glitch import Glitch, GlitchEdges, GlitchPercolate
from translucent_box import TranslucentBox
from duality import Duality, convert_edge
import random

class GlitchTransition(Scene):
    def construct(self):
        g = Duality((24, 14), 0.3)
        g.primal.highlight #TODO HIGHLIGHT ROOT
        self.play(
            GlitchEdges(g.primal, intensity=0.04),
            GlitchEdges(g.dual, intensity=0.04),
            run_time = 0.5
        )
