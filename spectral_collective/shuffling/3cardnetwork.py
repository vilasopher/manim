from manim import *
import solarized as sol

class ThreeCardStack(Group):
    def __init__(self, permutation, z_index=1, **kwargs):
        super().__init__(z_index=1, **kwargs)

        cards = [ Rectangle(color=sol.BASE3, height=0.5, width=1.5) for i in range(3) ]

        cards[0].set_fill(sol.RED, opacity=1)
        cards[1].set_fill(sol.BLUE, opacity=1)
        cards[2].set_fill(sol.FOREST_GREEN, opacity=1)

        for i in range(3):
            cards[i].add(DecimalNumber(i+1, num_decimal_places=0, color=sol.BASE3).next_to(cards[i], ORIGIN))

        a, b, c = (i-1 for i in permutation)

        cards[b].move_to(ORIGIN)
        cards[a].next_to(cards[b], UP, buff=0)
        cards[c].next_to(cards[b], DOWN, buff=0)

        self.occlusion = Square(color=sol.BASE02, stroke_width=0, side_length=1.55)
        self.occlusion.set_fill(sol.BASE02, opacity=0)
        self.opacity=0

        self.add(*cards)
        self.add(self.occlusion)

    def set_percentage(self, percentage):
        self.occlusion.set_fill(sol.BASE02, opacity=1-np.power(percentage,1/3))

class ThreeCardNetwork(Scene):
    def construct(self):
        cardstacks = {
            (1,2,3) : ThreeCardStack([1,2,3]).move_to([-2,0,0]),
            (3,1,2) : ThreeCardStack([3,1,2]).move_to([-4.5,2.5,0]),
            (2,3,1) : ThreeCardStack([2,3,1]).move_to([-4.5,-2.5,0]),
            (2,1,3) : ThreeCardStack([2,1,3]).move_to([2,0,0]),
            (1,3,2) : ThreeCardStack([1,3,2]).move_to([4.5,2.5,0]),
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

            mid = start + 1.5 * (end - start) / 2

            am = Group(
                Line(start,end,color=sol.BASE1,stroke_width=6, z_index=-1),
                Arrow(start,mid,color=sol.BASE1, z_index=-1)
            )

            arrowmobjects[a] = am

        self.add(*cardstacks.values())
        self.add(*arrowmobjects.values())

        self.play(
            *(cardstacks[c].animate.set_percentage(0)
                for c in cardstacks.keys() if c != (1,2,3)),
            *(FadeToColor(a,sol.BASE02) 
                for a in arrowmobjects.values())
        )

        self.wait()

        percentages = {
            c : ValueTracker(0) for c in cardstacks.keys()
        }
        percentages[(1,2,3)].set_value(1)

        percentagelabels = {
            c : DecimalNumber(
                percentages[c].get_value() * 100,
                color=sol.BASE3,
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
                    )
            )

        self.play(
            *(FadeIn(p) for p in percentagelabels.values())
        )

        self.wait()


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
                *(Indicate(arrowmobjects[a], scale_factor=1.1, color=sol.BASE2) for a in used_arrows)
            )

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
        self.wait(10)