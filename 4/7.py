def capitalizar_palabras(frase):
    palabras = frase.split()  # Dividir la frase en palabras
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]  # Capitalizar cada palabra
    nueva_frase = ' '.join(palabras_capitalizadas)  # Unir las palabras capitalizadas de nuevo en una frase
    return nueva_frase

#probador
frase_original = "hola mundo, cómo estás?"
frase_capitalizada = capitalizar_palabras(frase_original)
print(frase_capitalizada)
