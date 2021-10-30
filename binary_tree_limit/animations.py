from manim import *
import random
import highlight_ball as hb
import solarized as sol
import binary_tree as bt
import grid as gr
import networkx as nx

TEMPLATE = TexTemplate()
TEMPLATE.add_to_preamble(r"\usepackage{xcolor}")
TEMPLATE.add_to_preamble(r"\definecolor{ORANGE}{HTML}{cb4b16}")
TEMPLATE.add_to_preamble(r"\definecolor{BASE02}{HTML}{073642}")


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
        pass

        # This is because the balls in the grid graph mostly look like
        # the ball around the origin in the infinite grid.

        # More precisely, for any radius R, as the size N of the finite grids go to
        # infinity, the probability that the R-ball around a uniformly random vertex 
        # in the grid is isomorphic to to the R-ball in the infinite grid goes to 1.

        # This works because the number of vertices that are within distance R from 
        # the boundary of the grid scales like N, whereas the number of vertices
        # in the interior of the grid scales like N^2.

        # So for large enough N, there are far more vertices on the 
        # interior than near the boundary.


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

        # TODO: FIGURE OUT THIS FRACTION COLOR
        # fraction = MathTex(r"{ \color{BASE02} \frac{ {\color{ORANGE} 2^n} }{ 2^{n+1}-1 } }",
        #                    tex_template=TEMPLATE)

        self.play(hb.HighlightSubgraph(g,[nodes],[[]]))
        self.wait()

        # So, rather than looking at the binary tree from the top, let's see what it
        # looks like from the bottom, from the perspective of a leaf of the tree.

        self.play(hb.HighlightBall(g, 2 ** 6 - 1, 0))
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

        self.play(g.animate.change_layout(bt.binary_tree_layout(6, shift=2.7*UP)))
        self.play(hb.UnHighlight(g), run_time = 0.25)
        self.play(hb.HighlightSubgraph(g, [nodes], [[]]))
        self.wait()

        # Let's see what a large binary tree looks like from the perspective of one of these vertices.

        self.play(hb.HighlightBall(g, 2 ** 5 - 1, 0), run_time = 0.25)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=1)))

        # It looks the same as the picture from a leaf, but rooted one node further along the path.

        self.wait()

        # Similarly, if we examine a large binary tree from the perspective of a node which is 
        # two levels above a leaf, we will find the same picture, just shifted by one more node.

        self.play(hb.HighlightBall(g, 2 ** 4 - 1, 0), run_time = 0.25)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=2)))
        self.wait()


        # This leads us to conjecture that the random rooted graph which is the limit of the
        # finite binary trees will take *this* value with probability 1/2, 

        self.play(hb.HighlightBall(g, 2 ** 6 - 1, 0), run_time = 0.25)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=0)))
        self.wait()

        # *this* value with probability 1/4, 

        self.play(hb.HighlightBall(g, 2 ** 5 - 1, 0), run_time = 0.25)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=1)))
        self.wait()

        # *this* value with probability 1/8, et. cetera

        self.play(hb.HighlightBall(g, 2 ** 4 - 1, 0), run_time = 0.25)
        self.play(g.animate.change_layout(bt.canopy_tree_layout(6, height=2)))
        self.wait()

        # Since these probabilities add up to 1, this is a complete description of a random rooted graph.

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

class Plots(Scene):
    def construct(self):
        pass

        # We'll leave this as an exercise for you, but here are some plots of the numbers of
        # different R-balls in the finite binary trees.


# So, assuming you've done that exercise, we've found another example of a graph limit.
# Unlike all the limits we saw in the last video, this one can take infinitely many
# different values, each with positive probability.
# Of course, if we ignore the root, we will always get the same graph.
# But the rooting really does matter here, and so we consider each of these infinitely many outcomes distinct.

# Stay tuned for more videos!
