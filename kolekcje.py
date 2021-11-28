'''
n = int(input('Podaj ilość ocen'))

suma = 0

for i in range (n):
    ocena = float(input('podaj ocene'))
    suma +=ocena


print(f'średnia ocen wynosi {float(suma)/n}')


ocena1 = 3
ocena2 = 4
ocena3 = 6
ocena4 = 5

oceny = [3,5,4,6]
print(oceny)
oceny.append(3.5)
print(oceny)


lista = [
    'ala',
    'ma',
    'kota',
    1,
    2,
    3,
    True,
    ['druga','lista']
]

print(lista)


lista = [5,4,2,3,6]

lista2 = [
    'Uncharted 4',
    'fortnite',
    'minecraft',

]




pierwszy sposob = [
    ['Adam',''Kowalski',15]
]


#indeksy: 0 1 2 3 4 5 6 7 8 9 
liczby = [9,8,7,6,5,4,3,2,1,0]
print(liczby[8])

indeks = int(input('Podaj indeks: '))
if indeks <len(liczby):
   print(liczby[indeks])
else:
    print('Indeks nie może być większy niż liczba  w tablicy')


pierwszy_sposob = [
    ['Adam','Kowalski', 15],
    ['Kowalski', 'Lojalna',48],
    ['Piotr','Kowalski', 12],

]

print()

drugi_sposob = [
   ['Adam','Jola','Piotr'],
   ['Kowalski','Lojalna', 'Kwiatkowski'],
   [15,48,12]
]

suma = 0 
for i in range(len(pierwszy_sposob)):
    suma += pierwszy_sposob[i][2]
print(suma/len(pierwszy_sposob))



#Oblicz średnią ocen podawanych przez użytkownika:
#Nie wiemy ile ocen wprowadzi uzytkownik(wczytywanie dopóki użytkownik nie wprowadzi wartości siecjalnej)
#Po wczytaniu każdej oceny ma zostać wyświetlona lista dotychczas wprowadzonych ocen

oceny = []

while True:
    komunikat = input('Podaj ocene lub zakończ (q): ')
    if komunikat == 'q':
        break
    ocena = float(komunikat)
    if ocena < 1 or ocena > 6: 
        print('Podana ocena jest nieprawidłowa. ')
    oceny.append(ocena)
    print(oceny)
średnia = sum(oceny)/ len(oceny)
print(f'Średnia ocen to {średnia} ')




n = 5
lista = []

for i in range(n):
    lista.append(input('Wprowadź wartość:'))


for i in range(1, n+1):
    element = lista[-i]
    print(element)

#print(listap[::-1])
print(lista[0::2])


lista = [5,15,23,53,2]
iloczyn = 1
for i  in lista:
    iloczyn *= i
    print(iloczyn)
'''
lista = [1,2,3,3,4,4,5,5,31,]

zmienna1, zmienna2, zmienna3 = lista
print(zmienna2)

lista = [1,2,3]

zmienna1, zmienna2, zmienna3 = lista
print(zmienna2)

