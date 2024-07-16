from manim import *
import solarized as sol

tt = TexTemplate()
tt.add_to_preamble(r'\usepackage{amsfonts}')
tt.add_to_preamble(r'\usepackage{amsmath}')
tt.add_to_preamble(r'\usepackage{xcolor}')
tt.add_to_preamble(r'\addtolength{\jot}{-0.35em}')
tt.add_to_preamble(r'\renewcommand{\P}{\mathbb{P}}')
tt.add_to_preamble(r'\newcommand{\coloredt}{t}')
tt.add_to_preamble(r'\newcommand{\coloredn}{n}')
tt.add_to_preamble(r'\newcommand{\coloredeps}{\varepsilon}')