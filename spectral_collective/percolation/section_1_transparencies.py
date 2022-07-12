from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import ValueSlider

config.background_opacity = 0

class TitleBox(Scene):
    def construct(self):
        perc = Tex(r'\textbf{percolation}', color=sol.BASE03, font_size=200)
        perc.shift(0.81 * LEFT)
        tbox = TranslucentBox(perc)
        self.add(tbox)

class TitleStill(Scene):
    def construct(self):
        perc = Tex(r'\textbf{percolation}', color=sol.BASE03, font_size=200)
        perc.shift(0.81 * LEFT)
        tbox = TranslucentBox(perc)
        self.add(tbox, perc)

class TitleWrite(Scene):
    def construct(self):
        perc = Tex(r'\textbf{percolation}', color=sol.BASE03, font_size=200)
        perc.shift(0.81 * LEFT)
        self.play(Write(perc))
