from manim import *

class Labels(Scene):
    def construct(self):

        g = Graph([0,1], [(0,1)], layout='kamada_kawai')
        h = Graph([0],[], labels={ 0 : 'a' }, layout='kamada_kawai')

        self.play(Create(g))
        self.wait()
        self.play(Create(h))
        self.wait()
