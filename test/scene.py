from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class Shapes(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)


class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.move_to(LEFT * 2)
        square.next_to(circle, LEFT)
        triangle.align_to(circle,LEFT)

        self.add(circle, square, triangle)
        self.wait(2)


class AnimateExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        self.play(square.animate.set_fill(WHITE))
        self.wait(1)

        self.play(square.animate.shift(UP).rotate(PI / 3))
        self.wait(1)


class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        super().__init__(number, **kwargs)
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        number = DecimalNumber().set_color(WHITE).scale(5)
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        self.play(Count(number,0,100), run_time=4, rate_func=linear)

        self.wait()
