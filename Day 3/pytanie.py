odpowiedz = input("Czy 2+2 to 4? ")
a = str(odpowiedz.strip().casefold())

if a == "tak":
    print("Gratulacje, to prawidłowa odpowiedź!")
else:
    print("Źle, to niepoprawna odpowiedź.")