"""
Liczby parzyste w zakresie
Napisz funkcję, która przyjmuje dwie liczby i zwraca listę liczb parzystych
pomiędzy nimi. Wykorzystaj pętlę  while  lub  for
"""


# Z pętlą for
def even_numbers(start: int, stop: int) -> int:
    result = 0
    if start % 2 == 0:
        start += 1

    for x in range(start + 1, stop, 2):
        result += 1

    return result


print(even_numbers(1, 8))
print(even_numbers(2, 8))
print(even_numbers(1, 7))
print(even_numbers(2, 7))

print("-" * 5)


# Inne rozwiązanie
def even_numbers_2(start: int, stop: int) -> int:
    stop -= 1
    if start % 2 == 0:
        return (stop - start) // 2
    else:
        return (stop - start + 1) // 2


print(even_numbers_2(1, 8))
print(even_numbers_2(2, 8))
print(even_numbers_2(1, 7))
print(even_numbers_2(2, 7))
