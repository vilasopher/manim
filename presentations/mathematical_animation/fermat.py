from manim import *

def colorfunction(t, freq = 0.1, **kwargs):
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
            - 5 * np.sqrt(a**2 + 1) * np.cos(t),
            5 * (np.sqrt(a**2 + 1) * np.sin(t) - a) - 2,
            0 
        ]
    else:
        return [
            - 5 * np.sqrt(a**2 + 1) * np.cos(t),
            - 5 * (np.sqrt(a**2 + 1) * np.sin(t) + a) - 2,
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

        p = Dot([-5, -2, 0], z_index = 1)
        q = Dot([5, -2, 0], z_index = 1)

        static_arc_nonstationary = ParametricFunction(
            lambda t : gamma(5, t),
            t_range = gamma_range(5),
            stroke_width = 5,
            stroke_color = GRAY,
            z_index = -1
        )

        static_arc_stationary = ParametricFunction(
            lambda t : [t, -2, 0],
            t_range = [-5, 5, 0.1],
            stroke_width = 5,
            stroke_color = GRAY,
            z_index = -1
        )
        
        bs = [ ValueTracker(-0.1), ValueTracker(4) ]
        
        moving_arcs = [
            colored_plot(
                lambda t : gamma(b[i].get_value(), t),
                t_range = gamma_range(b[i].get_value())
            )
            for i in range(2)
        ]

        for i in range(2):
            moving_arcs[i].add_updater(
                lambda s : s.become(
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
            moving_arcs[0],
            moving_arcs[1]
        )

        for _ in range(1):
            self.play(
                b[0].animate.set_value(0.1),
                b[1].animate.set_value(6)
            )
            self.play(
                b[0].animate.set_value(-0.1),
                b[1].animate.set_value(4)
            )
