import random
#zadanie 1
liczba=random.randint(0, 30)
liczba*=2
f=open("plik.txt", "a")
liczba=str(liczba)
f.write(liczba)
f.close()

#zadanie2
f=open("plik.txt", "r")
print(f.read())

#zadanie3
with open("plik.txt", "a") as plik:
        plik.write("Linia\n")
with open("plik.txt", "r") as plik:
    for linia in plik:
        print(plik.read())

#zadanie4
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu)
        print(self.ilosc)
        print(self.jednostka_miary)
        print(self.cena_jed)
    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)
    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed
chleb=NaZakupy("Chleb", 5, "Szt", 1.5)
chleb.wyswietl_produkt()
chleb.ile_produktu()
print(chleb.ile_kosztuje())

#zadanie5
class ciagArytmetyczny:
    def __init__(self, a1, r, n):
        self.a1=a1
        self.r=r
        self.n=n
    def wyswietl_dane(self):
        wyraz=self.a1
        for x in range(self.n):
            print(wyraz)
            wyraz = wyraz + self.r
    def pobierz_elementy(self, x, roz, y):
        self.a1=x
        self.r=roz
        self.n=y
    def policz_sume(self):
        an=self.a1+(self.n-1)*self.r
        suma=((self.a1+an)/2)*self.n
        return suma
    #def policz_elementy(self):
ciag=ciagArytmetyczny(5,3,3)
ciag.wyswietl_dane()
ciag.pobierz_elementy(10,2,5)
ciag.wyswietl_dane()
print(ciag.policz_sume())

#zadanie6
class Robaczek:
    def __init__(self, x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self, ile_krokow):
        self.y=self.y+(self.krok*ile_krokow)
    def idz_w_dol(self, ile_krokow):
        self.y=self.y-(self.krok*ile_krokow)
    def idz_w_lewo(self, ile_krokow):
        self.x=self.x-(self.krok*ile_krokow)
    def idz_w_prawo(self, ile_krokow):
        self.x=self.x+(self.krok*ile_krokow)
    def pokaz_gdzie_jestes(self):
        print(self.x, self.y)
robak=Robaczek(0,0,2)
robak.idz_w_dol(5)
robak.idz_w_gore(3)
robak.idz_w_lewo(2)
robak.idz_w_prawo(6)
robak.pokaz_gdzie_jestes()