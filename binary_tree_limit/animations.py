from manim import *
import random
import highlight_ball as hb
import solarized as sol
import binary_tree as bt
import grid as gr
import networkx as nx
import mobject_labeled_bar_chart as mb

random.seed(4)

# In our last video, we presented a notion of graph convergence,
# where sparse sequences of graphs can converge to a graph limit.
# These limits are all random rooted graphs, which are the same thing as 
# probability distributions on the space of rooted graphs.
# [SHOW CLIPS FROM PREVIOUS VIDEO]

class ColorClip(Scene):
    def construct(self):
        return


class PreOpening(Scene):
    def construct(self):
        finite = MathTex(r'g_n', font_size=100, color=sol.NODE)
        arrow = MathTex(r'\longrightarrow', font_size=120, color=sol.NODE)
        limit = MathTex(r'\mathbf{g}^\bullet', font_size=120, color=sol.NODE)

        finite.move_to(2 * LEFT + 0.5 * UP)
        arrow.move_to(0.5 * UP)
        limit.move_to(2 * RIGHT + 0.7 * UP)

        text1 = Tex(r'sparse sequence of graphs', font_size=80, color=sol.NODE)
        text2 = Tex(r'random rooted graph', font_size=80, color=sol.NODE)
        text3 = Tex(r'probability distribution on $\mathcal{G}_D^\bullet$', font_size=80, color=sol.NODE)

        text1.move_to(2.5 * UP)
        text2.move_to(1.25 * DOWN)
        text3.move_to(2.5 * DOWN)


        self.add(finite, arrow, limit, text1, text2, text3)


class Opening(Scene):
    def construct(self):
        g = Graph([0], [],
                  vertex_config=sol.VERTEX_CONFIG,
                  edge_config=sol.EDGE_CONFIG,
                  layout=bt.binary_tree_layout(0))

        # Now, what is the limit of the sequence of complete finite binary trees?

        # 1 sec
        self.play(Create(g))

        # 4 sec
        for depth in range(1,5):
            nodes, edges = bt.binary_tree_layer(depth)
            self.play(g.animate.add_vertices(*nodes, positions=bt.binary_tree_layout(depth)),
                      g.animate.add_edges(*edges))

        # 4.75 sec
        self.wait(4.75)

        # A first guess might be that the limit is the random rooted graph whose value is,
        # with probability 1, the infinite binary tree, rooted at the top.

        text = Tex(r'(with probability $1$)', color=sol.NODE, font_size=100)
        text.move_to(2.75*UP)

        self.play(FadeIn(text, shift=DOWN), run_time=1.2333)


        for depth in range(5,7):
            nodes, edges = bt.binary_tree_layer(depth)
            self.play(g.animate.add_vertices(*nodes, positions=bt.binary_tree_layout(depth)),
                      g.animate.add_edges(*edges), run_time=0.25)

        self.wait(1.15)

        self.play(hb.HighlightBall(g,0,0, fadeout=False), run_time=0.5)

        self.wait(10)


#  After all, this is what happens with the path graphs and grid graphs,
# as we saw before: the limit of the sequence of finite path graphs is an
# infinite path graph rooted in the middle (with probability 1), and the limit 
# of the finite grid graphs is an infinite grid graph, again rooted in the middle (with probability 1). 
# [SHOW SCREENGRABS FROM PREVIOUS VIDEO]

class GridBalls(Scene):
    def construct(self):
        text1 = MathTex(r'B_r[n \times n \text{ grid with uniform random root}]', color=sol.NODE, font_size=60)
        text2 = MathTex(r'B_r[\text{infinite grid, rooted at the origin w.p. } 1]', color=sol.NODE, font_size=60)
        text3 = MathTex(r'\approx', color=sol.NODE, font_size=100)

        text1.move_to(1.5*UP)
        text2.move_to(1.5*DOWN)

        self.play(FadeIn(text1))

        self.wait(0.41666667)

        self.play(FadeIn(text3), run_time=0.83333333)

        self.play(FadeIn(text2))

        self.wait(5)


class Grids(Scene):
    def construct(self):

        occlusionthickness = 100
        occlusionwidth = 4
        occlusionheight = 4
        frame = Rectangle(color=sol.BASE2,
                          stroke_width=10,
                          width=occlusionwidth,
                          height=occlusionwidth)
        occlusion = Rectangle(color=sol.BASE3,
                              stroke_width=occlusionthickness,
                              width=occlusionwidth + occlusionthickness/100,
                              height=occlusionheight + occlusionthickness/100)

        frame.move_to(4*RIGHT + 1*UP)
        occlusion.move_to(4*RIGHT + 1*UP)

        # This is because the balls in the grid graph mostly look like
        # the ball around the origin in the infinite grid.

        grid = Graph(*gr.grid_nodes_edges(12),
                     layout=gr.grid_layout(12, shift=3*LEFT, scale=0.3),
                     vertex_config=sol.LIGHT_VERTEX_CONFIG,
                     edge_config=sol.LIGHT_EDGE_CONFIG)

        infgrid = Graph(*gr.grid_nodes_edges(4))

        infballv, infballe = hb.ball(infgrid, (0,0), 2)

        inf_vertex_config = { (0,0) : { 'fill_color' : sol.ROOT } }
        for i in range(1, len(infballv)):
            inf_vertex_config.update({ n : { 'fill_color' : sol.HIGHLIGHT_NODE } for n in infballv[i] })
        inf_vertex_config.update({ v : { 'fill_color' : sol.LIGHT_NODE } for v in infgrid.vertices if v not in inf_vertex_config.keys() })

        inf_edge_config = { }
        for i in range(len(infballe)):
            inf_edge_config.update({ e : { 'stroke_color' : sol.HIGHLIGHT_EDGE, 'stroke_width' : 6 } for e in infballe[i] })
        inf_edge_config.update({ e : { 'stroke_color' : sol.LIGHT_EDGE, 'stroke_width' : 4 } for e in infgrid.edges if e not in inf_edge_config.keys() })

        infgrid = Graph(*gr.grid_nodes_edges(4),
                        layout=gr.grid_layout(4, shift=4*RIGHT + 1*UP),
                        vertex_config=inf_vertex_config,
                        edge_config=inf_edge_config)


        self.add(infgrid)
        self.add(occlusion, frame)

        self.wait(5)
        
        self.play(Create(grid))

        self.wait(2)

        # More precisely, for any radius R, as the size N of the finite grids go to
        # infinity, the probability that the R-ball around a uniformly random vertex 
        # in the grid is isomorphic to to the R-ball in the infinite grid goes to 1.

        vertexlist = list(grid.vertices)
        boundaryvertices, boundaryedges = gr.grid_boundary(12, 2)

        for _ in range(25):
            v = random.choice(vertexlist)
            color = sol.HIGHLIGHT_NODE

            if v in boundaryvertices:
                color = sol.RED

            self.play(hb.HighlightBall(grid, v, 2, node_highlight_color=color, edge_highlight_color=color))


        # This works because the number of vertices that are within distance R from 
        # the boundary of the grid scales like N, whereas the number of vertices
        # in the interior of the grid scales like N^2.

        self.play(hb.HighlightSubgraph(grid, [boundaryvertices], [boundaryedges], node_highlight_color=[sol.YELLOW]))

        self.wait(1.25)

        fraction = MathTex(r"4 r n - 4 r^2", r"\over", r"n^2", color=config.background_color)
        fraction.set_color_by_tex(r"4 r n - 4 r^2", sol.YELLOW)

        fraction.move_to(4 * RIGHT + 2.5 * DOWN)

        self.play(FadeIn(fraction))

        self.wait(3.2833333333)

        self.play(fraction.animate.set_color_by_tex(r"\over", sol.NODE), run_time=0.5)
        self.play(fraction.animate.set_color_by_tex(r"n^2", sol.NODE), run_time=0.5)

        # So for large enough N, there are far more vertices on the 
        # interior than near the boundary.

        for _ in range(15):
            v = random.choice(vertexlist)
            color = sol.HIGHLIGHT_NODE

            if v in boundaryvertices:
                color = sol.RED

            self.play(hb.HighlightBall(grid, v, 2, node_highlight_color=color, edge_highlight_color=color))


class Trees(Scene):
    def construct(self):
        nxgraph = nx.balanced_tree(2,6)
        g = Graph.from_networkx(nxgraph,
                                vertex_config=sol.VERTEX_CONFIG,
                                edge_config=sol.EDGE_CONFIG,
                                layout=bt.binary_tree_layout(6, shift=2.7*UP))

        # However, the binary tree does not exhibit this 'small-boundary' behavior.
        self.play(Create(g), run_time=2)
        self.wait(0.916666666667)

        nodes, _ = bt.binary_tree_layer(6)

        self.play(hb.HighlightSubgraph(g,[nodes],[[]]))

        self.wait(4.433333333333)

        # In fact, as the size of the binary trees goes to infinity, the proportion
        # of vertices in the boundary of the tree goes to 1/2.
        nodes, _ = bt.binary_tree_layer(6)

        fraction = MathTex(r"2^n", r"\over", r"2^{n+1}-1", color=sol.BASE02)
        fraction.set_color_by_tex(r"2^n", sol.YELLOW)

        self.play(FadeIn(fraction, scale=1.5), run_time=2)
        self.wait(2.433333333333)

        # So, rather than looking at the binary tree from the top, let's see what it
        # looks like from the bottom, from the perspective of a leaf of the tree.

        self.wait(2.416666666667)

        self.play(hb.UnHighlight(g),
                  FadeOut(fraction))

        self.wait()

        self.play(hb.HighlightBall(g, 2 ** 6 - 1, 0, fadeout=False))

        self.wait(2)


        self.play(g.animate.change_layout(bt.canopy_tree_layout(6)))

        self.wait(2.45)

        # From a leaf's perspective, this is what the binary tree looks like.
        # If we grow the binary tree from here, the natural infinite graph is a 
        # one-way infinite path, where the nth node along the path has a binary tree
        # of depth n attached to it (where a binary tree of depth 0 is empty).

        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=4.9)), run_time=13.55)

        # Since this is what a large binary tree looks like from the perspective of the leaf,
        # and since the proportion of leaves in such a graph is about 1/2,
        # we might expect that the graph limit of the binary trees --- which is a random rooted
        # graph --- should take *this* value with probability 1/2.

        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=0)), run_time=5)
        self.wait(3.15)

        probtext1 = MathTex(r'\text{probability} =',
                            r'\frac{1}{2}',
                            r'= \lim_{n \to \infty}',
                            r'{',
                            r'2^n',
                            r'\over',
                            r'2^{n+1}-1',
                            r'}', color=sol.NODE, font_size=60)
        probtext1.move_to(2*UP)

        probtext1.set_color_by_tex(r'\frac{1}{2}', sol.ROOT)
        probtext1.set_color_by_tex(r'= \lim_{n \to \infty}', config.background_color)
        probtext1.set_color_by_tex(r'2^n', config.background_color)
        probtext1.set_color_by_tex(r'\over', config.background_color)
        probtext1.set_color_by_tex(r'2^{n+1}-1', config.background_color)

        self.play(FadeIn(probtext1, shift=DOWN));

        self.wait(0.58333333333)

        self.play(probtext1.animate.set_color_by_tex(r'= \lim_{n \to \infty}', sol.NODE), run_time=0.25)
        self.play(probtext1.animate.set_color_by_tex(r'2^n', sol.YELLOW), run_time=0.25)
        self.play(probtext1.animate.set_color_by_tex(r'\over', sol.NODE), run_time=0.25)
        self.play(probtext1.animate.set_color_by_tex(r'2^{n+1}-1', sol.NODE), run_time=0.25)

        self.wait(3.58333333333)

        self.play(FadeOut(probtext1), run_time=0.15)

        # Now, the set of nodes in a binary tree which are one level above a leaf
        # constitute about 1/4th of a large binary tree.

        nodes, _ = bt.binary_tree_layer(5)

        fraction = MathTex(r"2^{n-1}", r"\over", r"2^{n+1}-1", color=sol.BASE02)
        fraction.set_color_by_tex(r"2^{n-1}", sol.YELLOW)

        self.play(g.animate.change_layout(bt.binary_tree_layout(6, shift=2.7*UP)), run_time=0.4)
        self.play(hb.UnHighlight(g), run_time = 0.1)

        self.wait(0.2666666666666667)

        self.play(hb.HighlightSubgraph(g, [nodes], [[]]))

        self.wait(2)

        self.play(FadeIn(fraction, scale=1.5))
        self.wait(2.6666666666666667)

        # Let's see what a large binary tree looks like from the perspective of one of these vertices.

        self.play(hb.UnHighlight(g),
                  FadeOut(fraction))

        self.wait(0.8)


        self.play(hb.HighlightBall(g, 2 ** 5 - 1, 0, fadeout=False))

        self.wait(1.6666666666666667)

        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=1)))

        # It looks the same as the picture from a leaf, but rooted one node further along the path.

        self.wait(5.2)

        # Similarly, if we examine a large binary tree from the perspective of a node which is 
        # two levels above a leaf, we will find the same picture, just shifted by one more node.

        self.play(hb.UnHighlight(g))

        self.wait(3)

        self.play(hb.HighlightBall(g, 2 ** 4 - 1, 0, fadeout=False))

        self.wait(2)

        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=2)))

        self.wait(2)


        # This leads us to conjecture that the random rooted graph which is the limit of the
        # finite binary trees will take *this* value with probability 1/2, 

        probtext2 = MathTex(r'\text{probability} =', r'\frac{1}{2}', color=sol.NODE, font_size=80)
        probtext2.set_color_by_tex(r'\frac{1}{2}', sol.ROOT)
        probtext2.move_to(2*UP)

        self.play(hb.UnHighlight(g))

        self.wait(4)

        self.play(hb.HighlightBall(g, 2 ** 6 - 1, 0, fadeout=False), run_time = 0.25)

        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=0)), run_time=0.75)

        self.play(FadeIn(probtext2, shift=DOWN))

        self.wait(1)

        # *this* value with probability 1/4, 

        probtext3 = MathTex(r'\text{probability} =', r'\frac{1}{4}', color=sol.NODE, font_size=80)
        probtext3.set_color_by_tex(r'\frac{1}{4}', sol.ROOT)
        probtext3.move_to(2*UP)

        self.play(hb.UnHighlight(g), run_time=0.01)
        self.play(hb.HighlightBall(g, 2 ** 5 - 1, 0, fadeout=False), run_time = 0.24)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=1)), run_time=0.75)

        self.play(Transform(probtext2, probtext3))

        self.wait(1.5)

        # *this* value with probability 1/8, et. cetera

        probtext4 = MathTex(r'\text{probability} =', r'\frac{1}{8}', color=sol.NODE, font_size=80)
        probtext4.set_color_by_tex(r'\frac{1}{8}', sol.ROOT)
        probtext4.move_to(2*UP)

        self.play(hb.UnHighlight(g), run_time=0.01)
        self.play(hb.HighlightBall(g, 2 ** 4 - 1, 0, fadeout=False), run_time = 0.24)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=2)), run_time = 0.75)

        self.play(Transform(probtext2, probtext4))

        self.wait(0.5)

        ##########

        probtext5 = MathTex(r'\text{probability} =', r'\frac{1}{16}', color=sol.NODE, font_size=80)
        probtext5.set_color_by_tex(r'\frac{1}{16}', sol.ROOT)
        probtext5.move_to(2*UP)

        self.play(hb.UnHighlight(g), run_time=0.01)
        self.play(hb.HighlightBall(g, 2 ** 3 - 1, 0, fadeout=False),
                  Transform(probtext2, probtext5), run_time=0.74)

        probtext6 = MathTex(r'\text{probability} =', r'\frac{1}{32}', color=sol.NODE, font_size=80)
        probtext6.set_color_by_tex(r'\frac{1}{32}', sol.ROOT)
        probtext6.move_to(2*UP)

        self.play(hb.UnHighlight(g), run_time=0.01)
        self.play(hb.HighlightBall(g, 2 ** 2 - 1, 0, fadeout=False),
                  Transform(probtext2, probtext6), run_time=0.74)

        # Since these probabilities add up to 1, this is a complete description of a random rooted graph.

        self.play(hb.UnHighlight(g), 
                  FadeOut(probtext2),
                  run_time=0.25)

        label_size = 20

        mytemplate = TexTemplate()
        mytemplate.add_to_preamble(r"\usepackage{amsbsy}")

        h = Graph([0, 1, 3, 7, 15, 31, 63], [],
                  vertex_config={ 'fill_color' : sol.RED },
                  layout=bt.canopy_tree_layout(6, height=2),
                  labels={ 0  : MathTex(r'\pmb{\frac{1}{128}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           1  : MathTex(r'\pmb{\frac{1}{64}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           3  : MathTex(r'\pmb{\frac{1}{32}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           7  : MathTex(r'\pmb{\frac{1}{16}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           15 : MathTex(r'\pmb{\frac{1}{8}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           31 : MathTex(r'\pmb{\frac{1}{4}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           63 : MathTex(r'\pmb{\frac{1}{2}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE)})

        self.play(FadeIn(h), run_time=1)
        
        self.wait(3.25)

        treetext = Tex(r'Canopy Tree', font_size = 100, color=sol.BASE02)
        treetext.move_to(1.5*UP)

        self.play(Write(treetext), run_time=2)

        self.wait(10)



# Now, this is just a conjecture.
# To actually prove that this is the limit, we must refer back to the definition 
# of convergence for random rooted graphs.

# In particular, we must show that, for any R, the distribution of R-balls in the
# finite binary trees converges to the distribution of R-balls in the proposed graph limit.
# [SHOW SOME LATEX I GUESS]

class Definition(Scene):
    def construct(self):
        tex1 = Tex(r'for any radius $r$,', color=sol.NODE, font_size=80)
        tex2 = MathTex(r'B_r \Big[ \substack{ \text{binary tree of height } n \\ \text{with uniform random root}} \Big]', color=sol.NODE, font_size=60)
        tex3 = MathTex(r'B_r [ \text{Canopy Tree} ]', color=sol.NODE, font_size=60)
        tex4 = Tex(r'in distribution', color=sol.NODE, font_size=80)
        tex5 = MathTex(r'\longrightarrow', color=sol.NODE, font_size=60)

        tex1.move_to(1.5 * UP)
        tex2.move_to(3.25 * LEFT)
        tex3.move_to(4.25 * RIGHT)
        tex4.move_to(1.5 * DOWN)
        tex5.move_to(1.1 * RIGHT)

        self.play(FadeIn(tex1, shift=DOWN))
        self.wait(0.5)
        self.play(FadeIn(tex2, shift=RIGHT))
        self.wait(2)
        self.play(FadeIn(tex3, shift=LEFT), FadeIn(tex5))
        self.play(FadeIn(tex4, shift=UP))

        self.wait(5)

# plots explanation
class Plots1Ball3Binary(Scene):
    def construct(self):
        vconf = { 0 : { 'fill_color' : sol.ROOT , 'radius' : 0.3 } }
        vconf.update({ v : { 'fill_color' : sol.NODE , 'radius' : 0.3 } for v in range(1,10)})
        econf = { 'stroke_color' : sol.EDGE } 

        kwargs = { 'vertex_config' : vconf, 'edge_config' : econf } 

        rballs_1_initial = [
                Graph([0,1], [(0,1)], **kwargs, layout='tree', root_vertex=1),
                Graph([0,1,2,3], [(0,1),(0,2),(0,3)], **kwargs, layout='kamada_kawai', layout_scale=1.1),
                Graph([0,1,2], [(0,1),(0,2)], **kwargs, layout='tree', root_vertex=0)
                ]

        rballs_1_final = [
                Graph([0,1], [(0,1)], **kwargs, layout='tree', root_vertex=1),
                Graph([0,1,2,3], [(0,1),(0,2),(0,3)], **kwargs, layout='kamada_kawai', layout_scale=1.1),
                Graph([0,1,2], [(0,1),(0,2)], **kwargs, layout='tree', root_vertex=0)
                ]

        bar_3_initial = mb.MobjectLabeledBarChart(
                [0.0000001, 0.0000001, 0.0000001],
                max_value = 7,
                bar_names = rballs_1_initial,
                bar_label_scale_val = 0.3,
                bar_colors = [sol.BLUE],
                color = sol.BASE03,
                stroke_color = sol.BASE03,
                height = 3,
                width = 4
                )
        bar_3_initial.move_to(3.5 * LEFT + 0.75 * DOWN)

        bar_3_final = mb.MobjectLabeledBarChart(
                [4/7, 2/7, 1/7],
                max_value = 1,
                bar_names = rballs_1_final,
                bar_label_scale_val = 0.3,
                bar_colors = [sol.BLUE],
                color = sol.BASE03,
                stroke_color = sol.BASE03,
                height = 3,
                width = 4
                )
        bar_3_final.move_to(3.5 * LEFT + 0.75 * DOWN)

        #####################################################

        nxgraph = nx.balanced_tree(2,2)
        g = Graph.from_networkx(nxgraph,
                                vertex_config=sol.LIGHT_VERTEX_CONFIG,
                                edge_config=sol.LIGHT_EDGE_CONFIG,
                                layout=bt.binary_tree_layout(2, shift= 1.5 * UP + 3 * RIGHT, horizontal_scale=3))


        #####################################################
        
        text = Tex(r'Height-3 Binary Tree', color=sol.BASE02)
        text.move_to(3.1*LEFT + 2*UP)

        #####################################################


        self.play(Create(bar_3_initial))

        self.wait(1.38333333333333)

        self.play(Create(g),
                  FadeIn(text, shift=DOWN)
                  )

        self.wait(1.63333333333333)

        self.play(bar_3_initial.animate.change_bar_values([1, 0.0000001, 0.0000001]),
                  hb.HighlightBall(g, 3, 1, run_time=0.5, fade_run_time=0.1583333),
                  run_time=2.633333333333/4
                 )

        self.play(bar_3_initial.animate.change_bar_values([2, 0.0000001, 0.0000001]),
                  hb.HighlightBall(g, 4, 1, run_time=0.5, fade_run_time=0.1583333),
                  run_time=2.633333333333/4
                 )

        self.play(bar_3_initial.animate.change_bar_values([3, 0.0000001, 0.0000001]),
                  hb.HighlightBall(g, 5, 1, run_time=0.5, fade_run_time=0.1583333),
                  run_time=2.633333333333/4
                 )

        self.play(bar_3_initial.animate.change_bar_values([4, 0.0000001, 0.0000001]),
                  hb.HighlightBall(g, 6, 1, run_time=0.5, fade_run_time=0.1583333),
                  run_time=2.633333333333/4
                 )

        self.play(bar_3_initial.animate.change_bar_values([4, 1, 0.0000001]),
                  hb.HighlightBall(g, 1, 1, run_time=1, fade_run_time=0.041666667),
                  run_time=2.0833333333333/2
                 )

        self.play(bar_3_initial.animate.change_bar_values([4, 2, 0.0000001]),
                  hb.HighlightBall(g, 2, 1, run_time=1, fade_run_time=0.041666667),
                  run_time=2.0833333333333/2
                 )

        self.play(bar_3_initial.animate.change_bar_values([4, 2, 1]),
                  hb.HighlightBall(g, 0, 1, run_time=1.75, fade_run_time=0.25),
                  run_time=2
                 )
        
        self.wait(2.25)

        self.play(Transform(bar_3_initial, bar_3_final))

        self.wait(5)


class Plots1BallCanopy(Scene):
    def construct(self):

        vconf = { 0 : { 'fill_color' : sol.ROOT , 'radius' : 0.3 } }
        vconf.update({ v : { 'fill_color' : sol.NODE , 'radius' : 0.3 } for v in range(1,10)})
        econf = { 'stroke_color' : sol.EDGE } 

        kwargs = { 'vertex_config' : vconf, 'edge_config' : econf } 

        rballs = [
                Graph([0,1], [(0,1)], **kwargs, layout='tree', root_vertex=1),
                Graph([0,1,2,3], [(0,1),(0,2),(0,3)], **kwargs, layout='kamada_kawai', layout_scale=1.1),
                Graph([0,1,2], [(0,1),(0,2)], **kwargs, layout='tree', root_vertex=0)
                ]

        bar = mb.MobjectLabeledBarChart(
                [0.0000001, 0.0000001, 0.0000001],
                max_value = 1,
                bar_names = rballs,
                bar_label_scale_val = 0.3,
                bar_colors = [sol.BLUE],
                color = sol.BASE03,
                stroke_color = sol.BASE03,
                height = 3,
                width = 4
                )
        bar.move_to(3.5 * LEFT + 0.75 * DOWN)

        #####################################################

        nxgraph = nx.balanced_tree(2,4)
        g = Graph.from_networkx(nxgraph,
                                vertex_config=sol.LIGHT_VERTEX_CONFIG,
                                edge_config=sol.LIGHT_EDGE_CONFIG,
                                layout=bt.canopy_tree_layout(4, 0.1, stretch_parameter=1))


        #####################################################
        
        text = Tex(r'Canopy Tree', color=sol.BASE02)
        text.move_to(3.1*LEFT + 2*UP)

        #####################################################

        label_size = 20

        mytemplate = TexTemplate()
        mytemplate.add_to_preamble(r"\usepackage{amsbsy}")

        h = Graph([0, 1, 3, 7, 15], [],
                  vertex_config={ 'fill_color' : sol.LIGHT_NODE },
                  layout=bt.canopy_tree_layout(4, 0.1, stretch_parameter=1),
                  labels={ 0  : MathTex(r'\pmb{\frac{1}{32}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           1  : MathTex(r'\pmb{\frac{1}{16}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           3  : MathTex(r'\pmb{\frac{1}{8}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           7  : MathTex(r'\pmb{\frac{1}{4}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           15 : MathTex(r'\pmb{\frac{1}{2}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE)})

        #####################################################

        self.play(Create(bar))

        self.wait()

        self.play(Create(g),
                  Create(h),
                  FadeIn(text, shift=DOWN)
                  )

        self.wait()

        self.play(bar.animate.change_bar_values([0.5, 0.0000001, 0.0000001]),
                  hb.HighlightBall(g, 15, 1, run_time=3, fade_run_time=0.5),
                  hb.HighlightBall(h, 15, 0, run_time=3, fade_run_time=0.5),
                  hb.HighlightBall(h, 7, 0, run_time=3, fade_run_time=0.5, root_highlight_color=sol.NODE)
                 )

        self.play(hb.HighlightBall(g, 7, 1, run_time=1, fadeout=False),
                  hb.HighlightBall(h, 7, 0, run_time=1, fadeout=False),
                  hb.HighlightBall(h, 3, 0, run_time=1, fadeout=False, root_highlight_color=sol.NODE),
                  hb.HighlightBall(h, 15, 0, run_time=1, fadeout=False, root_highlight_color=sol.NODE)
                  )

        self.wait(0.75)

        self.play(bar.animate.change_bar_values([0.5, 0.25, 0.0000001]), run_time=0.75)

        self.play(hb.UnHighlight(g, node_base_color=sol.LIGHT_NODE, edge_base_color=sol.LIGHT_EDGE, run_time=0.08333333),
                  hb.UnHighlight(h, node_base_color=sol.LIGHT_NODE, run_time=0.08333333)
                 )

        self.play(bar.animate.change_bar_values([0.5, 0.25 + 0.125, 0.0000001]),
                  hb.HighlightBall(g, 3, 1, run_time=0.75, fade_run_time=0.16666667),
                  hb.HighlightBall(h, 3, 0, run_time=0.75, fade_run_time=0.16666667),
                  hb.HighlightBall(h, 7, 0, run_time=0.75, fade_run_time=0.16666667, root_highlight_color=sol.NODE),
                  hb.HighlightBall(h, 1, 0, run_time=0.75, fade_run_time=0.16666667, root_highlight_color=sol.NODE),
                  run_time=0.916666667
                 )

        self.play(bar.animate.change_bar_values([0.5, 0.25 + 0.125 + 0.0625, 0.0000001]),
                  hb.HighlightBall(g, 1, 1, run_time=0.75, fade_run_time=0.16666667),
                  hb.HighlightBall(h, 1, 0, run_time=0.75, fade_run_time=0.16666667),
                  hb.HighlightBall(h, 3, 0, run_time=0.75, fade_run_time=0.16666667, root_highlight_color=sol.NODE),
                  hb.HighlightBall(h, 0, 0, run_time=0.75, fade_run_time=0.16666667, root_highlight_color=sol.NODE),
                  run_time=0.916666667
                 )

        self.play(bar.animate.change_bar_values([0.5, 0.5, 0.0000001]),
                  hb.HighlightBall(g, 0, 1, run_time=0.75, fade_run_time=0.25),
                  hb.HighlightBall(h, 0, 0, run_time=0.75, fade_run_time=0.25),
                  hb.HighlightBall(h, 1, 0, run_time=0.75, fade_run_time=0.25, root_highlight_color=sol.NODE),
                  run_time=1
                 )

        self.wait(1.58333333333333)


        self.play(FadeOut(g, shift=7*RIGHT),
                  FadeOut(h, shift=7*RIGHT),
                  bar.animate.move_to(3.5 * RIGHT + 0.75 * DOWN),
                  text.animate.move_to(3.7 * RIGHT + 2 * UP))

        self.wait(5)


class Plots1Convergence(Scene):
    def construct(self):

        # We'll leave this as an exercise for you, but here are some plots of the numbers of
        # different R-balls in the finite binary trees.

        vconf = { 0 : { 'fill_color' : sol.ROOT , 'radius' : 0.3 } }
        vconf.update({ v : { 'fill_color' : sol.NODE , 'radius' : 0.3 } for v in range(1,10)})
        econf = { 'stroke_color' : sol.BASE02 } 

        kwargs = { 'vertex_config' : vconf, 'edge_config' : econf } 

        rballs_1_canopy = [
                Graph([0,1], [(0,1)], **kwargs, layout='tree', root_vertex=1),
                Graph([0,1,2,3], [(0,1),(0,2),(0,3)], **kwargs, layout='kamada_kawai', layout_scale=1.1),
                Graph([0,1,2], [(0,1),(0,2)], **kwargs, layout='tree', root_vertex=0)
                ]

        ballbar_canopy = mb.MobjectLabeledBarChart(
                [0.5, 0.5, 0.0],
                max_value = 1,
                bar_names = rballs_1_canopy,
                bar_label_scale_val = 0.3,
                bar_colors = [sol.BLUE],
                color = sol.BASE03,
                stroke_color = sol.BASE03,
                height=3,
                width=4
                )
        ballbar_canopy.move_to(3.5*RIGHT + 0.75*DOWN)

        text_canopy = Tex(r'Canopy Tree', color=sol.BASE02)
        text_canopy.move_to(3.7*RIGHT + 2*UP)

        rballs_1_finite = [
                Graph([0,1], [(0,1)], **kwargs, layout='tree', root_vertex=1),
                Graph([0,1,2,3], [(0,1),(0,2),(0,3)], **kwargs, layout='kamada_kawai', layout_scale=1.1),
                Graph([0,1,2], [(0,1),(0,2)], **kwargs, layout='tree', root_vertex=0)
                ]

        ballbar_finite_values = [ [ 2 ** i / (2 ** (i+1) - 1), (2 ** i - 2) / (2 ** (i+1) - 1) + 0.00001, 1 / (2 ** (i+1) - 1) ] for i in range(10) ]

        ballbar_finite = mb.MobjectLabeledBarChart(
                ballbar_finite_values[2],
                max_value = 1,
                bar_names = rballs_1_finite,
                bar_label_scale_val = 0.3,
                bar_colors = [sol.BLUE],
                color = sol.BASE03,
                stroke_color = sol.BASE03,
                height=3,
                width=4
                )
        ballbar_finite.move_to(3.5*LEFT + 0.75*DOWN)

        text_finite = [ Tex(r'Height-' r'$' + str(i+1) + '$' r' Binary Tree', color=sol.BASE02) for i in range(9) ]
        for tf in text_finite:
            tf.move_to(3*LEFT + 2*UP)

        #########################################

        self.add(ballbar_canopy, text_canopy)

        self.play(FadeIn(ballbar_finite), FadeIn(text_finite[2]))

        for i in range(3,9):
            self.play(Transform(text_finite[2],text_finite[i]),
                      ballbar_finite.animate.change_bar_values(ballbar_finite_values[i]),
                      run_time=8/6)

        self.wait()


class Plots2(Scene):
    def construct(self):

        # And here they are for the 2-balls

        vconf = { 0 : { 'fill_color' : sol.ROOT , 'radius' : 0.3 } }
        vconf.update({ v : { 'fill_color' : sol.NODE , 'radius' : 0.3 } for v in range(1,10)})
        econf = { 'stroke_color' : sol.BASE02 } 

        kwargs = { 'vertex_config' : vconf, 'edge_config' : econf } 

        rballs_2_canopy = [
                Graph([0,1,2,3], [(0,1),(1,2),(1,3)], **kwargs, layout='kamada_kawai', layout_scale=1.3),
                Graph([0,1,2,3,4,5], [(0,1),(0,2),(0,3),(3,4),(3,5)], **kwargs, layout='kamada_kawai', layout_scale=1.2),
                Graph([0,1,2,3,4,5,6,7,8,9], [(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,7),(3,8),(3,9)], **kwargs, layout='kamada_kawai', layout_scale=1.3),
                Graph([0,1,2,3,4,5,6], [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)], **kwargs, layout='tree', root_vertex=0)
                ]

        ballbar_canopy = mb.MobjectLabeledBarChart(
                [0.5, 0.25, 0.25, 0.0],
                max_value = 1,
                bar_names = rballs_2_canopy,
                bar_label_scale_val = 0.3,
                bar_colors = [sol.BLUE],
                color = sol.BASE03,
                stroke_color = sol.BASE03,
                height=3,
                width=5
                )
        ballbar_canopy.move_to(3.5*RIGHT + 0.75*DOWN)

        text_canopy = Tex(r'Canopy Tree', color=sol.BASE02)
        text_canopy.move_to(3.7*RIGHT + 2*UP)

        rballs_2_finite = [
                Graph([0,1,2,3], [(0,1),(1,2),(1,3)], **kwargs, layout='kamada_kawai', layout_scale=1.3),
                Graph([0,1,2,3,4,5], [(0,1),(0,2),(0,3),(3,4),(3,5)], **kwargs, layout='kamada_kawai', layout_scale=1.2),
                Graph([0,1,2,3,4,5,6,7,8,9], [(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,7),(3,8),(3,9)], **kwargs, layout='kamada_kawai', layout_scale=1.3),
                Graph([0,1,2,3,4,5,6], [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)], **kwargs, layout='tree', root_vertex=0)
                ]

        ballbar_finite_values = [ [ 2 ** i / (2 ** (i+1) - 1),
                                    (2 ** (i-1)) / (2 ** (i+1) - 1) + 0.00001,
                                    (2 ** (i-1) - 2) / (2 ** (i+1) - 1) + 0.00001,
                                    1 / (2 ** (i+1) - 1) ] for i in range(10) ]

        ballbar_finite = mb.MobjectLabeledBarChart(
                ballbar_finite_values[2],
                max_value = 1,
                bar_names = rballs_2_finite,
                bar_label_scale_val = 0.3,
                bar_colors = [sol.BLUE],
                color = sol.BASE03,
                stroke_color = sol.BASE03,
                height=3,
                width=4
                )
        ballbar_finite.move_to(3.5*LEFT + 0.75*DOWN)

        text_finite = [ Tex(r'Height-' r'$' + str(i) + '$' r' Binary Tree', color=sol.BASE02) for i in range(10) ]
        for tf in text_finite:
            tf.move_to(3*LEFT + 2*UP)

        ######################################

        self.play(Create(ballbar_finite), Create(ballbar_canopy), Write(text_canopy), Write(text_finite[2]))

        self.wait(0.75)

        for i in range(3,9):
            self.play(Transform(text_finite[2],text_finite[i+1]),
                      ballbar_finite.animate.change_bar_values(ballbar_finite_values[i]))

        self.wait()


# So, assuming you've done that exercise, we've found another example of a graph limit.
# Unlike all the limits we saw in the last video, this one can take infinitely many
# different values, each with positive probability.
# Of course, if we ignore the root, we will always get the same graph.
# But the rooting really does matter here, and so we consider each of these infinitely many outcomes distinct.

class EndScroll(Scene):
    def construct(self):
        nxgraph = nx.balanced_tree(2,8)
        g = Graph.from_networkx(nxgraph,
                                vertex_config=sol.VERTEX_CONFIG,
                                edge_config=sol.EDGE_CONFIG,
                                layout=bt.canopy_tree_layout(8))

        label_size = 20

        mytemplate = TexTemplate()
        mytemplate.add_to_preamble(r"\usepackage{amsbsy}")

        h = Graph([0, 1, 3, 7, 15, 31, 63, 127, 255], [],
                  vertex_config={ 'fill_color' : sol.RED },
                  layout=bt.canopy_tree_layout(8),
                  labels={ 0   : MathTex(r'\pmb{\frac{1}{512}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           1   : MathTex(r'\pmb{\frac{1}{256}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           3   : MathTex(r'\pmb{\frac{1}{128}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           7   : MathTex(r'\pmb{\frac{1}{64}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           15  : MathTex(r'\pmb{\frac{1}{32}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           31  : MathTex(r'\pmb{\frac{1}{16}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           63  : MathTex(r'\pmb{\frac{1}{8}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           127 : MathTex(r'\pmb{\frac{1}{4}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE),
                           255 : MathTex(r'\pmb{\frac{1}{2}}', tex_template=mytemplate, font_size=label_size, color=sol.NODE)})

        ##############################

        self.add(g,h)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(8, height=8, stretch_parameter=2, vertical_shrink=2.5/3)),
                  h.animate.change_layout(bt.canopy_tree_layout(8, height=8, stretch_parameter=2, vertical_shrink=2.5/3)),
                  run_time=60)


# Stay tuned for more videos!
