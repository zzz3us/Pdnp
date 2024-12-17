# # kolekcje
#
# # lista - przechowuje dowolną ilość danych, dowolny typ w jednej kolekcji
# # zachowuje kolejność przy dodawaniu danych
#
# lista = []
# print(lista)
# print(type(lista))
#
# pusta_lista = ()
# print(type(pusta_lista))
# print(pusta_lista)
#
# lista.append("Radek")
# lista.append("Marek")
# lista.append("Skwarek")
# lista.append("Jan")
# lista.append("Daniel")
#
# print(lista)
#
# print(len(lista))
# print(lista[0])
# print(lista[3])
#
# print(lista[4])
# print(lista[len(lista) - 1])
# print(lista[-1])
#
# print(lista[0:3])
# print(lista[:3])
# print(lista[2:])
# print(lista[2:6])
#
# print(lista[2:15])
# print(lista[:])
# print(lista[2:2])
#
# print(lista[-2:0])
# print(lista[-1:0])
# print(lista[0:-3])
#
# lista_15 = list(range(15))
#
# print(lista_15)
#
# print(lista_15[0:15:2])
#
# print(lista[::-1])
#
# lista.insert(15, "Żaklina")
# print(lista)
#
# lista.append("Asia")
# print(lista.index("Asia"))
# print(lista)
#
# lista.remove("Asia")
# print(lista)
#
# print(lista.pop(5))
#
# lista_2 = lista
# print(lista)
# print(lista_2)
# lista.clear()
#
# print(lista)
# print(lista_2)
#
# lista_copy = lista.copy()
#
# print(id(lista))
# print(id(lista_2))
# print(id(lista_copy))
#
# liczby = [54, 999, 34, 22, 12.34, 687]
#
# print(liczby)
#
# lista_osob = ['Radek', 'Ola', 'Maciek', 'Olek', 'Marta', 'Arawind']
# lista_osob.sort()
# print(lista_osob)
#
# lista_osob.reverse()
# print(lista_osob)
#
# print(lista_osob[::-1])
#
# liczby[3] = 666
# print(liczby[0:3])
# print(liczby[-2])
# print(liczby)

tekst = "Pyth on."
lista1 = list(tekst)
print(lista1)

# lista2 = [tekst]
# print(lista2)

krotka = tuple(lista1) #krotka to lista tylko do odczytu, jako jednoelementowa może służyć jako stała niemodyfikowalna
print(krotka)






