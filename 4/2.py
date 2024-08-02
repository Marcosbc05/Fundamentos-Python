def sumar_listas(lista1,lista2):
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
        if len(lista1)<len(lista2):
            lista_grande=lista2
            lista_peq=lista1
        else:
            lista_grande=lista1
            lista_peq=lista2
        for i in range(len(lista_peq)):
            a=lista1[i]+lista2[i]
            lista_sumada.append(a)
        for j in range(len(lista_peq),len(lista_grande)):
            b=lista_grande[j]  
            lista_sumada.append(b)       
        return lista_sumada
#probador
print(sumar_listas([1,2,3],[4,5,6]))
print(sumar_listas([1,2,3,4,5],[1,2,3]))