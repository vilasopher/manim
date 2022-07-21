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

def interp(alpha):
    return np.sqrt((1 - np.cos(2 * np.pi * alpha)) / 2)

def almost_linear(alpha):
    return interp(alpha) * alpha + (1 - interp(alpha)) * (1 - np.cos(np.pi * alpha)) / 2

class ForegroundAbstract(Scene):
    def abstract_construct(self, start, end):
        p = ValueTracker(start)

        slider = ValueSlider(z_index = 2)
        self.add(slider)

        slider.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.play(
            p.animate.set_value(end),
            rate_func = almost_linear,
            run_time = 10
        )

class Foreground0(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(0, 1)

class Foreground1(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(0, 1)

class Foreground2(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(0, 3/4)

class Foreground3(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(3/4, 1/4)

class Foreground4(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(1/4, 5/8)

class Foreground5(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(5/8, 3/8)

class Foreground6(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(3/8, 9/16)

class Foreground7(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(9/16, 7/16)
