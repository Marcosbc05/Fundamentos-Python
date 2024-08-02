def binario_puro(decimal):
    '''
    PRE: entero positivo
    '''
    if decimal == 0:
        bin = 0
    elif decimal == 1:
        bin = 1
    else:
        bin = str(binario_puro(decimal // 2)) + str((decimal % 2))
    return bin
def calculardora_bin():
    a = input("Inserte número decimal ('s' para salir): ")
    while a != "s":
        try:
            a = int(a)
            print("-> " + str(binario_puro(a)))
        except:
            print("Formato no válido")
        a = input("Inserte número decimal (o 's' para salir): ")
calculardora_bin()

def letra(letra):
    letras=['a','b','c','d','e','f']
    numeros=[10,11,12,13,14,15]
    pos=letras.index(letra)
    return numeros[pos]
#print(letra('b'))

def num_letra(num):
    letras=['a','b','c','d','e','f']
    numeros=[10,11,12,13,14,15]
    pos=numeros.index(num)
    return letras[pos]
#print(num_letra(14))
