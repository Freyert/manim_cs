from src.list import List
from manim import Scene, Create, Indicate, AnimationGroup


class Basic(Scene):
    def construct(self):
        l = List([1, 2, 3, 4])
        self.play(*[ Create(x) for x in l])
        self.play(Indicate(l[2]))
        self.wait()
        self.play(l.push(5), l.push(6))
        self.wait()