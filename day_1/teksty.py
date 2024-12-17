tekst = "Witaj Świecie"
print(tekst)  # Witaj Świecie
print(type(tekst))  # <class 'str'>

# teksty są niemutowalne
#  """ Return a copy of the string converted to uppercase. """
tekst.upper()
print(tekst)
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst_upper)  # WITAJ ŚWIECIE

print(tekst)
# Witaj Świecie
# 0123456789...

print(tekst.index("j"))  # indeks 4, pozycja 5
print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("j", 0, 4))  # wystąpi 0 razy, z prawej strony zbiór otwarty 0123

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

tekst_zamiana = "Witaj Dobry Świecie"
print(tekst_zamiana.replace("Dobry", ""))  # "Witaj  Świecie"

print(tekst.removeprefix("Witaj").strip())  # "Świecie"
# strip() - usunięcie białych znaków, spacji z przodu i z tyłu

print(tekst[4])  # "j" indeks 4

tekst = "Witaj świecie"
encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie'
# b dane typu bajtowego
print(type(encode_s))  # <class 'bytes'>
print(encode_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
# f - string, formatowanie tekstu
tekst_format = f"Mam na imię {imie} i lubie pythona."

tekst_format1 = f"\tMama na imię {imie}\n i lubię pythona.\b"
print(tekst_format1)
# \t tabulator
# \n nowa linia
# \b backspace
# "	  Mama na imię Radek
#  i lubię pythona"

starszy = "Witaj %s!"  # %s - str
print(starszy % imie)  # Witaj Radek!
print("Witaj {}!".format(imie))  # Witaj Radek!

print("Witaj", imie)  # Witaj Radek

# tekst wielolinijkowy
print("""Tekst
    wielolinijkowy""")

# "Tekst
#     wielolinijkowy"
"""Komentarz
    wielolinijkowy"""
