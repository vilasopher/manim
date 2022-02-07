from manim import *

def wave_function(t, f, u0, v0, u, v):
    r = f * np.sqrt((u-u0)**2 + (v-v0)**2)

    if r < t:
        return np.sin(r - t)
    else:
        return 0

def heat_map(f):
    img = ImageMobject(np.uint8([[
        f(u, v) * 127 + 128  for u in range(1920)
        ] for v in range(1080)]))
    img.height = 8
    img.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
    return img

class Waves(Scene):

    notifier = Dot(color=LIGHTER_GRAY, radius=0.05)
    notifier.move_to(7 * RIGHT + 3.9 * DOWN)

    def noticewait(self):
        self.add(self.notifier)
        self.wait()
        self.remove(self.notifier)

    def construct(self):
        hm = ImageMobject(np.uint8([[128 for u in range(1920)] for v in range(1080)]))

        self.add(hm)
        self.wait()
        self.noticewait()

        source1 = Dot([- 600 / 1080 * 8 , - 100 / 1080 * 8, 0], color=YELLOW, z_index=1)

        self.play(FadeIn(source1, scale=2))
        self.noticewait()

        t = ValueTracker(0)

        hm.add_updater(
            lambda s : s.become(
                heat_map(
                    lambda u, v : (1/3) * wave_function(
                        t.get_value(),
                        0.1,
                        1920 / 2 - 600,
                        1080 / 2 + 100,
                        u,
                        v
                    )
                )
            )
        )

        self.play(t.animate.set_value(50), run_time=10, rate_func=rate_functions.linear)
        self.noticewait()

        source2 = Dot(
            [- 200 / 1080 * 8, - 400 / 1080 * 8, 0],
            color=YELLOW,
            z_index=1
        )

        self.play(FadeIn(source2, scale=2))
        self.noticewait()

        hm.clear_updaters()
        hm.add_updater(
            lambda s : s.become(
                heat_map(
                    lambda u, v : (1/3) * wave_function(
                        t.get_value(),
                        0.1,
                        1920 / 2 - 600,
                        1080 / 2 + 100,
                        u,
                        v
                    ) + (1/3) * wave_function(
                        t.get_value() - 50,
                        0.1,
                        1920 / 2 - 200,
                        1080 / 2 + 400,
                        u,
                        v
                    )
                )
            )
        )

        self.play(t.animate.set_value(130), run_time=16, rate_func=rate_functions.linear)
        self.noticewait()

        source3 = Dot(
            [ 600 / 1080 * 8, 400 /1080 * 8, 0],
            color=YELLOW,
            z_index=1
        )

        self.play(FadeIn(source3, scale=2))
        self.noticewait()

        hm.clear_updaters()
        hm.add_updater(
            lambda s : s.become(
                heat_map(
                    lambda u, v : (1/3) * wave_function(
                        t.get_value(),
                        0.1,
                        1920 / 2 - 600,
                        1080 / 2 + 100,
                        u,
                        v
                    ) + (1/3) * wave_function(
                        t.get_value() - 50,
                        0.1,
                        1920 / 2 - 200,
                        1080 / 2 + 400,
                        u,
                        v
                    ) + (1/3) * wave_function(
                        t.get_value() - 130,
                        0.1,
                        1920 / 2 + 600,
                        1080 / 2 - 400,
                        u,
                        v
                    )
                )
            )
        )

        self.play(t.animate.set_value(250), run_time=24, rate_func=rate_functions.linear)
        self.noticewait()
        self.wait()
