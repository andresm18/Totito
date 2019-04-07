import random
quien_gan = "no"
jug = "X"
jug_2 = "O"
tablero = [
             [" "," "," "],
             [" "," "," "],
             [" "," "," "]]
def tabler():
    print(' ' + tablero[0][0] + '   |  ' + tablero[0][1] + ' |  ' + tablero [0][2])
    print('     |    |')
    print("------------------")
    print(' ' + tablero[1][0] + '   |  ' + tablero[1][1] + ' |  ' + tablero [1][2])
    print('     |    |')
    print("------------------")
    print(' ' + tablero[2][0] + '   |  ' + tablero[2][1] + ' |  ' + tablero [2][2])
    print('     |    |')


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
    tablero[0][0] = " "
    tablero[0][1] = " "
    tablero[0][2] = " "
    tablero[1][0] = " "
    tablero[1][1] = " "
    tablero[1][2] = " "
    tablero[2][0] = " "
    tablero[2][1] = " "
    tablero[2][2] = " "
    

def espacio_libre(posi,rt):
    if tablero[posi][rt] == " ":
        return True
    else:
        False

def ganador(owo):
    if tablero[0][0] == "X" and tablero[0][1] == "X" and tablero[0][2] == "X":
        ganador = "si"
        quien_gan = "Jugador 1"
    elif tablero[1][0] == "X" and tablero[1][1] == "X" and tablero[1][2] == "X":
        ganador = "si"
        quien_gan = "Jugador 1"
    elif tablero[2][0] == "X" and tablero[2][1] == "X" and tablero[2][2] == "X":
        ganador = "si"
        quien_gan = "Jugador 1"
    elif tablero[0][0] == "X" and tablero[1][0] == "X" and tablero[2][0] == "X":
        ganador = "si"
        quien_gan = "Jugador 1"
    elif tablero[0][1] == "X" and tablero[1][1] == "X" and tablero[2][1] == "X":
        ganador = "si"
        quien_gan = "Jugador 1"
    elif tablero[0][2] == "X" and tablero[1][2] == "X" and tablero[2][2] == "X":
        ganador = "si"
        quien_gan = "Jugador 1"
    elif tablero[0][0] == "X" and tablero[1][1] == "X" and tablero[2][2] == "X":
        ganador = "si"
        quien_gan = "Jugador 1"
    elif tablero[0][2] == "X" and tablero[1][1] == "X" and tablero[2][0] == "X":
        ganador = "si"
        quien_gan = "Jugador 1"

    elif tablero[0][0] == "O" and tablero[0][1] == "O" and tablero[0][2] == "O":
        ganador = "si"
        quien_gan = "Jugador 2"
    elif tablero[1][0] == "O" and tablero[1][1] == "O" and tablero[1][2] == "O":
        ganador = "si"
        quien_gan = "Jugador 2"
    elif tablero[2][0] == "O" and tablero[2][1] == "O" and tablero[2][2] == "O":
        ganador = "si"
        quien_gan = "Jugador 2"
    elif tablero[0][0] == "O" and tablero[1][0] == "O" and tablero[2][0] == "O":
        ganador = "si"
        quien_gan = "Jugador 2"
    elif tablero[0][1] == "O" and tablero[1][1] == "O" and tablero[2][1] == "O":
        ganador = "si"
        quien_gan = "Jugador 2"
    elif tablero[0][2] == "O" and tablero[1][2] == "O" and tablero[2][2] == "O":
        ganador = "si"
        quien_gan = "Jugador 2"
    elif tablero[0][0] == "O" and tablero[1][1] == "O" and tablero[2][2] == "O":
        ganador = "si"
        quien_gan = "Jugador 2"
    elif tablero[0][2] == "O" and tablero[1][1] == "O" and tablero[2][0] == "O":
        ganador = "si"
        quien_gan = "Jugador 2"
    else:
        ganador = "no"
    if ganador == "si":
        print("Termino el juego felicidades a: ",quien_gan)
        

def user_choiceP1():   
    eleccion = input("Ingrese en que posicion quiere poner su pieza:")
    if eleccion == "q":
        tablero[0][0] = "X"
    elif eleccion == "w":
        tablero[0][1] = "X"
    elif eleccion == "e":
        tablero[0][2] = "X"
    elif eleccion == "a":
        tablero[1][0] = "x"
    elif eleccion == "s":
        tablero[1][1] = "X"
    elif eleccion == "d":
        tablero[1][2] = "X"
    elif eleccion == "z":
        tablero[2][0] = "X"
    elif eleccion == "x":
        tablero[2][1] = "X"
    elif eleccion == "c":
        tablero[2][2] = "X" 
    tabler()
    

def user_choiceP2():
    eleccion = input("Ingrese en que posicion quiere poner su pieza:")
    if eleccion == "q":
        tablero[0][0] = "O"
    elif eleccion == "w":
        tablero[0][1] = "O"
    elif eleccion == "e":
        tablero[0][2] = "O"
    elif eleccion == "a":
        tablero[1][0] = "O"
    elif eleccion == "s":
        tablero[1][1] = "O"
    elif eleccion == "d":
        tablero[1][2] = "O"
    elif eleccion == "z":
        tablero[2][0] = "O"
    elif eleccion == "x":
        tablero[2][1] = "O"
    elif eleccion == "c":
        tablero[2][2] = "O"
    tabler()



def totito():
    tabler()
    jugador_1 = input("Ingrese nombre del primer jugador: ")
    jugador_2 = input("Ingrese nombre del segundo jugador: ")
    print(jugador_1,jugador_2)
    lista_jugadores = [jugador_1,jugador_2]
    quien_empieza = (random.choice(lista_jugadores))
    ejemplo_cordenadas()
    turno = 1
    while (turno <= 9):
        if(turno % 2 != 0):
            print("Es el turno de: " + quien_empieza )
        user_choiceP1()
        user_choiceP1()
        user_choiceP1()

    
    
    
totito()
