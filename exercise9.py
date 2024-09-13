"""
Liczby Fibonacciego
Napisz funkcję, która przyjmuje liczbę  n  i zwraca  n -ty element ciągu
Fibonacciego. Wykorzystaj pętlę  while  lub  for
"""


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n is negative")

    prev, curr = 0, 1
    while curr <= n:
        prev, curr = curr, prev + curr
    return prev


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(8))
print(fibonacci(10))
