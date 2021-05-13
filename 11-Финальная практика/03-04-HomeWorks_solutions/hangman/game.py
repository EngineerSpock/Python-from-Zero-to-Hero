import random

from hangman.game_status import GameStatus
from hangman.invalid_operation_exception import InvalidOperationException


class Game:

    def __init__(self, allowed_misses: int = 6):

        if allowed_misses < 5 or allowed_misses > 8:
            raise ValueError("Number of allowed misses should be between 5 and 8")

        self.__allowed_misses = allowed_misses
        self.__tries_counter = 0
        self.__tried_letters = []
        self.__open_indexes = []
        self.__game_status = GameStatus.NOT_STARTED
        self.__word = ""

    def generate_word(self):
        filename = "data\\WordsStockRus.txt"

        words = []
        with open(filename, encoding='UTF8') as file:
            for line in file:
                words.append(line.rstrip('\n'))

        rand_index = random.randint(0, len(words) - 1)

        self.__word = words[rand_index]

        self.__open_indexes = [False for _ in self.word]
        self.__game_status = GameStatus.IN_PROGRESS

        return self.word

    def guess_letter(self, letter: str):
        """

        :type letter: str
        """
        if self.tries_counter == self.allowed_misses:
            raise InvalidOperationException(f"Exceeded the max misses number: {self.allowedMisses}")
        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationException(f"Inappropriate status of game:{GameStatus}")

        open_any = False
        result = []

        for i in range(len(self.word)):
            cur_letter = self.word[i]
            if cur_letter == letter:
                self.__open_indexes[i] = True
                open_any = True

            if self.__open_indexes[i]:
                result.append(cur_letter)
            else:
                result.append("-")

        if not open_any:
            self.__tries_counter += 1

        self.__tried_letters.append(letter)

        if self.__is_winning():
            self.__game_status = GameStatus.WON
        elif self.tries_counter == self.allowed_misses:
            self.__game_status = GameStatus.LOST

        return result

    @property
    def game_status(self):
        return self.__game_status

    @property
    def word(self):
        return self.__word

    @property
    def allowed_misses(self):
        return self.__allowed_misses

    @property
    def tries_counter(self):
        return self.__tries_counter

    @property
    def tried_letters(self):
        return sorted(self.__tried_letters)

    @property
    def remaining_tries(self):
        return self.allowed_misses - self.tries_counter

    def __is_winning(self):
        for cur in self.__open_indexes:
            if not cur:
                return False
        return True
