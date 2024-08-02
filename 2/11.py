def es_bisiesto(x):
    '''int->str'''
    if x>=1582:
        if x%4==0:
            if x%100==0:
                if x%400!=0:
                    return 'no es bisiesto'
                if x%400==0:
                    return 'es bisiesto'
            elif x%100!=0:
                return 'es bisiesto'
        else:
            return 'no es bisiesto'
    else:
        return 'no es bisiesto'
print(es_bisiesto(int(input('inserte año: '))))