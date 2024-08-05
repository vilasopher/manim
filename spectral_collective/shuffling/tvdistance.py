from manim import *
import solarized as sol
from numpy.random import random
from sharedclasses import *

class Equivalence(Scene):
    def construct(self):
        text1 = MyTex(
            r'How close are we to perfect randomness?',
            font_size=60
        ).shift(2*UP)

        text2 = MyTex(
            r'What is the \emph{distance} between the uniform distribution \\ and the distribution of arrangements after {{$\ct$}} shuffles?',
            font_size=50
        ).shift(2*DOWN)

        arrow = DoubleArrow([0,1.5,0],[0,-1.3,0],color=sol.BASE1)

        #3:20:30
        self.play(FadeIn(text1, scale=0.75))

        self.wait(7.5)

        #3:29:00
        self.play(FadeIn(text2, shift=UP))
        self.play(FadeIn(arrow, scale=0.75))


        self.wait(10)


class Notations(Scene):
    def construct(self):
        notation = MyTex(
            r'\textbf{Notation}',
            font_size=70
        ).shift(3.25*UP + 5*LEFT)

        muomega = MyTex(
            r'$\mu$ denotes a \emph{probability distribution} on an \emph{outcome space} $\Omega$'
        ).shift(2.25*UP)

        omegalabeltext = MyTex(
            r'e.g. the set of all possible \\ arrangements of a deck of cards',
            font_size=40
        ).shift(3.25*RIGHT + 1.15*UP)

        omegalabelbox = SurroundingRectangle(
            omegalabeltext, color=sol.BASE01, corner_radius=0.05
        ).set_fill(sol.BASE2, opacity=1)

        omegalabelline = Line(
            muomega.get_corner(DOWN+RIGHT) + 0.05*DOWN + 0.5*LEFT,
            muomega.get_corner(DOWN+RIGHT) + 0.05*DOWN + 3.6*LEFT,
            color=sol.BASE01
        )

        omegalabelcurve = Line(
            omegalabelbox.get_top() + RIGHT,
            omegalabelline.get_center(),
            color=sol.BASE01
        )

        omegalabel = Group(omegalabelcurve, omegalabelline, omegalabelbox, omegalabeltext)


        mulabeltext = MyTex(
            r'determines how likely each \\ possible outcome in $\Omega$ is',
            font_size=40
        ).shift(3*LEFT + 1.15*UP)

        mulabelbox = SurroundingRectangle(
            mulabeltext, color=sol.BASE01, corner_radius=0.05
        ).set_fill(sol.BASE2, opacity=1)

        mulabelline = Line(
            muomega.get_corner(DOWN+LEFT) + 0.05*DOWN + 2.6*RIGHT,
            muomega.get_corner(DOWN+LEFT) + 0.05*DOWN + 7.6*RIGHT,
            color=sol.BASE01
        )

        mulabelcurve = Line(
            mulabelbox.get_top() + RIGHT,
            mulabelline.get_center(),
            color=sol.BASE01
        )

        mulabel = Group(mulabelcurve, mulabelline, mulabelbox, mulabeltext)

        example = MyTex(
            r'\textbf{Examples}',
            font_size=70
        ).align_to(notation, LEFT).shift(0.5*DOWN)

        exomegatext = MyTex(
            r'\bigg(with $\Omega = \bigg\{ \qquad, \qquad, \qquad, \qquad, \qquad, \qquad \bigg\}$ \bigg)',
            font_size=40
        ).next_to(example, RIGHT).shift(0.5*RIGHT)

        arrangements = Group(
            ThreeCardStack([1,2,3]).scale(0.5),
            ThreeCardStack([2,1,3]).scale(0.5),
            ThreeCardStack([2,3,1]).scale(0.5),
            ThreeCardStack([1,3,2]).scale(0.5),
            ThreeCardStack([3,1,2]).scale(0.5),
            ThreeCardStack([3,2,1]).scale(0.5)
        ).arrange().shift(0.5*DOWN+2.875*RIGHT)

        exomega = Group(exomegatext, arrangements)

        ex1 = MyMathTex(
            r'\bullet & \text{ if } \mu \text{ is the uniform} \\\
            & \text{ distribution on } \Omega, \\\
            & \qquad {\textstyle \mu(x) = \frac{1}{6}} \\\
            & \text{ for each } x \in \Omega.'
        ).shift(2.5*DOWN + 4.25*LEFT)

        ex2text = MyMathTex(
            r"\bullet & \text{ if } \mu \text{ is the distribution after one} \\\
                & \text{ top-to-random shuffle,} \\\
                & \quad {\textstyle \mu(\quad) = \mu(\quad) = \mu(\quad) = \frac{1}{3}}, \text{ and} \\\
                & \quad {\textstyle \mu(\quad) = \mu(\quad) = \mu(\quad) = 0}"
        ).align_to(ex1, UP).shift(2.75*RIGHT)

        ex2arrangements1 = Group(
            ThreeCardStack([1,2,3]).scale(0.275),
            ThreeCardStack([2,1,3]).scale(0.275),
            ThreeCardStack([2,3,1]).scale(0.275),
        ).arrange(buff=1.42).shift(2.85*DOWN + 2.175*RIGHT)

        ex2arrangements2 = Group(
            ThreeCardStack([1,3,2]).scale(0.275),
            ThreeCardStack([3,1,2]).scale(0.275),
            ThreeCardStack([3,2,1]).scale(0.275),
        ).arrange(buff=1.42).shift(3.43*DOWN + 2.175*RIGHT)

        ex2 = Group(ex2text, ex2arrangements1, ex2arrangements2)

        #3:39:00
        self.play(FadeIn(notation, shift=DOWN+RIGHT))

        self.wait()

        #3:41:00
        self.play(Write(muomega), run_time=3)

        self.wait(2)

        #3:46:00
        self.play(FadeIn(omegalabel, shift=LEFT))

        self.wait(4)

        #3:51:00
        self.play(FadeIn(mulabel, shift=RIGHT))

        self.wait(2)

        #3:54:00
        self.play(FadeIn(example, scale=0.75))

        #3:55:00
        self.play(
            FadeIn(exomega, shift=LEFT),
            FadeIn(ex1, shift=LEFT)
        )

        self.wait(10)

        #4:06:00
        self.play(FadeIn(ex2, shift=LEFT))

        self.wait(5)

        #4:12:30
        self.play(ApplyWave(ex2arrangements1))

        #4:14:30
        self.play(ApplyWave(ex2arrangements2))

        self.wait(10)


class TVDefinition(Scene):
    def construct(self):
        headertext = MyTex(
            r'Let {{$\cmuone$}} and {{$\cmutwo$}} be two probability distributions\\\
                on the same outcome space $\Omega$.',
        ).shift(3*UP)

        def1text = MyMathTex(
            r'\textbf{Definition 1: } \mathrm{d_{TV}}({{\cmuone}}, {{\cmutwo}}) = \frac{1}{2} \sum_{ {{\cx}} \in \Omega} |{{\cmuone}}({{\cx}}) - {{\cmutwo}}({{\cx}})|',
            font_size=55
        ).shift(1.25*UP)

        def2text = MyMathTex(
            r'\textbf{Definition 2: } \mathrm{d_{TV}}({{\cmuone}},{{\cmutwo}}) = \max_{ {{\cA}} \subseteq \Omega} | {{\cmuone}}({{\cA}}) - {{\cmutwo}}({{\cA}}) |',
            font_size=55
        ).next_to(def1text, DOWN).align_to(def1text, LEFT).shift(0.25*DOWN)

        def3text = MyMathTex(
            r'\textbf{Definition 3: } \mathrm{d_{TV}}({{\cmuone}}, {{\cmutwo}}) = \min_{\substack{ {{\cX_1}} \sim {{\cmuone}} \\ {{\cX_2}} \sim {{\cmutwo}} }} \mathbb{P}[{{\cX_1}} \neq {{\cX_2}}]',
            font_size=55
        ).next_to(def2text, DOWN).align_to(def1text, LEFT).shift(0.5*DOWN)

        nametext = MyTex(
            r"``Total Variation Distance''",
            font_size=80
        ).shift(0.5*DOWN)

        eventtext1 = MyTex(
            r'$A$ is an event \\ $\Leftrightarrow A \subseteq \Omega$',
            font_size=40
        ).shift(5*LEFT+1.75*DOWN)

        eventtext2 = MyMathTex(
            r'\mu(A) = \sum_{x \in A} \mu(x)',
            font_size=40
        ).next_to(eventtext1, DOWN).shift(0.25*DOWN)

        extext1 = MyMathTex(
            r'\text{e.g. } {{\cA}} = \{ x \in \Omega : \text{card } 2 \text{ is above card } 3 \}',
            font_size=40
        ).shift(2*RIGHT + 1.5*DOWN).set_color_by_tex(r'A', sol.YELLOW)

        extext2 = MyMathTex(
            r'\textstyle \bullet \text{ if } {{\cmuone}} \text{ is uniform, then } {{\cmuone}}({{\cA}}) = \frac{1}{2}',
            font_size=40
        ).next_to(extext1, DOWN).align_to(extext1, LEFT)

        extext3 = MyMathTex(
            r'\textstyle \bullet &\text{ if } {{\cmutwo}} \text{ is the distribution after one} \\ \textstyle &\text{ top-to-random shuffle, then } {{\cmutwo}}({{\cA}}) = 1',
            font_size=40
        ).next_to(extext2, DOWN).align_to(extext1, LEFT)

        extext4 = MyMathTex(
            r'\Rightarrow \mathrm{d_{TV}}({{\cmuone}},{{\cmutwo}}) \geq \frac{1}{2}'
        ).next_to(Group(extext1,extext2,extext3), RIGHT).shift(4*LEFT)

        exbrace = Brace(Group(extext1, extext2, extext3), RIGHT, color=sol.BASE03).shift(4.5*LEFT)

        popupbox = Rectangle(color=sol.BASE01, height=7, width=13).set_fill(sol.BASE2, opacity=1)
        popupocclusion = Rectangle(
            width=20, height=15, color=sol.BASE3
        ).set_fill(sol.BASE3, opacity=0.80)

        randomvars = MyTex(
            r'\textbf{Random Variables 101}',
            font_size=60
        ).align_to(popupbox, UP + LEFT).shift(0.5*(DOWN + RIGHT))

        rvtext1 = MyTex(
            r'\textbullet{} A \emph{random variable} is a random outcome $X \in \Omega$.'
        ).next_to(randomvars, DOWN).align_to(randomvars, LEFT).shift(0.25*DOWN + 0.5*RIGHT)

        rvtext2 = MyMathTex(
            r'\bullet & \text{ } X \sim \mu \text{ means that } X \text{ has distribution } \mu, \\ &\text{ i.e. } \mu(x) = \P[X = x] \text{ for each fixed } x \in \Omega.'
        ).next_to(rvtext1, DOWN).align_to(rvtext1, LEFT)

        rvtext3 = MyTex(
            r'\emph{different random variables may} \\ \emph{have the same distribution}'
        ).next_to(rvtext2, DOWN)
        rvtext3.shift([-rvtext3.get_center()[0], -0.15, 0])

        rvextext = MyMathTex(
            r'\textstyle &\textbf{Example:} \text{ flip a fair coin } 5 \text{ times. Let } X \text{ be the number of} \\\
              \textstyle &\text{ heads, and let } Y \text{ be the number of tails. Then } X \text{ and } Y \\\
              \textstyle &\text{ have the same distribution } \mu = \mathrm{Binomial}(5,\tfrac{1}{2}), \text{ but } X \neq Y.',
            font_size=45
        ).next_to(rvtext3, DOWN).align_to(randomvars, LEFT).shift(0.3*DOWN + 0.1*LEFT)

        couplingtext = MyTex(
            r"``coupling''",
            font_size=60
        ).next_to(def3text, DOWN).shift(LEFT + 0.25*UP)

        couplingtextprime = MyTex(
            r'a way to sample from {{$\cmuone$}} and {{$\cmutwo$}} simultaneously',
            font_size=40
        ).next_to(def3text, DOWN).shift(2*RIGHT)

        couplingarrow = Arrow(
            couplingtext.get_right(),
            def3text[5].get_left()+0.25*DOWN,
            color=sol.BASE1,
            tip_shape=StealthTip
        )

        def1obfuscation = SurroundingRectangle(
            Group(def1text[4][1:], def1text[5:]),
            stroke_width=0,
            color=sol.BASE3
        ).set_fill(sol.BASE3, opacity=1).set_z_index(10)

        self.add(def1obfuscation)

        overlay1 = SurroundingRectangle(
            Group(diaconistable[12], diaconistable[13]),
            color=sol.FOREST_GREEN,
            corner_radius=0.1
        ).set_fill(sol.FOREST_GREEN, opacity=0.25)

        overlay2 = SurroundingRectangle(
            Group(diaconistable[9], diaconistable[11]),
            color=sol.FOREST_GREEN,
            corner_radius=0.1
        ).set_fill(sol.FOREST_GREEN, opacity=0.25)

        #4:19:30
        self.play(FadeIn(headertext, shift=DOWN))

        self.wait(4.5)

        #4:25:00
        self.play(FadeIn(def1text, scale=0.75))

        self.wait(2.5)

        #4:28:30
        self.play(FadeOut(def1obfuscation))

        self.wait(0.5)

        #4:30:00
        self.play(Wiggle(Group(def1text[5][0], def1text[6][0:2])))

        self.wait(0.5)

        #4:32:30
        self.play(Wiggle(Group(def1text[7:10], def1text[10][0])))

        self.wait()

        #4:35:30
        self.play(Wiggle(Group(def1text[11:14], def1text[14][0])))

        self.wait()

        #4:38:30
        self.play(Wiggle(def1text[4][-1]))

        #4:40:30
        self.play(Wiggle(Group(def1text[4][-4:-1])))

        #4:42:30
        self.play(Circumscribe(Group(def1text[0][-4:], def1text[1:4], def1text[4][0]), color=sol.BASE03, fade_out=True),
                  run_time=2)
        
        self.wait(3)

        #4:47:30
        self.play(Write(nametext), run_time=2)

        self.wait()

        #4:50:30
        self.play(Wiggle(Group(def1text[0][-3:-1])))

        self.wait(8.5)

        #5:01:00
        self.play(FadeOut(nametext, shift=DOWN))

        #5:02:00
        self.play(FadeIn(def2text, scale=0.75))

        self.wait(4.5)

        #5:07:30
        self.play(FadeIn(eventtext1, shift=RIGHT))

        self.wait(1.5)

        #5:10:00
        self.play(FadeIn(eventtext2, shift=RIGHT))

        self.wait(5.5)

        #5:16:30
        self.play(FadeIn(extext1, scale=0.75))

        self.wait(5)

        #5:22:30
        self.play(FadeIn(extext2, shift=LEFT))

        self.wait(7)

        #5:30:30
        self.play(FadeIn(extext3, shift=LEFT))

        self.wait(6)

        #5:37:30
        self.play(
            FadeOut(Group(eventtext1, eventtext2), shift=4.5*LEFT),
            extext1.animate.shift(4.5*LEFT),
            extext2.animate.shift(4.5*LEFT),
            extext3.animate.shift(4.5*LEFT),
            FadeIn(Group(exbrace, extext4), shift=4.5*LEFT)
        )

        self.wait(6)

        #5:44:30
        self.play(
            FadeOut(Group(extext1, extext2, extext3, extext4, exbrace), shift=14*LEFT),
            FadeIn(diaconistable, shift=14*LEFT)
        )

        self.wait(2.5)

        #5:48:00
        self.play(FadeIn(overlay1, scale=1.25))

        self.wait(7)

        #5:56:00
        self.play(Transform(overlay1, overlay2))

        self.wait(17)

        #6:14:00
        self.play(FadeOut(overlay1, scale=1.25))

        self.wait(25.5)

        #6:40:30
        self.play(FadeIn(Group(popupocclusion, popupbox, randomvars), scale=0.75))

        self.wait(2.5)

        #6:44:00
        self.play(FadeIn(rvtext1, shift=LEFT)) 
        
        self.wait(3)

        #6:48:00
        self.play(FadeIn(rvtext2, shift=LEFT))

        self.wait(3.5)

        #6:52:30
        self.play(FadeIn(rvtext3, scale=0.75))

        self.wait(3)

        #6:56:30
        self.play(FadeIn(rvextext, scale=0.75))
        self.remove(diaconistable)

        self.wait(14.5)

        #7:12:00
        self.play(FadeOut(Group(popupocclusion, popupbox, randomvars, rvtext1, rvtext2, rvtext3, rvextext), scale=0.75))

        self.wait(1.5)

        #7:14:30
        self.play(FadeIn(def3text, scale=0.75))

        self.wait(1.5)

        #7:17:00
        self.play(ApplyWave(Group(def3text[5], def3text[9]), direction=LEFT, amplitude=0.05),
                  run_time=1)

        self.wait(0.5)

        #7:18:30
        self.play(Indicate(Group(def3text[6], def3text[10]), color=sol.BASE01))

        #7:19:30
        self.play(ApplyWave(Group(def3text[7], def3text[11]), direction=RIGHT, amplitude=0.05),
                  run_time=1)

        self.wait(2)

        #7:22:30
        self.play(Wiggle(Group(def3text[12:])))

        self.wait(6)

        #7:30:30
        self.play(FadeIn(couplingtextprime, shift=UP), GrowArrow(couplingarrow, scale=0.75))

        self.wait(5.5)

        #7:37:00
        self.play(
            LaggedStart(
                FadeOut(couplingtextprime, shift=4*RIGHT),
                Write(couplingtext),
                lag_ratio=0.25
            ),
            run_time=1.5
        )

        self.wait(20)


class Yapping(Scene):
    def construct(self):
        def1text = MyMathTex(
            r'\textbf{Definition 1: } \mathrm{d_{TV}}({{\cmuone}}, {{\cmutwo}}) = \frac{1}{2} \sum_{ {{\cx}} \in \Omega} |{{\cmuone}}({{\cx}}) - {{\cmutwo}}({{\cx}})|',
            font_size=55
        ).shift(2.75*UP)

        def2text = MyMathTex(
            r'\textbf{Definition 2: } \mathrm{d_{TV}}({{\cmuone}},{{\cmutwo}}) = \max_{ {{\cA}} \subseteq \Omega} | {{\cmuone}}({{\cA}}) - {{\cmutwo}}({{\cA}}) |',
            font_size=55
        ).shift(0.25*UP).align_to(def1text, LEFT)

        def3text = MyMathTex(
            r'\textbf{Definition 3: } \mathrm{d_{TV}}({{\cmuone}}, {{\cmutwo}}) = \min_{\substack{ {{\cX_1}} \sim {{\cmuone}} \\ {{\cX_2}} \sim {{\cmutwo}} }} \mathbb{P}[{{\cX_1}} \neq {{\cX_2}}]',
            font_size=55
        ).shift(2.25*DOWN).align_to(def1text, LEFT)

        number = MyTex(
            r'\emph{number of arrangements of a $52$ card deck is $52!$}',
            font_size=45
        ).next_to(def1text, DOWN)
        
        number2 = MyMathTex(
            r'= 8065817517 0943878571 6606368564 0376697528 9505440883 2778240000 00000000 \approx \text{number of atoms in the Milky Way galaxy}',
            font_size=45
        ).next_to(number, RIGHT)

        event = MyTex(
            r'\emph{any event gives a lower bound!}',
            font_size=45
        ).next_to(def2text, DOWN)
        event.shift(event.get_center()[0]*LEFT)

        coupling = MyTex(
            r'\emph{any coupling gives an upper bound!}',
            font_size=45
        ).next_to(def3text, DOWN)
        coupling.shift(coupling.get_center()[0]*LEFT)

        restofvideo1 = MyTex(
            r'\textbf{The rest of the video:}',
            font_size=60
        ).shift(UP + 3*LEFT)

        restofvideo2 = MyMathTex(
            r'&\text{constructing couplings to get upper bounds on the total} \\\
                &\text{variation distance between the uniform distribution and} \\\
                &\text{the distribution of arrangements after } {{\ct}} \text{ shuffles.}'
        ).next_to(restofvideo1, DOWN).align_to(restofvideo1, LEFT).shift(0.25*RIGHT)

        doft1 = MyMathTex(
            r'{{\mathrm{d}}} {{(}} {{\ct}} {{)}}',
            font_size=70
        ).shift(2.25*DOWN)
        doft2 = MyMathTex(
            r'{{\mathrm{d}}}^{{\text{[shuffle]}}} {{(}} {{\ct}} {{)}}',
            font_size=70
        ).shift(2.25*DOWN)
        doft3 = MyMathTex(
            r'{{\mathrm{d}}}^{{\text{top-to-random}}} {{(}} {{\ct}} {{)}}',
            font_size=70
        ).shift(2.25*DOWN)
        doft4 = MyMathTex(
            r'{{\mathrm{d}}}^{{\text{top-to-random}}}_{{\cn}} {{(}} {{\ct}} {{)}}',
            font_size=70
        ).shift(2.25*DOWN + 3*LEFT)

        ncards = MyMathTex(
            r'({{\cn}} = \text{number of cards})',
            font_size=50
        ).next_to(doft4, RIGHT).shift(RIGHT)

        doft5 = MyMathTex(
            r'{{\mathrm{d}}}^{{\text{top-to-random}}}_{{\cn}} {{(}} {{\ct}} {{)}} \leq f_{{\cn {} }} {{( {} }} {{\ct {} }} {{) {} }}',
            font_size=70
        ).shift(0.25*DOWN)

        tmix = MyMathTex(
            r'\tau^\text{top-to-random}_{{\cn}} {{(}} {{\ceps}} {{)}} \leq f^{-1}_{{\cn}} ({{\ceps}})',
            font_size=70
        ).shift(1.5*DOWN + 0.325*RIGHT)

        tmixexplanation1 = MyTex(
            r'number of shuffles before the distance is at most {{$\ceps$}}'
        ).shift(2.75*DOWN)

        tmixexplanation2 = MyTex(
            r'= the \emph{mixing time}'
        ).next_to(tmixexplanation1, DOWN)

        tmixarrow = CurvedArrow(tmixexplanation1.get_corner(UP+LEFT)+0.25*RIGHT, tmix.get_left() + 0.2*LEFT, color=sol.BASE1, radius=-2)

        #11:21:30
        self.play(
            LaggedStart(
                FadeIn(def1text, scale=0.75),
                FadeIn(def2text, scale=0.75),
                FadeIn(def3text, scale=0.75),
                lag_ratio=0.5
            ),
            run_time=2
        )

        self.wait(6.5)

        #11:30:00
        self.play(FadeIn(event, scale=0.75))

        self.wait(2.5)

        #11:33:30
        self.play(FadeIn(coupling, scale=0.75))

        self.wait(9.5)

        #11:44:00
        self.play(FadeIn(number, scale=0.75))

        self.wait(3.5)

        self.play(
            FadeIn(number2, shift=2*LEFT),
            rate_func=rate_functions.ease_in_sine,
            run_time=0.25
        )
        self.play(
            Group(number, number2).animate.shift(26*LEFT),
            rate_func=rate_functions.ease_out_sine,
            run_time=3.75
        )

        self.wait(3.5)

        #11:56:00
        self.play(
            FadeOut(Group(def1text, def2text, number, number2, event, coupling), shift=4.5*UP),
            def3text.animate.shift(4.5*UP)
        )

        #11:57:00
        self.play(FadeIn(restofvideo1, scale=0.75))
        self.play(Write(restofvideo2), run_time=7)

        self.wait(11)

        #12:16:00
        self.play(FadeIn(doft1, scale=0.75))

        self.wait(0.5)

        #12:17:30
        self.play(TransformMatchingTex(doft1, doft2))

        self.wait(3)

        #12:21:30
        self.play(TransformMatchingTex(doft2, doft3))

        self.wait(5)

        #12:27:30
        self.play(
            doft3.animate.shift(3*LEFT),
            FadeIn(ncards, shift=3*LEFT)
        )

        self.wait(2.5)

        #12:31:00
        self.play(TransformMatchingTex(doft3, doft4))

        self.wait(2)

        #12:34:00
        self.play(
            FadeOut(def3text, shift=2*UP),
            Group(restofvideo1, restofvideo2).animate.shift(2*UP),
            FadeOut(ncards, shift=2*UP + 3*RIGHT),
            TransformMatchingTex(doft4, doft5)
        )

        self.wait(4.5)

        #12:39:30
        self.play(FadeIn(tmix, shift=UP))

        #12:40:30
        self.play(
            FadeIn(tmixexplanation1, shift=UP),
            FadeIn(tmixarrow, scale=0.75)
        )

        self.wait(4.5)

        #12:46:00
        self.play(FadeIn(tmixexplanation2, scale=0.75))

        self.wait(10)