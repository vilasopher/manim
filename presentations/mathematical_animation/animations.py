from manim import *

class A1(Scene):
    def construct(self):
        c = Circle()
        self.add(c)

class A2(Scene):
    def construct(self):
        c = Circle()
        s = Square()

        s.next_to(c)
        self.add(c,s)

class A3(Scene):
    def construct(self):
        c = Circle()
        s = Square()

        self.play(Create(c))
        self.wait()
        self.play(Transform(c,s))
        self.wait()

class A4(Scene):
    def construct(self):
        c = Circle()
        
        self.play(Create(c))
        self.wait()
        #c.set_fill(YELLOW, opacity=1)
        self.play(c.animate.set_fill(YELLOW, opacity=1))
        self.wait()

class A5(Scene):
    def construct(self):
        c = Circle()

        self.play(Create(c))
        self.wait()
        #c.move_to(2 * RIGHT)
        self.play(c.animate.move_to(2 * RIGHT))
        c.wait()

class A6(Scene):
    def construct(self):
        t = MathTex(
            r'\sum_{n=1}^\infty \frac{1}{n^2}'
            r'= \frac{\pi^2}{6}',
            font_size = 100
        )

        self.play(Write(t))
        self.wait()

class A7(Scene):
    def construct(self):
        t1 = MathTex(r'{{a^2}} + {{b^2}} = {{c^2}}')
        t2 = MathTex(r'{{a^2}} = {{c^2}} - {{b^2}}')

        self.play(Write(t1))
        self.wait()
        self.play(TransformMatchingTex(t1,t2))
        self.wait()
        self.play(t2.animate.set_color_by_tex(r'a^2', RED))
        self.wait()

class A8(Scene):
    def construct(self):
        l1 = Line(2 * LEFT + 2 * UP, ORIGIN)
        l2 = Line(ORIGIN, 2 * RIGHT + 2 * DOWN)

        self.add(l1, l2)
        self.wait()

        x = ValueTracker(0)

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

        self.play(x.animate.set_value(3), run_time=3)
        self.wait()
        self.play(x.animate.set_value(-3), run_tim3=4)
        self.wait()

class A9(Scene):
    def construct(self):
        nodes = range(5) #= [0,1,2,3,4]
        edges = [
            (0,1), (0,2), (1,3), (1,4),
            (2,4), (2,3)
        ] 

        g = Graph(nodes, edges)
        
        self.play(Create(g))
        self.wait()
        self.play(g.animate.change_layout("circular"))
        self.wait()
        self.play(g.animate.change_layout("random"))
        self.wait()
        self.play(g.animate.change_layout("spring"))
        self.wait()
        self.play(g.animate.change_layout("spectral"))
        self.wait()

import networkx as nx

class A10(Scene):
    def construct(self):
        nxg = nx.paley_graph(13)

        g = Graph.from_networkx(
            nxg,
            edge_config = { "stroke_color" : GRAY }
        )

        self.play(Create(g))
        self.wait()
        self.play(g.animate.change_layout("circular"))
        self.wait()
        self.play(g.animate.change_layout("random"))
        self.wait()
        self.play(g.animate.change_layout("spring"))
        self.wait()
        self.play(g.animate.change_layout("spectral"))
        self.wait()

class A11(Scene):
    def construct(self):
        ax = Axes(
            x_range = [-0.2, 0.2, 0.05],
            y_range = [-0.1, 0.1, 0.05]
        )

        curve = ax.plot(
            lambda x : (x**2) * np.sin(1/x),
            x_range = [-0.2,0.2],
            color = BLUE
        )

        self.add(ax)
        self.wait()
        self.play(Create(curve))
        self.wait()

        dcurve = ax.plot(
            lambda x : 0.1 * (2 * x * np.sin(1/x) - np.cos(1/x)),
            x_range = [-0.2,0.2],
            color = RED
        )

        self.play(Create(dcurve))
        self.wait()
