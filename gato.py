import random

def dibujarTablero(tablero):
    # Dibuja el tablero recibido como argumento.
    # "tablero" es una lista de 10 cadenas representando el área de juego ( se ignora índice 0)
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('-----------')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('-----------')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])

def ingresaLetraJugador():
    # Permite al jugador escribir que letra desea ser.
    # Devuelve una lista con las letras de los jugadores como primer elemento,
    # y la de la PC como segundo.
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('¿Deseas ser X o O?')
        letra = input().upper()

    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def defineComienzo():
    # Elije al azar quien comienza.
    if random.randint(0, 1) == 0:
        return 'La PC'
    else:
        return 'El jugador'


def jugarDeNuevo():
    # Esta funcion devuelve True (Verdadero) si el jugador desea volver a jugar,
    # de lo contrario devuelve False (Falso).
    print('¿Quieres volver a jugar? (sí/no)?')
    return input().lower().startswith('s')

def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra

def esGanador(tablero, letra):
    # Dado un tablero y la letra de un jugador, devuelve True (verdadero) si el mismo ha ganado.
    return ((tablero[7] == letra and tablero[8] == letra and tablero[9] == letra) or  # horizontal superior
            (tablero[4] == letra and tablero[5] == letra and tablero[6] == letra) or  # horizontal medio
            (tablero[1] == letra and tablero[2] == letra and tablero[3] == letra) or  # horizontal inferior
            (tablero[7] == letra and tablero[4] == letra and tablero[1] == letra) or  # vertical izquierda
            (tablero[8] == letra and tablero[5] == letra and tablero[2] == letra) or  # vertical medio
            (tablero[9] == letra and tablero[6] == letra and tablero[3] == letra) or  # vertical derecha
            (tablero[7] == letra and tablero[5] == letra and tablero[3] == letra) or  # diagonal
            (tablero[9] == letra and tablero[5] == letra and tablero[1] == letra))  # diagonal


def hayEspacioLibre(tablero, jugada):
    # Devuelte true si hay espacio para efectuar la jugada en el tablero.
    return tablero[jugada] == ' '

def obtenerJugadaJugador(tablero):
    # Permite al jugador escribir su jugada.
    jugada = ' '
    while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not hayEspacioLibre(tablero, int(jugada)):
        print('¿Cuál es tu próxima jugada? (1-9)')
        jugada = input()
    return int(jugada)


def elegirAzarDeLista(tablero, listaJugada):
    # Devuelve una jugada válida en el tablero de la lista recibida.
    # Devuelve None si no hay ninguna jugada válida.
    listaPosibles = []
    for i in listaJugada:
        if hayEspacioLibre(tablero,i):
            listaPosibles.append(i)

    if len(listaPosibles) != 0:
        return random.choice(listaPosibles)
    else:
        return None


def tableroCompleto(tablero):
    # Devuelve True si cada espacio del tablero fue ocupado, caso contrario devuele False.
    for i in range(1,10):
        if hayEspacioLibre(tablero, i):
            return False
    return True

def copiaTablero(tablero):
    duplicado = tablero.copy()
    return duplicado

def obtenerJugadaComputadora(tablero, letraComputadora):
    if letraComputadora == 'X':
        letraJugador = 'O'
    else:
        letraJugador = 'X'

    # Algoritmo para nuestra IA del Gato
    # realizar la jugada ganadora
    for i in range(1,10):
        copia = copiaTablero(tablero)
        if hayEspacioLibre(copia,i):
            hacerJugada(copia,letraComputadora,i)
            if esGanador(copia,letraComputadora):
                return i

    # No hay ganador entonces tratar de bloquear
    for i in range(1,10):
        copia = copiaTablero(tablero)
        if hayEspacioLibre(copia,i):
            hacerJugada(copia, letraJugador, i)
            if esGanador(copia, letraJugador):
                return i

    jugada = elegirAzarDeLista(tablero, [1,3,7,9])
    if jugada != None:
        return jugada

    if hayEspacioLibre(tablero, 5):
        return 5

    return elegirAzarDeLista(tablero, [2,4,6,8])

def main():
    print("Bienvenido al  GATO!!!!!")

    while True:
        # reset del tablero
        elTablero = [' '] * 10
        letraJugador, letraComputadora = ingresaLetraJugador()
        print("JUGADOR = {}".format(letraJugador))
        print("COMPUTADORA = {}".format(letraComputadora))
        turno = defineComienzo()
        print(turno + " irá primero.")
        juegoEnCurso = True
        while juegoEnCurso:
            if turno == "El jugador":
                # turno del jugador
                print("Turno de el Jugador")
                dibujarTablero(elTablero)
                jugada = obtenerJugadaJugador(elTablero)
                hacerJugada(elTablero, letraJugador, jugada)
                if esGanador(elTablero, letraJugador):
                    dibujarTablero(elTablero)
                    print("Felicidades ya Ganaste ...")
                    juegoEnCurso = False
                else:
                    if tableroCompleto(elTablero):
                        dibujarTablero(elTablero)
                        print("Es un empate!!!!!")
                        break
                    else:
                        turno = 'La PC'
            else:
                # define el turno de la PC
                print("Turno de la PC")
                dibujarTablero(elTablero)
                jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
                hacerJugada(elTablero, letraComputadora, jugada)
                if esGanador(elTablero, letraComputadora):
                    dibujarTablero(elTablero)
                    print("La PC ha ganado, perdiste!!!! ")
                    juegoEnCurso = False
                else:
                    if tableroCompleto(elTablero):
                        dibujarTablero("Es un empate")
                        break
                    else:
                        turno = "El jugador"

        if not jugarDeNuevo():
            break

if __name__ == '__main__':
    main()