# # słownik - para klucz/wartość
# # {'user' : 'Radek', "wiek":76}\
# # odpowiednik jsona
# # klucze nie mogą się powtarzać
#
# # pusty słownik
#
# dictionary = dict()
# print(type(dictionary))
# print(dictionary)
#
# dictionary_1 = {}
# print(dictionary_1)
#
# dictionary["imie"] = "Radek"
# print(dictionary)
# dictionary["wiek"] = 39
# print(dictionary)
#
# print(dictionary.keys()) #
# print(dictionary.values()) #
# print(type(dictionary.items()))   #
#
# # nadpisanie elementów
#
# dictionary["imie"] = "Tomek"
# print(dictionary)
# print(dictionary["imie"])
# print(dictionary.get("Imie", "default"))
#
# dictionary.update({"data": '30-12-2024'})
# print(dictionary)

dict_small = {'x': 2}
print(dict_small)
dict_small.update([('y', 3), ("z", 6)])
print(dict_small)

# input() - wprowadzanie danych z prompta

tekst = input('Podaj Imię:')
print(tekst)

