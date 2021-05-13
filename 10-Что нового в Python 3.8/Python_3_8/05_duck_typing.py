from typing import Protocol, List


class Bird:
    def fly(self):
        print('fly with wings')


class Airplane:
    def fly(self):
        print('fly with fuel')


class Flyable(Protocol):
    def fly(self): ...


def process_flyables(flyables: List[Flyable]):
    for cur_obj in flyables:
        cur_obj.fly()


class Fish:
    def swim(self):
        print('fish swim in sea')


process_flyables([Bird(), Airplane(), Fish()])
