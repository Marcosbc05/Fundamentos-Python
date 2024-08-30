import os, random, time
def limpiar():
     os.system("cls")
def esperarTime(cadena="",s=4):
    print(cadena)
    time.sleep(s)
def esperar(cadena=""):
    wait=input(cadena)
def pos_secuencial(lista,elem):
    pos=None
    i=0
    while pos==None and i<len(lista):
        if lista[i]['pais']==elem: pos=i
        i+=1
    return pos
def ordenar():   
    long=len(paises)-1           
    for i in range(long):
        for j in range(long-i):
            if paises[j]['puntos']<paises[j+1]['puntos']:
                paises[j],paises[j+1]=paises[j+1],paises[j]

def añadir():
    incorrecto=True
    while incorrecto:   
        paisAux=input('Inserte pais clasificado para la Gran Final: ')
        pais=paisAux.upper()
        if  pais=="" or pais==" ": 
            print('Espacio en blanco.')
        elif pos_secuencial(paises,pais)!=None:
            print('Ese país ya ha sido añadido')
        else:
            dic={'pais':pais,'puntos':0}
            paises.append(dic)
            limpiar()
            mostrarPaises()
            print('Pais añadido satisfactoriamente')
            incorrecto=False

def preguntarPaises():
    t=True
    init=True
    while t:
        if init: 
            añadir()
            init=False
        else: 
            if len(paises)<len(votos): añadir()
            else:
                aAux=input('¿Desea añadir otro país (SI/NO): ')
                a=aAux.upper()
                if a!='SI' and a!='NO': 
                    limpiar()
                    mostrarPaises()
                if a=='SI':
                    limpiar()
                    mostrarPaises()
                    añadir()
                if a=='NO': t=False
    limpiar()
    mostrarPaises()
    print(f'Has añadido {len(paises)} países en total')   

def mostrarPaises():
    for i in range(len(paises)):
        print(i+1,'º ',paises[i]['pais'],': ',paises[i]['puntos'])


def votacionJurado():
    paisesVotados=[]
    for i in votos:
        incorrecto=True
        while incorrecto:
            if i==1: 
                p=input('¿A qué país otorga 1 punto?: ')
            else: 
                p=input(f'¿A qué país otorga {i} puntos?: ')
            pos=pos_secuencial(paises,p.upper())
            if pos==None:
                limpiar()
                mostrarPaises()
                print("PAÍS NO VÁLIDO. DEBE INTRODUCIR PAIS VÁLIDO.")
            elif p in paisesVotados:
                limpiar()
                mostrarPaises()
                print("Ese país ya ha sido votado.")
            else:
                paises[pos]['puntos']+=i
                incorrecto=False
                paisesVotados.append(p)
        ordenar()
        limpiar()
        mostrarPaises()

def votacionesJurado():
    cont=0
    k=True
    while k:
        cont+=1
        limpiar()
        mostrarPaises()
        print(f'Paises votando: {cont}')
        votacionJurado()
        while True:
            pregAux=input('¿Desea seguir votando? (SI/NO): ')
            preg=pregAux.upper()
            if preg=='NO': 
                k=False
                break
            elif preg=='SI': 
                k=True
                break
            limpiar()
            mostrarPaises()
    limpiar()
    mostrarPaises()
    if cont==1: print('LA VOTACION DEL JURADO HA FINALIZADO TRAS 1 VOTACIÓN')
    else: print('LA VOTACION DEL JURADO HA FINALIZADO TRAS',cont,'VOTACIONES')
    print('\nEl ganador de los jurados profesionales es ',paises[0]['pais'],'con',paises[0]['puntos'],'puntos')
    return cont


def orden_burbuja_asc(lista):   
    long=len(lista)-1           
    for i in range(long):
        for j in range(long-i):
            if lista[j]['puntos']>lista[j+1]['puntos']:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista

def getTelevotos():
    pts=[0]*len(paises)
    for i in range(cont):
        previa=[-1]
        for points in votos:
            while True:
                pos=random.randint(0,len(paises)-1)
                if not pos in previa: break
            previa.append(pos)
            pts[pos]+=points
    return pts

def ejecutarTelevoto(totTel):
    paises2=orden_burbuja_asc(paises)
    jury=[]
    for m in range(len(paises)):
        add=paises2[m]['pais']
        jury.append(add)

    for ñ in range(len(jury)):
        limpiar()
        ordenar()
        mostrarPaises()
        print('\n--->',jury[ñ])
        esperarTime('...',2)
        tele=getTelevotos()[ñ]
        totTel+=tele
        puesto=pos_secuencial(paises,jury[ñ])
        if jury[ñ]==jury[len(jury)-1]: 
            print('\nULTIMO PAIS EN RECIBIR TELEVOTO')
            esperarTime('ATENCION...')
            if paises[0]['puntos']-paises[puesto]['puntos']==0:
                print('Necesita 0 puntos, ya ha ganado independientemente del televoto')
            elif paises[0]['puntos']-paises[puesto]['puntos']>((len(paises)*12)-(totTel-tele)): print('YA ES IMPOSIBLE ALCANZAR ESA CIFRA')
            else:
                print('Necesita',(paises[0]['puntos']-paises[puesto]['puntos'])+1,'puntos')
            esperarTime('...')
        print(jury[ñ],'recibe',tele,'puntos')
        esperarTime("",2)
        puesto=pos_secuencial(paises,jury[ñ])
        paises[puesto]['puntos']+=tele
        paises[puesto]['pais']='>'+paises[puesto]['pais']
        ordenar()
        limpiar()
        mostrarPaises()
        esperarTime("",2)
    return totTel

#EJECUCION:
totTel=0
paises=[]
votos=[1,2,3,4,5,6,7,8,10,12]
limpiar()
print("Bienvenido a My Voting ESC")
print(f"El sistema de puntuación es: {votos}")
esperar("\nPulse Enter para iniciar")
if len(paises)<len(votos):
    limpiar()
    preguntarPaises()
esperarTime("\niniciando votación...",2)
limpiar()
esperarTime("SO, START VOTING NOW",2)
mostrarPaises()
cont=votacionesJurado()
esperarTime('\nAHORA VAMOS CON EL TELEVOTO...')
totTel=ejecutarTelevoto(totTel)
esperarTime('LA VOTACION HA FINALIZADO',2)
print('\nEl ganador es ',paises[0]['pais'].replace('>',''),'con',paises[0]['puntos'],'puntos')
print('\nTOT JURADO: ',cont*(sum(votos)))
print('TOT TELE: ',totTel)