from manim import *
from youngdiagrams import *
import numpy.random as ra

class LimitShape(Scene):
    def construct(self):
        ra.seed(3)
        nums = ra.uniform(size=9)

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

        self.add(YoungDiagram(nums))

        self.wait()
        
        return

        o = 3*UP + 6.1111111*LEFT

        self.play(tiles[0].animate.move_to(o))
        self.play(tiles[1].animate.move_to(o+RIGHT))
        self.play(
            tiles[2].animate.move_to(o+RIGHT),
            tiles[1].animate.move_to(o+DOWN)
        )
        self.play(
            tiles[3].animate.move_to(o),
            tiles[0].animate.shift(DOWN),
            tiles[1].animate.shift(DOWN)
        )
        self.play(
            tiles[4].animate.move_to(o),
            tiles[3].animate.shift(DOWN),
            tiles[0].animate.shift(DOWN),
            tiles[1].animate.shift(DOWN)
        )
        self.play(tiles[5].animate.move_to(o+2*RIGHT))
        self.play(
            tiles[6].animate.move_to(o+RIGHT),
            tiles[2].animate.move_to(o+RIGHT+DOWN)
        )

        self.wait()