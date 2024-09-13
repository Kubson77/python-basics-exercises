"""
Sumowanie liczb z pętli
Napisz program, który pyta użytkownika o 5 liczb, a następnie oblicza i
wyświetla ich sumę. Wykorzystaj pętlę  for .
"""

from typing import List


def max_number(numbers: List[int]) -> int:
    result = 0
    for number in numbers:
        result += number
    return result


source = []
for _ in range(5):
    try:
        source.append(int(input(f"Provide a number: ")))
    except ValueError:
        print("Entered value is not a number")
        exit(-1)

print(max_number(source))
