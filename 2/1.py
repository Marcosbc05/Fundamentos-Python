def fuerza(masa, aceleracion):
    '''float,int->float
    obj: calcular la fuerza a partir de la masa y la aceleracion'''
    return masa*aceleracion
#Probador
masa=float(input('inserte la masa: '))
aceleracion=int(input('inserte la aceleracion: '))
print(fuerza(masa, aceleracion), 'N (newtons)')
