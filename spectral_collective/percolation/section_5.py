from manim import *
import random
import grid as gr
import solarized as sol
from glitch import Glitch, RandomizeNumber, GlitchEdges
from more_graphs import HPCCGrid, HPGrid
from value_slider import ValueSlider

class CouplingNumbering(Scene):
    def construct(self):
        random.seed(7)

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

        self.play(
            FadeIn(bg),
            FadeIn(g)
        )

        self.wait(8)

        nums = {}

        for r, e in coupling:
            nums[e] = DecimalNumber(
                    r,
                    font_size=40,
                    z_index=1
                )
            nums[e].color = sol.BASE03
            nums[e].next_to(bg.edges[e], ORIGIN)

        randomedgeorder = [ e for r, e in coupling ]
        random.shuffle(randomedgeorder)

        self.play(
            LaggedStart(
                *(
                    Glitch(nums[e], inn=True, intensity=0.05, run_time=0.2)
                    for e in randomedgeorder
                ), lag_ratio = 1-0.141
            )
        )

        self.wait(6)

        self.wait()

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

class CouplingUnionFind_Fast_Zero_To_One(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(7, 0, 1, 6)

class REVERSEDCouplingUnionFind_Fast_One_To_Zero(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(7, 1, 0, 6)

class CouplingUnionFind_Slow_Zero_To_One(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(7, 0, 1, 18)

class REVERSEDCouplingUnionFind_One_To_OneHalf(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(7, 1, 1/2, 6)

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

        self.wait(2.5)

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
        self.construct_abstract(9, glitchout=False, standardized=True)

class NumberResamplesInitial(NumberResamplesAbstract):
    def construct(self):
        self.construct_abstract(7, glitchin=False, standardized=True)

class NumberResamples1(NumberResamplesAbstract):
    def construct(self):
        self.construct_abstract(random.random())

class NumberResamples2(NumberResamples1):
    pass

class NumberResamples3(NumberResamples1):
    pass

class NumberResamples4(NumberResamples1):
    pass

class NumberResamples5(NumberResamples1):
    pass

class NumberResamples6(NumberResamples1):
    pass

class NumberResamples7(NumberResamples1):
    pass

class NumberResamples8(NumberResamples1):
    pass

class NumberResamples9(NumberResamples1):
    pass

class REVERSEDCouplingUnionFind_NewSeed_OneHalf_To_Zero(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(9, 1/2, 0, 6)

class CouplingUnionFind_NewSeed_Zero_To_One(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(9, 0, 1, 12)

class REVERSEDCouplingUnionFind_NewSeed_One_To_Zero(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(9, 1, 0, 12)

class REVERSEDCouplingUnionFind_NewSeed_One_To_OneHalf(CouplingUnionFindAbstract):
    def construct(self):
        self.construct_abstract(9, 1, 1/2, 6)

class FadeInMidResCoupling(Scene):
    def construct(self):
        random.seed(2)

        g = HPCCGrid.from_grid((24,14),0.3)
        
        self.play(FadeIn(g))

class MidResCoupling(Scene):
    def construct(self):
        random.seed(2)

        g = HPCCGrid.from_grid((24,14),0.3)
        
        self.add(g)

        slider = ValueSlider(0, z_index = 2)
        #self.add(slider) TODO

        p = ValueTracker(0)

        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        g.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.play(
            p.animate.set_value(1),
            rate_func=rate_functions.linear,
            run_time=9
        )
