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
    def construct(self):
        self.camera.background_color = WHITE

        text = Tex(
            "\\textbf{Fermat's Principle}: \
                    light travels along the path \
                    which takes the least time.",
            color=BLACK,
            font_size=38
        )
        text.move_to(3.5*UP)
        self.add(text)

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

        moving_arcs = [
            colored_plot(
                lambda t : gamma(b[i].get_value(), t),
                t_range = gamma_range(b[i].get_value())
            )
            for i in range(2)
        ]
        
        for i in range(2):
            moving_arcs[i].add_updater(
                lambda s, i=i : s.become(
                    colored_plot(
                        lambda t : gamma(b[i].get_value(), t),
                        t_range = gamma_range(b[i].get_value())
                    )
                )
            )

        self.add(
            p,
            q,
            static_arc_nonstationary,
            static_arc_stationary,
            *moving_arcs,
        )

        for _ in range(5):
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
