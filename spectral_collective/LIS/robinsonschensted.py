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

        sortedtiles = [Mobject(), tiles[7], tiles[0], tiles[3], tiles[1], tiles[8], tiles[4], tiles[2], tiles[6], tiles[5]]

        self.play(
            sortedtiles[2].animate.shift(1.1*UP),
            sortedtiles[6].animate.shift(1.1*UP),
            sortedtiles[9].animate.shift(1.1*UP),
            sortedtiles[4].animate.shift(2.2*UP),
            sortedtiles[7].animate.shift(2.2*UP),
            FadeOut(row1text),
            FadeOut(row2text, shift=1.1*UP),
            FadeOut(row3text, shift=2.2*UP)
        )

        self.wait()

        yttext = Tex(
            r"Young Tableau",
            color=sol.BASE02,
            font_size=100
        ).shift(2.75*DOWN)

        self.play(Write(yttext))

        self.wait()

        llistext = Tex(
            r"""
            length of longest increasing \\
            subsequence of permutation
            """,
            color=sol.BASE02,
            font_size=50
        )

        lrowtext = Tex(
            r"""
            length of top row of \\
            resulting Young Tableau
            """,
            color=sol.BASE02,
            font_size=50
        )

        equals = MathTex(r"=", font_size=80, color=sol.BASE02)

        llistext.next_to(equals, LEFT)
        lrowtext.next_to(equals, RIGHT)

        Group(equals, llistext, lrowtext).move_to(2.75*UP)

        self.play(
            FadeIn(equals),
            FadeIn(llistext, shift=RIGHT),
            FadeIn(lrowtext, shift=LEFT),
            sortedtiles[1].submobjects[0].animate.set_fill(sol.RED, opacity=1),
            sortedtiles[3].submobjects[0].animate.set_fill(sol.RED, opacity=1),
            sortedtiles[5].submobjects[0].animate.set_fill(sol.RED, opacity=1),
            sortedtiles[8].submobjects[0].animate.set_fill(sol.RED, opacity=1)
        )

        self.wait()

        obfuscation1 = Rectangle(height=0.5, width=2.15, color=sol.BASE3).set_fill(sol.BASE3, opacity=1)
        obfuscation2 = Rectangle(height=0.5, width=2.65, color=sol.BASE3).set_fill(sol.BASE3, opacity=1)
        obfuscation1.align_to(llistext, UP+LEFT)
        obfuscation2.align_to(lrowtext, UP+LEFT)
        x = Cross(stroke_color=sol.RED).next_to(equals, ORIGIN).scale(0.4)

        self.play(
            LaggedStart(
                AnimationGroup(FadeIn(obfuscation1), FadeIn(obfuscation2)),
                FadeIn(x, scale=1.5),
                lag_ratio=0.25
             )
        )

        self.wait()

        self.play(
            FadeOut(obfuscation1),
            FadeOut(obfuscation2),
            FadeOut(x)
        )

        self.wait()

class EquivalenceProof(Scene):
    def construct(self):
        #TODO: give a proof that the lengths are equal
        pass