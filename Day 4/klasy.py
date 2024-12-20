class Human:
    def __init__(self, imie, wiek, wzrost, plec="k"):
        """

        :param self:
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        :return:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print("Nazywam sie", self.imie+".")
        print("Mam", self.wiek, "lat.")
        print("Mam", self.wzrost, "cm wzrostu.")
        if self.plec == "m":
            print("Jestem mężczyzną.")
        elif self.plec == "k":
            print("Jestem kobietą.")
        else:
            print("Jestem niebinarne.")

    def wypisz_wiek(self):
        print("Mam", self.wiek, "lat.")

    def wypisz_wzrost(self):
        print("Mam", self.wzrost, "cm wzrostu.")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę.")
        elif self.plec == "m":
            print("Ruszyłem w drogę.")
        else:
            print("Ruszyło w drogę.")

cz1 = Human("Riddick", 56, 190,"m")
cz2 = Human("Ewa", 22, 166, "k")
cz3 = Human("Lis", 26, 155, "x")

print(cz1)

# cz1.powitanie()
# cz2.powitanie()
cz3.powitanie()
cz3.ruszaj()