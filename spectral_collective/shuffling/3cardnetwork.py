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

    def set_opacity(self, opacity):
        self.opacity = opacity
        self.occlusion.set_fill(sol.BASE02, opacity=1-opacity)
    
    def get_opacity(self):
        return self.opacity

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
            *(cardstacks[c].animate.set_opacity(0) for c in cardstacks.keys() if c != (1,2,3)),
            *(FadeToColor(a,sol.BASE02) for a in arrowmobjects.values())
        )

        self.wait()

        percentages = {
            c : DecimalNumber(33, color=sol.BASE3, unit='\%', num_decimal_places=0) for c in cardstacks.keys()
        }

        percentages[(1,2,3)].next_to(cardstacks[(1,2,3)], DOWN)
        percentages[(2,1,3)].next_to(cardstacks[(2,1,3)], DOWN)
        percentages[(3,1,2)].next_to(cardstacks[(3,1,2)], LEFT)
        percentages[(2,3,1)].next_to(cardstacks[(2,3,1)], LEFT)
        percentages[(1,3,2)].next_to(cardstacks[(1,3,2)], RIGHT)
        percentages[(3,2,1)].next_to(cardstacks[(3,2,1)], RIGHT)

        for c in cardstacks.keys():
            percentages[c].set_value(0)
            percentages[c].add_updater(
                lambda x : x.set_value(cardstacks[c].get_opacity() * 100)
            )

        percentages[(1,2,3)].set_value(100)

        self.play(
            *(FadeIn(p) for p in percentages.values())
        )

        self.wait()

        self.play(
            cardstacks[(1,2,3)].animate.set_opacity(1/3),
            cardstacks[(2,3,1)].animate.set_opacity(1/3),
            cardstacks[(2,1,3)].animate.set_opacity(1/3),
        )

        #TODO: make the percentages background value trackers, do everything through them.