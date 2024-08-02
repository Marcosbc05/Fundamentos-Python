try:
    numerador=int(input('introduzca el numerador: '))
    denominador=int(input('introduzca el denominador: '))
    j=numerador/denominador
except ZeroDivisionError:
    print('No se puede dividir entre 0')
except NameError and ValueError:
    print('error en conversion de tipos')
except:
    print('¡Ha ocurrido algún error!')
else:
    print(j)