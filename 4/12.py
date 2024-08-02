def mostrar_al_reves_sin_a(cadena):
    resultado = ""
    for caracter in cadena[::-1]:
        if caracter.lower() != 'a':
            resultado += caracter
    return resultado

# Ejemplo de uso:
entrada = "barco naranja"
resultado_final = mostrar_al_reves_sin_a(entrada)
print(resultado_final)
