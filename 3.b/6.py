#???

def calcular_terminos_serie_armonica(limite):
    suma = 0
    n = 0
    while suma <= limite:
        n += 1
        suma += 1 / n
    return n

try:
    limite = float(input("Introduce un número límite: "))
    
    if limite <= 0:
        print("El número límite debe ser un entero positivo.")
    else:
        n_terminos = calcular_terminos_serie_armonica(limite)
        print(f"Para un límite de {limite}, se necesitan al menos {n_terminos} términos para superar ese límite.")
except ValueError:
    print("Debes ingresar un número válido.")
