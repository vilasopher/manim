from manim import *
from manim_presentation import Slide
from random import seed, choice, randint, random, sample
from numpy.linalg import norm, det
from numpy import array, average, transpose, pad
from numpy.ma import outer
from itertools import combinations
from math import sqrt, inf
import networkx as nx

seed(0)

notifier = Dot(color=DARK_GRAY, radius=0.05)
notifier.move_to(7 * RIGHT + 3.9 * DOWN)

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
    return { v : array(g[v].get_center()[:-1]) for v in nodes }

def Q(g):
    vp = vecs(g)
    distsq = [ norm(vp[x] - vp[y]) ** 2 for x in nodes for y in nodes if (x,y) in edges ]
    return 0.69 * sum(distsq) / 304 

def kmeans_objective(g, clusters):
    vp = vecs(g)
    ds = g._graph.degree

    volumes = { k : sum([ ds[v] for v in clusters[k] ]) for k in clusters.keys() }
    centers = { k : sum([ ds[v] * vp[v] for v in clusters[k] ]) / volumes[k]
                                                        for k in clusters.keys() }

    objectives = { k : sum([ ds[v] * norm(vp[v] - centers[k]) ** 2 for v in clusters[k]])
                                                        for k in clusters.keys() }
    objective = sum([ objectives[k] for k in clusters.keys() ])

    return objective / 100
    

def kmeans_step(g, clusters):
    vp = vecs(g)
    ds = g._graph.degree

    volumes = { k : sum([ ds[v] for v in clusters[k] ]) for k in clusters.keys() }
    centers = { k : sum([ ds[v] * vp[v] for v in clusters[k] ]) / volumes[k]
                                                        for k in clusters.keys() }

    newclusters =  { k : [] for k in clusters.keys() }

    for v in nodes:
        argminsofar = None
        minsofar    = inf

        for k in clusters.keys():
            dist = norm(vp[v] - centers[k])
            if dist < minsofar:
                argminsofar = k
                minsofar = dist

        newclusters[argminsofar].append(v)

    return newclusters

randomlayout = { v : 4 * LEFT + (random() * 6 - 3) * UP + (random() * 6 - 3) * RIGHT
                                                                            for v in nodes }
GRAPH = nx.Graph()
GRAPH.add_nodes_from(nodes)
GRAPH.add_edges_from(edges)
nxspectrallayout = nx.spectral_layout(GRAPH)
spectrallayout = { v : 3 * pad(nxspectrallayout[v],(0,1)) + 4 * LEFT for v in nodes }

class Slide1_QuadraticPlacement(Slide):
    def noticewait(self):
        self.add(notifier)
        self.wait()
        self.pause()
        self.remove(notifier)

    def construct(self):
        g = Graph(nodes, edges, 
                  layout=randomlayout,
                  edge_config = { 'stroke_color' : GRAY })

        template = TexTemplate()
        template.add_to_preamble(r'\usepackage{amsmath}')

        q_equation = MathTex(r'Q_d(\mathbf{r}_1, \dotsc, \mathbf{r}_n) = \sum_{i<j} w_{ij} \| \mathbf{r}_i - \mathbf{r}_j \|^2', tex_template=template)
        q_equation.move_to(3.3 * RIGHT + 2.5 * UP)

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
        matrixbars1.move_to(0.8 * RIGHT + 1.5 * DOWN)

        matrixbars2 = Matrix([[0,0],[0,0],[0,0],[0,0]])
        matrixbars2.move_to(5.25 * RIGHT + 1.5 * DOWN)

        occlusion1 = Rectangle(width=1.8,height=3)
        occlusion1.set_fill(BLACK, opacity=1)
        occlusion1.set_stroke(BLACK)
        occlusion1.move_to(0.8 * RIGHT + 1.5 * DOWN)

        equals = MathTex(r'= \mathbf{D}^{-1/2}')
        equals.move_to(3 * RIGHT + 1.5 * DOWN)

        occlusion2 = Rectangle(width=1.8,height=3)
        occlusion2.set_fill(BLACK, opacity=1)
        occlusion2.set_stroke(BLACK)
        occlusion2.move_to(5.25 * RIGHT + 1.5 * DOWN)

        uvecs = MathTex(r'\mathbf{u}_1 \dotsb \mathbf{u}_d')
        uvecs.move_to(5.25 * RIGHT + 1.5 * DOWN)

        r1 = MathTex(r'\mathbf{r}_1^*')
        vdots = MathTex(r'\vdots', font_size=60)
        rn = MathTex(r'\mathbf{r}_n^*')
        r1.move_to(0.8 * RIGHT + 0.3 * DOWN)
        vdots.move_to(0.8 * RIGHT + 1.5 * DOWN)
        rn.move_to(0.8 * RIGHT + 2.7 * DOWN)

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
        rocclusion.move_to(0.8 * RIGHT + 1.5 * DOWN)

        uocclusion = Rectangle(width=1.8, height=0.5)
        uocclusion.set_fill(BLACK, opacity=1)
        uocclusion.set_stroke(BLACK)
        uocclusion.move_to(5.25 * RIGHT + 1.5 * DOWN)

        occlusionleft = Rectangle(width=2.7, height=3.5)
        occlusionleft.set_fill(BLACK, opacity=1)
        occlusionleft.set_stroke(BLACK)
        occlusionleft.move_to(0.7 * RIGHT + 1.5 * DOWN)

        occlusionright = Rectangle(width=5, height=3.5)
        occlusionright.set_fill(BLACK, opacity=1)
        occlusionright.set_stroke(BLACK)
        occlusionright.move_to(4.6 * RIGHT + 1.5 * DOWN)

        ###################################################

        # self.add(g, q_equation, q_label, q_value,
        #          eigenvalues, matrixbars1, matrixbars2, occlusion1, occlusion2, equals,
        #          horizline1, horizlinen, rocclusion, r1, vdots, rn,
        #          vertline1, vertlined, uocclusion, uvecs)

        # return

        self.add(matrixbars1, occlusion1, horizline1, horizlinen, rocclusion, r1, vdots, rn,
                 equals, matrixbars2, occlusion2, vertline1, vertlined, uocclusion, uvecs)
        self.add(occlusionleft, occlusionright)


        self.play(Create(g), run_time=3)
        self.noticewait()
        
        self.play(Write(q_equation))
        self.noticewait()

        self.play(FadeIn(q_label, shift=UP), FadeIn(q_value, shift=UP))
        self.noticewait()

        self.play(g.animate.change_layout(spectrallayout),
                  run_time=10, rate_func=rate_functions.smooth)
        self.noticewait()
        
        self.play(FadeIn(eigenvalues, shift=LEFT))
        self.noticewait()

        self.play(FadeOut(occlusionleft))
        self.noticewait()

        self.play(FadeOut(occlusionright))
        self.noticewait()

        self.wait()



class Slide2_kMeans(Slide):
    def noticewait(self):
        self.add(notifier)
        self.wait()
        self.pause()
        self.remove(notifier)

    def construct(self):
        g = Graph(nodes, edges, 
                  layout=spectrallayout, 
                  edge_config = { 'stroke_color' : GRAY })

        template = TexTemplate()
        template.add_to_preamble(r'\usepackage{amsmath}')
        variance_equation = MathTex(r'S_k^2(\mathbf{r}_1, \dotsc, \mathbf{r}_n) = \min_{(V_1,\dotsc,V_k) \in \mathcal{P}_k} \sum_{i=1}^k \sum_{j \in V_i} d_j \| \mathbf{r}_j - \mathbf{c}_i \|^2',
                                    tex_template=template)
        variance_equation.move_to(1.7 * RIGHT + 2.5 * UP)

        variance_label = MathTex(r'S_k^2 \leq ')
        variance_label.move_to(2 * RIGHT + 0.5 * UP)

        clusters = { k : [ nodes[i] for i in range(len(nodes)) if i % 3 == k ] for k in range(3) }
        colors = [ RED, GREEN, BLUE ]

        variance_value = DecimalNumber(kmeans_objective(g, clusters))
        variance_value.move_to(3.2 * RIGHT + 0.5 * UP)

        nphard = Tex(r'Computing $S_k^2$ is NP-hard in general!')
        nphard.move_to(2.5 * RIGHT + 1 * DOWN)

        bound = MathTex(r'S_{2^d}^2 \leq \frac{\lambda_1 + \dotsb + \lambda_d}{\lambda_{d+1}}')
        bound.move_to(2 * RIGHT + 2.5 * DOWN)

        #######################################################

        self.add(g)
        self.wait()
        self.noticewait()

        self.play(Write(variance_equation))
        self.noticewait()

        h = Graph(nodes, edges, 
                  layout=spectrallayout, 
                  edge_config = { 'stroke_color' : DARKER_GRAY })

        self.play(Transform(g,h))
        self.noticewait()

        h = Graph(nodes, edges, 
                  vertex_config = { v : { 'fill_color' : colors[k] }
                                    for k in range(3) for v in clusters[k] },
                  layout=spectrallayout, 
                  edge_config = { 'stroke_color' : DARKER_GRAY })

        self.play(Transform(g,h))
        self.noticewait()

        self.play(FadeIn(variance_label, shift=RIGHT))
        self.play(Write(variance_value))
        self.noticewait()

        for _ in range(4):
            clusters = kmeans_step(g, clusters)
            h = Graph(nodes, edges, 
                      vertex_config = { v : { 'fill_color' : colors[k] }
                                        for k in range(3) for v in clusters[k] },
                      layout=spectrallayout, 
                      edge_config = { 'stroke_color' : DARKER_GRAY })

            dec = DecimalNumber(kmeans_objective(g,clusters))
            dec.move_to(3.2 * RIGHT + 0.5 * UP)
        
            self.play(Transform(g,h))
            self.play(Transform(variance_value, dec))
            self.noticewait()

        h = Graph(nodes, edges, 
                  layout=spectrallayout, 
                  edge_config = { 'stroke_color' : DARKER_GRAY })

        self.play(Transform(g,h), FadeOut(variance_label), FadeOut(variance_value))
        self.noticewait()

        shuf = [nodes[0]] + [nodes[2]] + [nodes[1]] + nodes[3:]
        clusters = { k : [ shuf[i] for i in range(len(shuf)) if i % 3 == k ] for k in range(3) }       

        variance_value = DecimalNumber(kmeans_objective(g, clusters))
        variance_value.move_to(3.2 * RIGHT + 0.5 * UP)

        h = Graph(nodes, edges, 
                  vertex_config = { v : { 'fill_color' : colors[k] }
                                    for k in range(3) for v in clusters[k] },
                  layout=spectrallayout,
                  edge_config = { 'stroke_color' : DARKER_GRAY })

        self.play(Transform(g,h))
        self.noticewait()

        self.play(FadeIn(variance_label, shift=RIGHT))
        self.play(Write(variance_value))
        self.noticewait()

        for _ in range(2):
            clusters = kmeans_step(g, clusters)
            h = Graph(nodes, edges, 
                      vertex_config = { v : { 'fill_color' : colors[k] }
                                        for k in range(3) for v in clusters[k] },
                      layout=spectrallayout, 
                      edge_config = { 'stroke_color' : DARKER_GRAY })

            dec = DecimalNumber(kmeans_objective(g,clusters))
            dec.move_to(3.2 * RIGHT + 0.5 * UP)
        
            self.play(Transform(g,h))
            self.play(Transform(variance_value, dec))
            self.noticewait()

        self.play(Write(nphard))
        self.noticewait()
        
        self.play(Write(bound))
        self.noticewait()
        self.wait()
