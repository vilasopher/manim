from manim import *

def colorfunction(t, freq = 0.1, **kwargs):
    return interpolate_color(BLUE, RED, (1 + np.cos(freq * PI * t)) / 2)

def colored_plot(f, **kwargs):
    curve = ParametricFunction(f, **kwargs)
    pieces = CurvesAsSubmobjects(curve)

    colors = [
        colorfunction(t, **kwargs)
        for t in range(curve.get_num_curves())
    ]

    pieces.set_color_by_gradient(*colors)
    return pieces

def gamma(a, t):
    return [
        - 5 * np.sqrt(a**2 + 1) * np.cos(t),
        5 * (np.sqrt(a**2 + 1) * np.sin(t) - a) - 3,
        0 
    ]

def gamma_range(a, step = 0.005):
    return [ 
        np.arccos(1 / np.sqrt(a**2 + 1)),
        PI - np.arccos(1 / np.sqrt(a**2 + 1)),
        step
    ]

class Test(Scene):
    def construct(self):
        
        a = ValueTracker(0.1)
        
        arc = colored_plot(
            lambda t : gamma(a.get_value(), t),
            t_range = gamma_range(a.get_value()),
            stroke_width = 10
        )

        arc.add_updater(
            lambda s : s.become(
                colored_plot(
                    lambda t : gamma(a.get_value(), t),
                    t_range = gamma_range(a.get_value()),
                    stroke_width = 10
                )
            )
        )

        self.add(arc)
        
        for _ in range(3):
            self.play(a.animate.set_value(0.3))
            self.play(a.animate.set_value(0.1))
