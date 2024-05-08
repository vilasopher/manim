from manim import *
import solarized as sol

class TVDefinition(Scene):
    def construct(self):
        def1text = MathTex(
            r'd_{\mathrm{TV}}(\mu, \lambda) = \frac{1}{2} \sum_{x \in \Omega} |\mu(x) - \lambda(x)|',
            color=sol.BASE3
        )

        self.add(def1text)