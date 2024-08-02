def obtener_parejas(texto):
    parejas = []
    comandos = texto.split('. ')  # Dividir el texto en frases usando el punto y espacio como separadores

    for comando in comandos:
        palabras = comando.split()  # Dividir cada frase en palabras
        codigo = palabras[0]  # La primera palabra es el código de operación
        resultado = palabras[-1]  # La última palabra es el resultado
        pareja = [codigo, resultado]
        parejas.append(pareja)
    return parejas

# Ejemplo de uso:
texto_entrada = "SUMAR 45 50 95. AND A B TRUE. MULT 30 20 600."
lista_parejas = obtener_parejas(texto_entrada)
print(lista_parejas)