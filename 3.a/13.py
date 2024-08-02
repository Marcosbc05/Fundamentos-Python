d=int(input('Inserte kilómetros: '))
if d<=300:
    print('Coste: 100€')
elif 300<d<=1000:
    coste=100+(d-300)*0.3
    print('Coste:',coste,'€')
elif 1000<d:
    coste=100+700*0.3+(d-1000)*0.2
    print('Coste:',coste,'€')