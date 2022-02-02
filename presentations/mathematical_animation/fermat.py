from manim import *

def colorfunction(t, freq = 0.1, **kwargs):
    return interpolate_color(
            PURE_BLUE,
            PURE_RED, 
            (1 + np.cos(freq * PI * t)) / 2
    )

def colored_plot(f, stroke_width = 10, z_index = 0, **kwargs):
    curve = ParametricFunction(f, **kwargs)
    pieces = CurvesAsSubmobjects(curve)

    colors = [
        colorfunction(t, **kwargs)
        for t in range(curve.get_num_curves())
    ]

    pieces.set_color_by_gradient(*colors)
    return pieces

def gamma(a, t):
    if a >= 0:
        return [
            - 5 * np.sqrt(a**2 + 1) * np.cos(t),
            5 * (np.sqrt(a**2 + 1) * np.sin(t) - a) - 2,
            0 
        ]
    else:
        return [
            - 5 * np.sqrt(a**2 + 1) * np.cos(t),
            - 5 * (np.sqrt(a**2 + 1) * np.sin(t) - a) - 2,
            0 
        ]

def gamma_range(a, step = 0.005):
    return [ 
        np.arccos(1 / np.sqrt(a**2 + 1)),
        PI - np.arccos(1 / np.sqrt(a**2 + 1)),
        step / np.sqrt(a**2 + 1)
    ]

class Fermat(Scene):
    def construct(self):

        p = Dot([-5, -2, 0], z_index = 1)
        q = Dot([5, -2, 0], z_index = 1)

        static_arc = ParametricFunction(
            lambda t : gamma(0.2, t),
            t_range = gamma_range(0.2),
            stroke_width = 5,
            stroke_color = GRAY,
            z_index = -1
        )

        self.add(p, q, static_arc)
        
        a = ValueTracker(0.1)
        
        moving_arc = colored_plot(
            lambda t : gamma(a.get_value(), t),
            t_range = gamma_range(a.get_value())
        )

        moving_arc.add_updater(
            lambda s : s.become(
                colored_plot(
                    lambda t : gamma(a.get_value(), t),
                    t_range = gamma_range(a.get_value())
                )
            )
        )

        self.add(moving_arc)

        self.play(
            a.animate.set_value(100),
            rate_func = rate_functions.rush_into
        )
        a.set_value(-100)
        self.play(
            a.animate.set_value(-0.1),
            rate_func = rate_functions.rush_from
        )

        return
        
        for _ in range(1):
            self.play(a.animate.set_value(0.3))
            self.play(a.animate.set_value(0.1))
