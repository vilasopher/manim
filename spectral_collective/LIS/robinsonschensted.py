from manim import *
from youngdiagrams import *

class RS(Scene):
    def construct(self):
        permutation = [2, 4, 7, 3, 6, 9, 8, 1, 5]

        tiles = [
            Tile(n).shift(3.25*UP + 5*LEFT + i*(1.25)*RIGHT)
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

        ABOVE1 = 2.05*UP + 1.5*LEFT
        ROW1 = UP + 1.5*LEFT
        ABOVE2 = 0.05*DOWN + 1.5*LEFT
        ROW2 = 1.1*DOWN + 1.5*LEFT
        ABOVE3 = 2.15*DOWN + 1.5*LEFT
        ROW3 = 3.2*DOWN + 1.5*LEFT

        row1text = Tex(r"Row 1 $\rightarrow$", color=sol.BASE02).move_to(ROW1+2*LEFT)
        row2text = Tex(r"Row 2 $\rightarrow$", color=sol.BASE02).move_to(ROW2+2*LEFT)
        row3text = Tex(r"Row 3 $\rightarrow$", color=sol.BASE02).move_to(ROW3+2*LEFT)

        self.wait()

        self.bring_to_front(tiles[0])
        self.play(tiles[0].animate.move_to(ROW1))
        self.bring_to_front(tiles[1])
        self.play(tiles[1].animate.move_to(ROW1+RIGHT))
        self.bring_to_front(tiles[2])
        self.play(tiles[2].animate.move_to(ROW1+2*RIGHT))
        self.bring_to_front(tiles[3])
        self.play(tiles[3].animate.move_to(ROW1+3*RIGHT))
        self.play(Wiggle(tiles[3]), Wiggle(tiles[2]))
        self.play(tiles[3].animate.move_to(ABOVE1+RIGHT))
        self.play(
            LaggedStart(
                tiles[3].animate.move_to(ROW1+RIGHT),
                tiles[1].animate.move_to(ABOVE2+RIGHT),
                lag_ratio=0.025
            )
        )
        self.play(
            tiles[1].animate.move_to(ROW2),
            FadeIn(row1text, row2text)
        )
        self.bring_to_front(tiles[4])
        self.play(tiles[4].animate.move_to(ABOVE1+2*RIGHT))
        self.play(
            LaggedStart(
                tiles[4].animate.move_to(ROW1+2*RIGHT),
                tiles[2].animate.move_to(ABOVE2+2*RIGHT),
                lag_ratio=0.025
            )
        )
        self.play(tiles[2].animate.move_to(ROW2+RIGHT))
        self.bring_to_front(tiles[5])
        self.play(tiles[5].animate.move_to(ROW1+3*RIGHT))
        self.bring_to_front(tiles[6])
        self.play(tiles[6].animate.move_to(ABOVE1+3*RIGHT))
        self.play(
            LaggedStart(
                tiles[6].animate.move_to(ROW1+3*RIGHT),
                tiles[5].animate.move_to(ABOVE2+3*RIGHT),
                lag_ratio=0.025
            )
        )
        self.play(tiles[5].animate.move_to(ROW2+2*RIGHT))
        self.bring_to_front(tiles[7])
        self.play(tiles[7].animate.move_to(ABOVE1))
        self.play(
            LaggedStart(
                tiles[7].animate.move_to(ROW1),
                tiles[0].animate.move_to(ABOVE2),
                lag_ratio=0.025
            )
        )
        self.play(
            LaggedStart(
                tiles[0].animate.move_to(ROW2),
                tiles[1].animate.move_to(ABOVE3),
                lag_ratio=0.025
            )
        )
        self.play(
            tiles[1].animate.move_to(ROW3),
            FadeIn(row3text)
        )
        self.bring_to_front(tiles[8])
        self.play(tiles[8].animate.move_to(ABOVE1+2*RIGHT))
        self.play(
            LaggedStart(
                tiles[8].animate.move_to(ROW1+2*RIGHT),
                tiles[4].animate.move_to(ABOVE2+2*RIGHT),
                lag_ratio=0.025
            )
        )
        self.play(tiles[4].animate.move_to(ABOVE2+RIGHT))
        self.play(
            LaggedStart(
                tiles[4].animate.move_to(ROW2+RIGHT),
                tiles[2].animate.move_to(ABOVE3+RIGHT),
                lag_ratio=0.025
            )
        )
        self.play(tiles[2].animate.move_to(ROW3+RIGHT))
        self.wait()
    
        return
        self.bring_to_front(tiles[0])
        self.play(tiles[0].animate.move_to(0.75*UP+0.5*RIGHT+2*LEFT))
        self.wait()
        self.bring_to_front(tiles[1])
        self.play(tiles[1].animate.move_to(0.75*UP+0.5*RIGHT+LEFT))
        self.wait()
        self.bring_to_front(tiles[2])
        self.play(tiles[2].animate.move_to(0.75*UP+0.5*RIGHT))
        self.wait()
        self.bring_to_front(tiles[3])
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
        self.bring_to_front(tiles[1])
        self.play(tiles[1].animate.move_to(0.5*DOWN+0.5*RIGHT+2*LEFT))
        self.wait()
        self.bring_to_front(tiles[4])
        self.play(tiles[4].animate.move_to(0.75*UP+0.5*RIGHT+1.1*UP))
        self.play(
            LaggedStart(
                tiles[4].animate.move_to(0.75*UP+0.5*RIGHT),
                tiles[2].animate.move_to(0.75*UP+0.5*RIGHT-1.1*UP)
            )
        )
        self.wait()
        self.bring_to_front(tiles[2])
        self.play(tiles[2].animate.move_to(0.5*DOWN+0.5*RIGHT+LEFT))
        self.wait()
        self.bring_to_front(tiles[5])
        self.play(tiles[5].animate.move_to(0.75*UP+0.5*RIGHT+2*LEFT+1.1*UP))
        self.play(
            LaggedStart(
                tiles[5].animate.move_to(0.75*UP+0.5*RIGHT+2*LEFT),
                tiles[0].animate.move_to(0.75*UP+0.5*RIGHT+2*LEFT-1.1*UP)
            )
        )
        self.wait()
        self.play(tiles[0].animate.move_to(0.5*DOWN+0.5*RIGHT+2*LEFT+1.1*UP))
        self.play(
            LaggedStart(
                tiles[0].animate.move_to(0.5*DOWN+0.5*RIGHT+2*LEFT),
                tiles[1].animate.move_to(0.5*DOWN+0.5*RIGHT+2*LEFT-1.1*UP)
            )
        )
        self.wait()