# błędy podczas działania programu

lista = []

try:
    # print(5 / 0)
    # print("a" + 9, aaa)
    # print(int("A"))
    # raise KeyError("Brak klucza")
    wynik = 90 / 33
except AttributeError:
    print("AttributeError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
except KeyError:
    print("KeyError")
else:
    print("Wynik: ", wynik)
finally:
    print("Wykonuje się zawsze")
