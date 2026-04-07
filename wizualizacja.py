def rysuj_funkcje_kosztu(iteracje, koszty):
    for i in range(len(iteracje)):
        print(f"Iteracja: {iteracje[i]} - Wartość kosztu: {koszty[i]}")

rysuj_funkcje_kosztu([1, 2, 3, 4], [100, 50, 25, 10])

def oblicz_r2(y_prawdziwe, y_przewidywane):
    srednia_y = sum(y_prawdziwe) / len(y_prawdziwe)
    suma_kwadratow_resztek = sum((y_prawdziwe[i] - y_przewidywane[i]) ** 2 for i in range(len(y_prawdziwe)))
    calkowita_suma_kwadratow = sum((y - srednia_y) ** 2 for y in y_prawdziwe)
    r2 = 1 - (suma_kwadratow_resztek / calkowita_suma_kwadratow)
    print(f"Współczynnik R2 wynosi: {r2}")
    return r2