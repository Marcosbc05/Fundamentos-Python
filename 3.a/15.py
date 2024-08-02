coef=int(input('inserte coeficiente: '))
exp=int(input('inserte exponente de la x positivo: '))
def monomio(coef,exp):
    '''int->str'''
    if coef==0:
        return ' '
    elif coef==1 and exp>1:
        return f'+x**{exp}'
    elif coef==1 and exp==1:
        return '+x'
    elif coef>1 and exp==1:
        return f'+{coef}x'
    elif coef>1 and exp>1:
        return f'+{coef}x**{exp}'
    elif coef==-1 and exp>1:
        return f'-x**{exp}'
    elif coef==-1 and exp==1:
        return '-x'
    elif coef<-1 and exp==1:
        return f'{coef}x'
    elif coef<-1 and exp>1:
        return f'{coef}x**{exp}'
print(monomio(coef,exp))