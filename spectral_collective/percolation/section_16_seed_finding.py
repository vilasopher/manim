from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from more_graphs import PercolatingGraph, HPGraph, HPGrid
from glitch import Glitch, GlitchEdges, GlitchPercolate
from translucent_box import TranslucentBox
from duality import Duality, convert_edge
import random

class CircuitAbstract(Scene):
    def construct_abstract(self, seed):
        random.seed(seed)
        g = Duality((24, 14), 0.3)
        g.percolate(0.5)
        g.primal.dramatically_highlight_ball((0,0))

        self.add(g)

class C0(CircuitAbstract):
    def construct(self):
        self.construct_abstract(0)
        
class C1(CircuitAbstract):
    def construct(self):
        self.construct_abstract(1)

class C2(CircuitAbstract):
    def construct(self):
        self.construct_abstract(2)

class C3(CircuitAbstract):
    def construct(self):
        self.construct_abstract(4)
        
class C4(CircuitAbstract):
    def construct(self):
        self.construct_abstract(4)

class C5(CircuitAbstract):
    def construct(self):
        self.construct_abstract(5)

class C6(CircuitAbstract):
    def construct(self):
        self.construct_abstract(6)

class C7(CircuitAbstract):
    def construct(self):
        self.construct_abstract(7)
        
class C8(CircuitAbstract):
    def construct(self):
        self.construct_abstract(8)

class C9(CircuitAbstract):
    def construct(self):
        self.construct_abstract(9)

class C10(CircuitAbstract):
    def construct(self):
        self.construct_abstract(10)
        
class C11(CircuitAbstract):
    def construct(self):
        self.construct_abstract(11)

class C12(CircuitAbstract):
    def construct(self):
        self.construct_abstract(12)

class C13(CircuitAbstract):
    def construct(self):
        self.construct_abstract(14)
        
class C14(CircuitAbstract):
    def construct(self):
        self.construct_abstract(14)

class C15(CircuitAbstract):
    def construct(self):
        self.construct_abstract(15)

class C16(CircuitAbstract):
    def construct(self):
        self.construct_abstract(16)

class C17(CircuitAbstract):
    def construct(self):
        self.construct_abstract(17)
        
class C18(CircuitAbstract):
    def construct(self):
        self.construct_abstract(18)

class C19(CircuitAbstract):
    def construct(self):
        self.construct_abstract(19)

class C20(CircuitAbstract):
    def construct(self):
        self.construct_abstract(20)
        
class C21(CircuitAbstract):
    def construct(self):
        self.construct_abstract(21)

class C22(CircuitAbstract):
    def construct(self):
        self.construct_abstract(22)

class C23(CircuitAbstract):
    def construct(self):
        self.construct_abstract(24)
        
class C24(CircuitAbstract):
    def construct(self):
        self.construct_abstract(24)

class C25(CircuitAbstract):
    def construct(self):
        self.construct_abstract(25)

class C26(CircuitAbstract):
    def construct(self):
        self.construct_abstract(26)

class C27(CircuitAbstract):
    def construct(self):
        self.construct_abstract(27)
        
class C28(CircuitAbstract):
    def construct(self):
        self.construct_abstract(28)

class C29(CircuitAbstract):
    def construct(self):
        self.construct_abstract(29)

class C30(CircuitAbstract):
    def construct(self):
        self.construct_abstract(30)
        
class C31(CircuitAbstract):
    def construct(self):
        self.construct_abstract(31)

class C32(CircuitAbstract):
    def construct(self):
        self.construct_abstract(32)

class C33(CircuitAbstract):
    def construct(self):
        self.construct_abstract(34)
        
class C34(CircuitAbstract):
    def construct(self):
        self.construct_abstract(34)

class C35(CircuitAbstract):
    def construct(self):
        self.construct_abstract(35)

class C36(CircuitAbstract):
    def construct(self):
        self.construct_abstract(36)

class C37(CircuitAbstract):
    def construct(self):
        self.construct_abstract(37)
        
class C38(CircuitAbstract):
    def construct(self):
        self.construct_abstract(38)

class C39(CircuitAbstract):
    def construct(self):
        self.construct_abstract(39)
