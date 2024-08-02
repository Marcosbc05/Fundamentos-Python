def inicializar_tablero(filas, columnas):
    return [[' ' for _ in range(columnas)] for _ in range(filas)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print('|'.join(fila))
        print('-' * (4 * len(fila) - 1))

def colocar_ficha(tablero, columna, jugador):
    fila = len(tablero) - 1
    while fila >= 0 and tablero[fila][columna] != ' ':
        fila -= 1
    if fila >= 0:
        tablero[fila][columna] = jugador
        return True
    else:
        print("Columna llena. Elija otra columna.")
        return False

def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if ' '.join(fila).count(jugador * 4) > 0:
            return True

    # Verificar columnas
    for col in range(len(tablero[0])):
        columna = [fila[col] for fila in tablero]
        if ' '.join(columna).count(jugador * 4) > 0:
            return True

    # Verificar diagonales
    for i in range(len(tablero) - 3):
        for j in range(len(tablero[0]) - 3):
            diagonal = [tablero[i + k][j + k] for k in range(4)]
            if ' '.join(diagonal).count(jugador * 4) > 0:
                return True

            diagonal_inversa = [tablero[i + 3 - k][j + k] for k in range(4)]
            if ' '.join(diagonal_inversa).count(jugador * 4) > 0:
                return True

    return False

if __name__ == "__main__":
    filas = 6
    columnas = 7
    jugador1 = 'X'
    jugador2 = 'O'

    tablero = inicializar_tablero(filas, columnas)
    turno = 1

    while True:
        mostrar_tablero(tablero)

        if turno % 2 != 0:
            jugador = jugador1
        else:
            jugador = jugador2

        columna = int(input(f"\nJugador {jugador}, elija una columna (0-{columnas - 1}): "))
        if 0 <= columna < columnas:
            if colocar_ficha(tablero, columna, jugador):
                if verificar_ganador(tablero, jugador):
                    mostrar_tablero(tablero)
                    print(f"\n¡Jugador {jugador} ha ganado!")
                    break
                turno += 1
            else:
                continue
        else:
            print("Columna inválida. Introduzca un número entre 0 y", columnas - 1)