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
        self.questions.shift(4.41 * LEFT + 2.9 * UP)

        self.crit = MathTex(
            r'\text{What is the critical value of } {{ p }} \text{?}',
            color=sol.BASE03
        ).next_to(self.questions, DOWN).align_to(self.questions, LEFT)
        self.crit.set_color_by_tex(r'p', sol.RED).set_color_by_tex(r'?', sol.BASE03)

        self.critans = MathTex(
            r'{{p_c}} = 1/2',
            color=sol.BASE03
        ).next_to(self.crit, DOWN).align_to(self.questions, LEFT).shift(0.5 * RIGHT)
        self.critans.set_color_by_tex(r'p', sol.BLUE).set_color_by_tex(r'=', sol.GREEN)

        self.uniq = Tex(
            r'Will there ever be more than one infinite cluster?',
            color=sol.BASE03
        ).next_to(self.critans, DOWN).align_to(self.questions, LEFT)

        self.uniqans = Tex(r'No, the infinite cluster is unique', color=sol.GREEN)
        self.uniqans.next_to(self.uniq, DOWN).align_to(self.questions, LEFT).shift(0.5 * RIGHT)

        self.fast = Tex(
            r'How fast does the phase transition happen?',
            color=sol.BASE03
        ).next_to(self.uniqans, DOWN).align_to(self.questions, LEFT)
        
        self.fastans = MathTex(r'n \hspace{-0.2em} \times \hspace{-0.2em} n \text{ box crossing window} \approx n^{-3/4} \text{ as } n \to \infty', color=sol.GREEN)
        self.fastans.next_to(self.fast, DOWN).align_to(self.questions, LEFT).shift(0.5 * RIGHT)

        self.merg = Tex(
            r'How large are the clusters before they merge?',
            color=sol.BASE03
        ).next_to(self.fastans, DOWN).align_to(self.questions, LEFT)

        self.mergans = MathTex(
            r'\text{Average size} \approx ({{p}} - {{p_c}})^{-43/18} \text{ as } {{p}} \nearrow {{p_c}}',
            color=sol.GREEN
        )
        self.mergans.set_color_by_tex(r'p', sol.RED)
        self.mergans.set_color_by_tex(r'p_c', sol.BLUE)
        self.mergans.set_color_by_tex(r')', sol.GREEN)
        self.mergans.set_color_by_tex(r'A', sol.GREEN)
        self.mergans.next_to(self.merg, DOWN).align_to(self.questions, LEFT).shift(0.5 * RIGHT)

        g = Group(
            self.questions,
            self.crit,
            self.critans,
            self.uniq,
            self.uniqans,
            self.fast,
            self.fastans,
            self.merg,
            self.mergans
        )
        g.move_to(0.81 * LEFT)



class Questions1(QuestionsAbstract):
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

        self.wait(11)

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

        self.wait(5)

class Questions1Box(QuestionsAbstract):
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
                    self.fast,
                    self.merg
                )
            )
        )#self.play(FadeIn(self.merg))

        self.wait(11)

        self.uniq.next_to(self.critans, DOWN).align_to(self.questions, LEFT)
        self.fast.next_to(self.uniq, DOWN).align_to(self.questions, LEFT)
        self.merg.next_to(self.fast, DOWN).align_to(self.questions, LEFT)

        self.play(
            Transform(
                tbox,
                TranslucentBox(
                    self.questions,
                    self.crit,
                    self.critans,
                    self.uniq,
                    self.fast,
                    self.merg
                )
            )
        )

        self.wait(5)

class Questions2(QuestionsAbstract):
    def construct(self):
        self.construct_abstract()

        self.crit.next_to(self.questions, DOWN).align_to(self.questions, LEFT)
        self.critans.next_to(self.crit, DOWN).align_to(self.questions, LEFT).shift(0.5 * RIGHT)
        self.uniq.next_to(self.critans, DOWN).align_to(self.questions, LEFT)
        self.fast.next_to(self.uniq, DOWN).align_to(self.questions, LEFT)
        self.merg.next_to(self.fast, DOWN).align_to(self.questions, LEFT)

        self.add(
            self.questions,
            self.crit,
            self.critans,
            self.uniq,
            self.fast,
            self.merg
        )

        self.wait(1.5)

        self.fast.add_updater(
            lambda s : s.align_to(self.questions, LEFT)
        )
        self.merg.add_updater(
            lambda s : s.next_to(self.fast, DOWN).align_to(self.questions, LEFT)
        )

        self.play(
            FadeIn(self.uniqans),
            self.fast.animate.next_to(self.uniqans, DOWN)
        )

        self.wait(5)

        self.merg.clear_updaters()
        self.merg.add_updater(
            lambda s : s.align_to(self.questions, LEFT)
        )

        self.play(
            FadeIn(self.fastans),
            self.merg.animate.next_to(self.fastans, DOWN),
            run_time = 0.5
        )

        self.play(
            FadeIn(self.mergans),
            run_time = 0.5
        )

        self.wait(6)

class Questions2Box(QuestionsAbstract):
    def construct(self):
        self.construct_abstract()

        self.crit.next_to(self.questions, DOWN).align_to(self.questions, LEFT)
        self.critans.next_to(self.crit, DOWN).align_to(self.questions, LEFT).shift(0.5 * RIGHT)
        self.uniq.next_to(self.critans, DOWN).align_to(self.questions, LEFT)
        self.fast.next_to(self.uniq, DOWN).align_to(self.questions, LEFT)
        self.merg.next_to(self.fast, DOWN).align_to(self.questions, LEFT)

        tbox = TranslucentBox(
            self.questions,
            self.crit,
            self.critans,
            self.uniq,
            self.fast,
            self.merg
        )
        self.add(tbox)

        self.wait(1.5)

        self.fast.next_to(self.uniqans, DOWN).align_to(self.questions, LEFT)
        self.merg.next_to(self.fast, DOWN).align_to(self.questions, LEFT)

        self.play(
            Transform(
                tbox,
                TranslucentBox(
                    self.questions,
                    self.crit,
                    self.critans,
                    self.uniq,
                    self.uniqans,
                    self.fast,
                    self.merg
                )
            )
        )

        self.wait(5)

        self.merg.next_to(self.fastans, DOWN).align_to(self.questions, LEFT)

        self.play(
            Transform(
                tbox,
                TranslucentBox(
                    self.questions,
                    self.crit,
                    self.critans,
                    self.uniq,
                    self.uniqans,
                    self.fast,
                    self.fastans,
                    self.merg
                )
            ),
            run_time = 0.5
        )

        self.play(
            Transform(
                tbox,
                TranslucentBox(
                    self.questions,
                    self.crit,
                    self.critans,
                    self.uniq,
                    self.uniqans,
                    self.fast,
                    self.fastans,
                    self.merg,
                    self.mergans
                )
            ),
            run_time = 0.5
        )

        self.wait(6)

class Kesten(Scene):
    def construct(self):
        pic = ImageMobject("pics/kesten.png")
        name = Tex(r'Harry Kesten', color=sol.BASE03).next_to(pic, DOWN)
        dates = Tex(r'1931-2019', color=sol.BASE03).next_to(name, DOWN)
        kesten = Group(pic, name, dates).move_to(4.6 * LEFT)
        tk = TranslucentBox(kesten)
        self.add(tk, kesten)

        thm0 = MathTex(
            r'\textbf{Theorem} \text{ (Kesten, 1980):}',
            color = sol.BASE03
        )

        thm1 = MathTex(
            r'\text{In Bernoulli percolation with}',
            color = sol.BASE03
        ).next_to(thm0, DOWN).align_to(thm0, LEFT).shift(0.5 * RIGHT)

        thm2 = MathTex(
            r'\text{parameter } {{p}} \text{ on the infinite}',
            color = sol.BASE03
        ).next_to(thm1, DOWN).align_to(thm1, LEFT)
        thm2.set_color_by_tex(r'p', sol.RED)
        thm2.set_color_by_tex(r'e', sol.BASE03)

        thm3a = MathTex(
            r'\text{square grid, if }',
            color = sol.BASE03
        )
        thm3b = MathTex(
            r'{{p}} < 1/2',
            color = sol.BASE03
        ).next_to(thm3a, RIGHT)
        thm3b.set_color_by_tex(r'p', sol.RED)
        thm3b.set_color_by_tex(r'<', sol.BASE03)
        thm3c = MathTex(
            r', \text{ then}',
            color = sol.BASE03
        ).next_to(thm3b, RIGHT)

        thm3 = Group(thm3a, thm3b, thm3c).next_to(thm2, DOWN).align_to(thm1, LEFT)

        thm4a = MathTex(
            r'\mathbb{P}_{{p}}[\text{infinite cluster}] = 0',
            color = sol.BASE03
        )
        thm4a.set_color_by_tex(r'p', sol.RED)
        thm4a.set_color_by_tex(r'[', sol.BASE03)
        thm4b = MathTex(
            r',',
            color = sol.BASE03
        ).next_to(thm4a, RIGHT).align_to(thm4a, DOWN).shift(0.03 * UP + 0.05 * LEFT)

        thm4 = Group(thm4a, thm4b).next_to(thm3, DOWN).align_to(thm1, LEFT).shift(0.5 * RIGHT)


        thm5a = MathTex(
            r'\text{and if }',
            color = sol.BASE03
        )
        thm5b = MathTex(
            r'{{p}} > 1/2',
            color = sol.BASE03
        ).next_to(thm5a, RIGHT)
        thm5b.set_color_by_tex(r'p', sol.RED)
        thm5b.set_color_by_tex(r'>', sol.BASE03)
        thm5c = MathTex(
            r', \text{ then}',
            color = sol.BASE03
        ).next_to(thm5b, RIGHT)

        thm5 = Group(thm5a, thm5b, thm5c).next_to(thm4, DOWN).align_to(thm1, LEFT)

        thm6a = MathTex(
            r'\mathbb{P}_{{p}}[\text{infinite cluster}] = 1}',
            color = sol.BASE03
        )
        thm6a.set_color_by_tex(r'p', sol.RED)
        thm6a.set_color_by_tex(r'[', sol.BASE03)
        thm6b = MathTex(
            r'.',
            color = sol.BASE03
        ).next_to(thm6a, RIGHT).align_to(thm6a, DOWN).shift(0.13 * UP + 0.05 * LEFT)

        thm6 = Group(thm6a, thm6b).next_to(thm5, DOWN).align_to(thm4, LEFT)

        thm = Group(
            thm0,
            thm1,
            thm2,
            thm3,
            thm4,
            thm5,
            thm6
        ).next_to(tk, RIGHT).shift(0.32 * RIGHT)

        tt = TranslucentBox(thm)

        everything = Group(tk, tt, kesten, thm)
        everything.move_to(0.81 * LEFT)

        self.add(everything)

        self.wait(3)
        self.play(Indicate(thm3b))
        self.wait(0.5)
        self.play(Indicate(thm4a))
        self.wait(2)
        self.play(Indicate(thm5b))
        self.wait(0.5)
        self.play(Indicate(thm6a))
        self.wait(5.5)

class HDC(Scene):
    def construct(self):
        pic = ImageMobject('pics/hdc.jpg')
        name = Tex(r'Hugo Duminil-Copin', color=sol.BASE03).next_to(pic, DOWN)
        dates = Tex(r'1985-present', color=sol.BASE03).next_to(name, DOWN)

        hdc = Group(pic)
        hbox = TranslucentBox(hdc)


        quote = MathTex(
            r'&\text{``Hugo Duminil-Copin is awarded the Fields Medal} \\',
            r'&\;\;\text{2022 for solving longstanding problems in the} \\',
            r'&\;\;\text{probabilistic theory of phase transitions in} \\',
            r'&\;\;\text{statistical physics, especially in dimensions} \\',
            r'&\;\;\text{three and four"}',
            color=sol.BASE03
        )

        cite = MathTex(
            r'&\qquad\qquad\text{-International Mathematical Union}',
            color=sol.BASE03
        ).next_to(quote, DOWN).align_to(quote, RIGHT).shift(0.1 * UP)

        imu = Group(quote, cite).next_to(hdc, DOWN).shift(0.32 * DOWN)
        ibox = TranslucentBox(imu)

        whole = Group(hbox, hdc, ibox, imu).move_to(0.81 * LEFT)
        self.add(whole)

