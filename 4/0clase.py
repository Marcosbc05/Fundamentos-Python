LETRAS='abcdefghijklmnñopqrstuvwxyz'
lista_contadores=[int(0)]*len(LETRAS)
###
salir=False
total=0
while  not salir:
    letra=input('Introduce una letra: ')
    if letra !=' 'and letra in LETRAS:
        pos=LETRAS.index(letra)
        lista_contadores[pos]+=1
        total+=1
    else:
        salir=True
print('Total letras: ',total)
for i in range(len(LETRAS)):
    print(f'{LETRAS[i]}: {lista_contadores[i]}',end=', ')
print()
#crear lista de 10 nº aleatorios y hacer: una funcion que reciba la lista y : devuelva el menor, otra el mayor, 
#reciba la lista y un numero y devuelva si está en la lista y otra que posición ocupa en la lista

import random
lista=[]
for i in range(10):
    lista.append(random.randint(0,100))
print(lista)
def menor(lista):
    menor=lista[0]
    for i in lista[1:]:
        if i<menor:
            menor=i
    return f'Menor: {menor}'
print(menor(lista))
def mayor(lista):
    mayor=0
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return f'Mayor: {mayor}'
print(mayor(lista))
def in_lista(lista,n):
    return n,n in lista
print(in_lista(lista,random.randint(0,100)))
def pos_lista(lista,n):
    if n in lista:
        pos=lista.index(n)
        return f'{n} está en la posición: {pos}'
    else:
        return f'el nº {n} no está en la lista'
print(pos_lista(lista,random.randint(0,100)))