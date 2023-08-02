from manim import *
import numpy as np
import numpy.random as ra
import solarized as sol
from youngdiagrams import YoungDiagram

TLC = 21*DOWN
R = 15*(LEFT+UP)
D = 15*(RIGHT+UP)

def wx(t):
    return (2*t/np.pi + 1) * np.sin(t) + (2/np.pi) * np.cos(t)

def wy(t):
    return (2*t/np.pi - 1) * np.sin(t) + (2/np.pi) * np.cos(t)

LIMIT_SHAPE = Polygon(
    TLC,
    *(
        TLC + wx(t)*R + wy(t)*D
        for t in np.linspace(-np.pi/2, np.pi/2, 200)
    ),
    TLC,
    color = sol.CYAN,
    stroke_width = 12
).set_fill(sol.CYAN, opacity=0.2)

class Thumbnail1(Scene):
    def insertPoint(self, p):
        start = -1
        end = len(self.points)
        mid = -1

        while start < end - 1:
            mid = (start+end)//2

            if p[0] < self.points[mid][0]:
                end = mid
            else:
                start = mid
            
        self.points = self.points[:end] + [p] + self.points[end:]

    def longestIncreasingSubsequence(self):
        P = {}
        M = {0 : -1}
        L = 0

        for i, p in enumerate(self.points):
            lo = 1
            hi = L+1

            while lo < hi:
                mid = lo + (hi-lo)//2

                if self.points[M[mid]][1] >= p[1]:
                    hi = mid
                else:
                    lo = mid+1
            
            newL = lo
            P[i] = M[newL-1]
            M[newL] = i
            
            if newL > L:
                L = newL
        
        S = []
        k = M[L]
        for j in reversed(range(L)):
            S.append(self.points[k])
            k = P[k]
        
        return list(reversed(S))

    def construct(self):
        self.points = []

        for _ in range(2000):
            self.insertPoint(tuple(ra.uniform(size=2)))

        pointcloud = {
            p : 
            Dot(
                radius = 0.12,
                color = sol.BASE03
            ).shift(2*UP + (20/np.sqrt(2))*LEFT + p[0] * 20*(RIGHT+UP) + p[1] * 20*(RIGHT+DOWN))
            for p in self.points
        }

        LIS = self.longestIncreasingSubsequence()

        self.add(*(pointcloud[p] for p in self.points))

        for p in LIS:
            self.bring_to_front(pointcloud[p])
            pointcloud[p].set_color(sol.RED)

        LISline = [
            Line(
                pointcloud[LIS[i]].get_center(),
                pointcloud[LIS[i+1]].get_center(),
                color=sol.RED,
                stroke_width=12
            ) for i in range(len(LIS)-1)
        ]

        self.add(*LISline)


class Thumbnail2(Scene):
    def construct(self):

        N = 2000

        self.add(YoungDiagram(ra.uniform(size=N), unit=np.sqrt(2)*15/np.sqrt(N), origin=21*DOWN).rotate(PI*3/4, about_point=21*DOWN))
        self.add(LIMIT_SHAPE)

        self.add(
        )

        permutation = [4, 1, 2, 7, 6, 5, 8, 9, 3]
        nums = [
            DecimalNumber(
                j,
                color=sol.BASE03,
                num_decimal_places=0,
                font_size=200
            ).move_to(1.5*(i-4)*RIGHT)
            for i,j in enumerate(permutation)
        ]
        for i in [1, 2, 4, 6, 7]:
            nums[i].set_color(sol.RED)

        self.add(*nums)