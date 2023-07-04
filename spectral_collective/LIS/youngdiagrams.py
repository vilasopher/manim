from manim import *
import solarized as sol

class Tile(Square):
    def __init__(
        self,
        number = None,
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

        self.push_self_into_submobjects()

        if not number is None:
            self.add(
                DecimalNumber(
                    number,
                    color = number_color,
                    num_decimal_places=0,
                    font_size = 80
                ).next_to(self, ORIGIN)
            )
        
class YoungDiagram(Group):
    def __init__(
        self,
        permutation,
        unit=1,
        origin=2*UP+2*LEFT,
        background_color=sol.BASE1,
        edge_color=sol.BASE02,
        first_row_highlighted=False
    ):
        self.unit = unit
        self.origin = origin
        self.background_color = background_color
        self.edge_color = edge_color
        self.first_row_highlighted = first_row_highlighted

        self.tableau = [[permutation[0]]]
        self.lengths = [1]
        self.heights = [1]

        for n in permutation[1:]:
            self.insert(n)

        super().__init__(*self.construct_submobjects())

    def insert_to_row(self, n, r):
        row = self.tableau[r]

        if len(row) == 0 or n > max(row):
            row.append(n)
            self.lengths[r] += 1
            if r == 0:
                self.heights.append(1)
            else:
                self.heights[self.lengths[r]-1] += 1
            return -1
        else:
            for i, m in enumerate(row):
                if m > n:
                    row[i] = n
                    return m

    def insert(self, n):
        r = -1
        m = n

        while m > -1:
            r += 1
            if len(self.tableau) <= r:
                self.tableau.append([])
                self.lengths.append(0)
            m = self.insert_to_row(m, r)

    def set_unit(self, unit):
        self.unit = unit

    def set_origin(self, origin):
        self.origin = origin

    def highlight_first_row(self):
        self.first_row_highlighted = True

    def unhighlight_first_row(self):
        self.first_row_highlighted = False

    def redraw(self):
        self.remove(*self.submobjects)
        self.add(*self.construct_submobjects())

    def construct_submobjects(self):
        rows = [
            Rectangle(
                color=self.edge_color,
                height=self.unit,
                width=self.unit*l,
                stroke_width=4*self.unit
            ).set_fill(
                self.background_color,
                opacity=1
            ).align_to(
                self.origin,
                UP + LEFT
            ).shift(h*self.unit*DOWN)
            for h, l in enumerate(self.lengths)
        ]
        
        if self.first_row_highlighted:
            rows[0].set_fill(sol.RED, opacity=1)

        verts = [
            Line(
                self.origin + l * self.unit * RIGHT,
                self.origin + l * self.unit * RIGHT 
                            + h * self.unit * DOWN,
                color = self.edge_color,
                stroke_width=4*self.unit
            )
            for l, h in enumerate(self.heights)
            if l > 0
        ]

        return [*rows, *verts]
