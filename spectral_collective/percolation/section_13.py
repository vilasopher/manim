from manim import *
import random
import grid as gr
import solarized as sol
from glitch import Glitch, RandomizeNumber, GlitchEdges
from more_graphs import HPCCGrid, HPGrid
from value_slider import ValueSlider

class CouplingUnionFindAbstract(Scene):
    def construct_abstract(self, seed, start, end, runtime, glitchin=False):
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

        if glitchin:
            self.play(
                *(
                    Glitch(nums[e])
                    for r, e in coupling
                ),
                GlitchEdges(g, intensity=0.03),
                run_time=0.25
            )


        truestart = start if start < end else end
        trueend = end if start < end else start
        incrementalruntime = (1/60) * runtime / (trueend - truestart)

        prev_r = truestart
        
        random.seed(seed)

        g.set_p(truestart)

        self.wait(incrementalruntime/2)

        for r, e in list(coupling):
            if r >= truestart and r <= trueend:
                self.play(
                    g.animate.set_p(r),
                    run_time = incrementalruntime,
                    rate_func = rate_functions.linear
                )
                prev_r = r

        if prev_r < trueend:
            self.play(
                g.animate.set_p(trueend),
                run_time = incrementalruntime,
                rate_func = rate_functions.linear
            )

        self.wait(incrementalruntime/2)
