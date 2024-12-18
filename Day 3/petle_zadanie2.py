dictionary = {"imie": "Radek", "nazwisko": "Kowalski"}

# for i in dictionary:
#     print(i)
#
# for v in dictionary.values():
#     print(v, sep="=>")

for i, j in dictionary.items():
    print(i, j, sep="=>", end="<<<")