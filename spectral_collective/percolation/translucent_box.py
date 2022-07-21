from manim import *
import solarized as sol

class TranslucentBox(Rectangle):
    def __init__(self, *enclosed_mobjects, margin = 0.2, opacity = 1): #0.925
        g = Group(*enclosed_mobjects)

        width = g.get_right()[0] - g.get_left()[0] + 2 * margin
        height = g.get_top()[1] - g.get_bottom()[1] + 2 * margin

        super().__init__(width=width, height=height, color=sol.BASE0)
        self.set_fill(sol.BASE3, opacity=opacity)
        self.move_to(g.get_center())

class TranslucentBoxOverlay(Rectangle):
    def __init__(self, *enclosed_mobjects, margin = 0.2, opacity = 1): #0.925
        g = Group(*enclosed_mobjects)

        width = g.get_right()[0] - g.get_left()[0] + 2 * margin
        height = g.get_top()[1] - g.get_bottom()[1] + 2 * margin

        super().__init__(width=width, height=height, color=sol.BASE0)
        self.set_fill(
            interpolate_color(sol.BASE3, WHITE, 0),
            opacity=opacity
        )
        self.move_to(g.get_center())
