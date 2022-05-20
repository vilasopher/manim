from manim import *
import random
import solarized as sol
import networkx as nx

class IntersectionVGroup(VGroup):
    def __init__(self, group, mobject):
        super().__init__()
        for g in group:
            self.add(Intersection(g, mobject))

class GlitchTest(Scene):

    def split_mobj(self, mobj, dy=0.3):
        mobj_width = mobj.width
        for_split_recs = VGroup(
            *[
                Rectangle(
                    height=dy+random.uniform(-0.05,0.05),
                    width=mobj_width+0.1
                ) for i in range(int(mobj.height // dy+1))
            ]
        ).arrange(DOWN,buff=0).move_to(mobj)
        return VGroup(*[
            VGroup(
                *[
                    IntersectionVGroup(i,mobj).set(color=c,opacity=0.5) 
                    for c in [
                        "#FFFF00",
                        "#00FFFF",
                        "#FF00FF",
                        "#FF0000",
                        "#00FF00",
                        "#0000FF"
                    ]
                ],
                IntersectionVGroup(i,mobj)
            ) for i in for_split_recs 
        ])
    
    def construct(self):
        #mobj = Text("This is a glitchy animation.", font="Consolas")

        mobj = Graph.from_networkx(
            nx.paley_graph(13),
            vertex_config = sol.VERTEX_CONFIG,
            edge_config = sol.EDGE_CONFIG
        )

        mobj = Line([-1,-1,0],[1,1,0])

        self.add(mobj)
        self.wait()
        self.remove(mobj)

        another = Intersection(mobj, Circle())
        self.add(another)
        self.wait()

        return

        split = self.split_mobj(mobj)

        self.remove(mobj)
        self.add(split)

        split.save_state()
        def updater(split):
            m = 0
            if random.random() < 0.6:
                m = np.array([random.uniform(-.05,.05),random.uniform(-.05,.05),0])
            if random.random() < 0.6:
                split.restore()
                for i in split:
                    x = random.uniform(-.4,.4)*RIGHT + m
                    for j in i:
                        j.shift(np.array([random.uniform(-.05,.05),random.uniform(-.05,.05),0])+x)
            
        self.play(UpdateFromFunc(split,updater),run_time=0.5)
        split.restore()
        self.remove(split)
        self.add(mobj)
        self.wait()
