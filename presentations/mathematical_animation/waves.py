"""
        text2 = Tex(
            r'\textbf{Wave Theory of Light:} '
            r'light propagates as a wave.'
        )

        text3 = Tex(
            r'\textbf{Consequence 1:} '
            r'light travels along \emph{all} paths.'
        )

        text4 = Tex(
            r'\textbf{Consequence 2:} '
            r'these paths interfere with each other.'
        )
"""

from manim import *

def wave_function(t, u0, v0, u, v):
    r = np.sqrt((u-u0)**2 + (v-v0)**2)

    if r < t:
        return np.sin(r - t)
    else:
        return 0

class Waves(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(
            x_range = [-40, 40],
            y_range = [-40, 40],
            z_range = [-1, 1],
            x_length = 20,
            y_length = 20,
            z_length = 1
        )

        source1 = Dot3D([0,0,0.25], color=YELLOW)

        occlusion = Surface(
            lambda u, v : ax.c2p(u, v, 0.25),
            u_range = [-20, 20],
            v_range = [-20, 20],
            checkerboard_colors = [BLACK, BLACK]
        )

        surf = Surface(
            lambda u, v : ax.c2p(u, v, wave_function(0, 0, 0, u, v)),
            u_range = [-20, 20],
            v_range = [-20, 20],
            checkerboard_colors = [YELLOW, YELLOW]
        )

        t = ValueTracker(0)

        surf.add_updater(
            lambda s : s.become(
                Surface(
                    lambda u, v : ax.c2p(
                        u,
                        v,
                        wave_function(t.get_value(), 0, 0, u, v)),
                    u_range = [-40, 40],
                    v_range = [-40, 40],
                    checkerboard_colors = [YELLOW, YELLOW]
                )
            )
        )

        self.set_camera_orientation(theta = 0 * DEGREES, phi = 30 * DEGREES)
        self.begin_ambient_camera_rotation()

        self.add(occlusion, source, surf)

        self.wait(5)
        self.play(t.animate.set_value(100), run_time = 10, rate_func=linear)
        self.wait(3)

        source2 = Dot3D([4/2, 2.33666/2, 0.25], color=YELLOW)

        surf.clear_updaters()
        surf.add_updater(
            lambda s : s.become(
                Surface(
                    lambda u, v : ax.c2p(
                        u,
                        v,
                        wave_function(t.get_value(), 0, 0, u, v) +
                        wave_function(t.get_value() - 100, 4, 2.33666, u, v)
                    ),
                    u_range = [-40, 40],
                    v_range = [-40, 40],
                    checkerboard_colors = [YELLOW, YELLOW]
                )
            )
        )

        self.play(Create(source2))
        self.wait(3)
        self.play(t.animate.set_value(200), run_time = 10, rate_func=linear)
        self.wait(5)

