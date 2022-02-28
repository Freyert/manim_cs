from manim import Group, Square, Text, SingleStringMathTex, Tex, BLACK, RIGHT, LEFT
from typing import List, TypeVar

T = TypeVar('T')

class List(Group):
    def __init__(self, elements: List[T]) -> None:
        super().__init__(*[LabeledSquare(str(e)) for e in elements])
        self.arrange_submobjects()

# Used for building labeled squares. Based on LabeledDot.
class LabeledSquare(Square):
    def __init__(self, label: str | SingleStringMathTex | Text | Tex, side_length=2.0, **kwargs):

        rendered_label = Text(label)

        super().__init__(side_length=side_length, **kwargs)
        rendered_label.move_to(self.get_center())
        self.add(rendered_label)