#Juegos

from random import choice

#Código para un juego del ahorcado,
#DEF Los colores junto con la palabra "_" y la palabra Jugar
#DEF Acceder a una sola variable de DEF FuncionColor
#DEF Ciclo while de iteracion de letras
#DEF Ciclo grande para anidar demas funciones
#
contador=0
vidas=3
continuar="s"

def funcionColor ():
    colores=["rojo", "azul", "amarillo", "verde", "negro", "blanco", "naranja", "rosa", "gris", "violeta"]
    palabraJugar=choice(colores) #Elije una palabra al azar
    #print(f"\n{palabraJugar}") #Debugging
    palabraGuion=["_"]*len(palabraJugar)
    return palabraJugar, palabraGuion


def cicloWhile():
    global vidas
    global palabraJugar, palabraGuion
    while vidas>0: #Itera la cantidad de letras en la palabra
        print(" ".join(palabraGuion))
        print(f"\nTienes {vidas} vidas restantes")
        if "_" not in palabraGuion:
            print(f"Has adivinado la palabra: {"".join(palabraGuion)+"\n"}")
            return True
        letraAdiv=input(f"\nEscribe una letra de la palabra secreta: ").lower() #Entrada de letra de usuario
        print(f"\nElejiste la letra {letraAdiv}") #Prueba de error
        if letraAdiv in palabraJugar:
            for indice in range(len(palabraJugar)):
                if palabraJugar[indice]==letraAdiv:
                    palabraGuion[indice]=letraAdiv
        else:
            vidas-=1
            print ("X Letra incorrecta")
    if vidas==0:
        print (f"\nJuego Terminado, se acabaron tus vidas. La palabra correcta era {palabraJugar}) ")
        return False
    return False

def whileRondas ():
    global contador
    global continuar
    global vidas, palabraJugar, palabraGuion
    while continuar=="s":
        contador+=1
        print(f"\nComienza la ronda: {contador}")
        vidas=3
        palabraJugar, palabraGuion =funcionColor()
        print("\nAhora adivina la palabra secreta: ")
        cicloWhile()
        continuar=input("\nQuieres seguir jugando (s/n): ").lower()
    print("Elejiste salir del juego, gracias")
    return
    
whileRondas ()