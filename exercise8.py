""""
Sprawdzanie palindromów
Napisz funkcję, która sprawdza, czy podany ciąg znaków (string) jest
palindromem. Funkcja powinna zwracać  True  lub  False .
"""


def is_palindrome(word: str) -> bool:
    return word == word[::-1]


print(is_palindrome("kajak"))
