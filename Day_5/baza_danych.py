import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Połączenie z bazą danych udane!")

    query = """CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT NOT NULL,
    nazwisko TEXT NOT NULL,
    data_urodzenia DATE NOT NULL,
    plec TEXT NOT NULL CHECK(plec IN ('M', 'K'))
            )"""

    insert = """INSERT INTO developers (imie, nazwisko, data_urodzenia, plec) VALUES (1, 'Radek', '19-12-2024', "M")"""

    for i in c.execute(query):
        print(i)

    for i in c.execute(insert):
        print(i)

    for i in c.execute("SELECT * FROM developers"):
        print(i)
except sqlite3.Error as e:
    print(f"Błąd przyłączenia do bazy danych: {e}")

finally:
    if conn:
        conn.close()
        print("Połączenie z bazą danych zamknięte!")