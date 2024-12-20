class Car:
    """

    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.predkosc = 0

    def gaz(self):
        self.predkosc += 10

    def hamulec(self):
        self.predkosc -= 10
        self.__zmien_bieg()  # metoda prywatna

    def __zmien_bieg(self):
        print("Zmieniam bieg")

    def licznik(self):
        print(f"Jadę z prędkością {self.predkosc} km/h")

sam = Car("Skoda TDI", 2024)

sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()

sam.licznik()

sam.hamulec()
sam.hamulec()
sam.hamulec()
sam.hamulec()
sam.hamulec()

sam.licznik()

sam.gaz()

sam.licznik()
__predkosc = 0

# hermatyzacja - pola prywatne
# enkapsulacja - hermetyzowanie pól i wystawianie metod do ich odczytu i zapisu




