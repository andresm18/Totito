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
    


def ganador():
    if tablero[0][0] == "X" and tablero[0][1] == "X" and tablero[0][2] == "X":
        ganador = "si"
        quien_gan = segundo
    elif tablero[1][0] == "X" and tablero[1][1] == "X" and tablero[1][2] == "X":
        ganador = "si"
        quien_gan = segundo
    elif tablero[2][0] == "X" and tablero[2][1] == "X" and tablero[2][2] == "X":
        ganador = "si"
        quien_gan = segundo
    elif tablero[0][0] == "X" and tablero[1][0] == "X" and tablero[2][0] == "X":
        ganador = "si"
        quien_gan = segundo
    elif tablero[0][1] == "X" and tablero[1][1] == "X" and tablero[2][1] == "X":
        ganador = "si"
        quien_gan = segundo
    elif tablero[0][2] == "X" and tablero[1][2] == "X" and tablero[2][2] == "X":
        ganador = "si"
        quien_gan = segundo
    elif tablero[0][0] == "X" and tablero[1][1] == "X" and tablero[2][2] == "X":
        ganador = "si"
        quien_gan = segundo
    elif tablero[0][2] == "X" and tablero[1][1] == "X" and tablero[2][0] == "X":
        ganador = "si"
        quien_gan = segundo

    elif tablero[0][0] == "O" and tablero[0][1] == "O" and tablero[0][2] == "O":
        ganador = "si"
        quien_gan = quien_empieza
    elif tablero[1][0] == "O" and tablero[1][1] == "O" and tablero[1][2] == "O":
        ganador = "si"
        quien_gan = quien_empieza
    elif tablero[2][0] == "O" and tablero[2][1] == "O" and tablero[2][2] == "O":
        ganador = "si"
        quien_gan = quien_empieza
    elif tablero[0][0] == "O" and tablero[1][0] == "O" and tablero[2][0] == "O":
        ganador = "si"
        quien_gan = quien_empieza
    elif tablero[0][1] == "O" and tablero[1][1] == "O" and tablero[2][1] == "O":
        ganador = "si"
        quien_gan = quien_empieza
    elif tablero[0][2] == "O" and tablero[1][2] == "O" and tablero[2][2] == "O":
        ganador = "si"
        quien_gan = quien_empieza
    elif tablero[0][0] == "O" and tablero[1][1] == "O" and tablero[2][2] == "O":
        ganador = "si"
        quien_gan = quien_empieza
    elif tablero[0][2] == "O" and tablero[1][1] == "O" and tablero[2][0] == "O":
        ganador = "si"
        quien_gan = quien_empieza
    else:
        ganador = "no"
    if ganador == "si":
        print("Termino el juego felicidades a:",quien_gan)
        exit(0)


def user_choiceP1():
    ganador() 
    valido = "n"
    while valido != "y":
        print(quien_empieza)
        eleccion = input("Ingrese en que posicion quiere poner su pieza: ")
        if eleccion == "q" and tablero[0][0] == " ":
            tablero[0][0] = "X"
            valido = "y"
        elif eleccion == "w" and tablero[0][1] == " ":
            tablero[0][1] = "X"
            valido = "y"
        elif eleccion == "e" and tablero[0][2] == " ":
            tablero[0][2] = "X"
            valido = "y"
        elif eleccion == "a" and tablero[1][0] == " ":
            tablero[1][0] = "X"
            valido = "y"
        elif eleccion == "s" and tablero[1][1] == " ":
            tablero[1][1] = "X"
            valido = "y"
        elif eleccion == "d" and tablero[1][2] == " ":
            tablero[1][2] = "X"
            valido = "y"
        elif eleccion == "z" and tablero[2][0] == " ":
            tablero[2][0] = "X"
            valido = "y"
        elif eleccion == "x" and tablero[2][1] == " ":
            tablero[2][1] = "X"
            valido = "y"
        elif eleccion == "c" and tablero[2][2] == " ":
            tablero[2][2] = "X" 
            valido = "y"
        else:
            print("lo siento ya esta tomada la posicion")
        tabler()
    

def user_choiceP2():
    ganador() 
    valido = "n"
    while valido != "y":
        print(segundo)
        eleccion = input("Ingrese en que posicion quiere poner su pieza: ")
        if eleccion == "q" and tablero[0][0] == " ":
            tablero[0][0] = "O"
            valido = "y"
        elif eleccion == "w" and tablero[0][1] == " ":
            tablero[0][1] = "O"
            valido = "y"
        elif eleccion == "e" and tablero[0][2] == " ":
            tablero[0][2] = "O"
            valido = "y"
        elif eleccion == "a" and tablero[1][0] == " ":
            tablero[1][0] = "O"
            valido = "y"
        elif eleccion == "s" and tablero[1][1] == " ":
            tablero[1][1] = "O"
            valido = "y"
        elif eleccion == "d" and tablero[1][2] == " ":
            tablero[1][2] = "O"
            valido = "y"
        elif eleccion == "z" and tablero[2][0] == " ":
            tablero[2][0] = "O"
            valido = "y"
        elif eleccion == "x" and tablero[2][1] == " ":
            tablero[2][1] = "O"
            valido = "y"
        elif eleccion == "c" and tablero[2][2] == " ":
            tablero[2][2] = "O" 
            valido = "y"
        else:
            print("lo siento ya esta tomada la posicion")
    tabler()
print("Bienvenido a Misere Tic-Tac-Toe, si completas la linea pierdes")
jugador_1 = input("Ingrese nombre del primer jugador: ")
jugador_2 = input("Ingrese nombre del segundo jugador: ")
lista_jugadores = [jugador_1,jugador_2]
num_juga = 2
lista_a_random = random.sample(lista_jugadores,num_juga)
quien_empieza = lista_a_random[0]
segundo = lista_a_random[1]

def totito():
    tabler()
    print("Empieza: ",quien_empieza)
    ejemplo_cordenadas()
    while quien_gan != "owo":
        tabler()
        user_choiceP1()
        user_choiceP2()
totito()