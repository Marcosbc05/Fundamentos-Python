def contar_longitudes_palabras():
    frecuencias = {}

    while True:
        palabra = input("Introduce una palabra (o 'fin' para terminar): ")
    
        if palabra.lower() == 'fin':
            break
        longitud = len(palabra)
        if longitud in frecuencias:
            frecuencias[longitud] += 1
        else:
            frecuencias[longitud] = 1
    return frecuencias

frecuencias_palabras = contar_longitudes_palabras()
print(frecuencias_palabras)
print("\nFrecuencias de longitudes de palabras:")
for longitud, frecuencia in frecuencias_palabras.items():
    print(f"Palabras de longitud {longitud}: {frecuencia}")
