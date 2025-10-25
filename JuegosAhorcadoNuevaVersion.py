#Juegos

from random import choice


#Código para un juego del ahorcado,
#Utilizar una lista para almacenar las palabras que serán utilizadas en el juego,
#La función choice de la librería random para elegir una palabra distinta cada vez que el juego se ejecute.
#Además, se deberá presentar en pantalla una serie como esta: _ _ _ _ _ _ _ _ _ 
#donde le dará al usuario la idea de cuántas letras forman la palabra secreta. 
#El usuario podrá ingresar letra por letra y el sistema mostrará si es el caso la letra encontrada, 
#si no lo es, restará una vida, en este juego el usuario cuenta con 3 vidas. 


colores=["rojo", "azul", "amarillo", "verde", "negro", "blanco", "naranja", "rosa", "gris", "violeta"]
contador=0
vidas=3
continuar="s"


while continuar=="s":
    contador+=1
    print(f"\nComienza la ronda: {contador}")
    palabraJugar=choice(colores) #Elije una palabra al azar
    #print(f"\n{palabraJugar}") #Debugging

    print("\nAhora adivina la palabra secreta: ")
    palabraGuion=["_"]*len(palabraJugar) #Crea la palabra con "_", necesitamos que sea una lista, para reemplazar la letra

    while vidas>0: #Itera la cantidad de letras en la palabra
        print(" ".join(palabraGuion))
        print(f"\nTienes {vidas} vidas restantes")
        letraAdiv=input(f"\nEscribe una letra de la palabra secreta: ") #Entrada de letra de usuario

        print(f"\nElejiste la letra {letraAdiv}") #Prueba de error
            
        if letraAdiv in palabraJugar:
            for indice in range(len(palabraJugar)):
                if palabraJugar[indice]==letraAdiv:
                    palabraGuion[indice]=letraAdiv
        else:
            vidas-=1
        
        if "_" not in palabraGuion:
            print(f"Has adivinado la palabra: {"".join(palabraGuion)+"\n"}")
            break

    if vidas==0:
        print("\nJuego Terminado, se acabaron tus vidas :) ")
        break
    
    continuar=input("\nQuieres seguir jugando (s/n): ")
    if continuar !="s" :
        print("Elejiste salir del juego, gracias")
        break
