# # biblioteka do działania na liczbach pseudolosowych
#
import random
#
# zbior = []
# losowanie = []
#
# # print(random.randint(1, 100))
# # print(random.randrange(1, 100))
# # print(random.randrange(5))
# # print(random.random())
# # print(random.random() * 8)
#
# zbior = list(range(1, 50))
#
# wyn
#
# print(zbior)
#
# a = random.choice(zbior)
#
# losowanie.append(a)
# zbior.remove(a)
#
# print(zbior)
# print("Losowanie: ", losowanie)

lista_kule = list(range(1, 50))
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)

print(random.choices(lista_kule, k=6))
print(random.sample(lista_kule, k=6))
print(random.sample(lista_kule, 6))