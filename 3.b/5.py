#original
def dibujar_rectangulo(a,b,simbolo):
    """ int,int,str -> None
    OBJ: Dibuja en pantalla un rectángulo de dimensiones 
    a por b utilizando el símbolo como relleno
    """
    for i in range(a):
        for j in range(b):
            print(simbolo, end='')
        print()
dibujar_rectangulo(5,3,'#')
#3.b
def dibujar_rectangulo(a,b,s1, s2):
    """ int,int,str -> None
    OBJ: Dibuja en pantalla un rectángulo de dimensiones 
    a por b utilizando el símbolo como relleno
    """
    for i in range(a//2):
        for j in range(b):
            print(s1, end='')
        print()
        for h in range(b):
            print(s2, end='')
        print()
dibujar_rectangulo(5,3,'#','$')
#3.b
def dibujar_rectangulo(a,b,s1, s2):
    """ int,int,str -> None
    OBJ: Dibuja en pantalla un rectángulo de dimensiones 
    a por b utilizando el símbolo como relleno
    """
    for i in range(a):
        for j in range(b//2):
            print(s1, end='')
            print(s2, end='')
        print()
dibujar_rectangulo(5,4,'#','$')