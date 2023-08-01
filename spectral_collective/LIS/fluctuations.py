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
        tick1 = Line(0.25*UP, 0.25*DOWN, stroke_width=2, color=sol.BASE00).shift(2.5*DOWN+(-2*np.sqrt(N)+4)*RIGHT+3.6111111111*LEFT)
        tick2 = Line(0.25*UP, 0.25*DOWN, stroke_width=2, color=sol.BASE00).shift(2.5*DOWN+4*RIGHT+3.6111111111*LEFT)
        self.add(numberline, end)
        self.add(tick1)
        self.add(tick2)
        self.add(MathTex(r"0", color=sol.BASE00).next_to(tick1, DOWN))
        self.add(MathTex(r"2\sqrt{n}", color=sol.BASE00).next_to(tick2, DOWN))

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

        self.play(FadeIn(Group(ax,graph,text), shift=3*UP))

        self.wait()

class TitleCard(Scene):
    def construct(self):
        text = Tex(
            r"""
                Fluctuations
            """,
            color = sol.BASE02,
            font_size = 100
        ).set_color_by_tex(r"L", sol.RED).set_color_by_tex(r")", sol.RED).shift(0.5*UP)
        heur = Tex(
            r"""
            (a connection to random matrix theory)
            """,
            color = sol.BASE02,
            font_size = 60
        ).next_to(text, DOWN).shift(0.5*DOWN)

        self.play(FadeIn(text, shift=DOWN))
        self.wait(0.5)
        self.play(FadeIn(heur))
        self.wait(10)

class Text1(Scene):
    def construct(self):
        #self.add(LIMIT_SHAPE)
        
        clt = Tex(r"\textbf{Central Limit Theorem:}", color=sol.BASE02).shift(DOWN + 2*LEFT)
        clttxt = Tex(r"fluctuations $\longrightarrow$ Gaussian", color=sol.BASE02).shift(1.75*DOWN)

        lis = Tex(r"\textbf{Longest Increasing Subsequence:}", color=sol.BASE02).align_to(clt, UP+LEFT)
        x = Cross(stroke_color=sol.RED).shift(1.8*DOWN+0.275*RIGHT).scale(0.25)

        tt = TexTemplate()
        tt.add_to_preamble(
            r"""
                \usepackage{amsmath, mathrsfs, mathtools}
            """
        )

        thm = MathTex(
            r"""
            { { {{L(}} \sigma_n {{)}} - 2 \sqrt{n} } \over n^{1/6} } \xlongrightarrow{d} \text{TW}_2
            """,
            color=sol.BASE02,
            font_size=60,
            tex_template=tt
        ).set_color_by_tex(r'L', sol.RED).set_color_by_tex(r')', sol.RED).shift(2.5*DOWN)

        eq = MathTex(r"=", font_size=60, color=sol.BASE02).next_to(thm, RIGHT).shift(1.5*LEFT)

        tw = Tex(r"Tracy-Widom \\ distribution", color=sol.BASE02).next_to(eq, RIGHT)

        ax = Axes(
            x_range=[-6, 3, 1],
            y_range=[0, 1/2, 1/8],
            tips=False,
            x_axis_config={"include_numbers": True, "color": sol.BASE02, "decimal_number_config": {"color": sol.BASE02, "num_decimal_places": 0}},
            y_axis_config={"include_numbers": True, "color": sol.BASE02, "decimal_number_config": {"color": sol.BASE02, "num_decimal_places": 3}, "label_direction": RIGHT}
        ).scale(0.5).shift(UP+3.6111111*RIGHT)

        tw2 = TracyWidom()

        graph = ax.plot(tw2.pdf, x_range=[-6,3,0.1], color=sol.FOREST_GREEN).set_fill(color=sol.FOREST_GREEN, opacity=0.5)

        twd = Tex(r"Tracy-Widom density", color=sol.BASE02).next_to(ax, DOWN).shift(0.5*DOWN)

        # time = 10

        self.play(FadeIn(clt))

        # time = 11

        self.wait(2.5)

        # time = 13:30

        self.play(FadeIn(clttxt, shift=UP))

        # time = 14:30

        self.wait(3.5)

        # time = 18

        self.play(
            FadeOut(clt, shift=LEFT),
            FadeIn(lis, shift=LEFT),
        )

        # time = 19

        self.wait()

        # time = 20

        self.play(
            FadeIn(x, scale=2)
        )

        # time = 21

        self.wait(5)

        # time = 26

        self.play(
            FadeOut(Group(clttxt,x), shift=0.5*UP),
            FadeIn(thm, shift=0.5*UP)
        )

        # time = 27

        self.wait(3.5)

        # time = 30:30

        self.play(
            thm.animate.shift(1.5*LEFT),
            FadeIn(Group(eq, tw), shift=1.5*LEFT)
        )

        # time = 31:30

        self.wait(1.5)

        # time = 33

        self.play(
            FadeOut(lis),
            FadeOut(eq),
            thm.animate.shift(3.5*UP+5*RIGHT),
            tw.animate.shift(1.5*UP+0.5*LEFT)
        )

        # time = 34

        self.wait(8.25)

        # time = 42:15

        self.play(
            FadeOut(Group(thm, tw), shift=5*UP),
            FadeIn(Group(ax, graph, twd), shift=5*UP)
        )

        self.wait(20)


class Text2(Scene):
    def construct(self):
        clt = Tex(r"\textbf{Central Limit Theorem:} independence $\Rightarrow$ Gaussian", color=sol.BASE02).shift(3*UP)

        ob = Rectangle(width=5.75,color=sol.BASE3).set_fill(sol.BASE3, opacity=1).align_to(clt, RIGHT+DOWN).set_z_index(2)
        self.add(ob)

        lis = Tex(r"\textbf{Longest Increasing Subsequence:}", font_size=60, color=sol.BASE02).align_to(clt, LEFT).shift(1.5*UP)
        int = Tex(r"interaction", color=sol.BASE02).align_to(clt, LEFT).shift(RIGHT + 0.5*UP)
        dep = Tex(r"dependence", color=sol.BASE02).align_to(clt, LEFT).shift(RIGHT + 0.5*DOWN)
        opt = Tex(
            r"""
                \end{center} optimization over \\ independent noise \begin{center}
            """,
            color=sol.BASE02
        ).align_to(clt, LEFT).shift(RIGHT + 1.75*DOWN)

        # time = 1:30

        self.play(FadeIn(clt))

        # time = 2:30

        self.wait(5)

        # time = 7:30

        self.play(FadeOut(ob))

        # time = 8:30

        self.wait(5)

        # time = 13:30

        self.play(FadeIn(lis))

        # time = 14:30

        self.wait()

        # time = 15:30

        self.play(FadeIn(int))
        self.play(FadeIn(dep))

        # time = 17:30

        self.wait(2)

        # time = 19:30

        self.play(FadeIn(opt))

        self.wait(30)


class ExactText(Scene):
    def construct(self):
        txt1 = Tex(r"algebraic connections", font_size=60, color=sol.BASE02).shift(1.5*RIGHT)
        ar = MathTex(r"\Rightarrow", font_size=60, color=sol.BASE02).rotate(-PI/2).next_to(txt1, DOWN)
        txt2 = Tex(r"exact calculations", font_size=60, color=sol.BASE02).next_to(ar, DOWN)

        self.add(txt1, ar, txt2)

class ThankYouText(Scene):
    def construct(self):
        txt = Tex(r"\textbf{thanks for watching!}", color=sol.BASE3, font_size=100)
        self.add(txt)
