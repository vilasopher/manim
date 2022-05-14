from manim import *

class A1(Scene):
    def construct(self):
        c = Circle()
        
        self.play(Create(c))
        self.wait()
        self.play(c.animate.move_to(2 * RIGHT))
        self.wait()

class A2(Scene):
    def construct(self):
        tex = MathTex(
            r'\sum_{n=1}^\infty \frac{1}{n^2}'
            r'= \frac{\pi^2}{6}',
            font_size=100
        )

        self.play(Write(tex))
        self.wait()

class A3(Scene):
    def construct(self):
        t1 = MathTex(r'{{a^2}} + {{b^2}} = {{c^2}}')
        t2 = MathTex(r'{{a^2}} = {{c^2}} - {{b^2}}')

        self.play(Write(t1))
        self.wait()
        self.play(TransformMatchingTex(t1,t2))
        self.wait()
        self.play(t2.animate.set_color_by_tex(r'a^2', RED))
        self.wait()

class A4(Scene):
    def construct(self):
        l1 = Line(2 * LEFT + 2 * UP, LEFT)
        l2 = Line(LEFT, 2 * RIGHT + 2 * DOWN)

        self.add(l1, l2)
        self.wait()

        x = ValueTracker(-1)

        l1.add_updater(
            lambda s : s.put_start_and_end_on(
                2 * LEFT + 2 * UP,
                x.get_value() * RIGHT
            )
        )

        l2.add_updater(
            lambda s : s.put_start_and_end_on(
                x.get_value() * RIGHT,
                2 * RIGHT + 2 * DOWN
            )
        )

        self.play(
            x.animate.set_value(3),
            run_time=3,
            rate_func = rate_functions.rush_into
        )
        self.wait()

        self.play(x.animate.set_value(-3), run_time=0.5)
        self.wait()

import networkx as nx

class A5(Scene):
    def construct(self):
        nxg = nx.paley_graph(13)

        g = Graph.from_networkx(
            nxg,
            edge_config = { "stroke_color" : GRAY }
        )

        self.play(Create(g))
        self.wait(2)
        self.play(g.animate.change_layout("circular"))
        self.wait(2)
        self.play(g.animate.change_layout("random"))
        self.wait(2)
        self.play(g.animate.change_layout("spring"))
        self.wait(2)
        self.play(g.animate.change_layout("spectral"))
        self.wait(2)
