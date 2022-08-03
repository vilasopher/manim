from manim import *
import random
import grid as gr
import solarized as sol
from glitch import Glitch, RandomizeNumber, GlitchEdges
from more_graphs import HPCCGrid, HPGrid
from value_slider import ValueSlider
from duality import Duality, convert_edge
from math import floor

frame = Rectangle(height=8, width=14.2222222222222, color=sol.BASE0, stroke_width=24, z_index=5)

class FrameTest(Scene):
    def construct(self):
        self.add(frame)

class BothGlitchTransition(Scene):
    def construct(self):
        self.add(frame)
        g = Duality()
        self.play(
            GlitchEdges(g.primal, intensity=0.03),
            GlitchEdges(g.dual, intensity=0.03),
            run_time=0.5
        )

class Duality1(Scene):
    def construct(self):
        self.add(frame)
        g = Duality()
        g.percolate()
        self.play(
            GlitchEdges(g.primal, intensity=0.03),
            GlitchEdges(g.dual, intensity=0.03), 
            run_time=0.25
        )
        self.wait(4)
        self.play(
            GlitchEdges(g.primal, intensity=0.03),
            run_time=0.25
        )

class Duality2(Duality1):
    pass

class Duality3(Duality1):
    pass

class Duality4(Duality1):
    pass

class Duality5(Duality1):
    pass

class Duality6(Duality1):
    pass

class CouplingUnionFindAbstract(Scene):
    def construct_abstract(self, seed, start, end, runtime, faded=False, fadeout=False):
        self.add(frame)
        random.seed(seed)

        g = HPCCGrid.from_grid((3,2), 2.5)

        coupling = list(g.coupling)

        coupling = [ ((i+1)/60, c[1]) for i, c in enumerate(coupling) ]

        g.coupling = list(coupling)

        bg = HPGrid.from_grid(
            (5,3),
            2.5,
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.VERY_LIGHT_EDGE_CONFIG
        )

        self.add(bg, g)

        occlusion = Rectangle(
            width=15,
            height=9,
            color=sol.BASE3,
            z_index=3
        ).set_fill(sol.BASE3, opacity=0)
        self.add(occlusion)

        if faded:
            occlusion.set_opacity(0.9)

        nums = {}

        for r, e in coupling:
            nums[e] = DecimalNumber(
                    r,
                    font_size=40,
                    z_index=1
                )
            nums[e].color = sol.BASE03
            nums[e].next_to(bg.edges[e], ORIGIN)
            self.add(nums[e])

        truestart = start if start < end else end
        trueend = end if start < end else start
        epsilon = 1/480
        incrementalruntime = (1/60) * floor(runtime / (trueend - truestart) + epsilon)

        prev_r = truestart
        
        random.seed(seed)

        g.set_p(truestart)

        if fadeout and not truestart == start:
            occlusion.set_opacity(0.9)

        self.wait(incrementalruntime/2)

        for r, e in list(coupling):
            if r >= truestart and r <= trueend:
                if fadeout:
                    self.play(
                        g.animate.set_p(r),
                        occlusion.animate.set_opacity(0.9 * (r - start)/(end - start)),
                        run_time = incrementalruntime,
                        rate_func = rate_functions.linear
                    )
                else:
                    self.play(
                        g.animate.set_p(r),
                        run_time = incrementalruntime,
                        rate_func = rate_functions.linear
                    )
                prev_r = r

        if prev_r < trueend:
            if fadeout and truestart == start:
                self.play(
                    g.animate.set_p(trueend),
                    occlusion.animate.set_opacity(0.9),
                    run_time = incrementalruntime,
                    rate_func = rate_functions.linear
                )
            else:
                self.play(
                    g.animate.set_p(trueend),
                    run_time = incrementalruntime,
                    rate_func = rate_functions.linear
                )

        self.wait(incrementalruntime/2)

class REVERSEDCouplingUnionFind_OneToZero(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(15, 1, 0, 12)

class CouplingUnionFind_ZeroToOne(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(15, 0, 1, 12)
