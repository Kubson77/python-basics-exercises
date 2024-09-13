"""
Kalkulator z operacjami matematycznymi
Napisz funkcję, która przyjmuje dwa argumenty (liczby) oraz znak operacji
matematycznej (czyli +, -, * lub /) i zwraca wynik. Jeśli użytkownik poda
nieprawidłowy znak, zwróć komunikat o błędzie
"""
from typing import Union


def calculator(x: int, y: int, operation: str) -> Union[int, float]:
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        if y == 0:
            raise ZeroDivisionError("Zero division error")
        return x / y
    else:
        raise ValueError("Invalid operation")


print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))
print(calculator(10, 0, "/"))
