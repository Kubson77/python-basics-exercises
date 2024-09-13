"""
Licznik liczb pierwszych
Napisz funkcję, która przyjmuje liczbę całkowitą i zwraca liczbę liczb
pierwszych mniejszych lub równych tej liczbie. Nie przejmuj się wydajnością,
załóżmy, że podana liczba jest niewielka.
"""


def prime_numbers(number: int) -> int:
    if number < 2:
        return 0
    if number < 3:
        return 1
    if number < 5:
        return 2
    if number < 6:
        return 3

    result = 3
    for i in range(6, number + 1):
        if not (number % 2 == 0 or number % 3 == 0 or number % 5 == 0):
            result += 1

    return result
