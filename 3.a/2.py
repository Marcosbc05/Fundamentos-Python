def doce_horas(h,m):
    '''int->string
    obj: leer en formato 12 horas
    pre: 0<=h<24'''
    if 0<=h<12:
        hora=h
        min=f'{m} AM'
    elif h==12:
        hora=h
        min=f'{m} PM'
    elif 12<h<24:
        hora=h-12
        min=f'{m} PM'
    return f'{hora}:{min}'
print(doce_horas(int(input('inserte hora en formato 24h: ')),int(input('inserte minutos: '))))