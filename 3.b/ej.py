#LABORATORIO
#1) A. Crear un subprograma de celsius a  kelvins
#B. Crear un subprograma de celsius a fahrenheit
#C. Validar la entrada
#D. Menu donde puedas elegir entre si convertir a fahrenheit, kelvins, introducir un nuevo dato o salir y que al introducir cualquiera de los 3 primeros vuelvas al menu.

def celsius_kelvin(c):
    '''int->int
    obj: celsius a kelvin'''
    k=c+273.15
    return f'{c}grados celsius son {k} kelvin'
def celsius_fahrenheit(c):
    '''int->int
    obj: celsius a fahrenheit'''
    f=c*(9/5)+32
    return f'{c} grados celsius son {f} grados fahrenheit'
c=input('INSERTE GRADOS EN CELSIUS: ')
a=True
while a:
    print('1.Convertir celsius a kelvin. 2.Convertir celsius a fahrenheit. 3.Introducir nuevo dato. 4.Salir')
    n=int(input('inserte número de opción: '))
    try:
        c=int(c)
        n=int(n)
    except ValueError:
        print('entrada no válida')
    else:
        if n==4:
            print('Adiós')
            a=False
        if n==1:
            print(celsius_kelvin(c))
        if n==2:
            print(celsius_fahrenheit(c))
        if n==3:
            c=input('INSERTE GRADOS EN CELSIUS: ')

#2) tabla de multiplicar de manera 3x5 = 10 + 5, una suma
#a. Tabla de multiplicar del 10 al 1
#b. Subrprograma de la tabla de multiplicar
#c. El subprograma pero validando la entrada