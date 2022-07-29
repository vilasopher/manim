from manim import *
import solarized as sol
import numpy as np

config.background_opacity = 0

hi_beta   = 0.4407 + 0.2
crit_beta = 0.4407
lo_beta   = 0.4407 - 0.1

hi_log2   = 21
crit_log2 = 18
lo_log2   = 15

epsilon = 0.02

def i(frame):
    return (1 - np.cos( (2 * np.pi * frame) / (24 * 60) )) / 2

def j(frame):
    return (2/3) * (1 - np.cos( (2 * np.pi * (frame - 4 * 60)) / (20 * 60) )) / 2 

def k(frame):
    return (1/3) + (1/3) * (1 + np.cos( (2 * np.pi * (frame - 10 * 60)) / (12 * 60) )) / 2

def interp(frame):
    if frame < 24 * 60:
        return i(frame)
    if frame < 34 * 60:
        return j(frame)
    if frame < 40 * 60:
        return k(frame)
    if frame <= 60 * 60:
        return 1/3

def beta(frame):
    return interp(frame) * hi_beta + (1 - interp(frame)) * lo_beta

def steps_between_frames(beta):
    s = 1 / (1 + np.exp( - (beta - crit_beta) / epsilon ))
    return int(2 ** (s * (hi_log2 - lo_log2) + lo_log2)) + 2**lo_log2

def speed(beta):
    return steps_between_frames(beta) / steps_between_frames(crit_beta)

class Ising(Scene):
    def construct(self):
        referencebox = Rectangle(
            height = 4.4444444444,
            width = 5/2 * 4.444444444,
            color = sol.BASE03
        )
        #self.add(referencebox)

        txt = Tex(r'Ising Model', color=sol.BASE03, font_size=150)
        txt.shift(3*UP)
        self.add(txt)

        lo_temp   = 1 / hi_beta
        crit_temp = 1 / crit_beta
        hi_temp   = 1 / lo_beta
        # (MID-LO)/(HI-LO) = 0.579816

        slider = NumberLine(
            include_ticks=False,
            stroke_width=5,
            x_range = [lo_temp, hi_temp],
            length = 9
        )
        slider.set_stroke(
            color_gradient(
                [PURE_RED, PURE_RED, BLUE_C, BLUE_C, BLUE_C],
                100
            )
        )
        slider.shift(3.1*DOWN + 1.5 * LEFT)
        self.add(slider)

        crit = Square(0.1/1.41, color=sol.BASE01).rotate(PI/4)
        crit.set_fill(color=sol.BASE01, opacity=1)
        crit.move_to(slider.number_to_point(crit_temp))
        self.add(crit)

        hot = Tex(r'hot', color=PURE_RED, font_size=35).next_to(slider, UP).align_to(slider, RIGHT)
        self.add(hot)

        cold = Tex(r'cold', color=BLUE_C, font_size=35).next_to(slider, UP).align_to(slider, LEFT)
        self.add(cold)

        crittext = Tex(r'critical', color=sol.BASE01, font_size=35).next_to(crit, UP).align_to(hot, DOWN)
        self.add(crittext)


        f = ValueTracker(0)
        self.add(f)

        b = ValueTracker(lo_beta)
        self.add(b)

        tick = slider.get_tick(
            1 / b.get_value()
        ).set(stroke_color = sol.BASE03) 
        self.add(tick)

        temp = Tex(
            r'temperature',
            color=sol.BASE03,
            font_size=35
        ).next_to(tick, DOWN).shift(0.1 * UP)
        self.add(temp)

        b.add_updater(
            lambda s : s.set_value(beta(f.get_value()))
        )

        tick.add_updater(
            lambda s : s.become(
                slider.get_tick(
                    1 / b.get_value()
                ).set(stroke_color = sol.BASE03) 
            )
        )
         
        temp.add_updater(
            lambda s : s.next_to(tick, DOWN).shift(0.1 * UP)
        )

        
        spd = DecimalNumber(speed(b.get_value()), color=sol.BASE03, font_size = 60)
        spd.move_to(2.9*DOWN + 5.3 * RIGHT)
        self.add(spd)

        times = MathTex(r'\times', color=sol.BASE03).next_to(spd, RIGHT).align_to(spd, DOWN).shift(0.1*LEFT)
        self.add(times)

        spdtext = Tex(r'speed', color=sol.BASE03).next_to(Group(spd, times), DOWN).shift(0.15*UP)
        self.add(spdtext)

        spd.add_updater(
            lambda s : s.set_value(speed(b.get_value()))
        )
        
        self.play(f.animate.set_value(3600), run_time=60)
