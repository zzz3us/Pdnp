import random

# # for i in range(5):
# #     print("Tekst")
#
# for i in range(10):
#     pass
#
# for _ in range(3):
#     print("Tekst")
#
# for i in range(5):
#     print(i * 2)
#     print(i + 2)
#
# losowanie = []
# lista_kule = list(range(1, 50))
#
# for _ in range(6):
#     wyn = random.choice(lista_kule)
#     losowanie.append(wyn)
#     lista_kule.remove(wyn)
#
# print(losowanie)
#
# for i in range(10):
#     if i % 2 == 0:
#         print(i, " parzysta")
#
# lista3 = [j for j in range(10) if j % 2 == 0]
# print(lista3)
#
# for c in lista_kule:
#     if c < 10:
#         print("Większy niż 10", c)
#     else:
#         print("Mniejsze niż 10", c)
#
# for i in range (10,0,-2):
#     print(i)
#
imiona = ["Radek", "Radeg", "Rodek", "Ridek", "Radok"]
#
# for p in imiona:
#     print(imiona.index(p), p)
#
# for p in range(len(imiona)):
#     print(p, imiona[p])

# enumerate - numeruje kolekcje i zwraca numer i element

for i, p in enumerate(imiona, start=1):
    print(i, p)

