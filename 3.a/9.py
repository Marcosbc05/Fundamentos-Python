import math
print('ax^2+bx+c=0')
a=int(input('inserte valor de a: '))
b= int(input('inserte valor de b: '))
c= int(input('inserte valor de c: '))
raiz = (b**2)-(4*a*c)
if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2*a)
    x2 = (-b - math.sqrt(raiz)) / (2*a)
    print("Las soluciones son x1 =", x1, "y x2 =", x2)
elif raiz == 0:
    x1 = -b / (2*a)
    print("Solo hay una solucion: x =", x1)
else:
    print("No hay soluciones reales")