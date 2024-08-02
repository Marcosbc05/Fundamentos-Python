import mi_biblio
entrada=input('inserte número: ')
comprobador=mi_biblio.entero(entrada)
numero_entradas=0
num_negativos=0
num_positivos=0
while entrada!=-9999 and comprobador==True:
    numero_entradas += 1
    if int(entrada)<0:
        num_negativos+=1
    elif int(entrada)>0:
        num_positivos+=1
    entrada=int(input('inserte número: '))
    comprobador=mi_biblio.entero(entrada)
print('Número de entradas: ',numero_entradas)
print('Número de valores negativos: ', num_negativos)
print('Número de valores positivos: ', num_positivos)