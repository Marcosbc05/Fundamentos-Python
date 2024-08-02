def ordenar_par_impar(lista):
    '''list->list,list
    obj: separar y ordenar por pares e impares
    pre:las listas deben ser del mismo tamaño'''
    lista_pares=[]
    lista_impares=[]
    for i in range(len(lista)):
        a=lista[i]
        if a%2==0: #es par
            lista_pares.append(a)
        if a%2!=0: #es impar
            lista_impares.append(a)
    lista_pares.sort()
    lista_impares.sort()
    return lista_pares, lista_impares

#probador
lista=[2,1,6,4,3,11,6,5,8,7,3,2,1,9,8,6,3,9,5,0,3,1,5,4,3,8,6,5,4]
print(ordenar_par_impar(lista))