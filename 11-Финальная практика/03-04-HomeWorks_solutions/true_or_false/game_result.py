from dataclasses import dataclass


@dataclass
class GameResult:
    questions_passed: int
    mistakes_made: int
    won: bool
