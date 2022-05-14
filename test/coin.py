from manim import *

class CoinFlip(Scene):
    def construct(self):
        c = Cylinder(color=BLUE_B, fill_opacity = 1, height=0.2, radius=1)
        top = Annulus(inner_radius=0.9, outer_radius=1).shift(OUT*0.1)
        top.add(Tex('H').scale(2).shift(OUT * 0.1))
        bot = Annulus(inner_radius=0.9, outer_radius=1).shift(IN*0.1)
        bot.add(Tex('T').scale(2).shift(IN* 0.1))
        c.add_bases()
        c.add(top)
        c.add(bot)


        x = ValueTracker(0)
        y = ValueTracker(0)
        z = ValueTracker(1)

        def update(s):
            s.set_direction(
                np.array(
                    [x.get_value(), y.get_value(), z.get_value()]
                )
            )
            if z.get_value() > 0:
                top.set_opacity(0)
                bot.set_opacity(1)
            else:
                top.set_opacity(1)
                bot.set_opacity(0)

        c.add_updater(update)
        self.add(c)


        self.play(
            y.animate.set_value(1),
            z.animate.set_value(0)
        )

        self.play(
            y.animate.set_value(0),
            z.animate.set_value(-1)
        )

        self.play(
            y.animate.set_value(-1),
            z.animate.set_value(0)
        )

        self.play(
            y.animate.set_value(0),
            z.animate.set_value(1)
        )
