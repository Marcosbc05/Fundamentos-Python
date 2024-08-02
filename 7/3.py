frases=['hola pepe','hola que tal','hola hasta luego adios','pero cuanto tiempo que pasa']
def orden_sel(lista):
    palabras=[]
    for i in range(len(lista)):
        division=lista[i].split()
        palabras.append(division)
        
    for j in range(len(palabras)-1):
        menor=j
        for k in range(j+1,len(palabras)):
            if len(palabras[k])<len(palabras[menor]):
                menor=k
        palabras[j],palabras[menor]=palabras[menor],palabras[j]
    return palabras
frases=orden_sel(frases)
for i in frases:
    print(i)