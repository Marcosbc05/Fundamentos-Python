def entero(numero):
    numero=True
    try:
        int(numero)
    except ValueError:
        numero=False
    return entero