entrada=input('Inserte un número entero, que será el número hasta el cuál se elevarán 2,3 y 5: ')
def entero(entrada):
    entero=True
    try:
        int(entrada)
    except ValueError:
        entero=False
    return entero
a=True
n=0
while a==True:
    if entero(entrada)==True:
        for i in range(int(entrada)+1):
            print(2**n, end=' ')
            n+=1
        print()
        n=0
        for j in range(int(entrada)+1):
            print(3**n, end=' ')
            n+=1
        print()
        n=0
        for h in range(int(entrada)+1):
            print(5**n, end=' ')
            n+=1
        print()
        a=False
    elif entero(entrada)==False:
        entrada=input('Inserte número entero, el anterior no lo era: ')