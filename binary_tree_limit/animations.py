from manim import *
import networkx as nx 
import random
import highlight_ball as hb
import solarized as sol
import binary_tree as bt

class BoxScene(Scene):
    def construct(self):
        self.camera.background_color = sol.BASE3

        nxgraph = nx.grid_2d_graph(15,15)

        vconf = { v : {'fill_color' : sol.BASE02} for v in nxgraph.nodes() }
        econf = { e : {'stroke_color' : sol.BASE01} for e in nxgraph.edges() }

        g = Graph.from_networkx(nxgraph, vertex_config=vconf, edge_config=econf)
        g.change_layout('kamada_kawai', layout_scale=3.5)

        self.add(g)

        for _ in range(5):
            v = random.choice(list(g.vertices))
            ballvs, __ = hb.ball(g,v,2)
            vball = [w for ws in ballvs for w in ws]

            if len(list(vball)) < 13:
                self.play(hb.HighlightBall(g,v,2))
            else:
                self.play(hb.HighlightBall(g,v,2,node_highlight_color=sol.BLUE,edge_highlight_color=sol.BLUE))
            self.wait(0.5)

class TreeScene(Scene):
    def construct(self):
        self.camera.background_color = sol.BASE3

        nxgraph = nx.balanced_tree(2,8)
        vconf = {'fill_color' : sol.BASE02}
        econf = {'stroke_color' : sol.BASE01}


        nxgraph = nx.balanced_tree(2,6)
        g = Graph.from_networkx(nxgraph, vertex_config=vconf, edge_config=econf, layout=bt.binary_tree_layout(8))
        self.add(g)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=2)))
        self.wait()
        
        return

        self.play(Create(g))

        for i in range(4):
            depth = i + 1
            nodes, edges = bt.binary_tree_layer(depth)
            self.play(g.animate.add_vertices(*nodes, positions=bt.binary_tree_layout(depth)),
                      g.animate.add_edges(*edges))
            self.wait(0.25)

        self.play(g.animate.change_layout(bt.canopy_tree_layout(5)))
        self.wait()
