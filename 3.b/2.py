entrada=input('inserte número entre 0 y 12: ')
def entero(entrada):
    entero=True
    try:
        int(entrada)
    except ValueError:
        entero=False
    return entero
a=True
while a==True:
    if entero(entrada)==False:
        entrada=input('inserte número entero, el anterior no lo era: ')
    elif entero(entrada)==True and 0<=int(entrada)<=12:
        print(f'El número {entrada} es entero y está entre 0 y 12')
        a=False
    elif entero(entrada)==True and int(entrada)<0 or int(entrada)>12:
        entrada=input('inserte número entero entre 0 y 12, el anterior estaba fuera de rango: ')