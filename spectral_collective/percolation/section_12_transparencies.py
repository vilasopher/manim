from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import ValueSlider, CriticalValueSlider

config.background_opacity = 0

LO = 0.45
HI = 0.52

class SliderSuper(Scene):
    def construct(self):
        cvs = CriticalValueSlider(HI)
        self.add(cvs)

class SliderSub(Scene):
    def construct(self):
        cvs = CriticalValueSlider(LO)
        self.add(cvs)

class SliderUp(Scene):
    def construct(self):
        p = ValueTracker(LO)
        cvs = CriticalValueSlider(p.get_value())

        cvs.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.add(cvs)

        self.play(p.animate.set_value(HI), run_time=0.5)

class SliderDown(Scene):
    def construct(self):
        p = ValueTracker(HI)
        cvs = CriticalValueSlider(p.get_value())

        cvs.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.add(cvs)

        self.play(p.animate.set_value(LO), run_time=0.5)

class CritSuper(Scene):
    def construct(self):
        cvs = CriticalValueSlider(HI)
        cvs.add_crit()
        self.add(cvs)

class CritSub(Scene):
    def construct(self):
        cvs = CriticalValueSlider(LO)
        cvs.add_crit()
        self.add(cvs)

class CritUp(Scene):
    def construct(self):
        p = ValueTracker(LO)
        cvs = CriticalValueSlider(p.get_value())
        cvs.add_crit()

        cvs.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.add(cvs)

        self.play(p.animate.set_value(HI), run_time=0.5)

class CritDown(Scene):
    def construct(self):
        p = ValueTracker(HI)
        cvs = CriticalValueSlider(p.get_value())
        cvs.add_crit()

        cvs.add_updater(
            lambda s : s.set_p(p.get_value())
        )

        self.add(cvs)

        self.play(p.animate.set_value(LO), run_time=0.5)

class ProbEquivalence(Scene):
    def construct(self):
        prob1 = MathTex(
            r'{{ \mathbb{P} }} _ {{ p }} {{ [\text{the cluster of } o \text{ is infinite}] }}',
            color=sol.BASE03,
            font_size = 40
        ).set_color_by_tex(r'p', sol.RED).move_to(0.6 * LEFT + UP)
        
        prob2 = MathTex(
            r'{{ \mathbb{P} }} _ {{ p }} {{ [\text{the cluster of } o \text{ is infinite}] }} {{ > 0 \Leftrightarrow \mathbb{P} }} _ {{ p \hspace{1em} }} {{ \hspace{-1em} [\text{there is an infinite cluster}] = 1 }}',
            color=sol.BASE03,
            font_size = 36
        ).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'[', sol.BASE03).move_to(0.6 * LEFT + UP)

        lem = MathTex(
            r'\textbf{Lemma: }',
            r'& {{ \mathbb{P} }} _ {{ p }} {{ [\text{the cluster of } o \text{ is infinite}] }} {{ > 0 \Leftrightarrow \mathbb{P} }} _ {{ p \hspace{1em} }} {{ \hspace{-1em} [\text{there is an infinite cluster}] = 1 }} {{,}} \\',
            r'\text{and }',
            r'& {{ \mathbb{P} \hspace{1em} \hspace{-1em} }} _ {{ p \hspace{2em} }} {{ \hspace{-2em} [\text{the cluster of } o \text{ is infinite}]=0 \Leftrightarrow \mathbb{P} }} _ {{ p \hspace{3em} }} {{ \hspace{-3em} [\text{there is an infinite cluster}] = 0. }}',
            color=sol.BASE03,
            font_size=36
        ).move_to(3.05 * UP).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'[', sol.BASE03).set_color_by_tex(r'\mathbb{P}', sol.BASE03)

        prob3 = MathTex(
            r'& {{ \mathbb{P} }} _ {{ p }} {{ [\text{the cluster of } o \text{ is infinite}] }} {{ > 0 \Leftrightarrow \mathbb{P} }} _ {{ p \hspace{1em} }} {{ \hspace{-1em} [\text{there is an infinite cluster}] = 1 }} {{,}} \\',
            r'& {{ \mathbb{P} \hspace{1em} \hspace{-1em} }} _ {{ p \hspace{2em} }} {{ \hspace{-2em} [\text{the cluster of } o \text{ is infinite}]=0 \Leftrightarrow \mathbb{P} }} _ {{ p \hspace{3em} }} {{ \hspace{-3em} [\text{there is an infinite cluster}] = 0. }}',
            color=sol.BASE03,
            font_size=36
        ).move_to(3.05 * UP + 0.6 * LEFT).set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'[', sol.BASE03).set_color_by_tex(r'\mathbb{P}', sol.BASE03)

        self.play(FadeIn(prob1))
        self.wait(5.5)
        self.play(TransformMatchingTex(prob1, prob2))
        self.wait(5)
        self.play(TransformMatchingTex(prob2, lem))
        self.wait(4.5)
        self.play(TransformMatchingTex(lem, prob3), run_time=0.5)
        self.wait(17.5)

class ProbEquivalenceBox(Scene):
    def construct(self):
        prob1 = MathTex(
            r'\mathbb{P}_{{p}}[\text{the cluster of } o \text{ is infinite}]',
            color=sol.BASE03,
            font_size = 40
        ).set_color_by_tex(r'p', sol.RED).move_to(0.6 * LEFT + UP)

        t1 = TranslucentBox(prob1)
        
        prob2 = MathTex(
            r'\mathbb{P}_{{p}}[\text{the cluster of } o \text{ is infinite}] > 0',
            r'\Leftrightarrow',
            r'\mathbb{P}_{{p}}[\text{there is an infinite cluster}] = 1',
            color=sol.BASE03,
            font_size = 36
        ).set_color_by_tex(r'p', sol.RED).move_to(0.6 * LEFT + UP)

        t2 = TranslucentBox(prob2)

        lem = MathTex(
            r'\textbf{Lemma: } ',
            r'&\mathbb{P}_{{p}}[\text{the cluster of } o \text{ is infinite}]>0',
            r'\Leftrightarrow',
            r'\mathbb{P}_{{p}}[\text{there is an infinite cluster}] = 1, \\',
            r'\text{and }',
            r'&\mathbb{P}_{{p}}[\text{the cluster of } o \text{ is infinite}]=0',
            r'\Leftrightarrow',
            r'\mathbb{P}_{{p}}[\text{there is an infinite cluster}] = 0.',
            color=sol.BASE03,
            font_size=36
        ).move_to(3.05 * UP).set_color_by_tex(r'p', sol.RED)

        tlem = TranslucentBox(lem)

        prob3 = MathTex(
            r'&\mathbb{P}_{{p}}[\text{the cluster of } o \text{ is infinite}]>0.',
            r'\Leftrightarrow',
            r'\mathbb{P}_{{p}}[\text{there is an infinite cluster}] = 1,\\',
            r'&\mathbb{P}_{{p}}[\text{the cluster of } o \text{ is infinite}]=0',
            r'\Leftrightarrow',
            r'\mathbb{P}_{{p}}[\text{there is an infinite cluster}] = 0.',
            color=sol.BASE03,
            font_size=36
        ).move_to(3.05 * UP + 0.6 * LEFT).set_color_by_tex(r'p', sol.RED)

        t3 = TranslucentBox(prob3)

        self.add(t1)
        self.wait()
        self.wait(5.5)
        self.play(Transform(t1, t2))
        self.wait(5)
        self.play(Transform(t1, tlem))
        self.wait(4.5)
        self.play(Transform(t1, t3), run_time=0.5)
        self.wait(17.5)

class FinalTheorem(Scene):
    def construct(self):
        thm1a = MathTex(r'\textbf{Theorem: }', color=sol.BASE03)
        thm1b = MathTex(r'\text{there exists }', color=sol.BASE03).next_to(thm1a, RIGHT)
        thm1c = MathTex(r'{{p_c}} \in (0,1)', color=sol.BASE03).next_to(thm1b, RIGHT)
        thm1c.set_color_by_tex(r'p_c', sol.BLUE)
        thm1d = MathTex(r'\text{ such that}', color=sol.BASE03).next_to(thm1c, RIGHT)

        thm1 = Group(thm1a, thm1b, thm1c, thm1d)

        thm2a = MathTex(r'\text{for } {{p}} < {{p_c}} \text{, }', color=sol.BASE03)
        thm2a.set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'p_c', sol.BLUE)
        thm2b = MathTex(r'\mathbb{P}_{{p}}[o \leftrightarrow \infty] = 0', color=sol.BASE03).next_to(thm2a, RIGHT)
        thm2b.set_color_by_tex(r'p', sol.RED)
        thm2c = MathTex(r'\text{, and}', color=sol.BASE03).next_to(thm2b, RIGHT).shift(0.15 * LEFT)

        thm2 = Group(thm2a, thm2b, thm2c).next_to(thm1, DOWN).align_to(thm1, LEFT).shift(RIGHT)
    
        thm3a = MathTex(r'\text{for } {{p}} > {{p_c}} \text{, }', color=sol.BASE03)
        thm3a.set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'p_c', sol.BLUE)
        thm3b = MathTex(r'\mathbb{P}_{{p}}[o \leftrightarrow \infty] > 0 \text{.}', color=sol.BASE03).next_to(thm3a, RIGHT)
        thm3b.set_color_by_tex(r'p', sol.RED)

        thm3 = Group(thm3a, thm3b).next_to(thm2, DOWN).align_to(thm2, LEFT)

        thm = Group(thm1, thm2, thm3).move_to(0.6 * LEFT + 2.5 * UP)
        tbox = TranslucentBox(thm)

        self.add(tbox)
        
        self.wait(0.5)

        self.play(Write(thm1a), run_time=1)
        self.wait()
        self.play(FadeIn(thm1b))
        self.wait(0.5)
        self.play(FadeIn(thm1c))
        self.play(FadeIn(thm1d))

        self.play(FadeIn(thm2a))
        self.play(FadeIn(thm2b))
        self.wait(3)
        self.play(FadeIn(thm2c), run_time=0.5)

        self.play(FadeIn(thm3a))
        self.play(FadeIn(thm3b))
        self.wait(5)
