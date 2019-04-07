import random
tablero = [
             ["","",""],
             ["","",""],
             ["","",""]]
def tabler():
    print(' ' + tablero[0][0] + '    |  ' + tablero[0][1] + '  |  ' + tablero [0][2])
    print('     |    |')
    print("------------------")
    print(' ' + tablero[1][0] + '    |  ' + tablero[1][1] + '  |  ' + tablero [1][2])
    print('     |    |')
    print("------------------")
    print(' ' + tablero[2][0] + '    |  ' + tablero[2][1] + '  |  ' + tablero [2][2])
    print('     |    |')
tabler()


def nombres_juga():
    jugador_1 = input("Ingrese nombre del primer jugador: ")
    jugador_2 = input("Ingrese nombre del segundo jugador: ")
    lista_jugadores = [jugador_1,jugador_2]
    print(jugador_1,jugador_2)
    quien_empieza = (random.choice(lista_jugadores))
    print("El jugador:" + quien_empieza + " " + "comenzara el juego")
    eleccion = input("Ingrese en que posicion quiere poner su pieza: ")
nombres_juga()

def espacio_libre():
    return tablero[posi] == " "


def totito():
    tablero()
    nombres_juga()
