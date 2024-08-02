cuantos = input('¿Cuántos números se van a introducir? ')
media=0
try:
    cuantos=int(cuantos)
except ValueError:
    print('intruduzca un número válido')
else:
    if cuantos <= 2: 
        print('Tienes que poner más de dos números') 
    else: 
        numero = cuantos 
        suma = numero 
        mayor = numero 
        menor = numero 
        for i in range(1, cuantos):
            numero = cuantos
            suma += numero
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
            media = suma/cuantos
        print(f'El mayor es {mayor}')
        print(f'El menor es {menor}')
        print(media)