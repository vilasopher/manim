from manim import *

def colorfunction(t, freq = 0.2, **kwargs):
    return interpolate_color(
            PURE_BLUE,
            PURE_RED, 
            (1 + np.cos(freq * PI * t)) / 2
    )

def colored_plot(f, stroke_width = 10, z_index = 0, **kwargs):
    curve = ParametricFunction(
        f,
        stroke_width = stroke_width,
        z_index = z_index,
        **kwargs
    )

    pieces = CurvesAsSubmobjects(curve)

    colors = [
        colorfunction(t, **kwargs)
        for t in range(curve.get_num_curves())
    ]

    pieces.set_color_by_gradient(*colors)
    
    return pieces

def gamma(a_inv, t):
    a = 1 / a_inv if a_inv != 0 else 2 ** 16

    if a >= 0:
        return [
            - 7 * np.sqrt(a**2 + 1) * np.cos(t),
            7 * (np.sqrt(a**2 + 1) * np.sin(t) - a) - 3,
            0 
        ]
    else:
        return [
            - 7 * np.sqrt(a**2 + 1) * np.cos(t),
            - 7 * (np.sqrt(a**2 + 1) * np.sin(t) + a) - 3,
            0 
        ]

def gamma_range(a_inv, step = 0.005):
    a = 1 / a_inv if a_inv != 0 else 2 ** 16
    
    return [ 
        np.arccos(1 / np.sqrt(a**2 + 1)),
        PI - np.arccos(1 / np.sqrt(a**2 + 1)),
        step / np.sqrt(a**2 + 1)
    ]

class Fermat(Scene):

    notifier = Dot(color=LIGHTER_GRAY, radius=0.05)
    notifier.move_to(7 * RIGHT + 3.9 * DOWN)

    def noticewait(self):
        self.add(self.notifier)
        self.wait()
        self.remove(self.notifier)

    def construct(self):
        self.camera.background_color = WHITE

        text = Tex(
            "{{\\textbf{Fermat's Principle}: \
                    light travels along}} the path \
                    which takes the least time.",
            color=BLACK,
            font_size=38
        )
        text.move_to(3.5*UP)

        self.add(text)
        self.wait()
        self.noticewait()

        p = Dot([-7, -3, 0], z_index = 1, color=BLACK)
        q = Dot([7, -3, 0], z_index = 1, color=BLACK)

        static_arc_nonstationary = ParametricFunction(
            lambda t : gamma(5, t),
            t_range = gamma_range(5),
            stroke_width = 5,
            stroke_color = YELLOW,
            z_index = -1
        )

        static_arc_stationary = ParametricFunction(
            lambda t : [t, -3, 0],
            t_range = [-7, 7, 0.1],
            stroke_width = 5,
            stroke_color = YELLOW,
            z_index = -1
        )

        mins = [-0.15, 3.5]
        maxs = [0.15, 8]
        
        b = [
            ValueTracker(mins[0]),
            ValueTracker(mins[1])
        ]

        moving_arcs_colored = [
            colored_plot(
                lambda t : gamma(b[i].get_value(), t),
                t_range = gamma_range(b[i].get_value())
            )
            for i in range(2)
        ]

        moving_arcs_yellow = [
            ParametricFunction(
                lambda t : gamma(b[i].get_value(), t),
                t_range = gamma_range(b[i].get_value()),
                color = YELLOW_E
            )
            for i in range(2)
        ]

        self.play(
            Create(p),
            Create(q)
        )
        self.noticewait()

        self.play(Create(static_arc_nonstationary))
        self.noticewait()

        self.play(FadeIn(moving_arcs_yellow[1]))
        self.noticewait()
        
        moving_arcs_yellow[1].add_updater(
            lambda s : s.become(
                ParametricFunction(
                    lambda t : gamma(b[1].get_value(), t),
                    t_range = gamma_range(b[1].get_value()),
                    color = YELLOW_E
                )
            )
        )

        self.play(b[1].animate.set_value(maxs[1]), run_time = 5)
        self.noticewait()

        self.play(b[1].animate.set_value(mins[1]))
        self.play(b[1].animate.set_value(maxs[1]), run_time = 5)
        self.play(b[1].animate.set_value(mins[1]))
        self.noticewait()

        self.play(
            FadeOut(moving_arcs_yellow[1]),
            FadeIn(moving_arcs_colored[1])
        )
        self.noticewait()

        moving_arcs_colored[1].add_updater(
            lambda s : s.become(
                colored_plot(
                    lambda t : gamma(b[1].get_value(), t),
                    t_range = gamma_range(b[1].get_value())
                )
            )
        )
        
        self.play(b[1].animate.set_value(maxs[1]), run_time = 5)
        self.noticewait()
        
        for _ in range(5):
            self.play(b[1].animate.set_value(mins[1]))
            self.play(b[1].animate.set_value(maxs[1]))
        self.play(b[1].animate.set_value(mins[1]))
        self.noticewait()

        self.play(Create(static_arc_stationary))
        self.noticewait()

        self.play(FadeIn(moving_arcs_yellow[0]))
        self.noticewait()
        
        moving_arcs_yellow[0].add_updater(
            lambda s : s.become(
                ParametricFunction(
                    lambda t : gamma(b[0].get_value(), t),
                    t_range = gamma_range(b[0].get_value()),
                    color = YELLOW_E
                )
            )
        )

        self.play(b[0].animate.set_value(maxs[0]), run_time = 3)
        self.play(b[0].animate.set_value(mins[0]), run_time = 3)
        self.noticewait()

        self.play(
            FadeOut(moving_arcs_yellow[0]),
            FadeIn(moving_arcs_colored[0])
        )
        self.noticewait()

        moving_arcs_colored[0].add_updater(
            lambda s : s.become(
                colored_plot(
                    lambda t : gamma(b[0].get_value(), t),
                    t_range = gamma_range(b[0].get_value())
                )
            )
        )

        for _ in range(5):
            self.play(b[0].animate.set_value(maxs[0]))
            self.play(b[0].animate.set_value(mins[0]))

        self.noticewait()

        tex_stationary = Tex("stationary", color=BLACK)
        tex_nonstationary = Tex("nonstationary", color=BLACK)
        tex_stationary.move_to(2 * DOWN)
        tex_nonstationary.move_to(1.5 * UP)

        self.play(FadeIn(tex_stationary, scale=1.5))
        self.noticewait()

        self.play(FadeIn(tex_nonstationary, scale=1.5))
        self.noticewait()

        text_true = Tex(
            "{{\\textbf{Fermat's Principle}: \
                    light travels along}} stationary paths.",
            color=BLACK,
            font_size=38
        )
        text_true.align_to(text, DL)

        self.play(
            FadeOut(text),
            FadeIn(text_true)
        )
        self.noticewait()

        for _ in range(10):
            self.play(
                *[
                    b[i].animate.set_value(maxs[i])
                    for i in range(2)
                ]
            )
            self.play(
                *[
                    b[i].animate.set_value(mins[i])
                    for i in range(2)
                ]
            )

        self.noticewait()
        self.wait()
