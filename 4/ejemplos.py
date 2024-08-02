def en_orden_ascendente (lista):  
    """ list -> bool      OBJ: Devuelve True si la lista está ordenada ascendentemente 
    PRE: Todos los elementos de la lista son comparables """ 
    ordenado=True
    if len(lista) == 1:      
        ordenado=True  
 
    if len(lista) > 1: # una lista con solo un elemento está ordenada 
        i = 1 
        ant = lista [0] 
        while i < len(lista) and ordenado: 
            if lista [i] < ant: 
                ordenado = False
            else:
                ant = lista [i] 
                i += 1  
    return ordenado
#PROBADOR  
mi_lista = [3,5,1,10] 
print('Ordenada: ', en_orden_ascendente(mi_lista)) 
print('Ordenada: ', en_orden_ascendente([3,5,5,6])) 