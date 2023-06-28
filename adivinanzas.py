import random
adivinaste = 0
palabra_singular = "palabra"
perdiste = 0
user_option = ""
palabras = ["perro", "gato","llave","corazon","patricio estrella","ballena","caracol","cangrejo","pikachu","trofeo","homero simpson","reloj","avion","pizza"]

nombre = input ("¿Como te llamas?\n")
print (f"¡Hola {nombre}! Es hora de jugar a las adivinanzas.\n")



while (user_option != 3):
    print("[......ESCOGE UNA OPCIÓN:.......]\n")
    print("1. Quiero jugar.")  
    print("2. Quiero saber los resultados")
    print("3. salir\n\n")
    user_option = int (input())

    if (user_option == 1):
            #instrucción del juego
            print("Tienes la opción de ingresar la palabra completa o adivinando las letras: ¡Tienes 6 intentos! ¡Suerte! ")
            
            #¡opción si el usuario adivino todas las palabras!
            if len(palabras) == 0:
                print("     __^__                     __^__  ")
                print("    ( ___ )-------------------( ___ ) ")
                print("     | / |   ¡Felicidades!     | / |  ")
                print("     | / |     Le acertaste    | / |  ")
                print("     |___|           a todas.  |___|  ")
                print("    (_____)-------------------(_____) ")

            else:
                print (f"Te quedan {len (palabras)} palabras por adivinar.")
                palabra_secreta = random.choice(palabras)
                intentos = 6
                letras_adivinadas = []

                if(palabra_secreta == "perro"):
                    print ("________________________________________ ")
                    print ("|Tiene patas, pero no puede caminar,    |")
                    print ("|tiene pelo, pero no es humano,         |")
                    print ("|ladra sin voz, pero comunica sin igual.|")
                    print ("| ¿Qué es este misterioso animal?       |")
                    print ("|_______________________________________|")

                elif(palabra_secreta == "gato"):
                    print("____________________________________________________________________________________________________ ")
                    print("|Silente y sigiloso, en la sombra se desliza, de noche es cazador y de día se echa largas siestas.  |")
                    print("|¿Qué misterioso felino es?                                                                         |")
                    print("|___________________________________________________________________________________________________|")
                
                elif(palabra_secreta == "llave"):
                    print("________________________________________________ ")
                    print("|No muerde ni ladra,                            |")
                    print("|pero tiene dientes y la casa guarda. ¿Qué es?  |")
                    print("|_______________________________________________|")

                elif(palabra_secreta == "corazon"):
                    print("_____________________________________________________________________________________")
                    print("|Sin descanso trabaja, bombeando sin cesar, llevando vida a cada rincón sin parar.  |")
                    print("|¿Qué órgano incansable puede ser?                                                  |")
                    print("____________________________________________________________________________________|")
                
                elif(palabra_secreta == "patricio estrella"):
                    print("___________________________________________  ")
                    print("|De color rosa y distraído sin igual,      |")
                    print("|vive bajo el mar en un hogar peculiar.    |")
                    print("|Amigo de Bob Esponja, siempre es leal.    |")
                    print("|¿Quién es este personaje especial?        |")
                    print("|__________________________________________|")

                elif(palabra_secreta == "ballena"):
                    print("_________________________________________________ ")
                    print("| En el océano grande y azul,                    |")
                    print("| un gigante majestuoso y muy corpulento.        |")
                    print("| ¿Quién es, de cola a cabeza, el más imponente? |")
                    print("|________________________________________________|")

                elif(palabra_secreta == "caracol"):
                    print("_________________________________________________")
                    print("|voy con mi casa al hombro, ando sin tener patas |")
                    print("|y voy marcando mi huella con un hilito de plata.|")
                    print("|¿Quien soy?                                     |")                                   
                    print("|________________________________________________|")

                elif(palabra_secreta == "cangrejo"):
                    print("___________________________________")
                    print("|Al ir parece que vengo y al venir |")
                    print("|es que me voy                     |")
                    print("|__________________________________|")

                elif(palabra_secreta == "pikachu"):
                    print("____________________________________________")
                    print("|De colita rayada y mejillas amarillas,      |")
                    print("|soy un pokémon eléctrico que brilla.        |")
                    print("|¿quién soy?                                 |")
                    print("|____________________________________________|")

                elif(palabra_secreta == "trofeo"):
                    print("______________________________________________")
                    print("|Objeto brillante, símbolo de victoria,       |")
                    print("|se otorga a aquellos que alcanzan la gloria. |")
                    print("|Simbolo de fuerza y momentos inolvidables.   |")
                    print("|_____________________________________________|")

                elif(palabra_secreta == "homero simpson"):
                    print("________________________________________________________")
                    print("|Amante de la comida rápida y la holgazanería,         |")
                    print("|su sabiduría es escasa, pero su corazón es de alegría.|")
                    print("|Con su lema '¡D'oh!' es famoso por su error,          |")
                    print("|¿quién es este padre de familia con mucho humor?      |")
                    print("________________________________________________________")

                elif(palabra_secreta == "reloj"):
                    print("___________________________________________________")
                    print("|Pequeño dispositivo de gran precisión,            |")
                    print("|con sus manecillas marca la ocasión.              |")
                    print("|Cronometra segundos, minutos y horas,             |")
                    print("|y en su tic-tac el tiempo se desliza sin demoras. |")
                    print("|__________________________________________________|")

                elif(palabra_secreta == "avion"):
                    print("___________________________________________________")
                    print("|Vuelo por los cielos, sin alas me desplazo.       |")
                    print("| Soy rápido y gigante, en el aire trazo. ¿Qué soy?|")
                    print("|__________________________________________________|")

                elif(palabra_secreta == "pizza"):
                    print("________________________________________________ ")
                    print("|Tiene masa y queso, con sabores sin fin,       |")
                    print("|    en cada bocado, un festín.                 |")
                    print("| ¿Qué comida es esta tan divina?               |")
                    print("|_______________________________________________|")

                # Primer print con estado de la adivinanza
                print("_ " * len(palabra_secreta))

                while True:
                    # Pedir una letra al jugador
                    letra_usuario = input("Ingresa una letra: ").lower().strip()

                    if letra_usuario == "":
                        continue

                    #si el usuario adivina la palabra de una:
                    
                    if letra_usuario in letras_adivinadas:
                        print("Ya has adivinado esa letra.")
                        continue

                    if letra_usuario in palabra_secreta:
                        letras_adivinadas.append(letra_usuario)
                        print("¡Correcto!")
                    
                    else:
                        intentos -= 1
                        print("Incorrecto.")
                        print(f"Te quedan {intentos} intentos.")
                    
                    # Verificar si el jugador perdió o no adivinó ninguna letra en esta vuelta
                    if len(letras_adivinadas) == 0:
                        continue
                    
                    if intentos == 0:
                        print(f"¡Has perdido! La palabra secreta era: {palabra_secreta}")
                        perdiste = perdiste + 1

                        break
                    
                    # Validar si ganó e ir imprimiendo 
                    palabra_secreta_intento = ""
                    
                    for letra in palabra_secreta:
                        if letra in letras_adivinadas or letra == " ":
                            palabra_secreta_intento += letra
                            print(f"{letra} ", end= "")
                        else:
                            palabra_secreta_intento += "_"
                            print(f"_ ", end= "")

                    print("\n\n")

                    if palabra_secreta_intento == palabra_secreta or letra_usuario == palabra_secreta :
                        print("¡Felicidades! ¡Has ganado!")
                        adivinaste = adivinaste + 1
                        palabras.remove(palabra_secreta)

                        if (palabra_secreta == "perro"):
                            print("░░░░░░▄█▄█░░░░░▄░░░░░░")
                            print("░░░░██████░░░░░░█░░░░░")
                            print("░░░░░░███████████░░░░░")
                            print("▒▒▒▒▒▒█▀▀█▀▀██▀██▒▒▒▒▒")
                            print("▒▒▒▒▒▄█▒▄█▒▒▄█▒▄█▒▒▒▒▒")
                        
                        if (palabra_secreta == "gato"):
                            print("░░░▄▀▌░▄▀▌░░░░░░░░░░░░")
                            print("░▄██▀▀▀█▀▀▀▄╔╦╗╔╗╔╗╗╗╗")
                            print("▐███░▐░█░▐░█║║║╠╝║║║║║")
                            print("███████╥████╝╝╝╚╝╚╝╩╩╝")
                            print("█████╚═╩═╝██░░░░░░░░░░")
                        
                        if (palabra_secreta == "llave"):
                            print("──▄▀▀▀▄───────────────")
                            print("──█───█───────────────")
                            print("─███████─────────▄▀▀▄─")
                            print("░██─▀─██░░█▀█▀▀▀▀█░░█░")
                            print("░███▄███░░▀░▀░░░░░▀▀░░")

                        if (palabra_secreta == "corazon"):
                            print("─────▄█▀█▄──▄███▄────❤")
                            print("────▐█░██████████▌────")
                            print("─────██▒█████████─────")
                            print("──────▀████████▀──────")
                            print("─────────▀██▀─────────")
                        
                        if (palabra_secreta == "patricio estrella"):
                            print ("────────────────────██████──────────")
                            print("──────────────────██▓▓▓▓▓▓██────────")
                            print("────────────────██▓▓▓▓▒▒▒▒██────────")
                            print("────────────────██▓▓▒▒▒▒▒▒██────────")
                            print("──────────────██▓▓▓▓▒▒▒▒██──────────")
                            print("──────────────██▓▓▒▒▒▒▒▒██──────────")
                            print("────────────██▓▓▓▓▒▒▒▒▒▒██──────────")
                            print("────────────████▒▒████▒▒██──────────")
                            print("────────────██▓▓▒▒▒▒▒▒▒▒██──────────")
                            print("──────────██────▒▒────▒▒██──────────")
                            print("──────────████──▒▒██──▒▒██──────────")
                            print("─────────██────▒▒────▒▒██──────────")
                            print("──────────██▒▒▒▒▒▒▒▒▒▒▒▒██──────────")
                            print("──────────████████████▒▒▒▒██────────")
                            print("────────██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██──────")
                            print("──────██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██────")
                            print("────██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██──")
                            print("──██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██")
                            print("██▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██")
                            print("██▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒██")
                            print("██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██")
                            print("──████▐▌▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▌▐▌████──")
                            print("────██▐▌▐▌▌▌▌▌▌▌▌▌▐▌▐▌▐▌▐▌▌▌▐▌██────")
                            print("────██▌▌▐▌▐▌▌▌▐▌▌▌▌▌▐▌▌▌▌▌▌▌▌▌██────")
                            print("──────██▌▌▐▌▐▌▐▌▐▌▐▌▐▌▐▌▌▌▌▌██──────")
                            print("──────██▐▌▐▌▐▌████████▐▌▌▌▌▌██──────")
                            print("────────██▒▒██────────██▒▒██────────")
                            print("────────██████────────██████────────")

                        if(palabra_secreta == "ballena"):
                            print("─────▀▄▀─────▄─────▄")
                            print("──▄███████▄──▀██▄██▀")
                            print("▄█████▀█████▄──▄█")
                            print("███████▀████████▀")
                            print("─▄▄▄▄▄▄███████▀")

                        if(palabra_secreta == "caracol"):
                            print("__●__ ●")
                            print(" _ █___█")
                            print(" __ █__ █_")
                            print(" __ █__ █")
                            print(" __ ███____________█████ 　　　")
                            print(" _█▒░░█_________██▓▒▒▓██ ☆")
                            print(" █▒░●░░█___ ██▓▒██▓▒▒▓█　　 ★")
                            print(" █░█▒░░██_ ██▓▒██▓▒░▒▓█")
                            print(" _██▒░░██ ██▓▒░██▓▒░▒▓█ 　　　★")
                            print(" ____█▒░██ ██▓▒░░ ████▓█")
                            print(" ___█▒░██__██▓▓▒▒░░░██ 　 ★★")
                            print(" ____█▒░██___████████████")
                            print(" _____█▒░█▒▒▒▒▒▒▒▒▒▒▒▒█")
                            print(" ______██████████████████.•°*”˜҈.•°*”˜҈.")

                        if(palabra_secreta == "cangrejo"):
                           print("░░▄█▀▀▀░░░░░░░░▀▀▀█▄")
                           print("▄███▄▄░░▀▄██▄▀░░▄▄███▄")
                           print("▀██▄▄▄▄████████▄▄▄▄██▀")
                           print("░░▄▄▄▄██████████▄▄▄▄")
                           print("░▐▐▀▐▀░▀██████▀░▀▌▀▌▌")

                        if(palabra_secreta == "pikachu"):
                           print("⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀⠀")
                           print("⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀")
                           print("⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀")
                           print("⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜")
                           print("⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇")
                           print("⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀")
                           print("⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀")
                           print("⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀")
                           print("⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀")
                           print("⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀")
                           print("⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀")
                           print("⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀")
                           print("⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀")
                           print("⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀")
                           print("⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋")

                        if(palabra_secreta == "trofeo"):
                           print("________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ")
                           print("_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ")
                           print("___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ")
                           print("_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ")
                           print("¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶ ")
                           print("¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶") 
                           print("¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶ ")
                           print("¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶ ")
                           print("¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶ ")
                           print("_¶¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶____¶¶¶ ")
                           print("_¶¶¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶__¶¶¶¶ ")
                           print("___¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶ ")
                           print("____¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶ ")
                           print("______¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶ ")
                           print("_______________¶¶¶¶¶¶¶¶¶¶¶¶ ")
                           print("_________________¶¶¶¶¶¶¶¶ ")
                           print("___________________¶¶¶¶ ")
                           print("___________________¶¶¶¶") 
                           print("___________________¶¶¶¶ ")
                           print("___________________¶¶¶¶ ")
                           print("_______________¶¶¶¶¶¶¶¶¶¶¶¶ ")
                           print("____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ")
                           print("____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ")
                           print("____________¶¶¶____________¶¶¶ ")
                           print("____________¶¶¶____________¶¶¶ ")
                           print("____________¶¶¶____________¶¶¶ ")
                           print("____________¶¶¶____________¶¶¶ ")
                           print("____________¶¶¶____________¶¶¶ ")
                           print("____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ")
                           print("____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ")
                           print("__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ")
                           print("_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")

                        if (palabra_secreta == "homero simpson"):
                           print("░░░░░░▄▄▄▄███▄▄▄▄░░░░░░░░░░░░░")
                           print("░░░▄▄█▀░░░░░░░░░▀▀▄▄░░░░░░░░░░")
                           print("░░█▀░░░░░░░░░░░░░░░▀█▄░░░░░░░░")
                           print("░█▀░░░░░░░░░░░░░░░░░░█▄░░░░░░░")
                           print("██░░░░░░░░░░░░░░░░░░░░█▄░░░░░░")
                           print("█░░░░░░░░░░░░░░░░░░░░░░█▄░░░░░")
                           print("██░░░░░░░░░░░░▄▄▄▄▄█▀▀▀██▄░░░░")
                           print("▀█░░░░░░░░░▄█▀▀░░▀▀█▄░░░░█▄░░░")
                           print("░█▄░▄░░░░░▄█░░░░░░░░█▄░█░░█░░░")
                           print("░▄█▄██▄░░░█▄░░██░░░░██▄▄▄██░░░")
                           print("░████░▀▀░░░█▄░░░░░░▄█░░░░░██░░")
                           print("░█░░██▄▄░░░░▀██▄▄██▀▄▄▄▄▄▄█░░░")
                           print("░░▄█▀░░░░░░░░░▄▄██▀▀▀▀▀▀▀░▀█▄░")
                           print("░░▀█░░░░░░░▄█▀▀░░░░░░░░░░░░░█▄")
                           print("░░░▀█▄▄█▀░█▀░░░░░░░░░░░░░░░▄█▀")
                           print("░░░░░░██░▄█░░░█▀██▀▀█▀██▀▀▀▀░░")
                           print("░░░░░▄█░░▀█░░▀█░█░░██░██░░░░░░")
                           print("░░░░██▀█▄░▀█▄░▀▀████▀▀██░░░░░░")
                           print("░░░░█░░░▀▀█▄▀█▄▄▄▄▄▄▄▄██▄░░░░")

                        if (palabra_secreta == "reloj"):
                           print("__________________________________________________")
                           print("_______¶¶¶¶¶___________________________¶¶¶¶_______")
                           print("______¶¶___¶¶¶¶¶¶¶______________¶¶¶¶¶¶¶¶__¶¶______")
                           print("______¶¶¶________¶¶¶__________¶¶¶¶______¶__¶______")
                           print("_____¶¶____________¶¶________¶¶___________¶¶¶_____")
                           print("____¶¶____________¶¶¶_______¶¶¶_____________¶¶____")
                           print("___¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________¶¶____")
                           print("___¶¶______¶¶_¶¶¶¶_____________¶¶¶¶¶_________¶____")
                           print("____¶¶__¶¶¶¶¶________________________¶¶¶____¶¶____")
                           print("____¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶_____")
                           print("_______¶¶¶____¶¶¶_______¶¶_______¶¶¶____¶¶¶¶¶_____")
                           print("______¶¶____¶¶___¶______¶¶______¶__¶¶¶____¶¶______")
                           print("_____¶¶___¶¶_____¶¶____________¶¶____¶¶¶___¶¶_____")
                           print("____¶¶___¶_____________________________¶¶___¶¶____")
                           print("___¶¶___¶__¶____________¶¶___________¶__¶¶___¶¶___")
                           print("__¶¶___¶____¶___________¶¶__________¶____¶¶___¶___")
                           print("__¶¶__¶¶________________¶¶________________¶___¶¶__")
                           print("__¶___¶_________________¶¶_________________¶__¶¶__")
                           print("_¶¶___¶_________________¶¶_________________¶___¶¶_")
                           print("_¶¶___¶_¶¶¶¶¶___________¶¶¶¶¶¶_______¶¶¶¶¶_¶___¶¶_")
                           print("_¶¶___¶____________________________________¶___¶¶_")
                           print("__¶___¶____________________________________¶___¶__")
                           print("__¶¶__¶¶__________________________________¶___¶¶__")
                           print("__¶¶___¶____¶_______________________¶_____¶___¶¶__")
                           print("___¶¶___¶__¶_________________________¶___¶___¶¶___")
                           print("____¶____¶______________________________¶___¶¶____")
                           print("____¶¶____¶______¶______¶¶______¶_____¶¶___¶¶_____")
                           print("_____¶¶¶___¶¶___¶_______¶¶_______¶__¶¶¶___¶¶______")
                           print("_______¶¶___¶¶¶_________¶¶________¶¶¶____¶¶_______")
                           print("________¶¶¶___¶¶¶¶¶¶__________¶¶¶¶¶___¶¶¶_________")
                           print("_______¶¶¶__¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶_¶¶_________")
                           print("______¶¶_______¶¶________________¶¶_____¶¶________")
                           print("______¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶________")
                           print("______¶¶¶______¶¶_______________¶¶______¶¶________")
                           print("________¶¶¶¶¶¶¶¶_________________¶¶¶¶¶¶¶¶_________")

                        if (palabra_secreta == "avion"):
                            print("░░░░░░░░░░░░░░░░░▄█▀▀█▄░░░░░░░░░░░░░░░░░")
                            print("░░░░░░░░░░░░░░░░█▀░░░░▀█░░░░░░░░░░░░░░░░")
                            print("░░░░░░░░░░░░░░░█▀░░▄▄░░▀█░░░░░░░░░░░░░░░")
                            print("░░░░░░░░░░░░░░▄█░▄█▀▀█▄░█▄░░░░░░░░░░░░░░")
                            print("░░░░░░░░░░░░░░█░░▀░░░░▀░░█░░░░░░░░░░░░░░")
                            print("░░░░░░░░▄█▀█░░█░░░░░░░░░░█░░█▀█▄░░░░░░░░")
                            print("░░░░░░░░█░░██▄█░░░░░░░░░░█▄██░░█░░░░░░░░")
                            print("░░░▄▄▄░░█▄▄██▀█░░░░░░░░░░█▀██▄▄█░░▄▄▄░░░")
                            print("░░█░░██▄█▀▀░░░█░░░░░░░░░░█░░░▀▀█▄██░░█░░")
                            print("░░█▄▄█▀▀░░░░░░█░░░░░░░░░░█░░░░░░▀▀█▄▄█░░")
                            print("░▄█▀▀░░░░░░░░░█▄░░░░░░░░▄█░░░░░░░░░▀▀█▄░")
                            print("█▀░░░░░▄▄▄▄▄████░░░░░░░░████▄▄▄▄▄░░░░░░█")
                            print("█▄▄▄█▀▀▀░░░░░░██░░░░░░░░██░░░░░░▀▀▀█▄▄▄█")
                            print("▀▀░░░░░░░░░░░░██░░░░░░░░██░░░░░░░░░░░░▀▀")
                            print("░░░░░░░░░░░░░░░█░░░░░░░░█░░░░░░░░░░░░░░░")
                            print("░░░░░░░░░░░░░░░█░░░░░░░░█░░░░░░░░░░░░░░░")
                            print("░░░░░░░░░░░░░░░█▄▄█▀▀█▄▄█░░░░░░░░░░░░░░░")
                            print("░░░░░░░░░░░░▄▄█▀▀░░░░░░▀▀█▄▄░░░░░░░░░░░░")
                            print("░░░░░░░░░░▄█▀░░░▄▄▄██▄▄▄░░░▀█▄░░░░░░░░░░")
                            print("░░░░░░░░░░█▄▄▄▄▄█▀░░░░▀█▄▄▄▄▄█░░░░░░░░░░")

                        if (palabra_secreta == "pizza"):
                            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░░░░░░░░")
                            print("░░░░░░░░░░░░░░▄▄▄▄▄▄▄▄░░░░░░█████▄░░░░░░")
                            print("░░░░░░░░░▄▄█████████████▀░░▄░░▀████▄░░░░")
                            print("░░░░░░▄▄███▀▀░░▄▄▄▄▄▄░░▀░░████▄░▀████░░░")
                            print("░░░░▄███▀░▄▄██████▀▀███░░▄█▀▀░▀▀▄░▀███▄░")
                            print("░░░▄██▀░▄███▀▀▀███▄▄██░░▄██░░░░░█▄░▀███░")
                            print("░░███░▄██████████████▀░░███▄░░░▄██▄░████")
                            print("░███░▄████░█████░▀██▀░░█████████▀▀▀░░░░░")
                            print("▄██░░██████▀▀███████░░▀▀▀▀▀░░░░░░░░░░░░░")
                            print("███░██████░░░░█████░░░░░░░░░▄▄▄▄░░██░░░░")
                            print("██░░██████▄░░▄█████▄▄▄█████▀▀███░░██░░░░")
                            print("███░███▄░▀█████▀▀███████████████░░██░░░░")
                            print("███░▀██████▀████▄▄█████▄▄███▀███░▄██░░░░")
                            print("░██▄░██████▄▄██████▀▀▀█████▄▄██░░██▀░░░░")
                            print("░▀██▄░▀█▀▀████████░░░░░███████░░██▀░░░░░")
                            print("░░▀██▄░▀███████████▄░▄▄█████▀░▄██▀░░░░░░")
                            print("░░░░▀██▄░░▀███▄▄▄████████▀▀░▄███▀░░░░░░░")
                            print("░░░░░░▀███▄░░▀▀▀▀▀▀▀▀▀▀░░▄▄███▀░░░░░░░░░")
                            print("░░░░░░░░▀▀████▄▄▄▄▄▄▄▄█████▀░░░░░░░░░░░░")
                            print("░░░░░░░░░░░░░▀▀▀▀▀▀▀▀▀▀░░░░░░░░░░░░░░░░░")
                            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                            print("░░░░░░░█████████████████████████░░░░░░░░")
                            print("░░░░░░░█────█───█────█────█────█░░░░░░░░")
                            print("░░░░░░░█─██─██─████──███──█─██─█░░░░░░░░")
                            print("░░░░░░░█────██─███──███──██────█░░░░░░░░")
                            print("░░░░░░░█─█████─██──███──███─██─█░░░░░░░░")
                            print("░░░░░░░█─████───█────█────█─██─█░░░░░░░░")
                            print("░░░░░░░█████████████████████████░░░░░░░░")
                            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")


                        break
                                     
    elif(user_option == 2):
            print("[Tus resultados]\n")
            
            if adivinaste > 1:
                 palabra_plural = palabra_singular +"s"
            else:
                 palabra_plural = palabra_singular
            print(f"Le acertaste: {adivinaste} {palabra_plural}")
            print(f"No lo lograste: {perdiste} veces.\n")
            
            input ("presiona enter para continuar:")
                    
    elif(user_option == 3):
            print ("¡Gracias por jugar!")
            print ("===================================================================================")


