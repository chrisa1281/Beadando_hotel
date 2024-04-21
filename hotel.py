from abc import ABC, abstractmethod
from datetime import datetime

# Absztrakt Szoba osztály
class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def info(self):
        pass

# EgyágyasSzoba osztály
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar=10000):
        super().__init__(szobaszam, ar)

    def info(self):
        return f"Egyágyas szoba, Szám: {self.szobaszam}, Ár: {self.ar}"

# KétagyasSzoba osztály
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar=15000):
        super().__init__(szobaszam, ar)

    def info(self):
        return f"Kétagyas szoba, Szám: {self.szobaszam}, Ár: {self.ar}"

# Szalloda osztály
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadas(self, szoba):
        self.szobak.append(szoba)

    def ervenyes_datum(self, datum):
        return datum >= datetime.today().date()

    def foglalas(self, szobaszam, datum):
        if any(f['szobaszam'] == szobaszam and f['datum'] == datum for f in self.foglalasok):
            return "A szoba ezen a napon már foglalt."
        if not self.ervenyes_datum(datum):
            return "A dátum érvénytelen. Kérjük, jövőbeli dátumot adjon meg."
        szoba = next((s for s in self.szobak if s.szobaszam == szobaszam), None)
        if not szoba:
            return "Nincs ilyen szobaszám."
        self.foglalasok.append({'szobaszam': szobaszam, 'datum': datum})
        return f"Foglalás megerősítve: {szobaszam} szobára, dátum: {datum}. Ár: {szoba.ar} Ft"

    def lemondas(self, szobaszam, datum):
        for f in self.foglalasok:
            if f['szobaszam'] == szobaszam and f['datum'] == datum:
                self.foglalasok.remove(f)
                return "Foglalás lemondva."
        return "Nincs ilyen foglalás."

    def foglalasok_listaja(self):
        if not self.foglalasok:
            return "Nincsenek foglalások."
        return "\n".join(f"Szobaszám: {f['szobaszam']}, Dátum: {f['datum']}" for f in self.foglalasok)

# Felhasználói felület
def main():
    hotel = Szalloda("Hotel")
    hotel.szoba_hozzaadas(EgyagyasSzoba(101))
    hotel.szoba_hozzaadas(KetagyasSzoba(102))
    hotel.szoba_hozzaadas(KetagyasSzoba(103))

    # Példa foglalások
    hotel.foglalas(101, datetime(2024, 5, 20).date())
    hotel.foglalas(102, datetime(2024, 5, 21).date())
    hotel.foglalas(103, datetime(2024, 5, 22).date())
    hotel.foglalas(101, datetime(2024, 5, 23).date())
    hotel.foglalas(102, datetime(2024, 5, 24).date())

    while True:
        print("\n1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listája")
        print("4. Kilépés")
        valasztas = input("Válasszon egy opciót: ")

        if valasztas == "1":
            szobaszam = int(input("Adja meg a szobaszámot: "))
            datum = datetime.strptime(input("Adja meg a dátumot (éééé-hh-nn): "), "%Y-%m-%d").date()
            print(hotel.foglalas(szobaszam, datum))
        elif valasztas == "2":
            szobaszam = int(input("Adja meg a szobaszámot: "))
            datum = datetime.strptime(input("Adja meg a dátumot (éééé-hh-nn): "), "%Y-%m-%d").date()
            print(hotel.lemondas(szobaszam, datum))
        elif valasztas == "3":
            print(hotel.foglalasok_listaja())
        elif valasztas == "4":
            print("Köszönjük, viszontlátásra!")
            break

if __name__ == "__main__":
    main()
