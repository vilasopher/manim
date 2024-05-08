from manim import *
import solarized as sol

class TVDefinition(Scene):
    def construct(self):
        def1text = MathTex(
            r'\textbf{Definition 1: } \mathrm{d_{TV}}(\mu, \lambda) = \frac{1}{2} \sum_{x \in \Omega} |\mu(x) - \lambda(x)|',
            color=sol.BASE03
        )
        def2text = MathTex(
            r'\textbf{Definition 2: } \mathrm{d_{TV}}(\mu,\lambda) = \max_{A \subseteq \Omega} |\mu(A) - \lambda(A)|',
            color=sol.BASE03
        )
        def3text = MathTex(
            r'\textbf{Definition 3: } \mathrm{d_{TV}}(\mu, \lambda) = \min_{\substack{X \sim \mu \\ Y \sim \lambda}} \mathbb{P}[X \neq Y]',
            color=sol.BASE03
        )

        def1text.next_to(def2text, UP).align_to(def2text, LEFT)
        def3text.next_to(def2text, DOWN).align_to(def2text, LEFT)

        self.add(def1text, def2text, def3text)