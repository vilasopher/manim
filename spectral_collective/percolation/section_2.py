from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from more_graphs import PercolatingGraph
from glitch import Glitch, GlitchEdges, GlitchPercolate
import random

class PipeSystemAbstract(Scene):
    def pipe_system(self, width, height, scale):
        nodes, edges = gr.grid_nodes_edges(width, height)
        nxgraph = nx.Graph()
        nxgraph.add_nodes_from(nodes)
        nxgraph.add_edges_from(edges)

        return PercolatingGraph.from_networkx(
            nxgraph,
            layout=gr.grid_layout(width, height, scale=scale),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )

class PipeSystem0(PipeSystemAbstract):
    def construct(self):
        pass

class PipeSystemFadeIn(PipeSystemAbstract):
    def construct(self):
         g = self.pipe_system(8,5,0.95)
         self.play(FadeIn(g))

class PipeSystemStatic(PipeSystemAbstract):
    def construct(self):
        g = self.pipe_system(8,5,0.95)
        self.add(g)

class GlitchingPipeSystem(PipeSystemAbstract):
    def construct(self):
        g = self.pipe_system(8,5,0.95)
        self.play(GlitchEdges(g, intensity=0.04), run_time=0.5)

class GlitchInPipeSystem1(PipeSystemAbstract):
    def construct(self):
        g = self.pipe_system(8,5,0.95)
        g.percolate()
        self.play(GlitchEdges(g, intensity=0.04), run_time=0.25)
        self.wait(2.5)
        self.play(GlitchEdges(g, intensity=0.04), run_time=0.25)

class GlitchInPipeSystem2(GlitchInPipeSystem1):
    pass

class GlitchInPipeSystem3(GlitchInPipeSystem1):
    pass

class GlitchInPipeSystem4(GlitchInPipeSystem1):
    pass

class GlitchZoomOutA(PipeSystemAbstract, MovingCameraScene):
    def construct(self):
        g = self.pipe_system(24, 14, 0.95)

        self.play(
            self.camera.frame.animate.scale(0.95/0.3),
            GlitchEdges(g, intensity=0.04),
            run_time = 0.5
        )


class GlitchZoomOutB(PipeSystemAbstract, MovingCameraScene):
    def construct(self):
        g = self.pipe_system(24, 14, 0.3)

        self.camera.frame.save_state()
        self.camera.frame.scale(0.3/0.95)

        self.play(
            self.camera.frame.animate.restore(),
            GlitchEdges(g, intensity=0.04),
            run_time = 0.5
        )

class DeletingEdges(PipeSystemAbstract, MovingCameraScene):
    def construct(self):
        random.seed(0)

        g = self.pipe_system(8,5,0.95)
        self.play(FadeIn(g), run_time=2)

        for v in g.vertices:
            g[v].set(z_index = 2)

        self.camera.frame.save_state()
        self.wait(3)

        e = g.edges[((-2,-3),(-2,-2))]
        self.play(self.camera.frame.animate.scale(0.15).move_to(e)) # 5
        self.wait(0.5) # 6

        self.play(Glitch(e, intensity=0.02, out=True), run_time = 1.5) # 6.5
        g.remove_edges(((-3,-2), (-2,-2)))
        self.wait() # 8

        e = g.edges[((-2,-2),(-1,-2))]
        self.play(self.camera.frame.animate.move_to(e)) # 9
 
        opentext = Tex(r'open', color=sol.BASE03, font_size=15)
        opentext.next_to(e, DOWN, buff=0.1)

        self.play(Glitch(e, intensity=0.02, out=False)) # 10
        #g.remove_edges(((-2,-2), (-1,-2)))
        self.wait(2) # 11

        self.play(FadeIn(opentext)) # 13
        self.wait(0.5) # 14

        e = g.edges[((-1,-2),(0,-2))]
        self.play(self.camera.frame.animate.move_to(e)) # 14.5

        closedtext = Tex(r'closed', color=sol.BASE03, font_size=15)
        closedtext.next_to(e, DOWN, buff=0.06)

        self.play(Glitch(e, intensity=0.02, out=True), run_time = 0.5) # 15.5
        g.remove_edges(((-1,-2), (-1,-1)))
        self.wait(0.5) # 16

        self.play(FadeIn(closedtext)) # 16.5
        self.wait(1)

        elist = [ ((u,v), (u+du,v+dv))
                    for u in range(7) for v in range(-2,2)
                    for du, dv in [(0,1),(1,0)] ]
        emobs = [ g.edges[e] for e in elist ]

        self.play(self.camera.frame.animate.scale(2.5).move_to(Group(*emobs)))
        self.wait()

        self.remove(opentext, closedtext)

        random.shuffle(elist)
        edict = { e : True if random.random() < 1/2 else False for e in elist }

        self.play(
            LaggedStart(
                *(
                    Glitch(
                        g.edges[e], 
                        intensity=0.03,
                        out = edict[e],
                        run_time = 0.75
                    ) for e in elist
                ),
                lag_ratio = 0.25
            )
        )
        g.remove_edges(*[ e for e in elist if edict[e] ])
        self.wait(1 + 26/60)

        elist = [ ((u,v), (u+du,v+dv))
                    for u in range(-7,0) for v in range(0,4)
                    for du, dv in [(0,1),(1,0)] ]
        emobs = [ g.edges[e] for e in elist ]
        self.play(self.camera.frame.animate.move_to(Group(*emobs)))

        random.shuffle(elist)
        edict = { e : True if random.random() < 1/2 else False for e in elist }

        self.play(
            LaggedStart(
                *(
                    Glitch(
                        g.edges[e], 
                        intensity=0.03,
                        out = edict[e],
                        run_time = 0.5
                    ) for e in elist
                ),
                lag_ratio = 0.25
            )
        )
        g.remove_edges(*[ e for e in elist if edict[e] ])
        self.wait(37/60)

        self.play(self.camera.frame.animate.restore())

        elist = list(g.edges)
        random.shuffle(elist)
        edict = { e : True if random.random() < 1/2 else False for e in elist }

        self.play(
            LaggedStart(
                *(
                    Glitch(
                        g.edges[e],
                        intensity=0.04,
                        out = edict[e],
                        run_time = 0.75
                    ) for e in elist
                ),
                lag_ratio = 0.015
            )
        )
        g.remove_edges(*[ e for e in elist if edict[e] ])
        self.wait(26.5 + 58/60)

        self.play(GlitchEdges(g, intensity = 0.04), run_time = 0.25)
