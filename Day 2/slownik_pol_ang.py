a = input("Wpisz słowo po angielsku: ")
# a = a.lower().strip().casefold()

slownik = {'dog' : 'pies', 'cat' : 'kot', 'bucket' : 'wiadro'}
# b = slownik[a]
#
# print(a, " to po polsku to ", b)

print(slownik.get(a.strip().casefold(), "nie ma"))
