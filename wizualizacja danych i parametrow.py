def funkcja_kosztu(x, y, theta_0, theta_1):
    m = len(x)
    suma_bledow = 0

    for i in range(m):
        przewidywane_y = theta_0 + (theta_1 * x[i])
        rzeczywiste_y = y[i]
        blad = (przewidywane_y - rzeczywiste_y) ** 2
        suma_bledow += blad

    koszt = suma_bledow / (2 * m)

    return (f"koszt wynosi: {koszt}")


x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

wynik = funkcja_kosztu(x, y, 0, 3)
print(wynik)