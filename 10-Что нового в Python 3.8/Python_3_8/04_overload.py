from typing import Union, Literal, overload


def parse_roman(roman):
    romans = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    result = 0
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and romans[roman[i]] < romans[roman[i + 1]]:
            result -= romans[roman[i]]
        else:
            result += romans[roman[i]]
    return result


def convert_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


@overload
def add(x: str, y: str, to_arabic: Literal[True]) -> int: ...


@overload
def add(x: str, y: str, to_arabic: Literal[False]) -> str: ...


def add(x: str, y: str, to_arabic: bool) -> Union[str, int]:
    a = parse_roman(x)
    b = parse_roman(y)

    c = a + b

    return c if to_arabic else convert_to_roman(c)


result1 = add('I', 'II', True)

# III
r = result1 / 3
