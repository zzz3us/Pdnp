# a = input("Wpisz słowo po angielsku: ")

slownik = {'dog' : 'pies', 'cat' : 'kot', 'bucket' : 'wiadro'}
# slownik2 = {}
#
# for k, v in slownik.items():
#     slownik2[v] = k
#
# # print(slownik.get(a.strip().casefold(), "nie ma"))
# print(slownik2)

print({value: key for key, value in slownik.items()})