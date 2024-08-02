def iguales(frase1,frase2):
    a=True
    if len(frase1)!=len(frase2):
        a=False
    else:
        for i in range(len(frase1)):
            if frase1[i]!=frase2[i]:
                a=False
    return a
#probador
print(iguales('Hola maja','Hola pepa'))
print(iguales('Hola pepa','Hola pepa'))