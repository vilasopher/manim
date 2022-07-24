from manim import *
import solarized as sol

class CriticalValueSlider(VGroup):
    def __init__(self, p=0.5, **kwargs):
        super().__init__(**kwargs)

        self.center = 7.111111111 - 0.7

        self.p = p

        self.bg = Rectangle(width=1.4, height=8.5, color=sol.BASE0)
        self.bg.set_fill(sol.BASE3, opacity=1) #0.925
        self.bg.move_to((self.center + 0.2) * RIGHT)

        self.line = Line(
            [self.center, -3.25, 0],
            [self.center, +3.25, 0],
            color=sol.BASE03
        )

        self.var = MathTex("p", color=sol.RED)
        self.var.move_to([self.center - 0.3, -3.25 + 6.5 * self.p, 0])

        self.crit = MathTex("p_c", color=sol.BLUE)
        self.crit.move_to([self.center + 0.4, 0, 0])

        self.vartick = Line(
            [self.center - 0.1, -3.25 + 6.5 * self.p, 0],
            [self.center + 0.1, -3.25 + 6.5 * self.p, 0],
            color = sol.BASE03,
            z_index = 2
        )

        self.crittick = Line(
            [self.center - 0.1, 0, 0],
            [self.center + 0.1, 0, 0],
            color = sol.BLUE,
            z_index = 1
        )

        self.crittick = Square(
            side_length = 0.1/1.41,
            color = sol.BLUE,
            z_index = 1
        ).set_fill(sol.BLUE, opacity=1).move_to([self.center, 0, 0]).rotate(PI/4)

        self.n0 = MathTex("0", color=sol.BASE03)
        self.n0.next_to(self.line, DOWN)

        self.n1 = MathTex("1", color=sol.BASE03)
        self.n1.next_to(self.line, UP)
        
        self.add(
            self.bg,
            self.line,
            self.var,
            self.vartick,
            self.n0,
            self.n1
        )

    def set_p(self, p):
        self.p = p

        self.var.move_to([self.center - 0.3, -3.25 + 6.5 * self.p, 0])

        self.vartick.put_start_and_end_on(
            [self.center - 0.1, -3.25 + 6.5 * self.p, 0],
            [self.center + 0.1, -3.25 + 6.5 * self.p, 0]
        )

    def add_crit(self):
        self.add(self.crittick, self.crit)

    @override_animate(add_crit)
    def _add_crit_animation(self, **kwargs):
        return FadeIn(Group(self.crittick, self.crit), **kwargs)

class ValueSlider(VGroup):
    def __init__(self, p=0.5, opacity=1, bar_color=sol.BASE0, **kwargs): #0.925
        super().__init__(**kwargs)

        self.p = p

        self.bg = Rectangle(width=1.7, height=8.5, color=bar_color)
        self.bg.set_fill(sol.BASE3, opacity=opacity)
        self.bg.move_to((6.35) * RIGHT)

        self.line = Line(
            [6, -3.25, 0],
            [6, +3.25, 0],
            color=sol.BASE03
        )

        self.var = MathTex("p", color=sol.RED)
        self.var.move_to([5.7, -3.25 + 6.5 * self.p, 0])

        self.dec = DecimalNumber(self.p, color=sol.BASE03)
        self.dec.next_to(self.var, RIGHT * 1.5)

        self.tick = Line(
            [5.9, -3.25 + 6.5 * self.p, 0],
            [6.1, -3.25 + 6.5 * self.p, 0],
            color=sol.BASE03
        )

        self.n0 = MathTex("0", color=sol.BASE03)
        self.n0.next_to(self.line, DOWN)

        self.n1 = MathTex("1", color=sol.BASE03)
        self.n1.next_to(self.line, UP)

        self.add(
            self.bg,
            self.line,
            self.var,
            self.dec,
            self.tick,
            self.n0,
            self.n1
        )

    def set_p(self, p):
        self.p = p

        self.var.move_to([5.7, -3.25 + 6.5 * self.p, 0])

        self.dec.set_value(self.p)
        self.dec.next_to(self.var, RIGHT * 1.5)

        self.tick.put_start_and_end_on(
            [5.9, -3.25 + 6.5 * self.p, 0],
            [6.1, -3.25 + 6.5 * self.p, 0]
        )
