from manim import *
import networkx as nx 
import random
import highlight_ball as hb
import solarized as sol

class TestScene(Scene):
    def construct(self):
        self.camera.background_color = sol.BASE3

        nxgraph = nx.balanced_tree(2,5)
        nxgraph = nx.grid_2d_graph(15,15)

        vconf = { v : {'fill_color' : sol.CYAN} for v in nxgraph.nodes() }
        econf = { e : {'stroke_color' : sol.BASE02} for e in nxgraph.edges() }

        g = Graph.from_networkx(nxgraph, vertex_config=vconf, edge_config=econf)
        g.change_layout('kamada_kawai', layout_scale=3.5)

        self.play(Create(g))

        for _ in range(15):
            v = random.choice(list(g.vertices))
            self.play(hb.HighlightBall(g,v,2))
            self.wait(0.5)

