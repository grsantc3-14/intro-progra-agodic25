##Tienda / Cotizador Simple
#Crea un programa que simule compras en una tienda.
#Opciones: calcular el total con IVA, calcular total con descuento + IVA, 
# calcular precio unitario dado un total y cantidad, o salir.
#El usuario ingresa precios y cantidades según la opción.
#Investiga cómo se aplica el IVA y cómo calcular descuentos.
#Para (1) y (2), pedir precio y cantidad; calcular subtotal, IVA, total.
#Para (2) aplicar primero descuento, luego IVA. 
# El descuento deberá ingresarse por el usuario como si fuera un cupón con los siguientes valores:
#VERANO = 10%
#SALDOS = 35%
#BBVA = 5%
#BANORTE25 = 25%
#Para (3) pedir total y cantidad; devolver unitario con 2 decimales.


menú=input("-.-.-.Bienvenido al AutoCajero.-.-.- " \
"\n " \
"\n-.-.-.Menú.-.-.-" \
"\n1. Calcular el total con IVA (Sin descuento)" \
"\n2. Calcular total con descuento + IVA" \
"\n3. Calcular precio unitario, Total con descuento y cantidad" \
"\n4. Salir "\
"\n "\
"\nA continuación elige una opción: ")

descuento=input("Elija su tipo de descuento o cupón" 
"\n1. VERANO = 10% "\
"\n2. SALDOS = 35%"\
"\n3. BBVA = 5% "\
"\n4. BANORTE25 = 25%")


print("Por favor siga las instrucciones")
producto1=float(input("Ingrese el precio de su primer producto: "))
cantidad1=float(input("Ingrese la cantidad de su primer producto: "))

producto2=float(input("Ingrese el precio de su primer producto: "))
cantidad2=float(input("Ingrese la cantidad de su primer producto: "))

producto3=float(input("Ingrese el precio de su primer producto: "))
cantidad3=float(input("Ingrese la cantidad de su primer producto: "))

if menú=="1": #Calcular el total con IVA (Sin descuento)
    totalCom=float(producto1*cantidad1 + producto2*cantidad2 + producto3*cantidad3)*1.16
    print(f"El total de su compra es {totalCom}, IVA incluido, sin descuento")

elif menú=="2": #Calcular total con descuento + IVA
    totalCom=float(producto1*cantidad1 + producto2*cantidad2 + producto3*cantidad3)*1.16

    if descuento=="1": #VERANO = 10% 
        totalDesc=totalCom*0.9
        totalIVA=totalCom*0.16
        print(f"El IVA de su compra es {totalIVA} pesos")
        print(f"El total de su compra es {totalDesc} pesos, IVA incluido, con descuento VERANO")

    elif descuento=="2": #SALDOS = 35%
        totalDesc=totalCom*0.65

        totalIVA=totalCom*0.16
        print(f"El IVA de su compra es {totalIVA} pesos")

        print(f"El total de su compra es {totalDesc} pesos, IVA incluido, con descuento SALDOS")

    elif descuento=="3": #BBVA = 5%
        totalDesc=totalCom*0.95

        totalIVA=totalCom*0.16
        print(f"El IVA de su compra es {totalIVA} pesos")
        print(f"El total de su compra es {totalDesc} pesos, IVA incluido, con descuento BBVA")

    else: #BANORTE25 = 25%
        totalDesc=totalCom*0.25

        totalIVA=totalCom*0.16
        print(f"El IVA de su compra es {totalIVA} pesos")
        print(f"El total de su compra es {totalDesc} pesos, IVA incluido, con descuento BANORTE25")


elif menú=="3": #Calcular precio unitario, Total con descuento y cantidad
    totalCom=float(producto1*cantidad1 + producto2*cantidad2 + producto3*cantidad3)*1.16

    if descuento=="1": #VERANO = 10% 
        totalDesc=totalCom*0.9

        precio1=producto1*cantidad1*0.9
        precio2=producto2*cantidad2*0.9
        precio3=producto2*cantidad2*0.9
        print(f"El precio unitario de su primer producto es: {precio2} pesos, con {cantidad1}")
        print(f"El precio unitario de su primer producto es: {precio2} pesos, con {cantidad2}")
        print(f"El precio unitario de su primer producto es: {precio3} pesos, con {cantidad3}")

        print(f"El total de su compra es {totalDesc}, IVA incluido, con descuento VERANO")

    elif descuento=="2": #SALDOS = 35%
        totalDesc=totalCom*0.65

        precio1=producto1*cantidad1*0.65
        precio2=producto2*cantidad2*0.65
        precio3=producto2*cantidad2*0.65

        print(f"El precio unitario de su primer producto es: {precio2} pesos, con {cantidad1} unidades")
        print(f"El precio unitario de su primer producto es: {precio2} pesos, con {cantidad2} unidades")
        print(f"El precio unitario de su primer producto es: {precio3} pesos, con {cantidad3} unidades")

        print(f"El total de su compra es {totalDesc}, IVA incluido, con descuento SALDOS")

    elif descuento=="3": #BBVA = 5%
        totalDesc=totalCom*0.95

        precio1=producto1*cantidad1*0.95
        precio2=producto2*cantidad2*0.95
        precio3=producto2*cantidad2*0.95

        print(f"El precio unitario de su primer producto es: {precio2} pesos, con {cantidad1}")
        print(f"El precio unitario de su primer producto es: {precio2} pesos, con {cantidad2}")
        print(f"El precio unitario de su primer producto es: {precio3} pesos, con {cantidad3}")

        print(f"El total de su compra es {totalDesc}, IVA incluido, con descuento BBVA")

    else: #BANORTE25 = 25%
        totalDesc=totalCom*0.75

        precio1=producto1*cantidad1*0.75
        precio2=producto2*cantidad2*0.75
        precio3=producto2*cantidad2*0.75

        print(f"El precio unitario de su primer producto es: {precio2} pesos, con {cantidad1}")
        print(f"El precio unitario de su primer producto es: {precio2} pesos, con {cantidad2}")
        print(f"El precio unitario de su primer producto es: {precio3} pesos, con {cantidad3}")

        print(f"El total de su compra es {totalDesc}, IVA incluido, con descuento BANORTE25")

elif menú=="4": #Salir
    print("Usted salio del sistema" \
    "\nBuen dia")
    
else:
    print("Lo siento esa opcion no exista, intente de nuevo")