def palindromo(palabra):
    '''
    str->bool
    comprobar palíndromo
    PRE: escribir en minusculas
    '''
    palabra=palabra.lower()
    p=False
    if palabra==palabra[::-1]:
        p=True
    return p
#probador
print(palindromo('bebe'))  
print(palindromo('reconocer'))  
print(palindromo('radar'))
print(palindromo('animal'))  
print(palindromo('Seres'))  