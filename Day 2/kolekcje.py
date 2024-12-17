# kolekcje

# lista - przechowuje dowolną ilość danych, dowolny typ w jednej kolekcji
# zachowuje kolejność przy dodawaniu danych

lista = []
print(lista)
print(type(lista))

pusta_lista = ()
print(type(pusta_lista))
print(pusta_lista)

lista.append("Radek")
lista.append("Marek")
lista.append("Skwarek")
lista.append("Jan")
lista.append("Daniel")

print(lista)

print(len(lista))
print(lista[0])
print(lista[3])

print(lista[4])
print(lista[len(lista) - 1])
print(lista[-1])
