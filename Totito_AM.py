import random

def tablero():
    print("aqui iria tablero")
tablero()

def nombres_juga():
    jugador_1 = input("Ingrese nombre del primer jugador: ")
    jugador_2 = input("Ingrese nombre del segundo jugador: ")
    lista_jugadores = [jugador_1,jugador_2]
    print(jugador_1,jugador_2)
    quien_empieza = (random.choice(lista_jugadores))
    print("El jugador:" + quien_empieza + " " + "comenzara el juego")
    eleccion = input("Ingrese en que posicion quiere poner su pieza: ")
nombres_juga()


def totito():
    tablero()
    nombres_juga()
