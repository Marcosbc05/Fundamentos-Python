x=(input('inserte nº de mes: ')) #TIENE QUE ESTAR EN INT PARA QUE HAGA CASO
def meses(x):
    '''int->str
    obj: pasar de n a mes
    pre: 1<=x<=12'''
    try:
        x=int(x)
    except ValueError:
        return 'valor no valido, inserte nº del 1 al 12'
    else:
        if x==1:
            return 'enero'
        elif x==2:
            return 'febrero'
        elif x==3:
            return 'marzo'
        elif x==4:
            return 'abril'
        elif x==5:
            return 'mayo'
        elif x==6:
            return 'junio'
        elif x==7:
            return 'julio'
        elif x==8:
            return 'agosto'
        elif x==9:
            return 'septiembre'
        elif x==10:
            return 'octubre'
        elif x==11:
            return 'noviembre'
        elif x==12:
            return 'diciembre'
print(meses(x))
