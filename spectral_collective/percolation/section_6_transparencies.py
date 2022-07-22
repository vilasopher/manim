from manim import *
import solarized as sol
from translucent_box import TranslucentBox
from value_slider import ValueSlider

config.background_opacity = 0

def interp(alpha):
    return np.sqrt((1 - np.cos(2 * np.pi * alpha)) / 2)

def almost_linear(alpha):
    return interp(alpha) * alpha + (1 - interp(alpha)) * (1 - np.cos(np.pi * alpha)) / 2

class ForegroundAbstract(Scene):
    def abstract_construct(self, start, end, run_time=10):
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
        self.abstract_construct(0, 1, run_time=20)

class Foreground1(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(1, 0)

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

class Foreground8(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(7/16, 17/32)

class Foreground9(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(17/32, 15/32)

class Foreground10(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(15/32, 33/64)

class Foreground11(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(33/64, 31/64)

class REVERSEDForeground0(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(1, 0, run_time=20)

class REVERSEDForeground1(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(0, 1)

class REVERSEDForeground2(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(3/4, 0)

class REVERSEDForeground3(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(1/4, 3/4)

class REVERSEDForeground4(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(5/8, 1/4)

class REVERSEDForeground5(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(3/8, 5/8)

class REVERSEDForeground6(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(9/16, 3/8)

class REVERSEDForeground7(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(7/16, 9/16)

class REVERSEDForeground8(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(17/32, 7/16)

class REVERSEDForeground9(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(15/32, 17/32)

class REVERSEDForeground10(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(33/64, 15/32)

class REVERSEDForeground11(ForegroundAbstract):
    def construct(self):
        self.abstract_construct(31/64, 33/64)

class QuestionsAbstract(Scene):
    def construct_abstract(self):
        self.questions = Tex(r'Questions:', color=sol.BASE03, font_size=80)
        self.questions.shift(4.35 * LEFT + 2.8 * UP)

        self.crit = MathTex(
            r'\text{What is the critical value of } {{ p }} \text{?}',
            color=sol.BASE03
        ).next_to(self.questions, DOWN).align_to(self.questions, LEFT)
        self.crit.set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'?', sol.BASE03)

        self.critans = MathTex(
            r'{{p_c}} = 1/2',
            color=sol.BASE03
        ).next_to(self.crit, DOWN).align_to(self.questions, LEFT).shift(RIGHT)
        self.critans.set_color_by_tex(r'p', sol.BLUE).set_color_by_tex(r'=', sol.GREEN)

        self.uniq = Tex(
            r'Will there ever be more than one infinite cluster?',
            color=sol.BASE03
        ).next_to(self.critans, DOWN).align_to(self.questions, LEFT)

        self.uniqans = Tex(r'No', color=sol.GREEN)
        self.uniqans.next_to(self.uniq, DOWN).align_to(self.questions, LEFT).shift(RIGHT)

        self.fast = Tex(
            r'How fast does the phase transition happen?',
            color=sol.BASE03
        ).next_to(self.uniqans, DOWN).align_to(self.questions, LEFT)
        
        self.fastans = MathTex(r'something', color=sol.GREEN)
        self.fastans.next_to(self.fast, DOWN).align_to(self.questions, LEFT).shift(RIGHT)

        self.merg = Tex(
            r'How large are the clusters before they merge?',
            color=sol.BASE03
        ).next_to(self.fastans, DOWN).align_to(self.questions, LEFT)

        self.mergans = MathTex(
            r'\chi({{p}}) \sim ({{p}} - {{p_c}})^{-43/18}',
            color=sol.GREEN
        )
        self.mergans.set_color_by_tex(r'p', sol.RED)
        self.mergans.set_color_by_tex(r'p_c', sol.BLUE)
        self.mergans.set_color_by_tex(r')', sol.GREEN)
        self.mergans.next_to(self.merg, DOWN).align_to(self.questions, LEFT).shift(RIGHT)

class Questions(QuestionsAbstract):
    def construct(self):
        self.construct_abstract()

        self.crit.next_to(self.questions, DOWN).align_to(self.questions, LEFT)
        self.uniq.next_to(self.crit, DOWN).align_to(self.questions, LEFT)
        self.fast.next_to(self.uniq, DOWN).align_to(self.questions, LEFT)
        self.merg.next_to(self.fast, DOWN).align_to(self.questions, LEFT)

        self.play(Write(self.questions), run_time=1)
        self.wait()
        self.play(FadeIn(self.crit))
        self.wait(10)
        self.play(FadeIn(self.uniq))
        self.wait(3)
        self.play(FadeIn(self.fast))
        self.wait(2)
        self.play(FadeIn(self.merg))

        self.wait(12)

        self.uniq.add_updater(
            lambda s : s.align_to(self.questions, LEFT)
        )
        self.fast.add_updater(
            lambda s : s.next_to(self.uniq, DOWN).align_to(self.questions, LEFT)
        )
        self.merg.add_updater(
            lambda s : s.next_to(self.fast, DOWN).align_to(self.questions, LEFT)
        )

        self.play(
            FadeIn(self.critans),
            self.uniq.animate.next_to(self.critans, DOWN)
        )

        self.wait(22)

        #TODO: continue

class QuestionsBox(Scene):
    def construct(self):
        self.construct_abstract()

        self.crit.next_to(self.questions, DOWN).align_to(self.questions, LEFT)
        self.uniq.next_to(self.crit, DOWN).align_to(self.questions, LEFT)
        self.fast.next_to(self.uniq, DOWN).align_to(self.questions, LEFT)
        self.merg.next_to(self.fast, DOWN).align_to(self.questions, LEFT)

        tbox = TranslucentBox(self.questions)
        self.add(tbox)
        self.wait() #self.play(Write(self.questions), run_time=1)
        self.wait()
        self.play(
            Transform(
                tbox,
                TranslucentBox(self.questions, self.crit)
            )
        ) #self.play(FadeIn(self.crit))
        self.wait(10)
        self.play(
            Transform(
                tbox,
                TranslucentBox(
                    self.questions,
                    self.crit,
                    self.uniq
                )
            )
        )#self.play(FadeIn(self.uniq))
        self.wait(3)
        self.play(
            Transform(
                tbox,
                TranslucentBox(
                    self.questions,
                    self.crit,
                    self.uniq,
                    self.fast
                )
            )
        )#self.play(FadeIn(self.fast))
        self.wait(2)
        self.play(
            Transform(
                tbox,
                TranslucentBox(
                    self.questions,
                    self.crit,
                    self.uniq,
                    self.fast
                )
            )
        )#self.play(FadeIn(self.merg))

        self.wait(12)

        self.uniq.next_to(self.critans, DOWN).align_to(self.questions, LEFT)
        self.fast.next_to(self.uniq, DOWN).align_to(self.questions, LEFT)
        self.merg.next_to(self.fast, DOWN).align_to(self.questions, LEFT)

        self.play(
            Transform(
                tbox,
                TranslucentBox(
                    self.questions,
                    self.crit,
                    self.uniq,
                    self.fast,
                    self.merg
                )
            )
        )

        self.wait(22)
