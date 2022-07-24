from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import ValueSlider, CriticalValueSlider

config.background_opacity = 0

def interp(alpha):
    return np.sqrt((1 - np.cos(2 * np.pi * alpha)) / 2)

def almost_linear(alpha):
    return interp(alpha) * alpha + (1 - interp(alpha)) * (1 - np.cos(np.pi * alpha)) / 2

class FadeInCrit(Scene):
    def construct(self):
        cvs = CriticalValueSlider(0.5)
        self.add(cvs)
        self.play(cvs.animate.add_crit())

class SliderAbstract(Scene):
    def construct_abstract(self, start, end, crit=False, time=10):
        p = ValueTracker(start)
        cvs = CriticalValueSlider(p.get_value())
        
        if crit:
            cvs.add_crit()

        cvs.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.add(cvs)

        self.play(
            p.animate.set_value(1),
            run_time=time,
            rate_func=almost_linear
        )

class SliderFullForwards(SliderAbstract):
    def construct(self):
        self.construct_abstract(0, 1)

class SliderFullBackwards(SliderAbstract):
    def construct(self):
        self.construct_abstract(1, 0)

class SliderZeroToHalf(SliderAbstract):
    def construct(self):
        self.construct_abstract(0, 1/2, time=5)

class SliderHalfToZero(SliderAbstract):
    def construct(self):
        self.construct_abstract(1/2, 0, time=5)

class SliderHalfToOne(SliderAbstract):
    def construct(self):
        self.construct_abstract(1/2, 1, time=5)

class SliderToOneToHalf(SliderAbstract):
    def construct(self):
        self.construct_abstract(1, 1/2, time=5)

class CritFullForwards(SliderAbstract):
    def construct(self):
        self.construct_abstract(0, 1, crit=True)

class CritFullBackwards(SliderAbstract):
    def construct(self):
        self.construct_abstract(1, 0, crit=True)

class CritZeroToHalf(SliderAbstract):
    def construct(self):
        self.construct_abstract(0, 1/2, time=5, crit=True)

class CritHalfToZero(SliderAbstract):
    def construct(self):
        self.construct_abstract(1/2, 0, time=5, crit=True)

class CritHalfToOne(SliderAbstract):
    def construct(self):
        self.construct_abstract(1/2, 1, time=5, crit=True)

class CritToOneToHalf(SliderAbstract):
    def construct(self):
        self.construct_abstract(1, 1/2, time=5, crit=True)

class SpacingTest(Scene):
    def construct(self):
        cvs = CriticalValueSlider(0.5)
        big = Rectangle(width=12, color=BLACK).shift(0.6 * LEFT).set_fill(BLACK, opacity=1)
        self.add(cvs, big)

class PpDefinitionExample(Scene):
    def construct(self):
        Pp = MathTex(
            r'& {{ \mathbb{P} }}_ {{ p }} {{ [ }} A {{ ] }} \phantom{= \text{the probability that}} \\',
            r'&\phantom{\text{event } A \text{ occurs in Bernoulli}} \\',
            r'&\phantom{\text{percolation with parameter } p}',
            color=sol.BASE03
        )

        eq = MathTex(
            r'&\phantom{\mathbb{P}_p[A]} = \text{the probability that} \\',
            r'&\text{event } A \text{ occurs in Bernoulli} \\',
            r'&\text{percolation with parameter } {{ p }}',
            color=sol.BASE03
        ).shift(0.6 * LEFT)

        Pp.align_to(eq, UP + LEFT)
        Pp.set_color_by_tex(r'p', sol.RED)
        Pp.set_color_by_tex(r'[', sol.BASE03)

        eq.set_color_by_tex(r'p', sol.RED)
        eq.set_color_by_tex(r'a', sol.BASE03)

        ex = MathTex(
            r'{{ \mathbb{P} }} _ {{ p }} {{ [ }} \text{infinite cluster} {{ ] }}',
            color=sol.BASE03
        ).set_color_by_tex(r'p', sol.RED).shift(0.6 * LEFT)

        self.add(Pp, eq)

        self.wait(5)
        self.play(Indicate(Pp))
        self.wait(6.75)
        self.play(FadeOut(eq), run_time=0.25)
        self.play(TransformMatchingTex(Pp, ex))
        self.wait(5)

class PpDefinitionExampleBox(Scene):
    def construct(self):
        Pp = MathTex(
            r'&\mathbb{P}_p[A] = \text{the probability that} \\',
            r'&\text{event } A \text{ occurs in Bernoulli} \\',
            r'&\text{percolation with parameter } {{ p }}'
        ).shift(0.6 * LEFT)

        tp = TranslucentBox(Pp)

        ex = MathTex(
            r'\mathbb{P} _ p [ \text{infinite cluster} ]'
        ).shift(0.6 * LEFT)

        te = TranslucentBox(ex)

        self.add(tp)

        self.wait(5)
        self.wait()
        self.wait(7)
        self.play(Transform(tp, te))
        self.wait(5)

class Theorem(Scene):
    def construct(self):
        thm1a = MathTex(r'\textbf{Theorem: }', color=sol.BASE03)
        thm1b = MathTex(r'\text{there exists }', color=sol.BASE03).next_to(thm1a, RIGHT)
        thm1c = MathTex(r'{{p_c}} \in (0,1)', color=sol.BASE03).next_to(thm1b, RIGHT)
        thm1c.set_color_by_tex(r'p_c', sol.BLUE)
        thm1d = MathTex(r'\text{ such that}', color=sol.BASE03).next_to(thm1c, RIGHT)

        thm1 = Group(thm1a, thm1b, thm1c, thm1d)

        thm2a = MathTex(r'\text{for } {{p}} < {{p_c}} \text{, }', color=sol.BASE03)
        thm2a.set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'p_c', sol.BLUE)
        thm2b = MathTex(r'\mathbb{P}_{{p}}[\text{infinite cluster}]', color=sol.BASE03).next_to(thm2a, RIGHT)
        thm2b.set_color_by_tex(r'p', sol.RED)
        thm2c = MathTex(r'= 0', color=sol.BASE03).next_to(thm2b, RIGHT)
        thm2d = MathTex(r'\text{, and}', color=sol.BASE03).next_to(thm2c, RIGHT).shift(0.15 * LEFT)

        thm2 = Group(thm2a, thm2b, thm2c, thm2d).next_to(thm1, DOWN).align_to(thm1, LEFT).shift(0.5 * RIGHT)
    
        thm3a = MathTex(r'\text{for } {{p}} > {{p_c}} \text{, }', color=sol.BASE03)
        thm3a.set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'p_c', sol.BLUE)
        thm3b = MathTex(r'\mathbb{P}_{{p}}[\text{infinite cluster}]', color=sol.BASE03).next_to(thm3a, RIGHT)
        thm3b.set_color_by_tex(r'p', sol.RED)
        thm3c = MathTex(r'= 1.', color=sol.BASE03).next_to(thm3b, RIGHT)

        thm3 = Group(thm3a, thm3b, thm3c).next_to(thm2, DOWN).align_to(thm2, LEFT)

        thm = Group(thm1, thm2, thm3).move_to(0.6 * LEFT + 2 * UP)
        tbox = TranslucentBox(thm)

        self.add(tbox)

        self.wait(0.5)
        self.play(Write(thm1a), run_time=1)
        self.wait(1.5)
        self.play(FadeIn(thm1b))
        self.wait(0.5)
        self.play(FadeIn(thm1c))
        self.wait(0.5)
        self.play(FadeIn(thm1d), run_time=0.5)

        self.play(FadeIn(thm2a))
        self.wait()
        self.play(FadeIn(thm2b))
        self.wait()
        self.play(FadeIn(thm2c))
        self.wait(0.5)
        self.play(FadeIn(thm2d), run_time=0.5)

        self.play(FadeIn(thm3a))
        self.wait(0.5)
        self.play(FadeIn(thm3b))
        self.wait(0.5)
        self.play(FadeIn(thm3c))

        self.wait(13)

        self.wait(0.5)
        self.play(Indicate(thm1c), run_time=2)
        self.wait(0.5)

        self.wait(8)


