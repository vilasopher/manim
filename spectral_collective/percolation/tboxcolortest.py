from manim import *
from translucent_box import TranslucentBox, TranslucentBoxOverlay
import solarized as sol

class Background(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(0.5)

        p = Dot(color = sol.BASE03)
        q = Dot(color = sol.BASE03)
        p.shift(2 * LEFT)
        q.shift(2 * RIGHT)
        self.add(p,q)

        l = Line(color = sol.BASE03)
        m = Line(color = sol.BASE03)
        l.rotate(PI/2).shift(2 * LEFT)
        m.rotate(PI/2).shift(2 * RIGHT)
        self.add(l,m)

        u = Line(color = sol.BASE03)
        u.shift(2 * LEFT)
        t = TranslucentBox(u)
        self.add(t,u)


class Foreground(MovingCameraScene):
    def construct(self):
        config.background_opacity = 0
        self.camera.frame.scale(0.5)

        v = Line(color = sol.BASE03)
        v.shift(2 * RIGHT)
        s = TranslucentBoxOverlay(v)
        self.add(s,v)
