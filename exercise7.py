"""
Funkcja potęgowania
Napisz funkcję  power(a, b) , która zwraca wynik podniesienia liczby  a  do
potęgi  b . Nie używaj operatora  ** . Wykorzystaj pętlę  for.
"""


def power(a: int, b: int) -> int:
    if b < 0:
        raise  NotImplemented("Function can only take positive exponent")

    result = 1
    for _ in range(b):
        result *= a

    return result


print(power(2, 0))
print(power(2, 3))
print(power(2, 5))

