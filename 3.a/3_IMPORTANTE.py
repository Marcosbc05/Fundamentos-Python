def entero(entrada):
    entero=True
    try:
        int(entrada)
    except ValueError:
        entero=False
    return entero
print(entero(input('inserte valor')))