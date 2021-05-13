from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    text: str
    is_true: bool
    explanation: str


# class Question:
#
#     def __init__(self, text, is_true, explanation):
#         self.text = text
#         self.is_true = is_true
#         self.explanation = explanation

