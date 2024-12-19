# while - pętla sterowania warunkiem
# for - pętla iterująca po elementach kolekcji  (listy, tuple, string, range)
#
# licznik = 0
# while True:
#     licznik += 1
#     print("Komunikat 2")
#     if licznik > 10:
#         break
#
# print("Koniec pętli")
#
# licznik = 0
# while licznik < 10:
#     licznik += 1
#     print(f"Komunikat {licznik}")
#
# password = input("Password: ")
# while password != "secret":
#     password = input("Wrong Password, please enter again: ")
#
# print("Hasło poprawne")
#
# lista =[]
# lista_int = []
# while True:
#     wej = input("Podaj liczbę: ")
#     if not wej.isnumeric():
#         break
#     lista.append(wej)
#     lista_int.append(int(wej))
#
# print(lista)
# print(lista_int)

# my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
# element_to_remove = 5
# while element_to_remove in my_list:
#     my_list.remove(element_to_remove)
# print(my_list)

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
print(dict.fromkeys(my_list))
unique_numbers = list(dict.fromkeys(my_list))
print(unique_numbers)