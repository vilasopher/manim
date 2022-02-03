from manim import *

class Snell(Scene):
    notifier = Dot(color=DARK_GRAY, radius=0.05)
    notifier.move_to(7 * RIGHT + 3.9 * DOWN)

    def noticewait(self):
        self.add(self.notifier)
        self.wait()
        self.remove(self.notifier)

    def construct(self):
        self.camera.background_color = WHITE

        # set up initial scene
        p = Dot([-1.5, 3, 0], color=BLACK, z_index=1)
        q = Dot([1.5, -3, 0], color=BLACK, z_index=1)
        interface = Line([-2,0,0], [2,0,0], color=BLUE)

        water = Rectangle(BLUE_B, height=4, width=4, z_index = -1)
        water.set_fill(BLUE_B, opacity=1)
        water.align_to(interface, UP)

        self.play(Create(water), Create(interface))
        self.play(Create(p), Create(q))
        self.noticewait()

        x = ValueTracker(0)

        ray1 = Line(p.get_center(), contact.get_center(), color=YELLOW)
        ray2 = Line(contact.get_center(), q.get_center(), color=YELLOW)

        ray1.add_updater(
            lambda s : s.put_start_and_end_on(
                p.get_center(),
                [x.get_value(),0,0]
            )
        )
        ray2.add_updater(
            lambda s : s.put_start_and_end_on(
                [x.get_value(),0,0],
                q.get_center()
            )
        )

        self.play(
            Create(ray1),
            run_time=0.5,
            rate_func=rate_functions.rush_into
        )
        self.play(
            Create(ray2),
            run_time=0.5,
            rate_func=rate_functions.rush_from
        )
        self.noticewait()

        self.play(x.animate.set_value(1))
        self.play(x.animate.set_value(-1.9))
        self.play(x.animate.set_value(1.5))
        self.play(x.animate.set_value(0))
        self.noticewait()

        fermat = Tex(
            "\\textbf{Fermat's Principle}: \
                    light travels along the path \
                    which takes the least time",
            color=BLACK,
            font_size=38
        )
        fermat.move_to(3.5*UP)

        self.play(Write(fermat))
        self.noticewait()

        self.play(ApplyWave(fermat))
