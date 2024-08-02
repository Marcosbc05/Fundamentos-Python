def contador_menos_uno():
    lista=[]
    for  i in range(10):
        a=input('introducza un número: ')
        lista.append(a)
    lista_rest=[]
    for i in range(len(lista)):
        if i==len(lista)-1:
            b=int(lista[len(lista)-1])-int(lista[0])
            lista_rest.append(b)
        else:
            b=int(lista[i])-int(lista[i+1])
            lista_rest.append(b)
    print(lista_rest)

contador_menos_uno()