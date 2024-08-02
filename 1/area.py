lado= ""
while(lado!=0):
    try:
        lado= int(input("introduce el lado del cuadrado ('0' para salir): "))
        area = pow(lado, 2)
        if(lado!=0):
            print ('el area del cuadrado es', area, 'metros cuadrados')  
    except:
        print("Formato de numero introducido no valido")