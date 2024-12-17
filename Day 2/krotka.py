# krotka(tuple) tylko do odczytu, efektywniej zarządza pamięcią
# krotka jednoelementowa może być stałą

tupla = ["Radek"]
print(tupla)

tupla_2 = ("Radek",)
print(tupla_2)

tupla_liczby = 43, 55, 22.34, 11, 200
print(tupla_liczby)
print(id(tupla_2))
print(id(tupla_liczby))

tupla_imiona = 'Radek', 'Tomek', 'Zenek', 'Ania', 'Eliza', 'Marek'
print(tupla_imiona)

print(tupla_imiona.index("Radek"))
print(tupla_imiona.index("Eliza"))

tup = 1, 2
a, b = 1, 2
print(a)
print(b)
a, b = tup
print(a, b)

# tup_2 = 1, 2, 3
# a, b = tup_2
#
# print(tup_2)

tup_imiona = ('name2', 'name1', 'name3', 'name4', 'name5')
print(type(tup_imiona))

# imie1, imie2, imie3 = tup_imiona
# print(imie1)
# print(imie2)
# print(imie3)

name1, name2, *name3 = tup_imiona

print(name1, name2, name3)

name1, *name2, name3 = tup_imiona

print(name1, name2, name3)

*name1, name2, name3 = tup_imiona

print(name1, name2, name3)

print(sorted(tup_imiona))

