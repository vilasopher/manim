from manim import *
import numpy.random as ra
import numpy.linalg as la
import numpy as np
import solarized as sol
from functools import partial


class RandomMatrix(Scene):
    def construct(self):
        N = 9
        X = np.reshape(ra.normal(size=N*N),(N,N))
        E = la.eigvalsh(0.5*(X+np.transpose(X)))

        M = DecimalMatrix([[0]])

        M.add_updater(
            lambda m : m.become(
                DecimalMatrix(
                    0.5*(X+np.transpose(X)),
                    element_to_mobject_config = {
                        "num_decimal_places": 2,
                        "color": sol.BASE03
                    },
                    bracket_config = {
                        "color": sol.BASE03
                    }
                )
            ).scale(0.5),
            call_updater=True
        )

        evalpts = [Dot(ORIGIN, color=sol.BASE03) for _ in range(N)]

        def evpup(x, i):
            x.become(
                Dot(
                    3*DOWN+E[i]*RIGHT,
                    color=sol.BASE03
                )
            )

        for i, ep in enumerate(evalpts):
            ep.add_updater(
                partial(evpup, i=i),
                call_updater=True
            )

        def scene_updater(dt):
            for i in range(N):
                for j in range(N):
                    X[i,j] += -2*0.05*dt*X[i,j]+2*np.sqrt(0.05*dt)*ra.normal()
            E2 = la.eigvalsh(0.5*(X+np.transpose(X)))
            for i in range(N):
                E[i] = E2[i]

        self.add_updater(scene_updater)

        self.add(M)

        self.add(*evalpts)

        self.wait(5)

