punkty = 0
odpowiedz = input("Czy 2+2 to 4? ")
a = str(odpowiedz.strip().casefold())

if a == "tak":
    punkty += 1
    print("Gratulacje, to prawidłowa odpowiedź!")
    print(punkty)
else:
    print("Źle, to niepoprawna odpowiedź.")
    print(punkty)

