def filtrar_diccionario(diccionario, lista):
    en_diccionario = [diccionario[elemento] for elemento in lista if elemento in diccionario]
    no_en_diccionario = [elemento for elemento in lista if elemento not in diccionario]
    return en_diccionario, no_en_diccionario

# Ejemplo de uso:
mi_diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
mi_lista = ['a', 'b', 'e', 'f']
valores_en_diccionario, valores_no_en_diccionario = filtrar_diccionario(mi_diccionario, mi_lista)
print("Valores en el diccionario:", valores_en_diccionario)
print("Valores no en el diccionario:", valores_no_en_diccionario)