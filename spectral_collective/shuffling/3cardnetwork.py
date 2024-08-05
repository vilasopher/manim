from manim import *
import solarized as sol
from sharedclasses import *

class ThreeCardNetwork(Scene):
    def construct(self):
        cardstacks = {
            (1,2,3) : ThreeCardStack([1,2,3]).move_to([-2,0,0]),
            (2,1,3) : ThreeCardStack([2,1,3]).move_to([2,0,0]),
            (2,3,1) : ThreeCardStack([2,3,1]).move_to([-4.5,-2.5,0]),
            (1,3,2) : ThreeCardStack([1,3,2]).move_to([4.5,2.5,0]),
            (3,1,2) : ThreeCardStack([3,1,2]).move_to([-4.5,2.5,0]),
            (3,2,1) : ThreeCardStack([3,2,1]).move_to([4.5,-2.5,0])
        }

        arrowdata = [
            ((a,b,c),(b,d,e))
            for a in range(1,4)
            for b in range(1,4)
            for c in range(1,4)
            for d in range(1,4)
            for e in range(1,4)
            if a != b and b != c and a != c 
            and (d == a and e == c or d == c and e == a)
        ]

        arrowmobjects = {}

        for a in arrowdata:
            start = cardstacks[a[0]].get_center()
            end = cardstacks[a[1]].get_center()

            if end[1] == start[1]:
                shift =  0.2 * np.sign(start[0]-end[0]) * UP    
                start += shift
                end += shift

            mid = start + 1.4 * (end - start) / 2

            am = Group(
                Line(start,end,color=sol.BASE01,stroke_width=6, z_index=-1),
                Arrow(start,mid,color=sol.BASE01, z_index=-1)
            )

            arrowmobjects[a] = am


        percentages = {
            c : ValueTracker(1) for c in cardstacks.keys()
        }

        percentagelabels = {
            c : DecimalNumber(
                percentages[c].get_value() * 100,
                color=sol.BASE03,
                unit='\%',
                num_decimal_places=1
            )
            for c in cardstacks.keys()
        }

        downlabels = [(1,2,3), (2,1,3)]
        leftlabels = [(3,1,2), (2,3,1)]
        rightlabels = [(1,3,2), (3,2,1)]

        for c in cardstacks.keys():
            cardstacks[c].add_updater(
                lambda x, card=c:
                    x.set_percentage(percentages[card].get_value())
            )

            percentagelabels[c].add_updater(
                lambda x, card=c: 
                    x.set_value(
                        percentages[card].get_value() * 100
                    ).next_to(
                        cardstacks[card],
                        DOWN if card in downlabels
                        else LEFT if card in leftlabels
                        else RIGHT
                    ).set(font_size=50)
            )

        def step_markov_chain():
            new_percentages = {
                c : 1/3 * (percentages[c].get_value()
                           + sum([percentages[a].get_value()
                                  for a,b in arrowdata if b==c]))
                for c in cardstacks.keys()
            }
            used_arrows = [
                (a,b) for (a,b) in arrowdata if percentages[a].get_value() > 0
            ]
            self_loops = [
                a for a in cardstacks.keys() if percentages[a].get_value() > 0
            ]
            self.play(
                *(percentages[c].animate.set_value(new_percentages[c]) for c in cardstacks.keys()),
                *(Indicate(arrowmobjects[a], scale_factor=1.1, color=sol.BASE01) for a in used_arrows)
            )

        perfdeftext = MyTex(
            r"``perfect randomness'' \\ $=$ \\ uniform distribution on all arrangements \\ (each arrangement is equally likely)",
            font_size=70
        )

        perfdefbox = SurroundingRectangle(
            perfdeftext, color=sol.BASE01, corner_radius=0.05, buff=MED_SMALL_BUFF
        ).set_fill(sol.BASE2, opacity=1)

        perfdefocclusion = Rectangle(
            width=20, height=15, color=sol.BASE3
        ).set_fill(sol.BASE3, opacity=0.80)

        perfdef = Group(perfdefocclusion, perfdefbox, perfdeftext, z_index=10)

        cardstacks[(1,2,3)].move_to(5*LEFT)
        cardstacks[(2,1,3)].move_to(3*LEFT)
        cardstacks[(2,3,1)].move_to(LEFT)
        cardstacks[(1,3,2)].move_to(RIGHT)
        cardstacks[(3,1,2)].move_to(3*RIGHT)
        cardstacks[(3,2,1)].move_to(5*RIGHT)

        external_occlusions = {
            c : Square(color=sol.BASE2, stroke_width=0, side_length=1.55, z_index=5).set_fill(sol.BASE2, opacity=1).next_to(cardstacks[c], ORIGIN)
            for c in cardstacks.keys()
        }

        cardstacks[(1,2,3)].move_to(ORIGIN).scale(2)
        cardstacks[(1,2,3)][0].shift(0.5*UP)
        cardstacks[(1,2,3)][2].shift(0.5*DOWN)


        #2:20:30
        self.play(FadeIn(cardstacks[(1,2,3)]))

        self.wait(0.5)

        #2:22:00
        self.play(
            cardstacks[(1,2,3)][0].animate(rate_func=rate_functions.ease_in_expo).shift(0.5*DOWN),
            cardstacks[(1,2,3)][2].animate(rate_func=rate_functions.ease_in_expo).shift(0.5*UP),
        )

        self.wait()

        #2:24:00
        self.play(
            LaggedStart(
                cardstacks[(1,2,3)].animate.move_to(5*LEFT).scale(0.5),
                FadeIn(cardstacks[(2,1,3)], shift=5*LEFT),
                FadeIn(cardstacks[(2,3,1)], shift=5*LEFT),
                FadeIn(cardstacks[(1,3,2)], shift=5*LEFT),
                FadeIn(cardstacks[(3,1,2)], shift=5*LEFT),
                FadeIn(cardstacks[(3,2,1)], shift=5*LEFT)
            ),
            run_time=2
        )

        self.wait(3)

        #2:29:00
        self.play(
            *(FadeIn(external_occlusions[c])
              for c in cardstacks.keys() if c != (1,2,3))
        )

        self.wait(5.5)

        #2:35:30
        self.play(
            FadeOut(external_occlusions[(2,1,3)]),
            FadeOut(external_occlusions[(2,3,1)])
        )

        self.wait(3)

        #2:39:30
        self.play(
            FadeOut(external_occlusions[(1,3,2)]),
            FadeOut(external_occlusions[(3,1,2)]),
            FadeOut(external_occlusions[(3,2,1)]),
            run_time=0.5
        )

        #2:40:00
        self.play(
            cardstacks[(1,2,3)].animate.move_to([-2,0,0]),
            cardstacks[(3,1,2)].animate.move_to([-4.5,2.5,0]),
            cardstacks[(2,3,1)].animate.move_to([-4.5,-2.5,0]),
            cardstacks[(2,1,3)].animate.move_to([2,0,0]),
            cardstacks[(1,3,2)].animate.move_to([4.5,2.5,0]),
            cardstacks[(3,2,1)].animate.move_to([4.5,-2.5,0]),
            run_time=0.5
        )

        #2:40:30
        self.play(
            *(FadeIn(a) for a in arrowmobjects.values())
        )

        self.wait(6.5)

        #2:48:00
        self.play(
            *(percentages[c].animate.set_value(0)
                for c in cardstacks.keys() if c != (1,2,3)),
            *(FadeToColor(a,sol.BASE2) 
                for a in arrowmobjects.values())
        )

        self.wait(0.5)

        #2:49:30
        self.play(
            FadeIn(Group(*(p for p in percentagelabels.values())))
        )

        self.wait(1.5)

        #2:52:00
        step_markov_chain()

        self.wait(2)
        
        #2:55:00
        self.play(
            Indicate(arrowmobjects[(1,2,3),(2,1,3)], scale_factor=1.2, color=sol.BASE02),
            Indicate(arrowmobjects[(1,2,3),(2,3,1)], scale_factor=1.2, color=sol.BASE02)
        )

        #2:56:00
        self.play(Wiggle(cardstacks[(1,2,3)]), run_time=1.5)

        self.wait(5.5)

        #3:03:00
        step_markov_chain()
        self.wait(2)

        #3:06:00
        step_markov_chain()
        self.wait(2)

        #3:09:00
        step_markov_chain()
        self.wait(2)

        #3:12:00
        step_markov_chain()
        self.wait(0.5)

        #3:13:30
        self.play(FadeIn(perfdef, scale=0.75))
        self.wait(0.5)

        #3:15:00
        step_markov_chain()
        self.wait(2)

        #3:18:00
        step_markov_chain()
        self.wait(5)


class Reversal(Scene):
    def construct(self):
        cardstacks = {
            (1,2,3) : ThreeCardStack([1,2,3]).move_to([-2,0,0]),
            (2,1,3) : ThreeCardStack([2,1,3]).move_to([2,0,0]),
            (2,3,1) : ThreeCardStack([2,3,1]).move_to([-4.5,-2.5,0]),
            (1,3,2) : ThreeCardStack([1,3,2]).move_to([4.5,2.5,0]),
            (3,1,2) : ThreeCardStack([3,1,2]).move_to([-4.5,2.5,0]),
            (3,2,1) : ThreeCardStack([3,2,1]).move_to([4.5,-2.5,0])
        }

        arrowdata = [
            ((a,b,c),(b,d,e))
            for a in range(1,4)
            for b in range(1,4)
            for c in range(1,4)
            for d in range(1,4)
            for e in range(1,4)
            if a != b and b != c and a != c 
            and (d == a and e == c or d == c and e == a)
        ]

        arrowmobjects = {}

        for a in arrowdata:
            start = cardstacks[a[0]].get_center()
            end = cardstacks[a[1]].get_center()

            if end[1] == start[1]:
                shift =  0.2 * np.sign(start[0]-end[0]) * UP    
                start += shift
                end += shift

            mid = start + 1.4 * (end - start) / 2

            am = Group(
                Line(start,end,color=sol.BASE01,stroke_width=6, z_index=-1),
                Arrow(start,mid,color=sol.BASE01, z_index=-1)
            )

            arrowmobjects[a] = am

        oldnetwork = Group(*arrowmobjects.values(), *cardstacks.values()).copy().stretch(0.6,0).stretch(0.7,1).shift(3.5*LEFT + 0.5*UP)

        oldtext = MyTex(
            r'Original Network',
            font_size=70
        ).shift(3.5*LEFT + 2.75*DOWN)

        newtext = MyTex(
            r'Reversed Network',
            font_size=70
        ).shift(3.5*RIGHT + 2.75*DOWN)

        isomorphism = MyMathTex(
            r'\cong',
            font_size=70
        ).shift(2.75*DOWN)

        rtttext = MyTex(
            r"``random-to-top'' shuffle",
            font_size = 70
        )

        rttbox = SurroundingRectangle(
            rtttext, color=sol.BASE01, buff=MED_SMALL_BUFF, corner_radius=0.1
        ).set_fill(sol.BASE2, opacity=1)

        rttocclusion = Rectangle(
            width=20, height=15, color=sol.BASE3
        ).set_fill(sol.BASE3, opacity=0.80)

        rtt = Group(rttocclusion, rttbox, rtttext).set_z_index(10)


        def1text = MyMathTex(
            r'\textbf{Definition 1: } \mathrm{d_{TV}}({{\cmuone}}, {{\cmutwo}}) = \frac{1}{2} \sum_{ {{\cx}} \in \Omega} |{{\cmutwo}}({{\cx}}) - {{\cmuone}}({{\cx}})|',
            font_size=40
        ).shift(3.2*UP)

        equality = MyMathTex(
            r'\mathrm{d}^\text{top-to-random}_{{\cn}}({{\ct}}) = \mathrm{d}^\text{random-to-top}_{{\cn}}({{\ct}})',
            font_size=80
        ).shift(2.75*DOWN)

        grouptext = Tex(
            r'Why? This is a \emph{random walk on a group}, specifically the symmetric group $S_n$.',
            font_size=35,
            color=sol.BASE01
        ).shift(3.25*UP)

        prob = MyMathTex(
            r'\leq \P[{{\cX_1}} \neq {{\cX_2}}]',
            font_size=80
        ).shift(1.25*UP).align_to(equality[4][1], LEFT).set_color_by_tex(r'X', sol.YELLOW)

        coupling = MyMathTex(
            r'&\text{\large for a specific coupling} \vspace{0.5cm} \\[0.5em]'
            r'&\quad {{\cX_1}} \sim \text{uniform distribution on all arrangements} \\'
            r'&\quad {{\cX_2}} \sim \text{distribution after } {{\ct}} \text{ random-to-top shuffles} \\[0.5em]'
            r'&\text{\large which we will construct next}',
            font_size=55
        ).shift(DOWN).set_color_by_tex(r'X', sol.YELLOW)

        def3 = MyMathTex(
            r'\text{(invoking Definition 3 for the Total Variation distance)}'
        ).shift(3.35*DOWN)

        sneakytrick = MyTex(
            r'{\Large \emph{sneaky trick:}} \\ reversing the shuffle',
            font_size=60
        )

        #12:54:30
        self.play(FadeIn(sneakytrick, scale=0.75))

        self.wait(2)

        #12:57:30
        self.play(FadeOut(sneakytrick, scale=1.25))

        #12:58:30
        self.play(FadeIn(Group(*cardstacks.values()), scale=0.75))
        self.play(FadeIn(Group(*arrowmobjects.values())))

        self.wait(4)

        #13:04:30
        self.play(
            *(am[1].animate.rotate(PI, about_point=am[0].get_center()) for am in arrowmobjects.values())
        )

        self.wait(4)

        #13:09:30
        self.play(FadeIn(rtt, scale=0.75))

        self.wait(3)

        #13:13:30
        self.play(FadeOut(rtt, scale=0.75))

        #13:14:30
        self.play(
            Group(*cardstacks.values(), *arrowmobjects.values()).animate.stretch(0.6, 0).stretch(0.7,1).shift(3.5*RIGHT + 0.5*UP),
            FadeIn(oldnetwork, shift=5*RIGHT),
            FadeIn(oldtext, shift=UP),
            FadeIn(newtext, shift=UP)
        )

        self.wait(8)

        #13:23:30
        self.play(
            *(Transform(c, Dot(c.get_center(), radius=0.4, color=sol.BASE02)) for c in cardstacks.values()),
            *(Transform(c, Dot(c.get_center(), radius=0.4, color=sol.BASE02)) for c in oldnetwork[12:]),
        )

        self.wait(4)

        #13:29:00
        self.play(SpinInFromNothing(isomorphism, angle=2*PI))

        self.wait(2)

        #13:31:30
        self.play(
            FadeIn(def1text, shift=DOWN)
        )

        self.wait(4)

        #13:36:30
        self.play(
            FadeOut(oldtext, shift=8*LEFT),
            FadeOut(newtext, shift=8*RIGHT),
            FadeOut(isomorphism, scale=0.75),
            FadeIn(equality, scale=0.25)
        )

        self.wait(9)

        #13:46:00
        self.play(
            FadeIn(grouptext, shift=DOWN),
            FadeOut(def1text, scale=0.5)
        )

        self.wait(16.5)

        #14:03:30
        self.play(
            Group(grouptext, oldnetwork, *cardstacks.values(), *arrowmobjects.values()).animate.shift(6*UP),
            equality.animate.shift(5.5*UP)
        )

        self.remove(grouptext, oldnetwork, *cardstacks.values(), *arrowmobjects.values())

        self.wait(2)

        #14:06:30
        self.play(
            LaggedStart(
                FadeIn(prob, shift=LEFT),
                FadeIn(coupling, scale=0.75),
                FadeIn(def3, shift=UP)
            ),
            run_time=1.5
        )

        self.wait(10)