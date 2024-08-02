import random
def generar_codigo_qr_version_1():
    tamano = 21
    # Inicializar la matriz del código QR con todos los píxeles en blanco
    codigo_qr = [[0]*21]*21
    # Generar aleatoriamente píxeles negros en la matriz
    for i in range(tamano):
        for j in range(tamano):
            if random.choice([True, False]):
                codigo_qr[i][j] = 'X'
    return codigo_qr

for fila in generar_codigo_qr_version_1():
    print(fila)