h=(input('inserte hora en formato 24: '))
m=(input('insete minutos: '))
def doce_horas(h,m):
    '''int->int
    obj: leer en formato 12 horas'''
    try:
        h=int(h)
        m=int(m)
        if 0<=h<12 and 0<=m<=59:
            hora=h
            min=f'{m} AM'
        elif h==12 and 0<=m<=59:
            hora=h
            min=f'{m} PM'
        elif 12<h<24 and 0<=m<=59:
            hora=h-12
            min=f'{m} PM'
        return f'{hora}:{min}'
    except UnboundLocalError:
        return 'valores no validos'
print(doce_horas(h,m))