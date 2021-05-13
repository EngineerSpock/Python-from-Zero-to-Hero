from true_or_false.game import Game
from true_or_false.game_result import GameResult
from true_or_false.game_status import GameStatus


def end_of_game_handler(result: GameResult):
    print(f"Questions asked:{result.questions_passed}. Mistakes made:{result.mistakes_made}.")
    print("You won!" if result.won else "You lost!")


game = Game("data\\Questions.csv", 3, end_of_game_handler)

while game.game_status == GameStatus.IN_PROGRESS:
    q = game.get_next_question()
    print("Do you believe in the next statement or question? Enter 'y' or 'n'")

    print(q.text)

    answer = input() == "y"

    if q.is_true == answer:
        print("Good job! You're right!")
    else:
        print("Oops, actually you're mistaken. Here is the commentary:")
        print(q.explanation)

    game.give_answer(answer)

