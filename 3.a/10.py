def es_bisiesto(x):
    '''int->str'''
    if x>=1582:
        if x%4==0:
            if x%100==0:
                if x%400!=0:
                    return 'no es bisiesto, porque aunque es divisible entre 4, también es divisible entre 100 pero no entre 400'
                if x%400==0:
                    return 'es bisiesto'
            elif x%100!=0:
                return 'es bisiesto'
        else:
            return 'no es bisiesto, porque no es divisible entre 4'
    else:
        return 'no es bisiesto, porque hasta 1582 no se implantaron los años bisiestos cada cuatro años'
print(es_bisiesto(int(input('inserte año: '))))