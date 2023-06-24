nombre = input ("¿Como te llamas?\n")
print (f"¡Hola {nombre}! Es hora de jugar al ahorcado.")


def jugar_ahorcado():
    palabra_secreta = "perro"
    intentos = 6
    letras_adivinadas = []
    while True:
        # Mostrar estado actual de la palabra
        palabra_mostrada = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "
        print(palabra_mostrada)
        # Pedir una letra al jugador
        letra = input("Ingresa una letra: ").lower()
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue
        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print("¡Correcto!")
        else:
            intentos -= 1
            print("Incorrecto.")
            print("Te quedan {} intentos.".format(intentos))
        # Verificar si el jugador ganó o perdió
        if intentos == 0:
            print("¡Has perdido! La palabra secreta era '{}'.".format(palabra_secreta))
            break
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("¡Felicidades! ¡Has ganado!")
            
            print (" _______________$$$$$$$________$$$$$$$$$   ")
            print(" _____________$$________________________$$$$")
            print(" ____________$$_____________________________$$")
            print(" ___________$__________________________________$$")
            print ("___________$$___________________________________$$")
            print("__________$$__$$______________________$$__________$$")
            print("________$$__$$___$$$$_________$$$$____$$__________$$$$")
            print("______$$___$$__$$$$__$$_____$$$$__$$_$$_____________$$$")
            print("______$$___$$____$$$$_________$$$$___$$_______________$$")
            print(" ______$$___$$________________________$$_______________$$")
            print("______$$____$$_______________________$$_____________$$")
            print("________$$__$$____$$$$$$_____________$$___________$$$")
            print("________$$__$$__$$______$$___________$$_________$$")
            print("________$$__$$__$$______$$___________$$_______$$")
            print("__________$$$$____$$$$$$_____________$$$$____$$$$")
            print("__________$$$$_____________________$$__$$____$$$")
            print("___________$$_$$$$$$$$$$$$_____$$$$______$$$$_$$")
            print("_____________$$___$$______$$$$$_______________$$")
            print("_____________$$_____$$$$$$$____________________$$")
            print("_____________$$________________________________$$")
            print("____________$$_________________________________$$")
            print("____________$$_________________________________$$")
            print("____________$$___________________________________$")
            print("____________$$___________________________________$$")
            print("__________$$_________________________$$___________$")
            print("__________$$__________$$___________$$_____________$$")
            print("________$$__$$________$$_________$$_______________$$")
            print("______$$____$$__________$$_______$$_______________$$")
            print("______$$____$$____________$$___$$_________________$$")
            print("____$$______$$_____________$$_$$_______$$_________$$")
            print("____$$______$$________$$____$$$________$$_________$$")
            print("____$$______$$________$$____$$$_______$$__________$$")
            print("____$$______$$________$$_______________$$__________$$")
            print("____$$______$$________$$_______________$$____________$")
            print("_$$$$_______$$________$$_______________$$____________$$")
            print("$___$$______$$________$$$$___________$$$$____________$$")
            print("$___$$______$$________$$__$$_______$$__$$____________$$")
            print("t_$$$$$______$$________$$____$$___$$_____$$___________$$")
            print("____$$______$$________$$______$$_______$$___________$$")
            print("____$$______$$________$$_____$$________$$___________$$")
            print("__$$________$$________$$$$$$$$___$$$$$$__$$_________$$")
            print("__$$________$$________$$______$$$______$$$$_________$$")
            print("$$________$$__________$$_________$$$$$$__$$__________$")
            print("$$______$$__________$$$$$$$$$$$$$$$______$$__________$")
            print("$$_$$_$$$__________$$_____________$$$$$$$__$$_________$")
            print("_$$$$$$$___________$$______________________$$________$$")
            print("_____$$__$$__$$__$$_$______________________$$__________$$")
            print("______$$$$__$___$__$$______________________$$____________$")
            print("_______$$___$___$__$________________________$$_$__$$__$$__$")
            print("_________$$$$$$$$$$__________________________$$_$_$$$$$$$$")
        
            break
jugar_ahorcado()