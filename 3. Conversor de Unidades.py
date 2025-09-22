##Conversor de Unidades
#Crea un menú que convierta diferentes unidades.
#Menú:
#Temperatura: Celsius → Fahrenheit
#Temperatura: Fahrenheit → Celsius
#Longitud: Metros → Centímetros
#Longitud: Centímetros → Metros
#Masa: Kilogramos → Gramos
#Masa: Gramos → Kilogramos
#Salir
#El usuario elige el tipo de conversión, ingresa el valor y recibe el resultado.

menú=input("-.-.-.Bienvenido al Conversor de Unidades.-.-.-" \
"\n1. Temperatura: Celsius → Fahrenheit" \
"\n2. Temperatura: Fahrenheit → Celsius" \
"\n3. Longitud: Metros → Centímetros"\
"\n4. Longitud: Centímetros → Metros"\
"\n5. Masa: Kilogramos → Gramos"\
"\n6. Masa: Gramos → Kilogramos"\
"\n7. Salir"\
"\nPor favor seleccione una opción: ")

#    farenheit=(gradosCel*(9/5)) + 32

if menú=="1": #Temperatura: Celsius → Fahrenheit
    gradosCel=float(input("Ingrese grados Celcius: "))
    farenheit=(gradosCel*(9/5)) + 32
    print(f"Grados Farenheit: {farenheit}")


elif menú=="2": #Temperatura: Fahrenheit → Celsius
    gradosFar=float(input("Ingrese grados Farenheit: "))
    celsius=(gradosFar-32)*5/9
    print(f"Grados Celcius: {celsius}")
    
elif menú=="3": #Longitud: Metros → Centímetros
    metros=float(input("Ingrese Metros: "))
    cent=metros*100
    print(f"Distancia en Centímetros: {cent}")

elif menú=="4": #Longitud: Centímetros → Metros
    centi=float(input("Ingrese Centímetros: "))
    metro=centi/100
    print(f"Distancia en Metros: {metro}")

elif menú=="5": #Masa: Kilogramos → Gramos
    kg=float(input("Ingrese masa en Kilogramos: "))
    gramos=kg*1000
    print(f"Masa en Gramos: {gramos}")

elif menú=="6": #Masa: Gramos → Kilogramos
    gramos=float(input("Ingrese masa en Gramos: "))
    kg=gramos/1000
    print(f"Masa en Kilogramos: {kg}")

elif menú=="7": #Salir
    print("Usted a salido de la operación")
else:
    print("Opción incorrecta, adiós. =D")
