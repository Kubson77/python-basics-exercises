"""
Największa liczba w liście
Napisz funkcję, która przyjmuje listę liczb i zwraca największą liczbę z tej
listy.
"""

from typing import List


def max_number(numbers: List[int]) -> int:
    return max(numbers)


print(max_number([1, 2, 77, 3, 4, 5]))
