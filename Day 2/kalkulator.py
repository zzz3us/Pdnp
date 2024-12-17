wartosc_a = int(input("Podaj pierwszą liczbę: "))
wartosc_b = int(input("Podaj drugą liczbę: "))
wartosc_c = int(input("Wybierz działanie: 1. Dodawanie, 2. Mnożenie, 3. Odejmowanie, 4. Dzielenie: "))

if wartosc_c == 1:
    wynik = wartosc_a + wartosc_b
elif wartosc_c == 2:
    wynik = wartosc_a * wartosc_b
elif wartosc_c == 3:
    wynik = wartosc_a - wartosc_b
else:
    wynik = wartosc_a / wartosc_b

print("Wynik to: ", wynik)