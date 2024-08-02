entrada=input('inserte número entero: ')
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
    elif entero(entrada)==True:
        print(f'El número {entrada} es entero')
        a=False