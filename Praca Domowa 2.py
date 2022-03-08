# Zadanie 1
sporty = ['pilka_nozna','koszykowka','siatkowka']
sporty.reverse()
sporty.append('Rugby')
print(sporty)

# Zadanie 2
slownik = {'Nr':'Numer', 'Prof':'Profesor', 'Dr':'Doktor'}
print(slownik['Nr'])

# Zadanie 3
slo = {'F1_2021':'7', 'Wiedzmin_3':'10', 'Lost_Ark':'9'}
print (len(slo))

# Zadanie 4
napis = input("Wprowadz napis: ")
i=0
for x in napis:
    if x=='a':
        i+=1
print(i)
#print(napis.count('a'))

# Zadanie 5
import sys as system

system.stdout.write("Podaj pierwsza liczbe: ")
a = system.stdin.readline()
system.stdout.write("Podaj drugą liczbe: ")
b = system.stdin.readline()
system.stdout.write("Podaj trzecią liczbe: ")
c = system.stdin.readline()

a = int(a)
b = int(b)
c = int(c)

wynik=pow(a, b)+c
wynik=str(wynik)

system.stdout.write(wynik)
print("\n")
# Zadanie 6
a = input("Podaj pierwszą liczbę: ")
b = input("Podaj druga liczbę: ")
c = input("Podaj trzecią liczbę: ")

a=int(a)
b=int(b)
c=int(c)

if a>b & a>c:
    print(str(a) + " jest największa liczba")
if b>a & b>c:
    print(str(b) + " jest najwieksza liczba")
if c>a & c>b:
    print(str(c) + " jest najwieksza liczba")


# Zadanie 7

import math
lista=[1, 4, 5.4, 2.3, 7, 6.5]

for x in lista:
    x=pow(x, 2)
    print(x)

# Zadanie 8
i=0
lista2=[]

while(i<11):
    x=input("Podaj liczbe: ")
    x=int(x)
    if(x%2==0):
        lista2.append(x)
    i+=1

print(lista2)

# Zadanie 9
a=input("Podaj liczbe")
a=int(a)

try:
    if (a<1):
        raise ValueError
    pierwiastek=math.sqrt(a)
    print(pierwiastek)

except ValueError:
    print("Podaj prawdiłową liczbe")



