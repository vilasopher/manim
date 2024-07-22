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

        perfdef = Group(perfdefbox, perfdeftext, z_index=10)

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

        self.play(FadeIn(cardstacks[(1,2,3)]))

        self.play(
            cardstacks[(1,2,3)][0].animate(rate_func=rate_functions.ease_in_expo).shift(0.5*DOWN),
            cardstacks[(1,2,3)][2].animate(rate_func=rate_functions.ease_in_expo).shift(0.5*UP),
        )

        self.play(
            LaggedStart(
                cardstacks[(1,2,3)].animate.move_to(5*LEFT).scale(0.5),
                FadeIn(cardstacks[(2,1,3)], shift=5*LEFT),
                FadeIn(cardstacks[(2,3,1)], shift=5*LEFT),
                FadeIn(cardstacks[(1,3,2)], shift=5*LEFT),
                FadeIn(cardstacks[(3,1,2)], shift=5*LEFT),
                FadeIn(cardstacks[(3,2,1)], shift=5*LEFT)
            )
        )

        self.play(
            *(FadeIn(external_occlusions[c])
              for c in cardstacks.keys() if c != (1,2,3))
        )

        self.play(
            FadeOut(external_occlusions[(2,1,3)]),
            FadeOut(external_occlusions[(2,3,1)])
        )

        self.play(
            FadeOut(external_occlusions[(1,3,2)]),
            FadeOut(external_occlusions[(3,1,2)]),
            FadeOut(external_occlusions[(3,2,1)]),
        )

        self.play(
            cardstacks[(1,2,3)].animate.move_to([-2,0,0]),
            cardstacks[(3,1,2)].animate.move_to([-4.5,2.5,0]),
            cardstacks[(2,3,1)].animate.move_to([-4.5,-2.5,0]),
            cardstacks[(2,1,3)].animate.move_to([2,0,0]),
            cardstacks[(1,3,2)].animate.move_to([4.5,2.5,0]),
            cardstacks[(3,2,1)].animate.move_to([4.5,-2.5,0])
        )

        self.play(
            *(FadeIn(a) for a in arrowmobjects.values())
        )

        self.play(
            *(percentages[c].animate.set_value(0)
                for c in cardstacks.keys() if c != (1,2,3)),
            *(FadeToColor(a,sol.BASE2) 
                for a in arrowmobjects.values())
        )

        self.wait()

        self.play(
            FadeIn(Group(*(p for p in percentagelabels.values())))
        )

        self.wait()

        step_markov_chain()
        self.wait()
        
        self.play(
            Indicate(arrowmobjects[(1,2,3),(2,1,3)], scale_factor=1.2, color=sol.BASE02),
            Indicate(arrowmobjects[(1,2,3),(2,3,1)], scale_factor=1.2, color=sol.BASE02)
        )

        self.play(Wiggle(cardstacks[(1,2,3)]))

        self.wait()
        step_markov_chain()
        self.wait()
        step_markov_chain()
        self.wait()
        step_markov_chain()
        self.wait()
        step_markov_chain()
        self.wait()
        self.play(FadeIn(perfdef, scale=0.75))
        self.wait()
        step_markov_chain()
        self.wait()
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

        self.play(FadeIn(Group(*cardstacks.values()), scale=0.75))
        self.play(FadeIn(Group(*arrowmobjects.values())))

        self.play(
            *(am[1].animate.rotate(PI, about_point=am[0].get_center()) for am in arrowmobjects.values())
        )

        self.play(
            Group(*cardstacks.values(), *arrowmobjects.values()).animate.stretch(0.6, 0).stretch(0.7,1).shift(3.5*RIGHT + 0.5*UP),
            FadeIn(oldnetwork, shift=5*RIGHT),
            FadeIn(oldtext, shift=UP),
            FadeIn(newtext, shift=UP)
        )

        self.play(
            *(Transform(c, Dot(c.get_center(), radius=0.4, color=sol.BASE02)) for c in cardstacks.values()),
            *(Transform(c, Dot(c.get_center(), radius=0.4, color=sol.BASE02)) for c in oldnetwork[12:]),
        )

        self.play(
            FadeIn(def1text, shift=DOWN)
        )

        self.play(
            FadeOut(oldtext, shift=8*LEFT),
            FadeOut(newtext, shift=8*RIGHT),
            FadeIn(equality, scale=0.25)
        )

        self.play(
            FadeIn(grouptext, shift=DOWN),
            FadeOut(def1text, scale=0.5)
        )

        self.play(
            Group(grouptext, oldnetwork, *cardstacks.values(), *arrowmobjects.values()).animate.shift(6*UP),
            equality.animate.shift(5.5*UP)
        )

        self.remove(grouptext, oldnetwork, *cardstacks.values(), *arrowmobjects.values())

        self.play(FadeIn(prob, shift=LEFT))
        self.play(FadeIn(coupling, scale=0.75))
        self.play(FadeIn(def3, shift=UP))

        self.wait(5)