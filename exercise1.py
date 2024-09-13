"""
Kalkulator BMI
Napisz funkcję, która przyjmuje jako argumenty wzrost (w metrach) i wagę (w
kilogramach), a następnie oblicza i zwraca wskaźnik BMI. Na podstawie wyniku
zwróć odpowiedni komunikat.
- BMI < 18.5: "Niedowaga"
- 18.5 <= BMI < 25: "Waga prawidłowa"
- 25 <= BMI < 30: "Nadwaga"
- BMI >= 30: "Otyłość"
"""


def bmi_calc(weight: int, height: int) -> str:
    bmi = weight / height
    if bmi < 18.5:
        result = "Niedowaga"
    elif bmi < 25:
        result = "Waga prawidłowa"
    elif bmi < 30:
        result = "Nadwaga"
    else:
        result = "Otyłość"

    return f"Twój wskaźnik BMI to: {bmi}, wynik: {result}"


print(bmi_calc(190, 100))
