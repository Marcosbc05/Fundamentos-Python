def contar_longitudes_palabras():
    contadores = [0] * 16

    palabra = input("Introduce una palabra (o 'fin' para terminar): ")

    while palabra.lower() != 'fin':
        longitud = len(palabra)
        if 1 <= longitud <= 15:
            contadores[longitud] += 1
        else:
            print("Longitud no permitida, la palabra debe tener entre 1 y 15 caracteres.")
        palabra = input("Introduce otra palabra (o 'fin' para terminar): ")

    for i in range(16):
        print(f"Palabras longitud {i}: {contadores[i]}")

#probador
contar_longitudes_palabras()
