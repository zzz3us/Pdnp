import sys

wiek = 47
rok = 2024
temp = 36.6

print(temp)
print(type(temp))  # <class 'float'>, liczby zmmiennoprzecinkowe

print(wiek + rok)  # 2071
print(wiek - rok)  # -1977
print(wiek * rok)  # 95128
print(wiek / rok)  # 0.023221343873517788

print(rok // wiek)  # częśc całkowita dzielenia, 43
print(rok % wiek)  # modulo, reszta z dzielenia, 3
print(5 % 2)  # 1

print(wiek ** rok)  # potęgowqaie

# len() - sprawdzanie długości
print(len(str(wiek ** rok)))  # 3385 znaków
# print(len(str(wiek ** rok ** 2))) # 3385 znaków
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# float ma bnłąd zzaokrąglenia
# wynika z zapisu wykładniczego
# 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
print(sys.float_info)
# sys.float_info(
#     max=1.7976931348623157e+308,
#     max_exp=1024,
#     max_10_exp=308,
#     min=2.2250738585072014e-308,
#     min_exp=-1021,
#     min_10_exp=-307,
#     dig=15,
#     mant_dig=53,
#     epsilon=2.220446049250313e-16,
#     radix=2, rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")  # Sprawdzenie zmiennej 36.6 47

print(f"""
{temp}
    {wiek}""")
# "36.6
#     47"

# typ logiczny
# prawda,  fałsz
# 1, 0
# True, False
czy_znasz_pythona = True
print(type(czy_znasz_pythona))  # <class 'bool'>, typ logiczny
print(czy_znasz_pythona)  # True

print(int(czy_znasz_pythona))  # 1
print(int(False))  # 0

print(bool(100))
print(bool(-10))
print(bool("radek"))

print(bool("0"))  # True
print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # odpowiednik null, nic, stan nieokreslony

# and - i
# Expression    Evaluates to
# True and True    True
# True and False    False
# False and True    False
# False and False    False
# The or Operator’s Truth Table:

print(True and True)  # True
print(True and False)  # False

# or - lub
# Expression    Evaluates to
# True or True    True
# True or False    True
# False or True    True
# False or False    False
# The not Operator’s Truth Table:
print(True or False)  # True

# not - negacja
# Expression    Evaluates to
# not True    False
# not False
print(not False)  # True

a = 8
b = 6

print(f"Porównanie {a} > {b} = {a > b}")
print(f"Porównanie {a} < {b} = {a < b}")
print(f"Porównanie {a} <= {b} = {a <= b}")
print(f"Porównanie {a} >= {b} = {a >= b}")
print(f"Porównanie {a} == {b} = {a == b}")  # == czy równe?
print(f"Porównanie {a} != {b} = {a != b}")  # != czy rózne?
# Porównanie 8 > 6 = True
# Porównanie 8 < 6 = False
# Porównanie 8 <= 6 = False
# Porównanie 8 >= 6 = True
# Porównanie 8 == 6 = False
# Porównanie 8 != 6 = True
