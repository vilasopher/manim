from manim import *
import random
import highlight_ball as hb
import solarized as sol
import binary_tree as bt
import grid as gr
import networkx as nx
import mobject_labeled_bar_chart as mb

random.seed(0)

# In our last video, we presented a notion of graph convergence,
# where every sequence of finite graphs has a graph limit.
# These limits are all random rooted graphs, i.e. random variables
# taking values in the space of rooted graphs.
# [SHOW CLIPS FROM PREVIOUS VIDEO]


class Opening(Scene):
    def construct(self):
        g = Graph([0], [],
                  vertex_config=sol.VERTEX_CONFIG,
                  edge_config=sol.EDGE_CONFIG,
                  layout=bt.binary_tree_layout(0))

        # Now, what is the limit of the sequence of complete finite binary trees?

        self.play(Create(g))

        for depth in range(1,5):
            nodes, edges = bt.binary_tree_layer(depth)
            self.play(g.animate.add_vertices(*nodes, positions=bt.binary_tree_layout(depth)),
                      g.animate.add_edges(*edges))

        self.wait()

        # A first guess might be that the limit is the random rooted graph whose value is,
        # with probability 1, the infinite binary tree, rooted at the top.

        for depth in range(5,7):
            nodes, edges = bt.binary_tree_layer(depth)
            self.play(g.animate.add_vertices(*nodes, positions=bt.binary_tree_layout(depth)),
                      g.animate.add_edges(*edges))

        self.play(hb.HighlightBall(g,0,0))

        self.wait()


#  After all, this is what happens with the finite path graphs and grid graphs,
# as we saw before: the limit of the sequence of finite path graphs is an
# infinite path graph, rooted in the middle, and the limit of the finite grid graphs
# is an infinite grid graph, rooted in the middle. 
# [SHOW SCREENGRABS FROM PREVIOUS VIDEO]


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


        self.add(grid, infgrid)
        self.add(occlusion, frame)

        # More precisely, for any radius R, as the size N of the finite grids go to
        # infinity, the probability that the R-ball around a uniformly random vertex 
        # in the grid is isomorphic to to the R-ball in the infinite grid goes to 1.

        vertexlist = list(grid.vertices)
        boundaryvertices, boundaryedges = gr.grid_boundary(12, 2)

        for _ in range(20):
            v = random.choice(vertexlist)
            color = sol.HIGHLIGHT_NODE

            if v in boundaryvertices:
                color = sol.RED

            self.play(hb.HighlightBall(grid, v, 2, node_highlight_color=color, edge_highlight_color=color))

        # This works because the number of vertices that are within distance R from 
        # the boundary of the grid scales like N, whereas the number of vertices
        # in the interior of the grid scales like N^2.

        self.play(hb.HighlightSubgraph(grid, [boundaryvertices], [boundaryedges], node_highlight_color=[sol.YELLOW]))

        fraction = MathTex(r"\sim 4 R \cdot n", r"\over", r"n^2", color=sol.BASE02)
        fraction.set_color_by_tex(r"\sim 4 R \cdot n", sol.YELLOW)

        fraction.move_to(4 * RIGHT + 2.5 * DOWN)

        self.play(Create(fraction))

        # So for large enough N, there are far more vertices on the 
        # interior than near the boundary.

        for _ in range(20):
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
        self.play(Create(g))
        self.wait()

        # In fact, as the size of the binary trees goes to infinity, the proportion
        # of vertices in the boundary of the tree goes to 1/2.
        nodes, _ = bt.binary_tree_layer(6)

        fraction = MathTex(r"2^n", r"\over", r"2^{n+1}-1", color=sol.BASE02)
        fraction.set_color_by_tex(r"2^n", sol.ORANGE)

        self.play(hb.HighlightSubgraph(g,[nodes],[[]]))
        self.play(Create(fraction))
        self.wait()

        # So, rather than looking at the binary tree from the top, let's see what it
        # looks like from the bottom, from the perspective of a leaf of the tree.

        self.play(hb.UnHighlight(g),
                  Uncreate(fraction))
        self.play(hb.HighlightBall(g, 2 ** 6 - 1, 0, fadeout=False))
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6)))
        self.wait()

        # From a leaf's perspective, this is what the binary tree looks like.
        # If we grow the binary tree from here, the natural infinite graph is a 
        # one-way infinite path, where the nth node along the path has a binary tree
        # of depth n attached to it (where a binary tree of depth 0 is empty).

        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=2)), run_time=2)
        self.wait()

        # Since this is what a large binary tree looks like from the perspective of the leaf,
        # and since the proportion of leaves in such a graph is about 1/2,
        # we might expect that the graph limit of the binary trees --- which is a random rooted
        # graph --- should take *this* value with probability 1/2.

        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=0)))
        self.wait()

        # Now, the set of nodes in a binary tree which are one level above a leaf
        # constitute about 1/4th of a large binary tree.

        nodes, _ = bt.binary_tree_layer(5)

        fraction = MathTex(r"2^{n-1}", r"\over", r"2^{n+1}-1", color=sol.BASE02)
        fraction.set_color_by_tex(r"2^{n-1}", sol.ORANGE)

        self.play(g.animate.change_layout(bt.binary_tree_layout(6, shift=2.7*UP)))
        self.play(hb.UnHighlight(g), run_time = 0.25)
        self.play(hb.HighlightSubgraph(g, [nodes], [[]]))
        self.play(Create(fraction))
        self.wait()

        # Let's see what a large binary tree looks like from the perspective of one of these vertices.

        self.play(hb.UnHighlight(g),
                  Uncreate(fraction), run_time=0.25)
        self.play(hb.HighlightBall(g, 2 ** 5 - 1, 0, fadeout=False),
                  run_time = 0.25)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=1)))

        # It looks the same as the picture from a leaf, but rooted one node further along the path.

        self.wait()

        # Similarly, if we examine a large binary tree from the perspective of a node which is 
        # two levels above a leaf, we will find the same picture, just shifted by one more node.

        self.play(hb.UnHighlight(g), run_time=0.01)
        self.play(hb.HighlightBall(g, 2 ** 4 - 1, 0, fadeout=False), run_time = 0.25)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=2)))
        self.wait()


        # This leads us to conjecture that the random rooted graph which is the limit of the
        # finite binary trees will take *this* value with probability 1/2, 

        self.play(hb.UnHighlight(g), run_time=0.01)
        self.play(hb.HighlightBall(g, 2 ** 6 - 1, 0, fadeout=False), run_time = 0.25)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=0)))
        self.wait()

        # *this* value with probability 1/4, 

        self.play(hb.UnHighlight(g), run_time=0.01)
        self.play(hb.HighlightBall(g, 2 ** 5 - 1, 0, fadeout=False), run_time = 0.25)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=1)))
        self.wait()

        # *this* value with probability 1/8, et. cetera

        self.play(hb.UnHighlight(g), run_time=0.01)
        self.play(hb.HighlightBall(g, 2 ** 4 - 1, 0, fadeout=False), run_time = 0.25)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=2)))
        self.wait()

        # Since these probabilities add up to 1, this is a complete description of a random rooted graph.

        return

        h = Graph.from_networkx(nxgraph,
                                vertex_config=sol.VERTEX_CONFIG,
                                edge_config=sol.EDGE_CONFIG,
                                layout=bt.canopy_tree_layout(6, height=0),
                                labels=True)
        # TODO: figure out how to add the right kinds of labels.


# Now, this is just a conjecture.
# To actually prove that this is the limit, we must refer back to the definition 
# of convergence for random rooted graphs.

# In particular, we must show that, for any R, the distribution of R-balls in the
# finite binary trees converges to the distribution of R-balls in the proposed graph limit.
# [SHOW SOME LATEX I GUESS]

class Plots1(Scene):
    def construct(self):

        # We'll leave this as an exercise for you, but here are some plots of the numbers of
        # different R-balls in the finite binary trees.

        vconf = { 0 : { 'fill_color' : sol.ROOT , 'radius' : 0.3 } }
        vconf.update({ v : { 'fill_color' : sol.NODE , 'radius' : 0.3 } for v in range(1,10)})
        econf = { 'stroke_color' : sol.BASE02 } 

        kwargs = { 'vertex_config' : vconf, 'edge_config' : econf } 

        rballs_1_canopy = [
                Graph([0,1], [(0,1)], **kwargs, layout='tree', root_vertex=1),
                Graph([0,1,2], [(0,1),(0,2)], **kwargs, layout='tree', root_vertex=0),
                Graph([0,1,2,3], [(0,1),(0,2),(0,3)], **kwargs, layout='kamada_kawai', layout_scale=1.3)
                ]

        ballbar_canopy = mb.MobjectLabeledBarChart(
                [0.5, 0.0, 0.5],
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
                Graph([0,1,2], [(0,1),(0,2)], **kwargs, layout='tree', root_vertex=0),
                Graph([0,1,2,3], [(0,1),(0,2),(0,3)], **kwargs, layout='kamada_kawai', layout_scale=1.3)
                ]

        ballbar_finite_values = [ [ 2 ** i / (2 ** (i+1) - 1), 1 / (2 ** (i+1) - 1), (2 ** i - 2) / (2 ** (i+1) - 1) + 0.00001 ] for i in range(10) ]

        ballbar_finite = mb.MobjectLabeledBarChart(
                ballbar_finite_values[1],
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

        text_finite = [ Tex(r'Height-' r'$' + str(i) + '$' r' Binary Tree', color=sol.BASE02) for i in range(10) ]
        for tf in text_finite:
            tf.move_to(3*LEFT + 2*UP)

        self.play(Create(ballbar_finite), Create(ballbar_canopy), Create(text_canopy), Create(text_finite[1]))

        for i in range(2,10):
            self.play(Transform(text_finite[1],text_finite[i]),
                      ballbar_finite.animate.change_bar_values(ballbar_finite_values[i]))

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
                Graph([0,1,2,3,4,5,6], [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)], **kwargs, layout='tree', root_vertex=0),
                Graph([0,1,2,3,4,5], [(0,1),(0,2),(0,3),(3,4),(3,5)], **kwargs, layout='kamada_kawai', layout_scale=1.3),
                Graph([0,1,2,3,4,5,6,7,8,9], [(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,7),(3,8),(3,9)], **kwargs, layout='kamada_kawai', layout_scale=1.3)
                ]

        ballbar_canopy = mb.MobjectLabeledBarChart(
                [0.5, 0.0, 0.25, 0.25],
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
                Graph([0,1,2,3,4,5,6], [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)], **kwargs, layout='tree', root_vertex=0),
                Graph([0,1,2,3,4,5], [(0,1),(0,2),(0,3),(3,4),(3,5)], **kwargs, layout='kamada_kawai', layout_scale=1.3),
                Graph([0,1,2,3,4,5,6,7,8,9], [(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,7),(3,8),(3,9)], **kwargs, layout='kamada_kawai', layout_scale=1.3)
                ]

        ballbar_finite_values = [ [ 2 ** i / (2 ** (i+1) - 1),
                                    1 / (2 ** (i+1) - 1),
                                    (2 ** (i-1)) / (2 ** (i+1) - 1) + 0.00001,
                                    (2 ** (i-1) - 2) / (2 ** (i+1) - 1) + 0.00001 ] for i in range(10) ]

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

        self.play(Create(ballbar_finite), Create(ballbar_canopy), Create(text_canopy), Create(text_finite[2]))

        for i in range(3,10):
            self.play(Transform(text_finite[2],text_finite[i]),
                      ballbar_finite.animate.change_bar_values(ballbar_finite_values[i]))

        self.wait()


# So, assuming you've done that exercise, we've found another example of a graph limit.
# Unlike all the limits we saw in the last video, this one can take infinitely many
# different values, each with positive probability.
# Of course, if we ignore the root, we will always get the same graph.
# But the rooting really does matter here, and so we consider each of these infinitely many outcomes distinct.

# Stay tuned for more videos!
