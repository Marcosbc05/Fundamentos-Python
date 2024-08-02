def conversor_seg(seg):
    '''int->int
    obj: pasar de segs a dias, horas, min y seg'''
    min=seg//60
    segs=seg%60
    hor=min//60
    mins=min%60
    dias=hor//24
    hors=hor%24
    return f'{dias} días, {hors} horas, {mins} minutos y {segs} segundos'

print(conversor_seg(int(input('inserte segundos totales: '))))

