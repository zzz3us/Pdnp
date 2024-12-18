# # instrukcje warunkowe
#
# odp = True
# print(bool(odp))
# # odp = False
#
# if odp:
#     print("x")
#     print("x")
#     print("x")
#     print("x")
#     print("x")
#     print("x")
#     print("x")
#
# print("Dalsza część")
#
#
#
# if odp:
#     print("Dane zostały odebrane")

# odp = 0
# if odp:
#     print("Działa")
# else:
#     print("zero - False")

a = "Radek"
n = len(a)
if n > 3:
    print(f'Długość wynsosi więcej niż 3, {n}')

# operator morsa, walrus operator
if (n := len(a)) > 3:
    print(f"Długość wynosi więcej niż 3, {n}")

