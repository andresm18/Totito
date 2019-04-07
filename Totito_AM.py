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



def nombres_juga():
    jugador_1 = input("Ingrese nombre del primer jugador: ")
    jugador_2 = input("Ingrese nombre del segundo jugador: ")
    lista_jugadores = [jugador_1,jugador_2]
    print(jugador_1,jugador_2)
    quien_empieza = (random.choice(lista_jugadores))
    print("El jugador:" + quien_empieza + " " + "comenzara el juego")

def ejemplo_cordenadas():
    print("Abajo esta el tablero con las teclas y sus respectivas posiciones")
    tablero[0][0] = "q"
    tablero[0][1] = "w"
    tablero[0][2] = "e"
    tablero[1][0] = "a"
    tablero[1][1] = "s"
    tablero[1][2] = "d"
    tablero[2][0] = "z"
    tablero[2][1] = "x"
    tablero[2][2] = "c"
    print(' ' + tablero[0][0] + '   |  ' + tablero[0][1] + '  |  ' + tablero [0][2])
    print('     |     |')
    print("------------------")
    print(' ' + tablero[1][0] + '   |  ' + tablero[1][1] + '  |  ' + tablero [1][2])
    print('     |     |')
    print("------------------")
    print(' ' + tablero[2][0] + '   |  ' + tablero[2][1] + '  |  ' + tablero [2][2])
    print('     |     |')
    

def espacio_libre():
    return tablero[posi] == " "

def ganador():

def user_choice():   
    eleccion = input("Ingrese en que posicion quiere poner su pieza:")



def totito():
    tabler()
    nombres_juga()
    ejemplo_cordenadas()
    user_choice()
totito()
