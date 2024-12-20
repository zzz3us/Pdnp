from abc import ABC, abstractmethod

class Ptak(ABC):
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek+".", "Lecę z szybkością", self.szybkosc, "km/h.")

    def wydaj_odglos(self):
        pass

# or1 = Ptak("Orzeł", 43)
# or1.latam()
# kur1 = Ptak("Kura", 0)
# kur1.latam()

class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek+".", "Nie latam, bo jestem kurą.")

    def wydaj_odglos(self):
        print("Kura domowa wydaje ko ko.")

    def dziobanie(self):
        print("Dziobanie")

kura1 = Kura("kurą domową")
# kura1.latam()
# kura1.wydaj_odglos()

class Orzel(Ptak):
    """
    Klasa dziedziczy z Ptak
    """
    def wydaj_odglos(self):
        print("Orzeł biały wydaje kir kir.")

    def polowanie(self):
        print("Polowanie")

orzel1 = Orzel("orzeł biały", 50)
# orzel1.latam()
# orzel1.wydaj_odglos()
# orzel1.polowanie()
# kura1.dziobanie()

lista = [kura1, orzel1]
for i in lista:
    i.wydaj_odglos()

