import datetime

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

# a = "Radek"
# n = len(a)
# if n > 3:
#     print(f'Długość wynsosi więcej niż 3, {n}')
#
# # operator morsa, walrus operator
# if (n := len(a)) > 3:
#     print(f"Długość wynosi więcej niż 3, {n}")
#
# podatek = 0
# zarobki = int(input("Podaj zarobki: "))
# if zarobki <= 10_000:
#     podatek = 0
# elif zarobki <= 30_000:
#     podatek = 0.2
# elif zarobki <= 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki}")

# sum_zam = 150
# # if sum_zam > 100:
# #     rabat = 25
# # else:
# #     rabat = 0
# #
# # print(f"Rabat wynosi {rabat}")
#
# rabat = 25 if sum_zam > 100 else 0
# print(f"Rabat wynosi {rabat}")

alert_system = input("Podaj system: ")
severity = input("Podaj krytyczność: ")
error_lista_mid = {}
error_lista_crit = {}

timestamp = datetime.date.today()

if alert_system == "console":
    if severity == "medium":
        error_lista_mid[timestamp] = "Console mid error"
        # error_lista_mid.append("Email mid error")
        print(error_lista_mid)
    elif severity == "high":
        error_lista_crit[timestamp] = "Console crit error"
        print(error_lista_crit)
elif alert_system == "email":
    if severity == "medium":
        error_lista_mid[timestamp] = "Email mid error"
        # error_lista_mid.append("Email mid error")
        print(error_lista_mid)
    elif severity == "high":
        error_lista_crit[timestamp] = "Email crit error"
        print(error_lista_crit)

else:
    print("Inny")


