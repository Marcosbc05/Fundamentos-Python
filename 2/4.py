def seg_desde_medianoche(horas, min, seg):
    '''int,int,int->float
    obj: calcular segundos desde media noche según hora actual'''
    horas(int(input('Horas: ')))
    seg(int(input('Segundos: ')))

    return horas*3600+min*60+seg
print('Introduzca hora actual:')

min(int(input('Minutos: ')))
print('han pasado', seg_desde_medianoche(horas, min, seg), 'segundos desde la última medianoche')