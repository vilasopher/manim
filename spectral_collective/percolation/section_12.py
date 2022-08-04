from manim import *
import grid as gr
import solarized as sol
import networkx as nx
from more_graphs import PercolatingGraph, HPGraph, HPGrid
from glitch import Glitch, GlitchEdges, GlitchPercolate
from translucent_box import TranslucentBox
import random

class KolmogorovOLD(Scene):
    def construct(self):
        temp = TexTemplate()
        temp.add_to_preamble(r'\usepackage[margin=0in]{geometry}')

        lem = MathTex(
            r'\textbf{Lemma: } '
            r'&\mathbb{P}_{{p}}[\text{there is an infinite cluster}] = 0'
            r'\Leftrightarrow'
            r'\mathbb{P}_{{p}}[\text{the cluster of } o \text{ is infinite}]=0 \\',
            r'\text{and }'
            r'&\mathbb{P}_{{p}}[\text{there is an infinite cluster}] = 1'
            r'\Leftrightarrow'
            r'\mathbb{P}_{{p}}[\text{the cluster of } o \text{ is infinite}]>0.',
            color=sol.BASE03,
            tex_template=temp,
            font_size=36
        ).move_to(3.05 * UP).set_color_by_tex(r'p', sol.RED)
        lembox = TranslucentBox(lem)
        self.add(lembox, lem)

        temp2 = TexTemplate()
        temp2.add_to_preamble(r'\usepackage[margin=1.5in]{geometry}')
        temp2.add_to_preamble(r'\usepackage[document]{ragged2e}')
        temp2.add_to_preamble(r'\usepackage[english]{babel}')
        temp2.add_to_preamble(r'\usepackage{amsmath}')
        proof = Tex(
            r'\raggedright'
            r'\setlength{\abovedisplayskip}{5pt}'
            r'\setlength{\belowdisplayskip}{5pt}'
            r'\textbf{\emph{Proof:}} First, notice that the event '
            r'$\{ \text{there is an infinite cluster} \}$'
            r' is a \emph{tail event}, i.e. it does not depend'
            r' on the state of any finite set of edges in the grid.'
            r" Therefore, by \emph{Kolmogorov's Zero-One Law},",
            r' for any parameter value $p$ we have ',
            r'$\mathbb{P}_p[\text{there is an infinite cluster}]=0\text{ or }1.$'
            r'\\ \hfill \\ \vspace{-0.1cm}'

            r'Now, suppose that '
            r'$\mathbb{P}_p[\text{the cluster of }o\text{ is infinite}]>0$. '
            r'Then, since'
            r'\begin{align*}'
            r'\{\text{the cluster of } o \text{ is infinite}\}'
            r'&\subseteq'
            r'\{\text{there is an infinite cluster}\}, \text{we have} \\'
            r'0 < \mathbb{P}_p[\text{the cluster of } o \text{ is infinte}]'
            r'&\leq \mathbb{P}_p[\text{there is an infinite cluster}].'
            r'\end{align*}'
            r'So we must have '
            r'$\mathbb{P}_p[\text{there is an infinite cluster}] = 1$ '
            r'by the Zero-One law.'
            r'\\ \hfill \\ \vspace{-0.1cm}'

            r'On the other hand, suppose that '
            r'$\mathbb{P}_p[\text{the cluster of }o\text{ is infinite}]=0$. '
            r'Then, since the percolation does not depend on the choice of origin, '
            r'for any node $v$ of the grid '
            r'we have $\mathbb{P}_p[\text{the cluster of }v\text{ is infinite}]=0$. '
            r'If there is an infinite cluster somewhere in the grid, then there is '
            r'some node $v$ whose cluster is infinite. '
            r'Thus, by countable additivity of probability '
            r'(the grid is countable), we obtain '
            r'$\mathbb{P}_p[\text{there is an infinite cluster}]=0$.'
            r'\hfill $\blacksquare$'
            ,color=sol.BASE03,
            tex_template = temp2,
            font_size = 33
        )
        proof.shift(0.75 * DOWN)
        self.add(proof)

class PPP(Scene):
    def construct(self):
        p = MathTex(r'p', color=sol.RED, font_size = 33).shift(RIGHT)
        pp = MathTex(r'\mathbb{P}_{{p}}', color=sol.BASE03, font_size = 33).shift(LEFT)
        pp.set_color_by_tex(r'p', sol.RED)
        self.add(p, pp)

class GlitchWholeRootedGrid(Scene):
    def construct(self):
        g = HPGrid.from_grid((24, 14), 0.3,
            vertex_config = {'fill_color' : sol.BASE00},
            edge_config = {'stroke_color' : sol.BASE1}
        )
        g.highlight_subgraph(
            [(0,0)],
            node_colors = { (0,0) : sol.ROOT },
            nodes_to_scale = [(0,0)],
            scale_factor = 2
        )

        self.play(GlitchEdges(g), run_time=0.5)

class Origin(Scene):
    def construct(self):
        g = HPGrid.from_grid((24, 14), 0.3)

        self.wait()

        self.play(FadeIn(g))

        self.wait()

        self.play(
            g.animate.highlight_subgraph(
                [(0,0)],
                node_colors = { (0,0) : sol.ROOT },
                nodes_to_scale = [(0,0)],
                scale_factor = 2
            )
        )

        self.wait(3)

class OriginClusterSuper1(Scene):
    def construct(self):
        g = HPGrid.from_grid((24, 14), 0.3)
        g.percolate(0.52)
        g.dramatically_highlight_ball((0,0))

        self.play(GlitchEdges(g), run_time=0.25)
        self.wait(2.5)
        self.play(GlitchEdges(g), run_time=0.25)

class OriginClusterSuper2(OriginClusterSuper1):
    pass

class OriginClusterSuper3(OriginClusterSuper1):
    pass

class OriginClusterSuper4(OriginClusterSuper1):
    pass

class OriginClusterSuper5(OriginClusterSuper1):
    pass

class OriginClusterSuper6(OriginClusterSuper1):
    pass

class OriginClusterSuper7(OriginClusterSuper1):
    pass

class OriginClusterSuper8(OriginClusterSuper1):
    pass

class OriginClusterSuper9(OriginClusterSuper1):
    pass

class OriginClusterSuper0(OriginClusterSuper1):
    pass

class OriginClusterSub1(Scene):
    def construct(self):
        g = HPGrid.from_grid((24, 14), 0.3)
        g.percolate(0.45)
        g.dramatically_highlight_ball((0,0))

        self.play(GlitchEdges(g), run_time=0.25)
        self.wait(2.5)
        self.play(GlitchEdges(g), run_time=0.25)

class OriginClusterSub2(OriginClusterSub1):
    pass

class OriginClusterSub3(OriginClusterSub1):
    pass

class OriginClusterSub4(OriginClusterSub1):
    pass

class OriginClusterSub5(OriginClusterSub1):
    pass

class OriginClusterSub6(OriginClusterSub1):
    pass

class OriginClusterSub7(OriginClusterSub1):
    pass

class OriginClusterSub8(OriginClusterSub1):
    pass

class OriginClusterSub9(OriginClusterSub1):
    pass

class OriginClusterSub0(OriginClusterSub1):
    pass

class OriginPathAnimation1(Scene):
    def construct(self):
        g = HPGrid.from_grid((24, 14), 0.3)
        g.percolate(0.52)
        g.dramatically_highlight_ball((0,0))

        self.play(GlitchEdges(g), run_time=0.25)
        self.wait(2)
        self.play(g.animate.highlight_path_to_boundary_from((0,0)))
        self.wait()
        self.play(GlitchEdges(g), run_time=0.25)

class OriginPathAnimation2(OriginPathAnimation1):
    pass

class OriginPathAnimation3(OriginPathAnimation1):
    pass

class OriginPathAnimation4(OriginPathAnimation1):
    pass

class OriginPathAnimation5(OriginPathAnimation1):
    pass

class OriginPathAnimation6(OriginPathAnimation1):
    pass

class OriginPathAnimation7(OriginPathAnimation1):
    pass

class OriginPathAnimation8(OriginPathAnimation1):
    pass

class OriginPathAnimation9(OriginPathAnimation1):
    pass

class OriginPathAnimation0(OriginPathAnimation1):
    pass

class OriginPath1(Scene):
    def construct(self):
        g = HPGrid.from_grid((24, 14), 0.3)
        g.percolate(0.52)
        g.dramatically_highlight_ball((0,0))
        g.highlight_path_to_boundary_from((0,0))

        self.play(GlitchEdges(g), run_time=0.25)
        self.wait(2.5)
        self.play(GlitchEdges(g), run_time=0.25)

class OriginPath2(OriginPath1):
    pass

class OriginPath3(OriginPath1):
    pass

class OriginPath4(OriginPath1):
    pass

class OriginPath5(OriginPath1):
    pass

class OriginPath6(OriginPath1):
    pass

class OriginPath7(OriginPath1):
    pass

class OriginPath8(OriginPath1):
    pass

class OriginPath9(OriginPath1):
    pass

class OriginPath0(OriginPath1):
    pass
