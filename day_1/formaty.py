user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # <class 'float'>, liczby zmiennoprzecinkowe
print(type(wersja))  # <class 'float'>
liczba = 456789123456  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# Witaj Tomek, masz teraz 39 lat.
# s - str
# d - digit
# TypeError: %d format: a real number is required, not str
# print("Witaj %d, masz teraz %s lat." % (user, wiek))

print("Witaj %(user)s, jestes %(user)s" % {'user': user})
# Witaj 'Tomek', jestes Tomek %a
# Witaj Tomek, jestes Tomek %s

print("Witaj {}. masz teraz {} lat.".format(user, wiek))
# f - string, tekst sforamtowany
print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.

print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3)  # Używamy wersji pythona 3.000000
print("Używamy wersji pythona %f" % 3.9)  # Używamy wersji pythona 3.900000
print("Używamy wersji pythona %.2f" % 3.9)  # Używamy wersji pythona 3.90
print("Używamy wersji pythona %.1f" % 3.9)  # Używamy wersji pythona 3.9
print("Używamy wersji pythona %.0f" % 3.9)  # Używamy wersji pythona 4 zaokrągli
print("Używamy wersji pythona %.f" % 3.9)  # Używamy wersji pythona 4
x = 3.8796
print(x)  # 3.8796
print("%.2f" % x)  # 3.88
print(x)  # 3.8796

# zaokrąglanie liczby
y = round(x)
print(y)  # 4

z = round(x, 2)
print(z)  # 3.88

print(f"Uzywamy wersji python {wersja}")  # Uzywamy wersji python 3.900001
print(f"Uzywamy wersji python {wersja:.1f}")  # Uzywamy wersji python 3.9
print(f"Uzywamy wersji python {wersja:.2f}")  # Uzywamy wersji python 3.90
print(f"Uzywamy wersji python {wersja:.0f}")  # Uzywamy wersji python 4

print(f"{user:<10}")  # "Tomek     "
print(f"{user:>20}")  # "               Tomek"
print(f"{user:^20}")  # "       Tomek        "
print(f"{user:.^20}")  # ".......Tomek........"

print(liczba)  # 456789123456
print(f"Nasza dua liczba {liczba:,}")  # Nasza dua liczba 456,789,123,456
print(f"Nasza dua liczba {liczba:_}")  # Nasza dua liczba 456_789_123_456
print(f"Nasza dua liczba {liczba:_}".replace("_", " "))
# Nasza dua liczba 456 789 123 456

liczba2 = 1500000000
liczba_2 = 1_500_000_000
print(type(liczba_2))  # <class 'int'>
print(liczba_2)  # 1500000000
