def rysuj_funkcje_kosztu(iteracje, koszty):
    for i in range(len(iteracje)):
        print(f"Iteracja: {iteracje[i]} - Wartość kosztu: {koszty[i]}")

rysuj_funkcje_kosztu([1, 2, 3, 4], [100, 50, 25, 10])