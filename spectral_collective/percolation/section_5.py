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

        coupling = [ ((i+1)/59, c[1]) for i, c in enumerate(coupling) ]

        g.coupling = coupling

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

        self.play(
            LaggedStart(
                *(
                    Glitch(nums[e], inn=True, intensity=0.05, run_time=0.25)
                    for r, e in coupling
                )
            ), lag_ratio=1 #TODO
        )

        self.wait(6)

        p = ValueTracker(0)
        slider = ValueSlider(p=0, opacity=0.95, bar_color=sol.BASE1, z_index = 2)
        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        #self.play(FadeIn(slider)) TODO
        self.wait()

class CouplingUnionFindFast(Scene):
    def construct(self):
        random.seed(7)

        g = HPCCGrid.from_grid((3,2), 2.5)

        coupling = list(g.coupling)

        coupling = [ ((i+1)/59, c[1]) for i, c in enumerate(coupling) ]

        g.coupling = coupling

        bg = HPGrid.from_grid(
            (5,3),
            2.5,
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.VERY_LIGHT_EDGE_CONFIG
        )

        self.add(bg, g)

        p = ValueTracker(0)

        slider = ValueSlider(p=0, opacity=0.95, bar_color=sol.BASE1, z_index = 2)
        #self.add(slider) TODO
        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

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

        prev_r = 0
        for r, e in list(coupling):
            self.play(
                g.animate.set_p(r),
                p.animate.set_value(r),
                run_time = 6 * (r - prev_r),
                rate_func = rate_functions.linear
            )
            prev_r = r

        if prev_r < 1:
            self.play(
                g.animate.set_p(1),
                p.animate.set_value(1),
                run_time = 6 * (1 - prev_r),
                rate_func = rate_functions.linear
            )

class CouplingUnionFindSlow(Scene):
    def construct(self):
        random.seed(7)

        g = HPCCGrid.from_grid((3,2), 2.5)

        coupling = list(g.coupling)

        coupling = [ ((i+1)/59, c[1]) for i, c in enumerate(coupling) ]

        g.coupling = coupling

        bg = HPGrid.from_grid(
            (5,3),
            2.5,
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.VERY_LIGHT_EDGE_CONFIG
        )

        self.add(bg, g)

        p = ValueTracker(0)

        slider = ValueSlider(p=0, opacity=0.95, bar_color=sol.BASE1, z_index = 2)
        #self.add(slider) TODO
        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

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

        prev_r = 0
        for r, e in list(coupling):
            self.play(
                g.animate.set_p(r),
                p.animate.set_value(r),
                run_time = 18 * (r - prev_r),
                rate_func = rate_functions.linear
            )
            prev_r = r

        if prev_r < 1:
            self.play(
                g.animate.set_p(1),
                p.animate.set_value(1),
                run_time = 18 * (1 - prev_r),
                rate_func = rate_functions.linear
            )

class CouplingUnionFindOneHalfFromAbove(Scene):
    def construct(self):
        random.seed(7)

        g = HPCCGrid.from_grid((3,2), 2.5)

        coupling = list(g.coupling)

        coupling = [ ((i+1)/59, c[1]) for i, c in enumerate(coupling) ]

        g.coupling = coupling

        bg = HPGrid.from_grid(
            (5,3),
            2.5,
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.VERY_LIGHT_EDGE_CONFIG
        )

        self.add(bg, g)

        p = ValueTracker(0)

        slider = ValueSlider(p=0, opacity=0.95, bar_color=sol.BASE1, z_index = 2)
        #self.add(slider) TODO
        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

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

        prev_r = 1/2
        g.set_p(1/2)
        p.set_value(1/2)

        for r, e in list(coupling):
            if r > 1/2:
                self.play(
                    g.animate.set_p(r),
                    p.animate.set_value(r),
                    run_time = 12 * (r - prev_r),
                    rate_func = rate_functions.linear
                )
                prev_r = r

        if prev_r < 1:
            self.play(
                g.animate.set_p(1),
                p.animate.set_value(1),
                run_time = 12 * (1 - prev_r),
                rate_func = rate_functions.linear
            )

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

class NumberResamples1(Scene):
    def construct(self):
        g = HPCCGrid.from_grid((3,2), 2.5)

        coupling = list(g.coupling)

        bg = HPGrid.from_grid(
            (5,3),
            2.5,
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.VERY_LIGHT_EDGE_CONFIG
        )

        self.add(bg, g)

        p = ValueTracker(0.5)
        slider = ValueSlider(p=0.5, opacity=0.95, bar_color=sol.BASE1, z_index = 2)
        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )
        #self.add(slider) TODO

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

        self.play(
            *(
                Glitch(nums[e])
                for r, e in coupling
            ),
            GlitchEdges(g, intensity=0.03),
            run_time=0.5
        )

        self.wait(2.5)

        self.play(
            *(
                Glitch(nums[e])
                for r, e in coupling
            ),
            GlitchEdges(g, intensity=0.03),
            run_time=0.5
        )

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

class NumberResamples0(NumberResamples1):
    pass

class CouplingUnionFindNewSeedOneHalfFromBelow(Scene):
    def construct(self):
        random.seed(9)

        g = HPCCGrid.from_grid((3,2), 2.5)

        coupling = list(g.coupling)

        coupling = [ ((i+1)/59, c[1]) for i, c in enumerate(coupling) ]

        g.coupling = coupling

        bg = HPGrid.from_grid(
            (5,3),
            2.5,
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.VERY_LIGHT_EDGE_CONFIG
        )

        self.add(bg, g)

        p = ValueTracker(0)

        slider = ValueSlider(p=0, opacity=0.95, bar_color=sol.BASE1, z_index = 2)
        #self.add(slider) TODO
        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

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

        prev_r = 0
        for r, e in list(coupling):
            if r <= 1/2:
                self.play(
                    g.animate.set_p(r),
                    p.animate.set_value(r),
                    run_time = 10 * (r - prev_r),
                    rate_func = rate_functions.linear
                )
                prev_r = r

        if prev_r < 1/2:
            self.play(
                g.animate.set_p(1/2),
                p.animate.set_value(1/2),
                run_time = 10 * (1/2 - prev_r),
                rate_func = rate_functions.linear
            )

class CouplingUnionFindNewSeed(Scene):
    def construct(self):
        random.seed(9)

        g = HPCCGrid.from_grid((3,2), 2.5)

        coupling = list(g.coupling)

        coupling = [ ((i+1)/59, c[1]) for i, c in enumerate(coupling) ]

        g.coupling = coupling

        bg = HPGrid.from_grid(
            (5,3),
            2.5,
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.VERY_LIGHT_EDGE_CONFIG
        )

        self.add(bg, g)

        p = ValueTracker(0)

        slider = ValueSlider(p=0, opacity=0.95, bar_color=sol.BASE1, z_index = 2)
        #self.add(slider) TODO
        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

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

        prev_r = 0
        for r, e in list(coupling):
            self.play(
                g.animate.set_p(r),
                p.animate.set_value(r),
                run_time = 10 * (r - prev_r),
                rate_func = rate_functions.linear
            )
            prev_r = r

        if prev_r < 1:
            self.play(
                g.animate.set_p(1),
                p.animate.set_value(1),
                run_time = 10 * (1 - prev_r),
                rate_func = rate_functions.linear
            )

class CouplingUnionFindNewSeedOneHalfFromAbove(Scene):
    def construct(self):
        random.seed(9)

        g = HPCCGrid.from_grid((3,2), 2.5)

        coupling = list(g.coupling)

        coupling = [ ((i+1)/59, c[1]) for i, c in enumerate(coupling) ]

        g.coupling = coupling

        bg = HPGrid.from_grid(
            (5,3),
            2.5,
            vertex_config = sol.LIGHT_VERTEX_CONFIG,
            edge_config = sol.VERY_LIGHT_EDGE_CONFIG
        )

        self.add(bg, g)

        p = ValueTracker(0)

        slider = ValueSlider(p=0, opacity=0.95, bar_color=sol.BASE1, z_index = 2)
        #self.add(slider) TODO
        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

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

        prev_r = 1/2
        g.set_p(1/2)
        p.set_value(1/2)

        for r, e in list(coupling):
            if r > 1/2:
                self.play(
                    g.animate.set_p(r),
                    p.animate.set_value(r),
                    run_time = 10 * (r - prev_r),
                    rate_func = rate_functions.linear
                )
                prev_r = r

        if prev_r < 1:
            self.play(
                g.animate.set_p(1),
                p.animate.set_value(1),
                run_time = 10 * (1 - prev_r),
                rate_func = rate_functions.linear
            )

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
