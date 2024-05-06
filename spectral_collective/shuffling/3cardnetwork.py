from manim import *
import solarized as sol

class ThreeCardStack(Group):
    def __init__(self, permutation):
        super().__init__()

        cards = [ Rectangle(color=sol.BASE01, height=0.5, width=1.5) for i in range(3) ]

        cards[0].set_fill(sol.RED, opacity=1)
        cards[1].set_fill(sol.GREEN, opacity=1)
        cards[2].set_fill(sol.BLUE, opacity=1)

        for i in range(3):
            cards[i].add(DecimalNumber(i+1, num_decimal_places=0, color=sol.BASE3).next_to(cards[i], ORIGIN))

        a, b, c = (i-1 for i in permutation)

        cards[b].move_to(ORIGIN)
        cards[a].next_to(cards[b], UP, buff=0)
        cards[c].next_to(cards[b], DOWN, buff=0)

        self.add(*cards)

class ThreeCardNetwork(Scene):
    def construct(self):
        cardstacks = {
            (1,2,3) : ThreeCardStack([1,2,3]).move_to([-2,0,0]),
            (3,1,2) : ThreeCardStack([3,1,2]).move_to([-5,2.5,0]),
            (2,3,1) : ThreeCardStack([2,3,1]).move_to([-5,-2.5,0]),
            (2,1,3) : ThreeCardStack([2,1,3]).move_to([2,0,0]),
            (1,3,2) : ThreeCardStack([1,3,2]).move_to([5,2.5,0]),
            (3,2,1) : ThreeCardStack([3,2,1]).move_to([5,-2.5,0])
        }

        arrows = [
            [(a,b,c),(b,d,e)]
            for a in range(1,4)
            for b in range(1,4)
            for c in range(1,4)
            for d in range(1,4)
            for e in range(1,4)
            if a != b and b != c and a != c 
            and (d == a and e == c or d == c and e == a)
        ]

        for a in arrows:
            start = cardstacks[a[0]].get_center()
            end = cardstacks[a[1]].get_center()
            mid = start + 1.5 * (end - start) / 2
            self.add(Line(start,end,color=sol.BASE1,stroke_width=6))
            self.add(Arrow(start,mid,color=sol.BASE1))

        self.add(*cardstacks.values())