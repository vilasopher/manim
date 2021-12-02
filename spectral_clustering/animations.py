from manim import *
from manim_presentation import Slide
from random import seed, choice, randint, random
from numpy.linalg import norm, det
from numpy import array, average, transpose
from numpy.ma import outer
from itertools import combinations
from math import sqrt

seed(0)

num_clusters = 3
add_prob = 0.04
remove_prob = 0.02

ncounts = [ randint(8,10) for _ in range(num_clusters) ]

nodes = [ (i,j) for i in range(num_clusters) for j in range(ncounts[i]) ]

original_edges  = [ (a,b) for a in nodes for b in nodes
                    if a[0] == b[0] and a[1] < b[1] ]
edges_to_add    = [ (a,b) for a in nodes for b in nodes
                    if a[0] != b[0] and random() < add_prob ] 
edges_to_remove = [ e for e in original_edges if random() < remove_prob ]
edges = [ e for e in original_edges + edges_to_add if e not in edges_to_remove ]

def vecs(g):
    return { v : np.array(g[v].get_center()[:-1]) for v in nodes }

def Q(g):
    vp = vecs(g)
    distsq = [ norm(vp[x] - vp[y]) ** 2 for x in nodes for y in nodes if (x,y) in edges ]
    return 0.69 * sum(distsq) / 304 

class Slide1_QuadraticPlacement(Slide):
    def construct(self):
        g = Graph(nodes, edges, 
                  layout='random', 
                  edge_config = { 'stroke_color' : GRAY },
                  layout_scale=3)
        g.move_to(3.5 * LEFT)

        template = TexTemplate()
        template.add_to_preamble(r'\usepackage{amsmath}')

        q_equation = MathTex(r'Q_d(\mathbf{r}_1, \dotsc, \mathbf{r}_n) = \sum_{i<j} \| \mathbf{r}_i - \mathbf{r}_j \|^2', tex_template=template)
        q_equation.move_to(3.5 * RIGHT + 2.5 * UP)

        q_label = MathTex(r'Q_d =')
        q_label.move_to(1.2 * RIGHT + 1.2 * UP)

        q_value = DecimalNumber(
                Q(g),
                )
        q_value.add_updater(lambda d : d.set_value(Q(g)))
        q_value.move_to(2.3 * RIGHT + 1.2 * UP)

        eigenvalues = MathTex(r'= \lambda_1 + \dotsb + \lambda_d')
        eigenvalues.move_to(4.6 * RIGHT + 1.2 * UP)

        matrixbars1 = Matrix([[0,0],[0,0],[0,0],[0,0]])
        matrixbars1.move_to(1.75 * RIGHT + 1.5 * DOWN)

        matrixbars2 = Matrix([[0,0],[0,0],[0,0],[0,0]])
        matrixbars2.move_to(5.25 * RIGHT + 1.5 * DOWN)

        occlusion1 = Rectangle(width=1.8,height=3)
        occlusion1.set_fill(BLACK, opacity=1)
        occlusion1.set_stroke(BLACK)
        occlusion1.move_to(1.75 * RIGHT + 1.5 * DOWN)

        equals = MathTex(r'=')
        equals.move_to(3.5 * RIGHT + 1.5 * DOWN)

        occlusion2 = Rectangle(width=1.8,height=3)
        occlusion2.set_fill(BLACK, opacity=1)
        occlusion2.set_stroke(BLACK)
        occlusion2.move_to(5.25 * RIGHT + 1.5 * DOWN)

        uvecs = MathTex(r'\mathbf{u}_1 \dotsb \mathbf{u}_d')
        uvecs.move_to(5.25 * RIGHT + 1.5 * DOWN)

        r1 = MathTex(r'\mathbf{r}_1')
        vdots = MathTex(r'\vdots', font_size=60)
        rn = MathTex(r'\mathbf{r}_n')
        r1.move_to(1.75 * RIGHT + 0.3 * DOWN)
        vdots.move_to(1.75 * RIGHT + 1.5 * DOWN)
        rn.move_to(1.75 * RIGHT + 2.7 * DOWN)

        horizline1 = Line()
        horizline1.move_to(r1)
        horizlinen = Line()
        horizlinen.move_to(rn)

        vertline1 = Line(start = 1.5 * UP, end = 1.5 * DOWN)
        vertline1.move_to(4.6 * RIGHT + 1.5 * DOWN)
        vertlined = Line(start = 1.5 * UP, end = 1.5 * DOWN)
        vertlined.move_to(5.9 * RIGHT + 1.5 * DOWN)

        rocclusion = Rectangle(width=0.5, height=3)
        rocclusion.set_fill(BLACK, opacity=1)
        rocclusion.set_stroke(BLACK)
        rocclusion.move_to(1.75 * RIGHT + 1.5 * DOWN)

        uocclusion = Rectangle(width=1.8, height=0.5)
        uocclusion.set_fill(BLACK, opacity=1)
        uocclusion.set_stroke(BLACK)
        uocclusion.move_to(5.25 * RIGHT + 1.5 * DOWN)

        occlusionleft = Rectangle(width=3, height=3.5)
        occlusionleft.set_fill(BLACK, opacity=1)
        occlusionleft.set_stroke(BLACK)
        occlusionleft.move_to(1.75 * RIGHT + 1.5 * DOWN)

        occlusionright = Rectangle(width=4, height=3.5)
        occlusionright.set_fill(BLACK, opacity=1)
        occlusionright.set_stroke(BLACK)
        occlusionright.move_to(5.255 * RIGHT + 1.5 * DOWN)

        ###################################################

        # self.add(g, q_equation, q_label, q_value,
        #         eigenvalues, matrixbars1, matrixbars2, occlusion1, occlusion2, equals,
        #         horizline1, horizlinen, rocclusion, r1, vdots, rn,
        #         vertline1, vertlined, uocclusion, uvecs)

        self.add(matrixbars1, occlusion1, horizline1, horizlinen, rocclusion, r1, vdots, rn,
                 equals, matrixbars2, occlusion2, vertline1, vertlined, uocclusion, uvecs)
        self.add(occlusionleft, occlusionright)


        self.play(Create(g))
        self.wait()
        self.pause()
        
        self.play(Write(q_equation))
        self.wait()
        self.pause()

        self.play(FadeIn(q_label, shift=UP), FadeIn(q_value, shift=UP))
        self.wait()
        self.pause()

        self.play(g.animate.change_layout('spectral', layout_scale=3).move_to(5 * LEFT),
                  run_time=10)
        self.wait()
        self.pause()
        
        self.play(FadeIn(eigenvalues, shift=LEFT))
        self.wait()
        self.pause()

        self.play(FadeOut(occlusionleft))
        self.wait()
        self.pause()

        self.play(FadeOut(occlusionright))
        self.wait()
        self.pause()

class Slide2_kMeans(Slide):
    def construct(self):
        pass
