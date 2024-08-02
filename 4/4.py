import random
lista=[]
def crear_lista(n):
    for i in range (n):
        a=random.randint(1,20)
        lista.append(a)
    return lista
lista=crear_lista(10)
print(lista)
suma=0
for i in range (len(lista)):
    suma+=lista[i]
print('Media: ',suma/len(lista))
menor=20
for i in range (len(lista)):
    if lista[i]<menor:
        menor=lista[i]
print(f'Menor: {menor}')
mayor=0
for i in range (len(lista)):
    if lista[i]>mayor:
        mayor=lista[i]
print(f'Mayor: {mayor}')