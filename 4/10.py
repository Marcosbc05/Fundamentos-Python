def codificar_frase(frase):
    frase_codificada = ""
    for letra in frase:
        if letra.lower() == 'a':
            frase_codificada += '4'
        elif letra.lower() == 'e':
            frase_codificada += '3'
        elif letra.lower() == 'i':
            frase_codificada += '1'
        elif letra.lower() == 'o':
            frase_codificada += '0'
        elif letra.lower() == 'u':
            frase_codificada += '#'
        else:
            frase_codificada += letra

    return frase_codificada

# Ejemplo de uso:
frase_original = "vote for spain"
frase_codificada = codificar_frase(frase_original)
print(frase_codificada)
