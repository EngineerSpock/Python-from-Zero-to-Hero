# f = open(r'C:\file.txt', 'v')
# from typing import Literal, Final
#
#
# def open_file(file, mode: Literal['r', 'w']):
#     pass
#
#
# open_file(r'C:\file.txt', 'v')
#
# pi: Final = 3.14
#
# pi = 1.2
from typing import final, Dict, Any


@final
class Dog:
    def __init__(self):
        self.paws = 4
        self.health = 100
        self.sound = 'woof-woof'

    def bark(self):
        print(self.sound)


class SuperDog(Dog):
    def __init__(self):
        super().__init__()
        self.health = 200
        self.sound = 'super-woof'


dog = SuperDog()
print(dog.health)
dog.bark()

person: Dict[str, str] = {'name': 'john', 'last_name': 'conrad', 'sex': 'm'}

dict_result: Dict[str, Any] = {'word': 'hello', 'count': 5, 'comment': 'a very interesting word'}
dict_result['comment'] = 123
print(dict_result['lol'])

from typing import TypedDict


class WordStat(TypedDict):
    word: str
    count: int
    comment: str


dict_result: WordStat = {'word': 'hello', 'count': 5, 'comment': 'a very interesting word'}

# dict_result: WordStat = {'word': 'hello', 'comment': 'a very interesting word'}

print(dict_result['lol'])
