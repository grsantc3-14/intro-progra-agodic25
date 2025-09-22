
saldo=1000
print("---- Bienvenido al Banco Maya ---")
operación =input ("-°-°-°- Menú de operaciones a realizar -°-°-°-}" \
"\n1. Consultar Saldo" \
"\n2. Retirar" \
"\n3. Depositar" \
"\n4. Salir" \
"\nPor favor Selecione una opcion ")



if operación=="1":
    print(f"Tu saldo actual es {saldo} pesos")

elif operación=="2":
    retiro=float (input("Selecione la cantidad a retirar" \
        "\nTengo Billetes de " \
        "\n100 pesos" \
        "\n200 pesos" \
        "\n500 pesos"\
        "\nSeleccione la cantidad a retirar: "))
    
    if (saldo<retiro):
        
        print("Lo siento tu saldo es insuficiente")

    elif (retiro%100==0 and retiro<=saldo):
        print (f"Su retiro es de {retiro} pesos")
        nuevoSaldo=saldo-retiro
        print(f"Tu nuevo saldo es {nuevoSaldo} pesos")
    else:
        print ("Lo siento no tengo billetes de esa denominación")
    
elif operación=="3":
    deposito=float(input("Selecione la cantidad a depositar" \
        "\nIngrese Billetes de " \
        "\n100 pesos" \
        "\n200 pesos" \
        "\n500 pesos"\
        "\nAsegurate de ingresar billetes en buenas condiciones: "))
    
    print(f"Su deposito es de {deposito}")
    

    if (deposito%100==0 and deposito>=100):
        nuevoDeposito=saldo+deposito
        print(f"Tu nuevo saldo es {nuevoDeposito}")
    else:
        print ("Lo siento no se pueden realizar depositos esa denominación")
        
elif  operación=="4":
    print("Usted ha salido del Menu")

else:
    print("No conozco esa operación")