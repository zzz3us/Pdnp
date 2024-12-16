# snake_case
# PEP8
# ctrl alt l - formatowanie kodu
import sys

print()  # wypisz/wydrukuj
print("Nazywam sie Radek")
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
# ctrl d - powielanie linii
# print("Nazywam się Radek')SyntaxError: unterminated string literal (detected at line 16)
# ctrl / - automatyczny komentarz
print('Nazywam się "Radek"')  # Nazywam się "Radek"

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'> - dane tekstowe
print("39")  # 39, str

print(39)  # 39
print(type(39))  # <class 'int'>

print("39" + "39")  # konkatenacja, łączenie tekstów
print(39 + 39)  # 78
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# silne typowanie - nie zamienia sam typu danych
# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str

print(int("39"))  # int() rzutowanie na liczbę
# print(int("A"))  # ValueError: invalid literal for int() with base 10: 'A'

print("39" + str(39))  # str() rzutowanie na str

print(5 * "4")  # 44444
print("160" * 25)  # 160160160160160160160160160160160160160160160160160160160160160160160160160
print(160 * 25)

# zmienna - pudełko na dane, przechowuje jeden element
# snake_case
# nazwa zmiennej powinna sugerowac co zawiera

liczba = 39
print(liczba)
print(type(liczba))  # <class 'int'>

liczba = "39"
print(type(liczba)) # <class 'str'>

name = "Radek"
print(name + "Kowalski") # RadekKowalski
name = 90
# print(name + "Radek") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# to jest tylko podpowiedź
name: str = "Radek"
print(name)
name = 90
print(name) # 90
print(type(name)) # <class 'int'>

age = 56
print(age)
print(type(age))
# 56
# <class 'int'>
