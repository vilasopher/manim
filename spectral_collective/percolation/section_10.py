from manim import *
import solarized as sol

class Rest(Scene):
    def construct(self):
        rest = Tex(
            r'The rest of this video:',
            color=sol.BASE03,
            font_size=80
        )
        proof = Tex(
            r'A mathematical proof that there \emph{is} a phase transition.',
            color=sol.BASE03
        ).next_to(rest, DOWN).align_to(rest, LEFT).shift(RIGHT + 0.1 * DOWN)

        preq = Tex(
            r'Prerequisites:',
            color=sol.BASE03,
            font_size=80
        ).next_to(proof, DOWN).align_to(rest, LEFT).shift(DOWN)
        prob = Tex(
            r'Basic probability theory and graph theory.',
            color=sol.BASE03
        ).next_to(preq, DOWN).align_to(preq, LEFT).shift(RIGHT)

        g = Group(rest, proof, preq, prob).move_to(ORIGIN)

        self.play(Write(rest))
        self.play(FadeIn(proof))
        self.wait(4)
        self.play(Write(preq))
        self.wait(0.5)
        self.play(FadeIn(prob))
        self.wait(10)
