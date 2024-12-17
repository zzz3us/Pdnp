#zbiór przechowuje tylko wartości unikalne

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)

print(zbior)

zb2 = set()
print(zb2)

zbior.add(33)
zbior.add(33)
zbior.add(11)
zbior.add(88)
zbior.add(999)

print(zbior)