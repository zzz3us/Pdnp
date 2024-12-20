class Car:
    """

    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.predkosc = 0

    def gaz(self):
        self.predkosc += 10

sam = Car("Skoda TDI", 2024)

sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()

print(sam.predkosc, "km/h")