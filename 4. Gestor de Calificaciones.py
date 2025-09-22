

##Gestor de Calificaciones
#Crea un programa que gestione calificaciones de tres parciales.
#Opciones: calcular promedio, calcular calificación final con ponderaciones, 
# mostrar mayor y menor calificación, verificar si el alumno aprueba o reprueba.

#El programa debe pedir las calificaciones solo cuando se necesiten.
#El usuario deberá proveer las tres calificaciones de los parciales
#y además pide las ponderaciones p.ej. 30% + 30% + 40%, 
# de modo que puedas calcular tus calificaciones según la materia y sus ponderaciones.


menú=input("-.-.-.Bienvenido al Gestor de Calificaciones.-.-.- " \

"\n                                           " \
"\n-.-.-.Menú.-.-.-" \
"\n1. Promedio" \
"\n2. Calificación final con ponderaciones, Aprobado/Reprobado" \
"\n3. Mostrar mayor y menor calificación" \
"\n4. Salir "\
"\nA continuación elige una opción: ")

materia=input("Ingrese el nombre de la materia: ")
calif1=float(input("Ingrese su primer Calificación: "))
calif2=float(input("Ingrese su segunda Calificación: "))
calif3=float(input("Ingrese su tercer Calificación: "))



if menú=="1": #calcular promedio
    sumaT=calif1+calif2+calif3
    promedio=sumaT/3
    print(f"Su promedio es {promedio}")

elif menú=="2": #calificación final con ponderaciones, Aprobado/Reprobado
    print ("Continue las instrucciones")
    pond1=input("Ingresa la primer ponderación en %: ")
    pond2=input("Ingresa la segunda ponderación en %: ")
    pond3=input("Ingresa la tercer ponderación en %: ")

    califFinal=calif1*(pond1/100)+calif2*(pond2/100)+calif3*(pond3/100)
    if califFinal>=7:
        print(f"Felicidades su calificación final de {materia} es {califFinal}, Aprobado")
    else:
        print(f"Lo sentimos su calificación final de {materia} es {califFinal}, Reprobado")

elif menú=="3": #mayor y menor calificación
    máximo =max(calif1, calif2, calif3)
    mínimo =min(calif1, calif2, calif3)
    print(f"En {materia} su calificación máxima es {máximo}, y la mínima {mínimo}")

elif menú=="4": #Salir
    print("Usted a salido del sistema")

else:
    print("Lo siento no conzco esa opción")