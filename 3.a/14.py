ingresos=int(input('INSERTE INGRESOS: '))
def puntos(ingresos):
    '''int->int
    obj: calc puntos segun ingresos'''
    if 0<=ingresos<1800:
        return '4 PUNTOS'
    elif 1800<=ingresos<3500:
        return '3 PUNTOS'
    elif 3500<=ingresos<5000:
        return '2 PUNTOS'
    elif 5000<ingresos:
        return '1 PUNTO'
print('Según los ingresos, corresponden ',puntos(ingresos))