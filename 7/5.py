def introducir_datos(n):
    lista=[]
    for i in range(n):
        nombre=input('inserte nombre: ')
        nota=int(input('inserte nota: '))
        dic={'nombre':nombre,'nota':nota}
        lista.append(dic)
    return lista
lista=introducir_datos(int(input('¿De cuantos elementos será la lista?: ')))
print(lista)
def modificar(lista,nombre,nota_nueva):
    pos=None
    i=0
    while pos==None and i<len(lista):
        if lista[i]['nombre']==nombre: pos=i
        i+=1
    lista[pos]['nota']=nota_nueva
    return lista
print(modificar(lista,input('inserte nombre a buscar: '),int(input('inserte nota nueva: '))))
def ord_asc2(lista):
    for i in range(len(lista)-1):
        menor=i
        for j in range(i+1,len(lista)):
            if lista[j]['nombre']<lista[menor]['nombre']:
                menor=j
        lista[menor],lista[i]=lista[i],lista[menor]
    return lista
def buscar(lista,nombre):
    lista2=ord_asc2(lista)
    pos=None
    ini=0
    fin=len(lista2)-1
    while ini<len(lista2) and pos==None:
        centro=(ini+fin)//2
        if lista[centro]['nombre']==nombre: pos=centro
        elif lista[centro]['nombre']<nombre: ini=centro+1
        else: fin=centro-1
    return lista[pos]
print(buscar(lista,input('inserte nombre que busca info completa: ')))
def media(lista):
    suma=0
    for i in range(len(lista)):
        nota=lista[i]['nota']
        suma+=nota
    return f'media: {suma/len(lista)}'
print(media(lista))
def media_aprob(lista):
    suma=0
    j=0
    for i in range(len(lista)):
        if lista[i]['nota']>=5:
            nota=lista[i]['nota']
            suma+=nota
            j+=1
    return f'media de notas >=5 es {suma/j}'
print(media_aprob(lista))
def ord_desc(lista):
    for i in range(len(lista)-1):
        mayor=i
        for j in range(i+1,len(lista)):
            if lista[j]['nota']>lista[mayor]['nota']:
                mayor=j
        lista[mayor],lista[i]=lista[i],lista[mayor]
    return lista, 'mejor nota: ',lista[0]
print(ord_desc(lista))
def ordenar_asc(lista):
    for i in range(1,len(lista)):
        actual=lista[i]
        indice=i
        while indice>0 and actual['nota']<lista[indice-1]['nota']:
            lista[indice]=lista[indice-1]
            indice-=1
        lista[indice]=actual
    return lista,'peor nota: ',lista[0]
print(ordenar_asc(lista))
