from manim import *
import random
import grid as gr
import solarized as sol
from glitch import Glitch, RandomizeNumber, GlitchEdges
from more_graphs import HPCCGrid, HPGrid
from value_slider import ValueSlider
from math import floor

class CouplingUnionFindAbstract(Scene):
    def construct_abstract(self, seed, start, end, runtime, faded=False, fadeout=False):
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

class NumberRandomizationTransition(Scene):
    def construct(self):
        g = HPCCGrid.from_grid((3,2), 2.5)
        bg = HPGrid.from_grid((5,3), 2.5)
        self.add(bg)

        coupling = list(g.coupling)

        nums = {}

        for r, e in coupling:
            nums[e] = DecimalNumber(
                    r,
                    font_size=40,
                    z_index=1
                )
            nums[e].color = sol.BASE03
            nums[e].next_to(bg.edges[e], ORIGIN)

        self.play(
            *(
                RandomizeNumber(nums[e])
                for r, e in coupling
            ),
            GlitchEdges(bg, intensity=0.03),
            run_time=0.5
        )

class NumberResamplesAbstract(Scene):
    def construct_abstract(self, seed, glitchin=True, glitchout=True, standardized=False):
        random.seed(seed)
        g = HPCCGrid.from_grid((3,2), 2.5)

        coupling = list(g.coupling)

        if standardized:
            coupling = [ ((i+1)/60, c[1]) for i, c in enumerate(coupling) ]
            g.coupling = list(coupling)

        bg = HPGrid.from_grid(
            (5,3),
            2.5,
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.VERY_LIGHT_EDGE_CONFIG
        )

        self.add(bg, g)

        random.seed(seed)
        g.set_p(0.5)

        nums = {}

        for r, e in coupling:
            nums[e] = DecimalNumber(
                    r,
                    font_size=40,
                    z_index=1
                )
            nums[e].color = sol.BASE03
            nums[e].next_to(bg.edges[e], ORIGIN)

        if glitchin:
            self.play(
                *(
                    Glitch(nums[e])
                    for r, e in coupling
                ),
                GlitchEdges(g, intensity=0.03),
                run_time=0.25
            )
        else:
            self.add(*(nums[e] for r, e in coupling))

        self.wait(2 + 2/3)

        if glitchout:
            self.play(
                *(
                    Glitch(nums[e])
                    for r, e in coupling
                ),
                GlitchEdges(g, intensity=0.03),
                run_time=0.25
            )

class NumberResamplesFinal(NumberResamplesAbstract):
    def construct(self):
        self.construct_abstract(13, glitchout=False, standardized=True)

class NumberResamplesInitial(NumberResamplesAbstract):
    def construct(self):
        self.construct_abstract(12, glitchin=False, standardized=True)

class NumberResamples1(NumberResamplesAbstract):
    def construct(self):
        self.construct_abstract(random.random())

class NumberResamples2(NumberResamples1):
    pass

class NumberResamples3(NumberResamples1):
    pass

########################################################

class CouplingUnionFind_HalfToOne(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(12, 1/2, 1, 2)

class REVERSEDCouplingUnionFind_OneToZero(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(12, 1, 0, 4)

class CouplingUnionFind_ZeroToOne(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(12, 0, 1, 4)

class REVERSEDCouplingUnionFind_OneToHalf(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(12, 1, 1/2, 2)

########################################################

class REVERSEDCouplingUnionFind_NewSeed_HalfToZero(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(13, 1/2, 0, 3)

class CouplingUnionFind_NewSeed_ZeroToOne(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(13, 0, 1, 6)

class REVERSEDCouplingUnionFind_NewSeed_OneToTwoThirds(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(13, 1, 2/3, 2)

class REVERSEDCouplingUnionFind_NewSeed_TwoThirdsToOneThird(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(13, 2/3, 1/3, 2, fadeout=True)

class REVERSEDCouplingUnionFind_NewSeed_OneThirdToZero(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(13, 1/3, 0, 2, faded=True)

class CouplingUnionFind_NewSeed_ZeroToOne_Faded(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(13, 0, 1, 6, faded=True)

class REVERSEDCouplingUnionFind_NewSeed_OneToZero_Faded(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(13, 1, 0, 6, faded=True)
