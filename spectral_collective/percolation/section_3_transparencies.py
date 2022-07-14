from manim import *
import solarized as sol
from translucent_box import TranslucentBox

config.background_opacity = 0

class ClusterDef(Scene):
    def construct(self):
        text = Tex(
                r'connected components = open clusters',
                color = sol.BASE03,
                font_size=70
            )
        tbox = TranslucentBox(text)
        self.add(tbox, text)
