def convertir_a_m2(barn):
    '''int->int
    obj: pasar de barn a m2'''
    return barn*(10**-28)
def convertir_a_barn(m2):
    '''int->int
    obj pasar de m2 a barn'''
    return m2*(10**28)
print(convertir_a_barn(1))
print(convertir_a_m2(3460))