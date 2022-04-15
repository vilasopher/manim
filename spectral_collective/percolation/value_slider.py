from manim import *
import solarized as sol

class ValueSlider(VGroup):
    def __init__(self, p=0.5, opacity=0.75, bar_color=sol.BASE2, **kwargs):
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

        self.var = MathTex("p", color=sol.BASE03)
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
