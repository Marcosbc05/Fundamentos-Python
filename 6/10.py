def decimal_a_otra_base(numero, base):
    '''PRE: 1<base<11'''
    if numero < base:
        res=str(numero)
    else:
        res=decimal_a_otra_base(numero // base, base) + str(numero % base)
    return res
print(decimal_a_otra_base(23,2))

