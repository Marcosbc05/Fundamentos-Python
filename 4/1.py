def sumar_listas_iguales(lista1,lista2):
    '''
    list,list->list
    '''
    lista_sumada=[]
    if len(lista1)==len(lista2):
        for i in range(len(lista1)):
            a=lista1[i]+lista2[i]
            lista_sumada.append(a)
        return lista_sumada
    else:
        return 'Las listas no son de la misma longitud'
#probador
print(sumar_listas_iguales([1,2,3],[2,5,7]))
print(sumar_listas_iguales([1,3],[2,5,7]))