#from math import * #Nos importamos toda la librería
import math 


print("---- Bienvenida a mi Calculadora de Figuras ---")
print("-°-°-°- Menú de figuras -°-°-°-")
print("1. Cubo")
print("2. Prisma")
print("3. Pirámide")
print("4. Cilindro")
print("5. Cono")
print("6. Esfera")

figura = input("Figura (1-6): ")

print("-°-°-°- Menú de opciones -°-°-°-")
print("1. Calcular el área")
print("2. Calcular el volumen")
print("3. Calcular ambos")
print("4. Salir")

opción = input("Opción (1-4): ")

##Cubo
if figura == "1": ##Cubo
    if opción == "1":##Calcular area
        
        lado = float (input("Lado (cm):"))
        areaCubo = 6*lado**2
        print(f"El área del cubo es: {areaCubo:.2} cm")

    elif opción == "2":##Calcular Volumen
        
        lado = float(input("Lado (cm):"))
        volumenCubo = lado**3
        print(f"El volumen del cubo es: {volumenCubo:.2} cm")

    elif opción == "3":##Calcular ambos
        
        lado = float(input("Lado (cm):"))
        areaCubo = 6*lado**2
        print(f"El área del cubo es: {areaCubo:.2} cm")
        volumenCubo = lado**3
        print(f"El volumen del cubo es: {volumenCubo:.2} cm")

    elif opción == "4":
        print ("Usted ha salido del sistema")
    else:
        print("No conozco esa figura. ")

##Prisma
elif figura == "2": ##Prisma
    
    if opción == "1": ##Calcular area
        ladoAncho = float (input("Lado Ancho (cm): "))
        ladoBase = float (input("Lado Base (cm): "))
        ladoLargo=float (input("Lado Largo (cm): "))
        areaPrisma = 2*(ladoBase*ladoAncho+ladoLargo*ladoAncho+ladoBase*ladoAncho)
        print(f"El área del prisma es: {areaPrisma:.2} cm")
        
    elif opción == "2":##Calcular Volumen
        ladoAncho = float (input("Lado Ancho (cm):"))
        ladoBase = float (input("Lado Base (cm):"))
        ladoLargo=float (input("Lado Largo (cm):"))
        vulumenPrisma=(ladoAncho*ladoBase*ladoLargo)
        print(f"El volumen del prisma es: {vulumenPrisma:.2} cm")

    elif opción == "3":##Calcular ambos
        ladoAncho = float (input("Lado Ancho (cm):"))
        ladoBase = float (input("Lado Base (cm):"))
        ladoLargo=float (input("Lado Largo (cm):"))
        areaPrisma = 2*(ladoBase*ladoAncho+ladoLargo*ladoAncho+ladoBase*ladoAncho)
        print(f"El área del prisma es: {areaPrisma:.2} cm")
        vulumenPrisma=(ladoAncho*ladoBase*ladoLargo)
        print(f"El volumen del prisma es: {vulumenPrisma:.2} cm")

    elif opción == "4":
        print ("Usted ha salido del sistema")

    else:
        print("No conozco esa figura. ")

##Piramide
elif figura == "3": ##Piramide

    if opción == "1": #Area
        lado = float(input("Lado de piramide cuadrangular (cm): "))
        alturaPiram=float(input ("Algura de la piramide (cm): " ))
        areaBase = lado*lado
        areaPiramide = 4*[(lado*alturaPiram)/2]+areaBase

        print(f"El área de la Piramide Cadrangular es: {areaPiramide:.2} cm")
        

       
    elif opción == "2": ##Calcular Volumen
        lado = float(input("Lado de piramide cuadrangular (cm): "))
        alturaPiram=float(input ("Algura de la piramide (cm): " ))
        areaBase = lado*lado

        volumenPiramide = (areaBase*alturaPiram)/3
        print(f"El volumen de la piramide es: {volumenPiramide:.2} cm")


    elif opción == "3": ##Calcular ambos
        lado = float(input("Lado de piramide cuadrangular (cm): "))
        alturaPiram=float(input ("Algura de la piramide (cm): " ))
        areaBase = lado*lado

        areaPiramide = 4*[(lado*alturaPiram)/2]+areaBase
        print(f"El área de la Piramide Cadrangular es: {areaPiramide:.2} cm")

        volumenPiramide = (areaBase*alturaPiram)/3
        print(f"El volumen de la piramide es: {volumenPiramide:.2} cm")

    elif opción == "4":
        print ("Usted ha salido del sistema")

    else:
        print("No conozco esa figura. ")

##Cilindro
elif figura == "4": ##Cilindro

    if opción == "1": ##Calcular area
        radio= float(input("Radio de base de Cilindro (cm): "))
        alturaCilindro= float(input("Altura de Cilindro (cm): "))

        areaCilindro=2*math.pi*(radio**2)+2*math.pi*radio*alturaCilindro
        print(f"El área de un Cilindro es: {areaCilindro:.2} cm")
        

    elif opción == "2": ##Calcular Volumen
        
        radio= float(input("Radio de base de Cilindro (cm): "))
        alturaCilindro= float(input("Altura de Cilindro (cm): "))

        volumenCilindro=math.pi*(radio**2)*alturaCilindro
        print(f"El volumen de un Cilindro es: {volumenCilindro:.2} cm")

    elif opción == "3": ##Calcular ambos
        radio= float(input("Radio de base de Cilindro (cm): "))
        alturaCilindro= float(input("Altura de Cilindro (cm): "))

        areaCilindro=2*math.pi*(radio**2)+2*math.pi*radio*alturaCilindro
        volumenCilindro=math.pi*(radio**2)*alturaCilindro

        print(f"El área de un Cilindro es: {areaCilindro:.2} cm")
        print(f"El volumen de un Cilindro es: {volumenCilindro:.2} cm")
    

    elif opción == "4":
        print ("Usted ha salido del sistema")

    else:
        print("No conozco esa figura. ")

##Cono
elif figura == "5": ##Cono
    if opción == "1": ##Calcular area
        
        radio= float(input("Radio de base de Cono (cm): "))
        generatriz= float(input("Generatriz de Cono (cm): "))
        áreaCono=math.pi*(radio**2)+math.pi*radio*generatriz

        print(f"El área del Cono es: {áreaCono:.2}")

    elif opción == "2": ##Calcular Volumen
        
        radio= float(input("Radio de base de Cono (cm): "))
        generatriz= float(input("Generatriz de Cono (cm): "))
        alturaCono=float(input("Altura de Cono (cm): "))
        volumenCono=(math.pi*(radio**2)*alturaCono)/3

        print(f"El volumen del Cono es: {volumenCono:.2}")

    elif opción == "3": ##Calcular ambos
        
        radio= float(input("Radio de base de Cono (cm): "))
        generatriz= float(input("Generatriz de Cono (cm): "))
        alturaCono=float(input("Altura de Cono (cm): "))
        áreaCono=math.pi*(radio**2)+math.pi*radio*generatriz
        volumenCono=(math.pi*(radio**2)*alturaCono)/3
        
        print(f"El área del Cono es: {áreaCono:.2}")
        print(f"El volumen del Cono es: {volumenCono:.2}")
        

    elif opción == "4":
        print ("Usted ha salido del sistema")

    else:
        print("No conozco esa figura. ")

##Esfera
elif figura == "6": ##Esfera
    if opción == "1": ##Calcular area
        
        radio= float(input("Radio de la Esfera (cm): "))
        areaEsfera = 4*math.pi*radio**2
        print(f"El área de la Esfera es: {areaEsfera:.2}")

    elif opción == "2": ##Calcular Volumen
        
        radio= float(input("Radio de la Esfera (cm): "))
        volumenEsfera=(4/3)*math.pi*radio**3
        print(f"El volumen de la Esfera es: {volumenEsfera:.2}")

    elif opción == "3": ##Calcular ambos
        radio= float(input("Radio de la Esfera (cm): "))
        areaEsfera = 4*math.pi*radio**2
        volumenEsfera=(4/3)*math.pi*radio**3

        print(f"El área de la Esfera es: {areaEsfera:.2}")
        print(f"El volumen de la Esfera es: {volumenEsfera:.2}")
    elif opción == "4":
        print ("Usted ha salido del sistema")

    else:
        print("No conozco esa figura. ")
    
else:
    print("Opción incorrecta, adiós. =D")