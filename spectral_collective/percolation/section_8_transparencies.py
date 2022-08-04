from manim import *
import solarized as sol
from translucent_box import TranslucentBox

config.background_opacity = 0

class Note(Scene):
    def construct(self):
        n1 = Tex(
            r'\textbf{Note:} this is specific to the square lattice.',
            color = sol.BASE03,
            font_size = 30
        ).shift(3.4 * UP + 3.8 * RIGHT)
        n2 = Tex(
            r'For more information, see the description.',
            color = sol.BASE03,
            font_size = 30
        ).next_to(n1, DOWN).align_to(n1, RIGHT).shift(0.2 * UP)

        self.add(TranslucentBox(n1, n2, margin=0.15), n1, n2)
