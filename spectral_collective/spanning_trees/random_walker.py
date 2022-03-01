from manim import *
import random

class RandomWalker(VGroup):
    def __init__(self, graph, start):
        super().__init__()

        if not start in graph.vertices:
            raise Exception("Starting position not in graph.")

        self.position = start
        self.graph = graph
        self.walker = Dot(
            graph.vertices[start].get_center(),
            color=RED,
            radius=0.1
        )

        self.add(graph, self.walker)

    def update_position(self):
        neighbors = self.graph._graph.neighbors(self.position)
        self.position = random.choice(list(neighbors))

    def step(self):
        self.update_position()
        self.walker.move_to(
            self.graph.vertices[self.position].get_center()
        )

    @override_animate(step)
    def _step_animation(self, **anim_args):
        self.update_position()
        return self.walker.animate(**anim_args).move_to(
            self.graph.vertices[self.position].get_center(),
        ).build()


