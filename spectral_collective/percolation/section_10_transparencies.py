from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import ValueSlider

config.background_opacity = 0

class KestenQuote(Scene):
    def construct(self):
        k = ImageMobject("pics/kesten.png")
        tk = TranslucentBox(k)
        kb = Group(tk, k)

        quote = MathTex(
            r'``&\text{Quite apart from the fact that percolation} \\',
            r'  &\text{theory had its origin in an honest applied} \\',
            r'  &\text{problem, it is a source of fascinating} \\',
            r'  &\text{problems of the best kind a mathematician} \\',
            r'  &\text{can wish for: problems which are easy to} \\',
            r'  &\text{state with a minimum of preparation, but} \\',
            r'  &\text{whose solutions are (apparently) difficult} \\',
            r'  &\text{and require new methods.}"',
            color=sol.BASE03,
            font_size=36
        )
        cite = Tex(r'-Harry Kesten', color=sol.BASE03)
        cite.next_to(quote, DOWN).align_to(quote, RIGHT).shift(0.2 * UP)
        q = Group(quote, cite)
        tq = TranslucentBox(q)
        qb = Group(tq, q)

        qb.next_to(kb, RIGHT).shift(0.1 * RIGHT)

        a = Group(kb, qb)
        a.move_to(0.81 * LEFT + UP)

        self.add(a)
