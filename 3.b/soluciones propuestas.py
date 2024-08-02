def factorial(n):
    """ int -> int 
    OBJ: Calcula el factorial de un numero entero
    PRE: 0 <= n <= 30
    """
    acu = 1
    #for i in range(1, n+1):
    #acu *= i
    #return acu
#print(factorial(5))

def salida_numerica():
    """ None -> None
    OBJ: Muestra una tabla numérica por pantalla 
    """
    for i in range (1,4):
        for j in range (0,4):
            print(i,'-', j, end='\t')
        print() #para que haga solo salto de linea al acabar el for j...
print(salida_numerica())

def dibujar_rectangulo(a,b,simbolo):
     """ int,int,str -> None
     OBJ: Dibuja en pantalla un rectángulo de dimensiones 
     a por b utilizando el símbolo como relleno
     """
     for i in range(a):
         for j in range(b):
             print(simbolo, end=' ')
         print()
dibujar_rectangulo(3,5,'?')

intentos = 1
print('Intente adivinar el símbolo oculto')
simbolo = input('Haga su apuesta: ')
while simbolo != '#':
 simbolo = input('Ese no es el símbolo oculto. Haga su apuesta: ')
 intentos += 1
print(f'Por fin! Ha necesitado {intentos} intentos para adivinarlo.')
