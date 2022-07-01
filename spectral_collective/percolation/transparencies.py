from manim import *
import solarized as sol
from value_slider import ValueSlider, CriticalValueSlider
from translucent_box import TranslucentBox

config.background_opacity = 0

class TransparencyTest(Scene):
    def construct(self):
        slider = CriticalValueSlider(0.75)

        bg = Rectangle(width=11.5, height=7, color=sol.BASE2)
        bg.set_fill(sol.BASE3, opacity=0.95)
        bg.move_to(0.6111111 * LEFT)

        self.add(slider, bg)

        self.wait()
        self.play(slider.animate.add_crit())
        self.wait()

class Thumbnail(Scene):
    def construct(self):
        text = Tex(r'\textbf{percolation}', color=sol.BASE02, font_size=220)

        self.add(text)

class TheoremScene(Scene):
    def construct(self):
        temp = TexTemplate()
        temp.add_to_preamble(r'\usepackage{amsmath, amsfonts, xcolor}')
        temp.add_to_preamble(r'\raggedright')
        theorem = MathTex(
            r'&\textbf{Theorem:} \text{ there exists } {{p_c}} \in (0,1) \text{ such that} \\',
            r'&\,\, \text{for all } {{p}} < {{p_c}} \text{, } \mathbb{P}_{{p}}[\text{infinite cluster}] = 0 \text{, and} \\',
            r'&\,\, \text{for all } {{p}} > {{p_c}} \text{, } \mathbb{P}_{{p}}[\text{infinite cluster}] = 1.',
            color=sol.BASE03
            )
        theorem.set_color_by_tex(r'p', sol.RED)
        theorem.set_color_by_tex(r'p_c', sol.BLUE)

        tbox = TranslucentBox(theorem)

        self.add(tbox, theorem)
