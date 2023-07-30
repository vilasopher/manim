from manim import *
from youngdiagrams import *

class TitleCard(Scene):
    def construct(self):
        text = Tex(
            r"""
                Proof Idea
            """,
            color = sol.BASE02,
            font_size = 100
        ).set_color_by_tex(r"L", sol.RED).set_color_by_tex(r")", sol.RED)
        heur = Tex(
            r"""
            (via the Robinson-Schensted algorithm)
            """,
            color = sol.BASE02,
            font_size = 60
        ).next_to(text, DOWN)

        self.play(FadeIn(text, shift=DOWN))
        self.wait(0.5)
        self.play(FadeIn(heur))
        self.wait(10)

class RS(Scene):
    def construct(self):
        permutation = [2, 4, 7, 3, 6, 9, 8, 1, 5]

        tiles = [
            Tile(n).shift(3.25*UP + 5*LEFT + i*(1.25)*RIGHT)
            for i, n in enumerate(permutation)
        ]

        # time = 35

        self.play(
            LaggedStart(
                *(
                    FadeIn(t, shift=0.5*DOWN)
                    for t in tiles
                ),
                lag_ratio=0.2
            ),
            run_time=2
        )

        # time = 37

        ABOVE1 = 2.05*UP + 1.5*LEFT
        ROW1 = UP + 1.5*LEFT
        ABOVE2 = 0.05*DOWN + 1.5*LEFT
        ROW2 = 1.1*DOWN + 1.5*LEFT
        ABOVE3 = 2.15*DOWN + 1.5*LEFT
        ROW3 = 3.2*DOWN + 1.5*LEFT

        row1text = Tex(r"Row 1 $\rightarrow$", color=sol.BASE02).move_to(ROW1+2*LEFT)
        row2text = Tex(r"Row 2 $\rightarrow$", color=sol.BASE02).move_to(ROW2+2*LEFT)
        row3text = Tex(r"Row 3 $\rightarrow$", color=sol.BASE02).move_to(ROW3+2*LEFT)

        self.wait(4)

        # time = 41

        self.bring_to_front(tiles[0])
        self.play(tiles[0].animate.move_to(ROW1))

        # time = 42

        self.wait(4)

        # time = 46

        self.bring_to_front(tiles[1])
        self.play(tiles[1].animate.move_to(ROW1+RIGHT))

        # time = 47

        self.wait(4)

        # time = 51

        self.bring_to_front(tiles[2])
        self.play(tiles[2].animate.move_to(ROW1+2*RIGHT))

        # time = 52

        self.wait(3.5)

        # time = 55:30

        self.bring_to_front(tiles[3])
        self.play(tiles[3].animate.move_to(ROW1+3*RIGHT))

        # time = 56:30

        self.play(Wiggle(tiles[3]), Wiggle(tiles[2]), run_time=1)

        # time = 57:30

        self.wait(1.5)

        # time = 59

        self.play(tiles[3].animate.move_to(ABOVE1+RIGHT))

        self.wait()

        # time = 1

        self.play(
            LaggedStart(
                tiles[3].animate.move_to(ROW1+RIGHT),
                tiles[1].animate.move_to(ABOVE2+RIGHT),
                lag_ratio=0.025
            ),
            run_time = 1
        )

        # time = 2

        self.play(
            tiles[1].animate.move_to(ROW2),
            FadeIn(row1text, row2text),
            run_time=1
        )

        self.wait(2)

        # time = 5

        self.bring_to_front(tiles[4])
        self.play(tiles[4].animate.move_to(ABOVE1+2*RIGHT), run_time=1)

        # time = 6

        self.play(
            LaggedStart(
                tiles[4].animate.move_to(ROW1+2*RIGHT),
                tiles[2].animate.move_to(ABOVE2+2*RIGHT),
                lag_ratio=0.025
            ),
            run_time=1
        )

        # time = 7

        self.play(tiles[2].animate.move_to(ROW2+RIGHT), run_time=1)

        # time = 8

        self.bring_to_front(tiles[5])
        self.play(tiles[5].animate.move_to(ROW1+3*RIGHT), run_time=0.75)

        self.bring_to_front(tiles[6])
        self.play(tiles[6].animate.move_to(ABOVE1+3*RIGHT), run_time=0.75)

        self.play(
            LaggedStart(
                tiles[6].animate.move_to(ROW1+3*RIGHT),
                tiles[5].animate.move_to(ABOVE2+3*RIGHT),
                lag_ratio=0.025
            ),
            run_time=0.75
        )

        self.play(tiles[5].animate.move_to(ROW2+2*RIGHT), run_time=0.75)

        # time = 11

        self.bring_to_front(tiles[7])
        self.play(tiles[7].animate.move_to(ABOVE1), run_time=2/3)

        self.play(
            LaggedStart(
                tiles[7].animate.move_to(ROW1),
                tiles[0].animate.move_to(ABOVE2),
                lag_ratio=0.025
            ),
            run_time=2/3
        )

        self.play(
            LaggedStart(
                tiles[0].animate.move_to(ROW2),
                tiles[1].animate.move_to(ABOVE3),
                lag_ratio=0.025
            ),
            run_time=2/3
        )

        self.play(
            tiles[1].animate.move_to(ROW3),
            FadeIn(row3text),
            run_time=2/3
        )

        self.bring_to_front(tiles[8])
        self.play(tiles[8].animate.move_to(ABOVE1+2*RIGHT), run_time=2/3)

        self.play(
            LaggedStart(
                tiles[8].animate.move_to(ROW1+2*RIGHT),
                tiles[4].animate.move_to(ABOVE2+2*RIGHT),
                lag_ratio=0.025
            ),
            run_time=0.5
        )

        self.play(tiles[4].animate.move_to(ABOVE2+RIGHT), run_time=0.5)

        self.play(
            LaggedStart(
                tiles[4].animate.move_to(ROW2+RIGHT),
                tiles[2].animate.move_to(ABOVE3+RIGHT),
                lag_ratio=0.025
            ),
            run_time=0.5
        )

        self.play(tiles[2].animate.move_to(ROW3+RIGHT), run_time=0.5)

        sortedtiles = [Mobject(), tiles[7], tiles[0], tiles[3], tiles[1], tiles[8], tiles[4], tiles[2], tiles[6], tiles[5]]

        self.wait(2/3)

        # time = 17

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

        # time = 18

        self.wait()

        # time = 19

        self.play(
            ShowPassingFlash(
                Arrow(start=ROW1 + UP+0.5*LEFT, end=ROW1 + UP+0.5*LEFT + 4*RIGHT, color=sol.BASE02),
                time_width=3
            ),
            ShowPassingFlash(
                Arrow(start=ROW1 + LEFT+0.5*UP, end=ROW1 + LEFT+0.5*UP + 3*DOWN, color=sol.BASE02),
                time_width=3
            ),
            run_time=3
        )

        # time = 22

        self.wait(0.5)

        yttext = Tex(
            r"Young Tableau",
            color=sol.BASE02,
            font_size=100
        ).shift(2.75*DOWN)

        # time = 22:30

        self.play(Write(yttext), run_time=2)

        # time = 24:30

        self.wait(3)

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
            length of first row of \\
            resulting Young Tableau
            """,
            color=sol.BASE02,
            font_size=50
        )

        equals = MathTex(r"=", font_size=80, color=sol.BASE02)

        llistext.next_to(equals, LEFT)
        lrowtext.next_to(equals, RIGHT)

        Group(equals, llistext, lrowtext).move_to(2.75*UP)

        # time = 27:30

        self.play(
            FadeIn(equals),
            FadeIn(llistext, shift=RIGHT),
            FadeIn(lrowtext, shift=LEFT),
            sortedtiles[1].submobjects[0].animate.set_fill(sol.RED, opacity=1),
            sortedtiles[3].submobjects[0].animate.set_fill(sol.RED, opacity=1),
            sortedtiles[5].submobjects[0].animate.set_fill(sol.RED, opacity=1),
            sortedtiles[8].submobjects[0].animate.set_fill(sol.RED, opacity=1)
        )

        # time = 28:30

        self.wait(7.75)

        obfuscation1 = Rectangle(height=0.5, width=2.15, color=sol.BASE3).set_fill(sol.BASE3, opacity=1)
        obfuscation2 = Rectangle(height=0.5, width=2.65, color=sol.BASE3).set_fill(sol.BASE3, opacity=1)
        obfuscation1.align_to(llistext, UP+LEFT)
        obfuscation2.align_to(lrowtext, UP+LEFT).shift(0.1*LEFT)
        x = Cross(stroke_color=sol.RED).next_to(equals, ORIGIN).scale(0.4)

        # time = 36:15

        self.play(
            LaggedStart(
                AnimationGroup(FadeIn(obfuscation1), FadeIn(obfuscation2)),
                FadeIn(x, scale=1.5),
                lag_ratio=0.25
            ),
            run_time=1
        )

        # time = 37:15

        self.wait(6.25)

        # time = 43:30

        self.play(
            FadeOut(obfuscation1),
            FadeOut(obfuscation2),
            FadeOut(x)
        )

        self.wait(10)

class EquivalenceProof(Scene):
    def construct(self):
        permutation = [2, 4, 7, 3, 6, 9, 8, 1, 5]

        tiles = [
            Tile(n).shift(3.25*UP + 5*LEFT + i*(1.25)*RIGHT)
            for i, n in enumerate(permutation)
        ]


        tiles[0].submobjects[0].set_fill(sol.RED, opacity=1)
        tiles[2].submobjects[0].set_fill(sol.RED, opacity=1)
        tiles[6].submobjects[0].set_fill(sol.RED, opacity=1)

        # time = 48:30

        self.play(
            LaggedStart(
                *(
                    FadeIn(t, shift=0.5*DOWN)
                    for t in tiles
                ),
                lag_ratio=0.2
            ),
            run_time=2
        )

        # time = 50:30

        ABOVE1 = 2.05*UP + 1.5*LEFT
        ROW1 = UP + 1.5*LEFT
        ABOVE2 = 0.05*DOWN + 1.5*LEFT
        ROW2 = 1.1*DOWN + 1.5*LEFT
        ABOVE3 = 2.15*DOWN + 1.5*LEFT
        ROW3 = 3.2*DOWN + 1.5*LEFT

        row1text = Tex(r"Row 1 $\rightarrow$", color=sol.BASE02).move_to(ROW1+2*LEFT)
        row2text = Tex(r"Row 2 $\rightarrow$", color=sol.BASE02).move_to(ROW2+2*LEFT)
        row3text = Tex(r"Row 3 $\rightarrow$", color=sol.BASE02).move_to(ROW3+2*LEFT)

        self.wait(1.5)

        # time = 52

        self.bring_to_front(tiles[0])
        self.play(tiles[0].animate.move_to(ROW1))

        # time = 53

        self.wait(0.5)

        # time = 53:30

        self.bring_to_front(tiles[1])
        self.play(tiles[1].animate.move_to(ROW1+RIGHT))

        # time = 54:30

        self.wait(0.5)

        # time = 55

        self.bring_to_front(tiles[2])
        self.play(tiles[2].animate.move_to(ROW1+2*RIGHT))

        # time = 56

        self.wait(6)

        # time = 2

        self.bring_to_front(tiles[3])
        self.play(tiles[3].animate.move_to(ABOVE1+RIGHT), run_time=0.5)

        # time = 2:30

        self.play(
            LaggedStart(
                tiles[3].animate.move_to(ROW1+RIGHT),
                tiles[1].animate.move_to(ABOVE2+RIGHT),
                lag_ratio=0.025
            ),
            run_time=0.5
        )

        # time = 3

        self.play(
            tiles[1].animate.move_to(ROW2),
            FadeIn(row1text, row2text),
            run_time=0.5
        )

        # time = 3:30

        self.bring_to_front(tiles[4])
        self.play(tiles[4].animate.move_to(ABOVE1+2*RIGHT), run_time=0.5)

        # time = 4

        self.play(
            LaggedStart(
                tiles[4].animate.move_to(ROW1+2*RIGHT),
                tiles[2].animate.move_to(ABOVE2+2*RIGHT),
                lag_ratio=0.025
            ),
            run_time=0.5
        )

        # time = 4:30

        self.play(tiles[2].animate.move_to(ROW2+RIGHT), run_time=0.5)

        # time = 5

        self.bring_to_front(tiles[5])
        self.play(tiles[5].animate.move_to(ROW1+3*RIGHT), run_time=0.5)

        # time = 5:30

        self.bring_to_front(tiles[6])
        self.play(tiles[6].animate.move_to(ABOVE1+3*RIGHT), run_time=0.5)

        # time = 6

        self.play(
            LaggedStart(
                tiles[6].animate.move_to(ROW1+3*RIGHT),
                tiles[5].animate.move_to(ABOVE2+3*RIGHT),
                lag_ratio=0.025
            ),
            run_time=1
        )

        # time = 7

        self.wait()

        # time = 8

        self.play(tiles[5].animate.move_to(ROW2+2*RIGHT), run_time=0.5)

        self.bring_to_front(tiles[7])
        self.play(tiles[7].animate.move_to(ABOVE1), run_time=0.5)

        self.play(
            LaggedStart(
                tiles[7].animate.move_to(ROW1),
                tiles[0].animate.move_to(ABOVE2),
                lag_ratio=0.025
            ),
            run_time=0.5
        )

        self.play(
            LaggedStart(
                tiles[0].animate.move_to(ROW2),
                tiles[1].animate.move_to(ABOVE3),
                lag_ratio=0.025
            ),
            run_time=0.5
        )

        self.play(
            tiles[1].animate.move_to(ROW3),
            FadeIn(row3text),
            run_time=0.5
        )

        self.bring_to_front(tiles[8])
        self.play(tiles[8].animate.move_to(ABOVE1+2*RIGHT), run_time=0.5)

        self.play(
            LaggedStart(
                tiles[8].animate.move_to(ROW1+2*RIGHT),
                tiles[4].animate.move_to(ABOVE2+2*RIGHT),
                lag_ratio=0.025
            ),
            run_time=0.5
        )

        self.play(tiles[4].animate.move_to(ABOVE2+RIGHT), run_time=0.5)

        self.play(
            LaggedStart(
                tiles[4].animate.move_to(ROW2+RIGHT),
                tiles[2].animate.move_to(ABOVE3+RIGHT),
                lag_ratio=0.025
            ),
            run_time=0.5
        )

        self.play(tiles[2].animate.move_to(ROW3+RIGHT), run_time=0.5)

        sortedtiles = [Mobject(), tiles[7], tiles[0], tiles[3], tiles[1], tiles[8], tiles[4], tiles[2], tiles[6], tiles[5]]

        conclusion1 = MathTex(
            r"""
                {{ \text{length of top row} }}
                {{ \geq }}
                {{ \text{length of} }}
                {{ \text{ \emph{any} } }}
                {{ \text{increasing subsequence} }}
            """,
            color=sol.BASE02,
            font_size=50
        ).shift(2.75*DOWN)

        # time = 13

        self.play(
            sortedtiles[2].animate.shift(1.1*UP),
            sortedtiles[6].animate.shift(1.1*UP),
            sortedtiles[9].animate.shift(1.1*UP),
            sortedtiles[4].animate.shift(2.2*UP),
            sortedtiles[7].animate.shift(2.2*UP),
            FadeOut(row1text),
            FadeOut(row2text, shift=1.1*UP),
            FadeOut(row3text, shift=2.2*UP),
            FadeIn(conclusion1, shift=2.5*UP)
        )

        self.wait(5.5)

        # time = 18:30

        self.play(
            tiles[0].submobjects[0].animate.set_fill(sol.BASE1, opacity=1),
            tiles[2].submobjects[0].animate.set_fill(sol.BASE1, opacity=1),
            tiles[6].submobjects[0].animate.set_fill(sol.BASE1, opacity=1)
        )

        # time = 19:30

        self.play(
            sortedtiles[2].animate.shift(1.1*DOWN),
            sortedtiles[6].animate.shift(1.1*DOWN),
            sortedtiles[9].animate.shift(1.1*DOWN),
            sortedtiles[4].animate.shift(2.2*DOWN),
            sortedtiles[7].animate.shift(2.2*DOWN),
            FadeIn(row1text),
            FadeIn(row2text, shift=1.1*DOWN),
            FadeIn(row3text, shift=2.2*DOWN),
            FadeOut(conclusion1, shift=2.5*DOWN)
        )

        # time = 20:30

        faketiles = [
            Tile(n).shift(3.25*UP + 5*LEFT + i*(1.25)*RIGHT)
            for i, n in enumerate(permutation)
        ]

        self.wait(4.5)

        # time = 26

        self.play(sortedtiles[8].submobjects[0].animate.set_fill(sol.RED, opacity=1))

        self.wait(0.75)

        # time = 27:45

        self.play(tiles[2].animate.move_to(ABOVE3+RIGHT), run_time=0.25)

        self.play(
            LaggedStart(
                tiles[2].animate.move_to(ROW2+RIGHT),
                tiles[4].animate.move_to(ABOVE2+RIGHT),
                lag_ratio=0.025
            ),
            run_time=0.25
        )

        self.play(tiles[4].animate.move_to(ABOVE2+2*RIGHT), run_time=0.25)

        self.play(
            LaggedStart(
                tiles[4].animate.move_to(ROW1+2*RIGHT),
                tiles[8].animate.move_to(ABOVE1+2*RIGHT),
                lag_ratio=0.025
            ),
            run_time=0.25
        )

        self.bring_to_front(tiles[8])
        self.play(tiles[8].animate.next_to(faketiles[8], ORIGIN), run_time=0.25)

        self.play(
            tiles[1].animate.move_to(ABOVE3),
            FadeOut(row3text),
            run_time=0.25
        )
        
        self.play(
            LaggedStart(
                tiles[1].animate.move_to(ROW2),
                tiles[0].animate.move_to(ABOVE2),
                lag_ratio=0.025
            ),
            run_time=0.25
        )

        self.play(
            LaggedStart(
                tiles[0].animate.move_to(ROW1),
                tiles[7].animate.move_to(ABOVE1),
                lag_ratio=0.025
            ),
            run_time=0.25
        )

        self.bring_to_front(tiles[7])
        self.play(tiles[7].animate.next_to(faketiles[7], ORIGIN), run_time=0.25)

        # time = 29:30

        self.play(tiles[5].animate.move_to(ABOVE2+3*RIGHT), run_time=0.25)

        self.wait()

        # time = 31:30

        self.play(
            LaggedStart(
                tiles[5].animate.move_to(ROW1+3*RIGHT),
                tiles[6].animate.move_to(ABOVE1+3*RIGHT),
                lag_ratio=0.025
            ),
            sortedtiles[6].submobjects[0].animate.set_fill(sol.RED, opacity=1),
            run_time=1
        )

        # time = 32:30

        self.wait()

        # time = 33:30

        self.bring_to_front(tiles[6])
        self.play(tiles[6].animate.next_to(faketiles[6], ORIGIN), run_time=0.25)

        self.bring_to_front(tiles[5])
        self.play(tiles[5].animate.move_to(faketiles[5], ORIGIN), run_time=0.25)

        self.play(tiles[2].animate.move_to(ABOVE2+2*RIGHT), run_time=0.25)

        self.play(
            LaggedStart(
                tiles[2].animate.move_to(ROW1+2*RIGHT),
                tiles[4].animate.move_to(ABOVE1+2*RIGHT),
                lag_ratio=0.025
            ),
            sortedtiles[3].submobjects[0].animate.set_fill(sol.RED, opacity=1),
            run_time=0.5
        )

        self.wait(0.5)

        self.bring_to_front(tiles[4])
        self.play(tiles[4].animate.next_to(faketiles[4], ORIGIN), run_time=0.25)

        self.play(
            tiles[1].animate.move_to(ABOVE2+RIGHT),
            FadeOut(row2text),
            run_time=0.25
        )

        self.play(
            LaggedStart(
                tiles[1].animate.move_to(ROW1+RIGHT),
                tiles[3].animate.move_to(ABOVE1+RIGHT),
                lag_ratio=0.025
            ),
            sortedtiles[2].submobjects[0].animate.set_fill(sol.RED, opacity=1),
            run_time=0.5
        )

        self.wait(0.5)

        self.bring_to_front(tiles[3])
        self.play(tiles[3].animate.next_to(faketiles[3], ORIGIN), run_time=0.25)

        self.bring_to_front(tiles[2])
        self.play(tiles[2].animate.next_to(faketiles[2], ORIGIN), run_time=0.25)

        self.bring_to_front(tiles[1])
        self.play(tiles[1].animate.next_to(faketiles[1], ORIGIN), run_time=0.25)

        self.bring_to_front(tiles[0])
        self.play(
            tiles[0].animate.next_to(faketiles[0], ORIGIN),
            FadeOut(row1text),
            run_time=0.25
        )

        self.wait(0.75)

        conclusion2 = MathTex(
            r"""
                {{ \text{length of top row} }}
                {{ = }}
                {{ \text{length of} }}
                {{ \text{ \emph{some} } }}
                {{ \text{increasing subsequence} }}
            """,
            color=sol.BASE02,
            font_size=50
        ).shift(1.5*UP)

        # time = 38:30

        self.play(FadeIn(conclusion2))

        # time = 39:30

        self.wait(1.5)

        # time = 41

        self.play(FadeIn(conclusion1))

        self.wait()

        conclusion3a = MathTex(
            r"""
                {{ \text{length of top row} }}
            """,
            color=sol.BASE02,
            font_size=70
        )
        conclusion3b = MathTex(
             r"""{{ = }}""",
             color=sol.BASE02,
             font_size=100
        )
        conclusion3c = MathTex(
            r"""
                {{ \text{length of} }} 
                {{ \text{ \emph{longest} } }}
                {{ \text{increasing subsequence} }}
            """,
            color=sol.BASE02,
            font_size=70
        )

        conclusion3b.shift((1.5-2.75)/2*UP)
        conclusion3a.next_to(conclusion3b, 1.5*UP)
        conclusion3c.next_to(conclusion3b, 1.5*DOWN)

        faketext1 = MathTex(
            r"""{{ \geq }}""",
            color=sol.BASE3,
            font_size=70
        ).next_to(conclusion3b, ORIGIN).shift(2*LEFT+0.75*DOWN).set_z_index(-1)
        faketext2 = MathTex(
            r"""
            {{ \text{ \emph{any} } }}
            """,
            color=sol.BASE3,
            font_size=70
        ).next_to(conclusion3c, ORIGIN).shift(2*LEFT).set_z_index(-1)
        faketext3 = MathTex(
            r"""
            {{ \text{ \emph{some} } }}
            """,
            color=sol.BASE3,
            font_size=70
        ).next_to(conclusion3c, ORIGIN).shift(2*LEFT).set_z_index(-1)

        self.play(
            TransformMatchingTex(
                Group(conclusion1, conclusion2), 
                Group(conclusion3a, conclusion3b, conclusion3c,
                      faketext1, faketext2, faketext3)
            )
        )

        self.wait(20)

class RecordingTableau(Scene):
    def construct(self):
        #TODO: explain the recording tableau
        #TODO: discuss the plancherel measure and the mapping
        pass