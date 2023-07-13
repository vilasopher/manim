from manim import *
from youngdiagrams import *
import numpy.random as ra
import numpy as np
from functools import partial

class LimitShape(Scene):
    def construct(self):
        ra.seed(3)
        nums = list(ra.uniform(size=9))

        tiles = [
            Tile(n, font_size=30, num_decimal_places=3).shift((8+i)*1.1*RIGHT)
            for i, n in enumerate(nums)
        ]

        self.play(
            LaggedStart(
                *(
                    t.animate.shift(12*1.1*LEFT)
                    for t in tiles
                )
            )
        )

        self.wait()

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

        self.wait()

        ra.seed(2)

        nums += list(ra.uniform(size=5))
        tiles += [
            Tile(nums[i], font_size=30, num_decimal_places=3).shift(8*RIGHT)
            for i in range(9,14)
        ]

        self.play(tiles[9].animate.move_to(ORIGIN))

        self.wait()

        self.play(
            tiles[9].animate.move_to(o+2*RIGHT),
            tiles[4].animate.move_to(o+2*RIGHT+DOWN)
        )

        self.wait()

        self.play(tiles[10].animate.move_to(ORIGIN))
        
        self.wait()

        self.play(
            tiles[10].animate.move_to(o),
            tiles[8].animate.move_to(o+DOWN),
            tiles[6].animate.move_to(o+2*DOWN),
            tiles[2].animate.move_to(o+3*DOWN),
            tiles[0].animate.move_to(o+4*DOWN)
        )

        self.wait()

        self.play(tiles[11].animate.move_to(ORIGIN))

        self.wait()

        self.play(
            tiles[11].animate.move_to(o+3*RIGHT),
            tiles[5].animate.move_to(o+3*RIGHT+DOWN)
        )

        self.wait()

        self.play(
            tiles[12].animate.move_to(o+2*RIGHT),
            tiles[9].animate.move_to(o+RIGHT+DOWN),
            tiles[3].animate.move_to(o+RIGHT+2*DOWN),
            tiles[1].animate.move_to(o+RIGHT+3*DOWN)
        )
        
        self.wait()

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
            ob_opacity.animate.set_value(1)
        )

        self.wait()

        yd = YoungDiagram(nums, origin=o+0.5*(UP+LEFT))

        self.remove(*tiles)
        self.add(yd)

        self.remove(*obfuscations)

        self.wait()

        ra.seed(10)

        for _ in range(8):
            nums.append(ra.uniform())
            newd = YoungDiagram(nums, origin=o+0.5*(UP+LEFT)).set_z_index(-1)
            self.play(FadeIn(newd))
            self.remove(yd)
            yd = newd
            yd.set_z_index(1)

        self.play(
            yd.animate.scale(
                (7/2)/np.sqrt(len(nums)),
                about_point=3.5*UP+6.61111111*LEFT
            ),
            rate_func=rate_functions.rush_into,
            run_time=0.5
        )
        
        self.remove(yd, newd)

        self.time = 0

        self.growingd = YoungDiagram(nums, origin=o+0.5*(UP+LEFT))
        self.nums = nums

        def scene_updater(dt):
            self.time += dt

            for _ in range(
                    max(1, int(ra.choice(
                            [
                                np.floor(self.time/5),
                                np.ceil(self.time/5)
                            ],
                            p=[
                                1-self.time/5+np.floor(self.time/5),
                                self.time/5-np.floor(self.time/5)
                            ]
                    )))
                ):
                self.nums.append(ra.uniform())

            self.moving_mobjects.clear()
            self.foreground_mobjects.clear()
            self.mobjects.clear()
            self.clear()
            self.add(
                YoungDiagram(
                    nums,
                    unit=(7/2)/np.sqrt(len(self.nums)),
                    origin=o+0.5*(UP+LEFT)
                )
            )

        self.add_updater(scene_updater)
        
        self.wait(13.6)

        self.fadeinstarttime = self.time

        def scene_updater_fadein_limitshape(dt):
            self.time += dt

            for _ in range(
                    max(1, int(ra.choice(
                            [
                                np.floor(self.time/5),
                                np.ceil(self.time/5)
                            ],
                            p=[
                                1-self.time/5+np.floor(self.time/5),
                                self.time/5-np.floor(self.time/5)
                            ]
                    )))
                ):
                self.nums.append(ra.uniform())

            self.moving_mobjects.clear()
            self.foreground_mobjects.clear()
            self.mobjects.clear()
            self.clear()
            self.add(
                YoungDiagram(
                    nums,
                    unit=(7/2)/np.sqrt(len(self.nums)),
                    origin=o+0.5*(UP+LEFT)
                )
            )
            self.add(
                Square().shift(3*UP+2*LEFT).set_fill(sol.CYAN, opacity=min(1,self.time-self.fadeinstarttime))
            )

        self.moving_mobjects.clear()
        self.foreground_mobjects.clear()
        self.mobjects.clear()
        self.clear()
        self.remove_updater(scene_updater)
        self.add_updater(scene_updater_fadein_limitshape)
        
        self.wait(3)

        #TODO: figure out why this is starting over a bit...
        