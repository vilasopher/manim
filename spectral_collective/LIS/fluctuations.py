from manim import *
import numpy.random as ra
import numpy.linalg as la
import numpy as np
import solarized as sol
from functools import partial
from youngdiagrams import YoungDiagram
from TracyWidom import TracyWidom

class RandomMatrix(Scene):
    def construct(self):
        N = 12
        X = np.reshape(ra.normal(size=N*N),(N,N))
        E = la.eigvalsh(0.5*(X+np.transpose(X)))

        M = DecimalMatrix([[0]])

        M.add_updater(
            lambda m : m.become(
                DecimalMatrix(
                    0.5*(X+np.transpose(X)),
                    element_to_mobject_config = {
                        "num_decimal_places": 2,
                        "color": sol.BASE03
                    },
                    bracket_config = {
                        "color": sol.BASE03
                    }
                )
            ).scale(0.35).shift(1.75*UP+3.6111111111*LEFT),
            call_updater=True
        )

        evalpts = [Dot(ORIGIN, color=sol.BASE03) for _ in range(N)]

        def evpup(x, i):
            if i < N-1:
                x.become(
                    Dot(
                        2.5*DOWN+(E[i]-2*np.sqrt(N)+4)*RIGHT+3.6111111111*LEFT,
                        color=sol.BASE03
                    )
                )
            else:
                x.become(
                    Dot(
                        2.5*DOWN+(E[i]-2*np.sqrt(N)+4)*RIGHT+3.6111111111*LEFT,
                        color=sol.RED
                    )
                )

        for i, ep in enumerate(evalpts):
            ep.add_updater(
                partial(evpup, i=i),
                call_updater=True
            )

        ar = Arrow(1.8*UP+0.9*LEFT, ORIGIN, color=sol.BASE01, tip_shape=StealthTip)
        text = Tex(r"highest eigenvalue", color=sol.BASE02).next_to(M, DOWN).shift(0.25*DOWN)

        ar.add_updater(
            lambda x : x.next_to(evalpts[-1], 0.25*UP+0.05*LEFT),
            call_updater = True
        )

        self.add(text)
        self.add(ar)

        def scene_updater(dt):
            for i in range(N):
                for j in range(N):
                    X[i,j] += -2*0.05*dt*X[i,j]+2*np.sqrt(0.05*dt)*ra.normal()
            E2 = la.eigvalsh(0.5*(X+np.transpose(X)))
            for i in range(N):
                E[i] = E2[i]

        self.add_updater(scene_updater)

        self.add(M)

        numberline = Line(8*LEFT, 3*RIGHT, stroke_width=2, color=sol.BASE00).shift(2.5*DOWN+3.6111111111*LEFT)
        end = Line(3*RIGHT, 3.5*RIGHT, stroke_width=2).set_color([sol.BASE3, sol.BASE00]).shift(2.5*DOWN+3.6111111111*LEFT)
        tick = Line(0.25*UP, 0.25*DOWN, stroke_width=2, color=sol.BASE00).shift(2.5*DOWN+(-2*np.sqrt(N)+4)*RIGHT+3.6111111111*LEFT)
        self.add(numberline, end)
        self.add(tick)
        self.add(MathTex(r"0", color=sol.BASE00).next_to(tick, DOWN))

        self.add(*evalpts)

        self.wait(30)

TLC = 2.5*UP + 25*LEFT
R = 15*RIGHT
D = 15*DOWN

def wx(t):
    return (2*t/np.pi + 1) * np.sin(t) + (2/np.pi) * np.cos(t)

def wy(t):
    return (2*t/np.pi - 1) * np.sin(t) + (2/np.pi) * np.cos(t)

LIMIT_SHAPE = Polygon(
    TLC,
    *(
        TLC + wx(t)*R + wy(t)*D
        for t in np.linspace(-np.pi/2, np.pi/2, 200)
    ),
    TLC,
    color = sol.CYAN,
    stroke_width = 4
).set_fill(sol.CYAN, opacity=0.2)

class LimitShapeFluctuations(Scene):
    def construct(self):
        self.nums = list(ra.uniform(size=300))

        def scene_updater(dt):
            for _ in range(4):
                self.nums.append(ra.uniform())

            self.moving_mobjects.clear()
            self.foreground_mobjects.clear()
            self.mobjects.clear()
            self.clear()
            self.add(
                YoungDiagram(
                    self.nums,
                    unit=(15)/np.sqrt(len(self.nums)),
                    origin=TLC,
                    first_row_highlighted=True,
                )
            )
            self.add(
                LIMIT_SHAPE
            )

        self.moving_mobjects.clear()
        self.foreground_mobjects.clear()
        self.mobjects.clear()
        self.clear()
        self.add_updater(scene_updater)

        self.wait(70)

class TracyWidomDensity(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-6, 3, 1],
            y_range=[0, 1/2, 1/8],
            tips=False,
            x_axis_config={"include_numbers": True, "color": sol.BASE02, "decimal_number_config": {"color": sol.BASE02, "num_decimal_places": 0}},
            y_axis_config={"include_numbers": True, "color": sol.BASE02, "decimal_number_config": {"color": sol.BASE02, "num_decimal_places": 3}, "label_direction": RIGHT}
        ).scale(0.5).shift(UP+3.6111111*RIGHT)

        tw2 = TracyWidom()

        graph = ax.plot(tw2.pdf, x_range=[-6,3,0.1], color=sol.FOREST_GREEN).set_fill(color=sol.FOREST_GREEN, opacity=0.5)

        text = Tex(r"Tracy-Widom density", color=sol.BASE02).next_to(ax, DOWN).shift(0.5*DOWN)

        self.play(FadeIn(Group(ax,graph,text), shift=4*LEFT))

        self.wait()

class Text(Scene):
    def construct(self):
        pass

