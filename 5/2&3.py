persona1={'Nombre':'Marcos','Edad':17,'Sexo':'M'}
persona2={'Nombre':'Laura','Edad':15,'Sexo':'F'}
persona3={'Nombre':'Pepi','Edad':70,'Sexo':'F'}
persona4={'Nombre':'Carlos','Edad':76,'Sexo':'M'}
persona5={'Nombre':'Olivia','Edad':14,'Sexo':'F'}
persona6={'Nombre':'Benjamin','Edad':53,'Sexo':'M'}
persona7={'Nombre':'Chanel','Edad':13,'Sexo':'F'}
persona8={'Nombre':'Eustaquio','Edad':93,'Sexo':'M'}
persona9={'Nombre':'Eva','Edad':29,'Sexo':'F'}
persona10={'Nombre':'Simón','Edad':31,'Sexo':'M'}
datos=[persona1,persona2,persona3,persona4,persona5,persona6,persona7,persona8,persona9,persona10]
#media general
suma=0
for i in range(len(datos)):
    suma+=datos[i]['Edad']
media=suma/len(datos)
print(f'Media general: {media}')
#media por sexo
suma_m=0
suma_f=0
m=0
f=0
for i in range(len(datos)):
    if datos[i]['Sexo']=='M':
        suma_m+=datos[i]['Edad']
        m+=1
    if datos[i]['Sexo']=='F':
        suma_f+=datos[i]['Edad']
        f+=1
print(f'Media masculina: {suma_m/m}')
print(f'Media femenina: {suma_f/f}')
#mujeres entre 13 y 16 años
contador=0
for i in range(len(datos)):
    if datos[i]['Sexo']=='F':
        if datos[i]['Edad']<=16 and datos[i]['Edad']>=13:
            contador+=1
print(f'Mujeres entre 13 y 16 años: {contador}')
#hombre menores 20 años
contador=0
for i in range(len(datos)):
    if datos[i]['Sexo']=='M':
        if datos[i]['Edad']<20:
            contador+=1
print(f'Hombres de menos de 20 años: {contador}')
#ampliación ejercicio 3 (mostras datos del hombre y mujer menores)
menor=200
for i in range(len(datos)):
    if datos[i]['Sexo']=='M':
        if datos[i]['Edad']<menor:
            menor=datos[i]['Edad']
for i in range(len(datos)):
    if datos[i]['Edad']==menor:
        print(f'Los datos completos del hombre menor son: {datos[i]}')
menor=200
for i in range(len(datos)):
    if datos[i]['Sexo']=='F':
        if datos[i]['Edad']<menor:
            menor=datos[i]['Edad']
for i in range(len(datos)):
    if datos[i]['Edad']==menor:
        print(f'Los datos completos de la mujer menor son: {datos[i]}')