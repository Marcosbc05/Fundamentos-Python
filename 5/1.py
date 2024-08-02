datos={}
datos['Nombre']='Pepe'
datos['Sexo']='Masculino'
datos['Edad']=62
print(datos)
print(datos['Edad'])
print(datos.keys())
print(datos.values())

def leer_datos(datos):
    for i in datos:
        print(f'{i}: {datos[i]}',end=', ')
print(leer_datos(datos))

def mostrar_datos(datos):
    for i in datos:
        print(datos[i],end=',')
print(mostrar_datos(datos))
print(datos)
