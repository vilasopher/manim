from manim import *
import solarized as sol

class Tile(Square):
    def __init__(
        self,
        number,
        side_length = 1,
        background_color = sol.BASE1,
        edge_color = sol.BASE02,
        number_color = sol.BASE03
    ):
        super().__init__(
            side_length=side_length,
            color=edge_color
        )

        self.set_fill(background_color, opacity=1)

        self.add(
            DecimalNumber(
                number,
                color = number_color,
                num_decimal_places=0,
                font_size = 70
            ).next_to(self, ORIGIN)
        )