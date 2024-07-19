from manim import *
import solarized as sol

tt = TexTemplate()
tt.add_to_preamble(r'\usepackage{amsfonts}')
tt.add_to_preamble(r'\usepackage{amsmath}')
tt.add_to_preamble(r'\usepackage{xcolor}')
tt.add_to_preamble(r'\addtolength{\jot}{-0.35em}')
tt.add_to_preamble(r'\renewcommand{\P}{\mathbb{P}}')
tt.add_to_preamble(r'\newcommand{\coloredt}{t}')
tt.add_to_preamble(r'\newcommand{\coloredn}{n}')
tt.add_to_preamble(r'\newcommand{\coloredeps}{\varepsilon}')

def MyMathTex(text, color=sol.BASE03, **kwargs):
    return MathTex(
        text,
        color=color,
        tex_template=tt,
        **kwargs
    ).set_color_by_tex(
        r'\mu_1', sol.CRIMSON_RED
    ).set_color_by_tex(
        r'\mu_2', sol.ROYAL_BLUE
    ).set_color_by_tex(
        r'\coloredn', sol.FOREST_GREEN
    ).set_color_by_tex(
        r'\coloredeps', sol.CRIMSON_RED
    ).set_color_by_tex(
        r'\coloredt', sol.ROYAL_BLUE
    )

class ThreeCardStack(Group):
    def __init__(self, permutation, z_index=1, **kwargs):
        super().__init__(z_index=1, **kwargs)

        cards = [ Rectangle(color=sol.BASE02, height=0.5, width=1.5) for i in range(3) ]

        cards[0].set_fill(sol.CRIMSON_RED, opacity=1)
        cards[1].set_fill(sol.ROYAL_BLUE, opacity=1)
        cards[2].set_fill(sol.FOREST_GREEN, opacity=1)

        for i in range(3):
            cards[i].add(DecimalNumber(i+1, num_decimal_places=0, color=sol.BASE3).next_to(cards[i], ORIGIN))

        a, b, c = (i-1 for i in permutation)

        cards[b].move_to(ORIGIN)
        cards[a].next_to(cards[b], UP, buff=0)
        cards[c].next_to(cards[b], DOWN, buff=0)

        self.occlusion = Square(color=sol.BASE2, stroke_width=0, side_length=1.55)
        self.occlusion.set_fill(sol.BASE2, opacity=0)
        self.opacity=0

        self.add(*cards)
        self.add(self.occlusion)

    def set_percentage(self, percentage):
        self.occlusion.set_fill(sol.BASE2, opacity=1-np.power(percentage,1/4))

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
            self.play(
                *(percentages[c].animate.set_value(new_percentages[c]) for c in cardstacks.keys()),
                *(Indicate(arrowmobjects[a], scale_factor=1.1, color=sol.BASE01) for a in used_arrows)
            )

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

        self.play(
            LaggedStart(
                FadeIn(cardstacks[(1,2,3)], shift=LEFT),
                FadeIn(cardstacks[(2,1,3)], shift=LEFT),
                FadeIn(cardstacks[(2,3,1)], shift=LEFT),
                FadeIn(cardstacks[(1,3,2)], shift=LEFT),
                FadeIn(cardstacks[(3,1,2)], shift=LEFT),
                FadeIn(cardstacks[(3,2,1)], shift=LEFT)
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
        step_markov_chain()
        self.wait()
        step_markov_chain()
        self.wait()
        step_markov_chain()
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

        oldtext = Tex(
            r'Original Network',
            color=sol.BASE03,
            font_size=70
        ).shift(3.5*LEFT + 2.75*DOWN)

        newtext = Tex(
            r'Reversed Network',
            color=sol.BASE03,
            font_size=70
        ).shift(3.5*RIGHT + 2.75*DOWN)

        equality = MyMathTex(
            r'\mathrm{d}^\text{top-to-random}_{{\coloredn}}({{\coloredt}}) = \mathrm{d}^\text{random-to-top}_{{\coloredn}}({{\coloredt}})',
            font_size=80
        ).shift(2.75*DOWN)

        grouptext = Tex(
            r'Why? This is a \emph{random walk on a group}, specifically the symmetric group $S_n$.',
            font_size=35,
            color=sol.BASE01
        ).shift(3.25*UP)

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
            FadeOut(oldtext, shift=8*LEFT),
            FadeOut(newtext, shift=8*RIGHT),
            FadeIn(equality, scale=0.25)
        )

        self.play(FadeIn(grouptext, shift=DOWN))

        self.wait(5)