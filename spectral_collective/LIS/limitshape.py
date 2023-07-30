from manim import *
from youngdiagrams import *
import numpy.random as ra
import numpy as np
from functools import partial

TLC = 3.5*UP + 6.6111111111111111111*LEFT
R = 3.5*RIGHT
D = 3.5*DOWN

def wx(t):
    return (2*t/np.pi + 1) * np.sin(t) + (2/np.pi) * np.cos(t)

def wy(t):
    return (2*t/np.pi - 1) * np.sin(t) + (2/np.pi) * np.cos(t)

LIMIT_SHAPE = Polygon(
    TLC,
    *(
        TLC + wx(t)*R + wy(t)*D
        for t in np.linspace(-np.pi/2, np.pi/2, 100)
    ),
    TLC,
    color = sol.CYAN,
    stroke_width = 1
).set_fill(sol.CYAN, opacity=0)

class LimitShape(Scene):
    def construct(self):
        ra.seed(3)
        nums = list(ra.uniform(size=9))

        tiles = [
            Tile(n, font_size=30, num_decimal_places=3).shift((8+i)*1.1*RIGHT)
            for i, n in enumerate(nums)
        ]

        # time = 15

        self.play(
            LaggedStart(
                *(
                    t.animate.shift(12*1.1*LEFT)
                    for t in tiles
                )
            ),
            run_time = 3
        )

        # time = 18

        self.wait(8)

        # time = 26

        o = 3*UP + 6.1111111*LEFT

        self.play(tiles[0].animate.move_to(o))
        self.play(tiles[1].animate.move_to(o+RIGHT))
        self.play(
            tiles[2].animate.move_to(o),
            tiles[0].animate.move_to(o+DOWN)
        )
        self.play(
            tiles[3].animate.move_to(o+RIGHT),
            tiles[1].animate.move_to(o+RIGHT+DOWN)
        )
        self.play(tiles[4].animate.move_to(o+2*RIGHT))
        self.play(tiles[5].animate.move_to(o+3*RIGHT))
        self.play(
            tiles[6].animate.move_to(o),
            tiles[2].animate.move_to(o+DOWN),
            tiles[0].animate.move_to(o+2*DOWN)
        )
        self.play(
            tiles[7].animate.move_to(o+RIGHT),
            tiles[3].animate.move_to(o+RIGHT+DOWN),
            tiles[1].animate.move_to(o+RIGHT+2*DOWN)
        )
        self.play(
            tiles[8].animate.move_to(o),
            tiles[6].animate.move_to(o+DOWN),
            tiles[2].animate.move_to(o+2*DOWN),
            tiles[0].animate.move_to(o+3*DOWN)
        )

        # time = 35

        self.wait(4.5)

        ra.seed(2)

        nums += list(ra.uniform(size=5))
        tiles += [
            Tile(nums[i], font_size=30, num_decimal_places=3).shift(8*RIGHT)
            for i in range(9,14)
        ]

        # time = 39:30

        self.play(tiles[9].animate.move_to(ORIGIN))

        # time = 40:30

        self.wait()

        # time = 41:30

        self.play(
            tiles[9].animate.move_to(o+2*RIGHT),
            tiles[4].animate.move_to(o+2*RIGHT+DOWN)
        )

        # time = 42:30

        self.wait(4.5)

        # time = 47

        self.play(tiles[10].animate.move_to(ORIGIN))

        # time = 48
        
        self.wait()

        # time = 49

        self.play(
            tiles[10].animate.move_to(o),
            tiles[8].animate.move_to(o+DOWN),
            tiles[6].animate.move_to(o+2*DOWN),
            tiles[2].animate.move_to(o+3*DOWN),
            tiles[0].animate.move_to(o+4*DOWN)
        )

        # time = 50

        self.wait(0.5)

        # time = 50:30

        self.play(tiles[11].animate.move_to(ORIGIN), run_time=0.5)

        # time = 51

        self.wait(0.5)

        # time = 51:30

        self.play(
            tiles[11].animate.move_to(o+3*RIGHT),
            tiles[5].animate.move_to(o+3*RIGHT+DOWN),
            run_time=0.5
        )

        # time = 52

        self.play(
            tiles[12].animate.move_to(o+2*RIGHT),
            tiles[9].animate.move_to(o+RIGHT+DOWN),
            tiles[3].animate.move_to(o+RIGHT+2*DOWN),
            tiles[1].animate.move_to(o+RIGHT+3*DOWN),
            run_time=0.5
        )

        # time = 52:30
        
        obfuscations = [
            Rectangle(
                height=0.5,
                width=0.75,
                color=sol.BASE1,
                z_index=1
            ).set_fill(
                sol.BASE1,
                opacity=1
            ).next_to(t, ORIGIN).set_opacity(0)
            for t in tiles
        ]

        self.add(*obfuscations)

        ob_opacity = ValueTracker(0)

        def ob_up(x, t, o):
            x.next_to(t, ORIGIN).set_opacity(o.get_value())

        for i in range(len(tiles)):
            obfuscations[i].add_updater(partial(ob_up, t=tiles[i], o=ob_opacity))

        movers = [1, 3, 9, 12, 13]

        for i in movers:
            tiles[i].set_z_index(2)
            obfuscations[i].set_z_index(3)

        self.play(
            tiles[13].animate.move_to(o+2*RIGHT),
            tiles[12].animate.move_to(o+RIGHT+DOWN),
            tiles[9].animate.move_to(o+RIGHT+2*DOWN),
            tiles[3].animate.move_to(o+RIGHT+3*DOWN),
            tiles[1].animate.move_to(o+RIGHT+4*DOWN),
            ob_opacity.animate.set_value(1),
            run_time = 0.5
        )

        # time = 53

        yd = YoungDiagram(nums, origin=o+0.5*(UP+LEFT))

        self.remove(*tiles)
        self.add(yd)

        self.remove(*obfuscations)

        ra.seed(10)

        for _ in range(8):
            nums.append(ra.uniform())
            newd = YoungDiagram(nums, origin=o+0.5*(UP+LEFT)).set_z_index(-1)
            self.play(FadeIn(newd), run_time=0.25)
            self.remove(yd)
            yd = newd
            yd.set_z_index(1)
        
        # time = 55

        self.wait(3)

        # time = 58

        self.play(
            yd.animate.scale(
                (7/2)/np.sqrt(len(nums)),
                about_point=3.5*UP+6.61111111*LEFT
            ),
            rate_func=rate_functions.rush_into,
            run_time=0.5
        )

        # time = 58:30
        
        self.remove(yd, newd)

        self.time = 0

        self.growingd = YoungDiagram(nums, origin=o+0.5*(UP+LEFT))
        self.nums = nums

        def scene_updater(dt):
            self.time += dt

            for _ in range(
                    min(4, max(1, int(ra.choice(
                                [
                                    np.floor(self.time/4),
                                    np.ceil(self.time/4)
                                ],
                                p=[
                                    1-self.time/4+np.floor(self.time/4),
                                    self.time/4-np.floor(self.time/4)
                                ]
                    ))))
                ):
                self.nums.append(ra.uniform())

            self.moving_mobjects.clear()
            self.foreground_mobjects.clear()
            self.mobjects.clear()
            self.clear()
            self.add(
                YoungDiagram(
                    self.nums,
                    unit=(7/2)/np.sqrt(len(self.nums)),
                    origin=o+0.5*(UP+LEFT)
                )
            )

        self.add_updater(scene_updater)
        
        self.wait(17)

        # time = 15:30

        self.fadeinstarttime = self.time

        def scene_updater_fadein_limitshape(dt):
            self.time += dt

            for _ in range(
                    min(4, max(1, int(ra.choice(
                            [
                                np.floor(self.time/4),
                                np.ceil(self.time/4)
                            ],
                            p=[
                                1-self.time/4+np.floor(self.time/4),
                                self.time/4-np.floor(self.time/4)
                            ]
                    ))))
                ):
                self.nums.append(ra.uniform())

            self.moving_mobjects.clear()
            self.foreground_mobjects.clear()
            self.mobjects.clear()
            self.clear()
            self.add(
                YoungDiagram(
                    self.nums,
                    unit=(7/2)/np.sqrt(len(self.nums)),
                    origin=o+0.5*(UP+LEFT)
                )
            )
            self.add(
                LIMIT_SHAPE.set_fill(sol.CYAN, opacity=0.2*min(1, self.time-self.fadeinstarttime))
            )

        self.moving_mobjects.clear()
        self.foreground_mobjects.clear()
        self.mobjects.clear()
        self.clear()
        self.remove_updater(scene_updater)
        self.add_updater(scene_updater_fadein_limitshape)
        
        self.wait(56)

        def scene_updater_toprow(dt):
            self.time += dt

            for _ in range(4):
                self.nums.append(ra.uniform())

            self.moving_mobjects.clear()
            self.foreground_mobjects.clear()
            self.mobjects.clear()
            self.clear()
            self.add(
                YoungDiagram(
                    self.nums,
                    unit=(7/2)/np.sqrt(len(self.nums)),
                    origin=o+0.5*(UP+LEFT),
                    first_row_highlighted=True
                )
            )
            self.add(
                LIMIT_SHAPE.set_fill(sol.CYAN, opacity=0.2)
            )

        self.moving_mobjects.clear()
        self.foreground_mobjects.clear()
        self.mobjects.clear()
        self.clear()
        self.remove_updater(scene_updater_fadein_limitshape)
        self.add_updater(scene_updater_toprow)

        self.wait(74)