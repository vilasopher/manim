from manim import *
from random_walker import *

class Walk(Scene):
    def construct(self):
        g = Graph([1,2,3,4], [(1,2),(2,3),(3,4),(4,1)])
        rw = RandomWalker(g, 1)

        self.add(rw)

        for _ in range(6):
            self.play(rw.animate.step())
