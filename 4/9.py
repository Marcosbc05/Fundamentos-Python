def cinco_vocales(palabra):
    a=True
    palabra.lower()
    vocales='aeiou'
    contador=[0]*5
    for i in range(len(palabra)):
        if palabra[i] in vocales:
            pos=vocales.index(palabra[i])
            contador[pos]+=1
    if 0 in contador:
        a=False
    return a
#probador
print(cinco_vocales('murcielago'))
print(cinco_vocales('melancolia'))
print(cinco_vocales('albaricoque'))

def cinco_vocales_unicas(palabra):
    a=True
    palabra.lower()
    vocales='aeiou'
    contador=[0]*5
    for i in range(len(palabra)):
        if palabra[i] in vocales:
            pos=vocales.index(palabra[i])
            contador[pos]+=1
    if contador!=[1,1,1,1,1]:
        a=False
    return a
#probador
print(cinco_vocales_unicas('murcielago'))
print(cinco_vocales_unicas('melancolia'))
print(cinco_vocales_unicas('albaricoque'))