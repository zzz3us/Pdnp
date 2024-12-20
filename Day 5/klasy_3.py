class Pojazd:
    """
    Klasa Pojazd
    """
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print("Kolor:", self.kolor+".")

pojazd1 = Pojazd("czerwony")

# pojazd1.info()

class Samochod(Pojazd):
    """
    Klasa samochód dziedziczy po klasie Pojazd
    """
    def __init__(self, kolor, marka):
        super().__init__(kolor) # musimy wywołać konstruktor klasy wyższej
        self.marka = marka

    def info(self):
        super().info() # możemy wywołać metodę klasy wyższej
        print("Marka:", self.marka+".")

car1 = Samochod("biały", "Skoda")
car1.info()

