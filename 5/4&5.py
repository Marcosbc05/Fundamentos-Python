import random
import math
def generar_punto():
    x=random.randint(0,20)
    y=random.randint(0,20)
    return {'x':x,'y':y}
p1=generar_punto()
p2=generar_punto()
print('p1:',p1,'p2:',p2)
def suma_puntos(p1,p2):
    q1=p1['x']+p2['x']
    q2=p1['y']+p2['y']
    return {'x':q1,'y':q2}
print('suma',suma_puntos(p1,p2))
def resta_puntos(p1,p2):
    q1=p1['x']-p2['x']
    q2=p1['y']-p2['y']
    return {'x':q1,'y':q2}
print('resta',resta_puntos(p1,p2))
#ejercicio 5
def distancia(p1,p2):
    q=resta_puntos(p1,p2)
    d=math.sqrt(q['x']**2+q['y']**2)
    return d
print('Distancia entre p1 y p2:',distancia(p1,p2))