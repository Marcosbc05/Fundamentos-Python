import math
print('1.Seno, 2.Coseno, 3.Tangente, 4.Cosecante, 5. Secante, 6. Tangente, 0. Salir')
x=int(input('inserte nº de opción: '))
if x==0:
    print('programa finalizado')
    SystemExit
if x==1:
    a=int(input('angulo: '))
    b=math.radians(a)
    print(math.sin(b))
if x==2:
    a=int(input('angulo: '))
    b=math.radians(a)
    print(math.cos(b))
if x==3:
    a=int(input('angulo: '))
    b=math.radians(a)
    print(math.tan(b))
if x==4:
    a=int(input('angulo: '))
    b=math.radians(a)
    print(1/math.sin(b))
if x==5:
    a=int(input('angulo: '))
    b=math.radians(a)
    print(1/math.cos(b))
if x==6:
    a=int(input('angulo: '))
    b=math.radians(a)
    print(1/math.tan(b))
