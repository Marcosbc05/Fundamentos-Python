import random
PALABRAS = ['eurovision','lo','gana','quien','el','jurado','apuestas','influyen','en','televoto','entre','unanimidad','y']
for i in range(20):
    frase = ''
    num_palabras = random.randint(3, 7)
    for j in range(num_palabras):
        palabra = PALABRAS[random.randint(0,len(PALABRAS)-1)]
        frase += palabra + ' '
    print(frase)
