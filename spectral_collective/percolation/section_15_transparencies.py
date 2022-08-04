from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import CriticalValueSlider, ValueSlider
import math

config.background_opacity = 0

lemma = MathTex(
    r'\textbf{Lemma: } {{ p_c }} < 1.',
    color = sol.BASE03
).set_color_by_tex(r'p_c', sol.BLUE).move_to(4.75 * LEFT + 3.25 * UP)

primal = MathTex(
    r'\text{Primal} {{ \text{ Grid} }}',
    color = sol.BASE03,
    font_size = 60
)

dual = MathTex(
    r'\text{Dual} {{ \text{ Grid} }}',
    color = sol.CYAN,
    font_size = 60
)

class Lemma(Scene):
    def construct(self):
        self.add(TranslucentBox(lemma), lemma)

class PrimalDualTex(Scene):
    def construct(self):
        self.play(Write(primal))
        self.wait(1)
        self.play(TransformMatchingTex(primal, dual))
        self.wait(10)

class PrimalDualBox(Scene):
    def construct(self):
        tbox = TranslucentBox(primal)
        self.add(tbox)

        self.wait()
        self.wait(1)
        self.play(Transform(tbox, TranslucentBox(dual)))
        self.wait(10)

class SliderMid(Scene):
    def construct(self):
        cvs = ValueSlider(0.5)
        self.add(cvs)

class SliderHi(Scene):
    def construct(self):
        cvs = ValueSlider(0.75)
        self.add(cvs)

class SliderLo(Scene):
    def construct(self):
        cvs = ValueSlider(0.25)
        self.add(cvs)

class SliderThird(Scene):
    def construct(self):
        cvs = ValueSlider(1/3)
        self.add(cvs)

class SliderMidToHi(Scene):
    def construct(self):
        p = ValueTracker(0.5)
        cvs = ValueSlider(p.get_value())
        cvs.add_updater(lambda s : s.set_p(p.get_value()))
        self.add(cvs)

        self.play(p.animate.set_value(0.75), run_time=0.5)

class SliderHiToLo(Scene):
    def construct(self):
        p = ValueTracker(0.75)
        cvs = ValueSlider(p.get_value())
        cvs.add_updater(lambda s : s.set_p(p.get_value()))
        self.add(cvs)

        self.play(p.animate.set_value(0.25), run_time=0.5)

class SliderLoToMid(Scene):
    def construct(self):
        p = ValueTracker(0.25)
        cvs = ValueSlider(p.get_value())
        cvs.add_updater(lambda s : s.set_p(p.get_value()))
        self.add(cvs)

        self.play(p.animate.set_value(0.5), run_time=0.5)

class SliderLoToThird(Scene):
    def construct(self):
        p = ValueTracker(0.25)
        cvs = ValueSlider(p.get_value())
        cvs.add_updater(lambda s : s.set_p(p.get_value()))
        self.add(cvs)

        self.play(p.animate.set_value(1/3), run_time=0.5)

class SliderThirdToMid(Scene):
    def construct(self):
        p = ValueTracker(1/3)
        cvs = ValueSlider(p.get_value())
        cvs.add_updater(lambda s : s.set_p(p.get_value()))
        self.add(cvs)

        self.play(p.animate.set_value(0.5), run_time=0.5)
