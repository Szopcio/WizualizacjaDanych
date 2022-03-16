# Zadanie 1
a1 = "Kot"
a2 = "pies"

b1 = 2
b2 = 4

c1 = 2.456
c2 = 45.5432

d1 = 3+3
d2 = 5+5

print(a1, 'i', a2)
print(b1, 'i', b2)
print(c1, 'i', c2)
print(d1, 'i', d2)

# Zadanie 2
a=5
b=4
print('Dodawanie= ', a+b)
print('Odejmowanie= ', a-b)
print('Mnożenie= ', a*b)
print('Dzielenie= ', a/b)
print('Dzielenie całkowite= ', a//b)
print('Dzielenie modulo= ', a%b)
print('Potęgowanie= ', pow(a,b))

# Zadanie 3
a = 5
b = 3
c = 5-3

print("wynik działania %(z1)d - %(z2)d = %(z3)d" % {'z1':a, 'z2':b, 'z3':c})

# Zadanie 4
import math
a=math.e
a=pow(a,10)
print(a)
b=math.pow(math.log(5+math.pow(math.sin(8),2)),1/6)
print(b)
c=math.floor(3.55)
print(c)
d=math.ceil(4.8)
print(d)

# Zadanie 5
a="SZYMON"
b="DZIEŻYC"
print(a.capitalize(),b.capitalize())

# Zadanie 6
a="la la la"
print(a.count("la"))

# Zadanie 7
a="Polska górą"
print(a[1],a[10])

# Zadanie 8
a="Polska górą"
print(a.split())

# Zadanie 9
a="Polska górą"
b=5.43
c=0x32
print(a,"\n",b,"\n",'{0:x}'.format(c))