from manim import *
import solarized as sol

class EX(Scene):
    def construct(self):
        hyp = Tex(
            r'\textbf{Lemma:} Let $X$ be a random variable \\'
            r'taking values in $\{0,1,2,3,4,...\}$. Then',
            color=sol.BASE03,
            font_size=50
        ).move_to(3.2 * UP + 2.5 * RIGHT)
        conc = MathTex(
            r'\mathbb{E}[X] = \sum_{n=1}^\infty \mathbb{P}[X \geq n]',
            color=sol.BASE03,
            font_size=50
        ).move_to(1.6 * UP + 4.2 * RIGHT)

        # TODO: THIS BG STILL KIND OF LOOKS BAD!
        bg = Circle(
            radius = 15,
            color=sol.BASE2,
            fill_opacity=1
        ).move_to(15.75 * UP + 5.5 * RIGHT)
        self.add(bg)

        self.add(hyp,conc)

        npn = [
            MathTex(
                str(n) + r'\cdot p_' + str(n),
                color=sol.BLUE,
                font_size=30
            ).move_to(6 * LEFT + n * DOWN - 2.6 * DOWN)
            for n in range(1,7)
        ]
        plus1 = [ MathTex(r'+', color=sol.BASE03, font_size=30).move_to(
                        6 * LEFT + n * DOWN - 2.1 * DOWN)
                    for n in range(1,7)
        ]
        sideqs = [ MathTex(r'=', color=sol.BLUE, font_size=30).move_to(
                        5 * LEFT + n * DOWN - 2.6 * DOWN)
                    for n in range(1,7)
        ]
        self.add(*npn)
        self.add(*plus1)
        self.add(*sideqs)

        temp = TexTemplate()
        temp.add_to_preamble(r'\usepackage{mathtools}')

        hint = Tex(r'(where $p_m \coloneqq \mathbb{P}[X=m]$)',
                color=sol.BASE01,
                tex_template=temp,
                font_size=30)
        hint.move_to(3.6 * UP + 5.3 * LEFT)
        self.add(hint)

        ex = MathTex(r'\mathbb{E}[X]', color=sol.BASE03, font_size=35)
        ex.move_to(6 * LEFT + 2.8 * UP)
        eq = MathTex(r'\coloneqq',
                tex_template=temp,
                color=sol.BASE03,
                font_size=35)
        eq.rotate(-PI/2)
        eq.move_to(6 * LEFT + 2.2 * UP)
        self.add(ex, eq)

        gridcirc = [
            Circle(color=sol.BASE1, fill_opacity=1, radius=0.2).move_to(
                (4 - 2 * i) * LEFT + n * DOWN - 2.6 * DOWN)
            for n in range(1,7) for i in range(n)
        ]

        gridpn = [
            MathTex(r'p_'+str(n), color=sol.BASE03, font_size=25).move_to(
                (4 - 2 * i) * LEFT + n * DOWN - 2.6 * DOWN)
            for n in range(1,7) for i in range(n)
        ]
        self.add(*gridcirc)
        self.add(*gridpn)

        horizrects = [
            Rectangle(
                width = 0.6 + 2 * n,
                height = 0.6,
                color = sol.BLUE
            ).move_to((4 - n) * LEFT + n * DOWN - 1.6 * DOWN)
            for n in range(6)
        ]
        self.add(*horizrects)

        vertrects = [
            Rectangle(
                width = 0.75,
                height = 10,
                color = sol.RED
            ).move_to( (4 - 2 * n) * LEFT + n * DOWN + 3.025 * DOWN)
            for n in range(6)
        ]
        self.add(*vertrects)

        pxn = [
            MathTex(
                r'\mathbb{P}[X \geq' + str(n) + r']',
                color=sol.RED,
                font_size=30
            ).move_to((6 - 2 * n) * LEFT + (n-1) * DOWN - 2.9 * DOWN)
            for n in range(1,7)
        ]
        verteqs = [
            MathTex(r'=', color=sol.RED, font_size=30).rotate(
                -PI/2).move_to(
                (6 - 2 * n) * LEFT + (n-1) * DOWN - 2.4 * DOWN)
            for n in range(1,7)
        ]
        self.add(*pxn)
        self.add(*verteqs)

class Kolmogorov(Scene):
    def construct(self):
        temp = TexTemplate()
        temp.add_to_preamble(r'\usepackage[margin=0in]{geometry}')

        lem1 = Tex(
            r'\textbf{Lemma:} '
            r'$\mathbb{P}_p[\text{there is an infinite cluster}] = 0'
            r'\Leftrightarrow'
            r'\mathbb{P}_p[\text{the cluster of } o \text{ is infinite}]=0$',
            color=sol.BASE03,
            tex_template=temp,
            font_size=36
        ).move_to(3.5 * UP)
        lem2 = Tex(
            r'and '
            r'$\mathbb{P}_p[\text{there is an infinite cluster}] = 1'
            r'\Leftrightarrow'
            r'\mathbb{P}_p[\text{the cluster of } o \text{ is infinite}]>0$.',
            color=sol.BASE03,
            tex_template=temp,
            font_size=36
        ).move_to(3 * UP + 0.52 * RIGHT)

        bg = Rectangle(width = 15, height = 3, color=sol.BASE2, fill_opacity=1)
        bg.move_to(4.1 * UP)
        self.add(bg)
        self.add(lem1, lem2)

        temp2 = TexTemplate()
        temp2.add_to_preamble(r'\usepackage[margin=1.5in]{geometry}')
        temp2.add_to_preamble(r'\usepackage[document]{ragged2e}')
        temp2.add_to_preamble(r'\usepackage[english]{babel}')
        temp2.add_to_preamble(r'\usepackage{amsmath}')
        proof = Tex(
            r'\raggedright'
            r'\setlength{\abovedisplayskip}{5pt}'
            r'\setlength{\belowdisplayskip}{5pt}'
            r'\textbf{\emph{Proof:}} First, notice that the event '
            r'$\{ \text{there is an infinite cluster} \}$'
            r' is a \emph{tail event}, i.e. it does not depend'
            r' on the state of any finite set of edges in the grid.'
            r" Therefore, by \emph{Kolmogorov's Zero-One Law},",
            r' for any parameter value $p$ we have ',
            r'$\mathbb{P}_p[\text{there is an infinite cluster}]=0\text{ or }1.$'
            r'\\ \hfill \\ \vspace{-0.1cm}'

            r'Now, suppose that '
            r'$\mathbb{P}_p[\text{the cluster of }o\text{ is infinite}]>0$. '
            r'Then, since'
            r'\begin{align*}'
            r'\{\text{the cluster of } o \text{ is infinite}\}'
            r'&\subseteq'
            r'\{\text{there is an infinite cluster}\}, \text{we have} \\'
            r'0 < \mathbb{P}_p[\text{the cluster of } o \text{ is infinte}]'
            r'&\leq \mathbb{P}_p[\text{there is an infinite cluster}].'
            r'\end{align*}'
            r'So we must have '
            r'$\mathbb{P}_p[\text{there is an infinite cluster}] = 1$ '
            r'by the Zero-One law.'
            r'\\ \hfill \\ \vspace{-0.1cm}'

            r'On the other hand, suppose that '
            r'$\mathbb{P}_p[\text{the cluster of }o\text{ is infinite}]=0$. '
            r'Then, since the percolation does not depend on the choice of origin, '
            r'for any node $v$ of the grid '
            r'we have $\mathbb{P}_p[\text{the cluster of }v\text{ is infinite}]=0$. '
            r'If there is an infinite cluster somewhere in the grid, then there is '
            r'some node $v$ whose cluster is infinite. '
            r'Thus, by countable additivity of probability '
            r'(the grid is countable), we obtain '
            r'$\mathbb{P}_p[\text{there is an infinite cluster}]=0$.'
            r'\hfill $\blacksquare$'
            ,color=sol.BASE03,
            tex_template = temp2,
            font_size = 33
        )
        proof.shift(0.7 * DOWN)
        self.add(proof)

