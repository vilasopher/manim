from manim import *
import solarized as sol
from translucent_box import TranslucentBox

config.background_opacity = 0

class pOneHalf(Scene):
    def construct(self):
        pval = MathTex(r'{{ p }} = 1/2', color = sol.BASE03)
        pval.set_color_by_tex(r'p', sol.RED)
        pval.move_to(5.8 * RIGHT + 3.3 * DOWN)
        tbox = TranslucentBox(pval)
        self.add(tbox, pval)

class BernoulliPercolationStill(Scene):
    def construct(self):
        bperc = Tex(r'Bernoulli Percolation', color = sol.BASE03, font_size = 100)
        bperc.move_to(UP)
        tbox = TranslucentBox(bperc)
        self.add(tbox, bperc)

class BernoulliPercolationBox(Scene):
    def construct(self):
        bperc = Tex(r'Bernoulli Percolation', color = sol.BASE03, font_size = 100)
        bperc.move_to(UP)
        tbox = TranslucentBox(bperc)
        self.add(tbox)

class BernoulliPercolationWrite(Scene):
    def construct(self):
        bperc = Tex(r'Bernoulli Percolation', color = sol.BASE03, font_size = 100)
        bperc.move_to(UP)
        self.play(
            Write(bperc)
        )

class BernoulliRV(Scene):
    def construct(self):
        brv = MathTex(r'&\text{a \emph{Bernoulli Random Variable} takes} \\',
                      r'&\text{one of exactly \emph{two} different values.}',
                      color = sol.BASE03)
        brv.move_to(DOWN)
        tbox = TranslucentBox(brv)
        self.add(tbox, brv)
        
