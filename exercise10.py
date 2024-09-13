"""
Konwersja temperatury
Napisz funkcję, która przyjmuje temperaturę w stopniach Celsjusza i zwraca jej
odpowiednik, który jest wyrażony w stopniach Fahrenheitach. Dla chętnych: dodaj
opcję odwrotną -- przeliczanie temperatury wyrażonej w Fahrenheitach na
Celsjusze.
"""
from typing import Union


def to_fahrenheit(celsius: Union[int, float]) -> Union[int, float]:
    return celsius * 1.8 + 32


def to_celsius(fahrenheit: Union[int, float]) -> Union[int, float]:
    return (fahrenheit - 32) / 1.8


print(to_fahrenheit(25))
print(to_celsius(77.0))
