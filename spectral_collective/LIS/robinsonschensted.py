from manim import *
from youngdiagrams import *

class RS(Scene):
    def construct(self):
        permutation = [2, 4, 9, 3, 6, 1, 8, 7, 5]

        tiles = [
            Tile(n).shift(3*UP + 5*LEFT + i*(1.25)*RIGHT)
            for i, n in enumerate(permutation)
        ]

        self.play(
            LaggedStart(
                *(
                    FadeIn(t, shift=0.5*DOWN)
                    for t in tiles
                ),
                lag_ratio=0.2
            )
        )

        self.wait()

        self.play(tiles[0].animate.move_to(0.75*UP+0.5*RIGHT+2*LEFT))
        self.wait()
        self.play(tiles[1].animate.move_to(0.75*UP+0.5*RIGHT+LEFT))
        self.wait()
        self.play(tiles[2].animate.move_to(0.75*UP+0.5*RIGHT))
        self.wait()
        self.play(tiles[3].animate.move_to(0.75*UP+0.5*RIGHT+RIGHT))
        self.play(Wiggle(tiles[2]),Wiggle(tiles[3]))
        self.wait()
        self.play(tiles[3].animate.move_to(0.75*UP+0.5*RIGHT+LEFT+1.1*UP))
        self.wait()
        self.play(
            LaggedStart(
                tiles[3].animate.move_to(0.75*UP+0.5*RIGHT+LEFT),
                tiles[1].animate.move_to(0.75*UP+0.5*RIGHT+LEFT-1.1*UP)
            )
        )
        self.wait()
        self.play(tiles[1].animate.move_to(0.5*DOWN+0.5*RIGHT+2*LEFT))
        self.wait()
        self.play(tiles[4].animate.move_to(0.75*UP+0.5*RIGHT+1.1*UP))
        self.play(
            LaggedStart(
                tiles[4].animate.move_to(0.75*UP+0.5*RIGHT),
                tiles[2].animate.move_to(0.75*UP+0.5*RIGHT-1.1*UP)
            )
        )
        self.wait()
        self.play(tiles[2].animate.move_to(0.5*DOWN+0.5*RIGHT+LEFT))
        self.wait()
        self.play(tiles[5].animate.move_to(0.75*UP+0.5*RIGHT+2*LEFT+1.1*UP))
        self.play(
            LaggedStart(
                tiles[5].animate.move_to(0.75*UP+0.5*RIGHT+2*LEFT),
                tiles[0].animate.move_to(0.75*UP+0.5*RIGHT+2*LEFT-1.1*UP)
            )
        )
        self.wait()