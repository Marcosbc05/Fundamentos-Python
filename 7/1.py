fechas=[{'año':2016,'mes':5,'día':14},{'año':2021,'mes':12,'día':19},{'año':2017,'mes':6,'día':3},
        {'año':2018,'mes':9,'día':27},{'año':2012,'mes':11,'día':24},
        {'año':2020,'mes':10,'día':28},{'año':2005,'mes':12,'día':17}]
def buscar(fechas,categoria,elem):
    if categoria=='mes':
        pos=None
        i=0
        while pos==None and i<len(fechas):
            if fechas[i]['mes']==elem: pos=i
            i+=1
    elif categoria=='año':
        pos=None
        i=0
        while pos==None and i<len(fechas):
            if fechas[i]['año']==elem: pos=i
            i+=1        
    elif categoria=='día':
        pos=None
        i=0
        while pos==None and i<len(fechas):
            if fechas[i]['día']==elem: pos=i
            i+=1
    print('La fecha buscada por categoria:',categoria,':',elem,'es',fechas[pos]['día'],'/',fechas[pos]['mes'],'/',fechas[pos]['año'])
buscar(fechas,'mes',12)

def orden_año(fechas):
    for i in range(1,len(fechas)):
        actual=fechas[i]
        indice=i
        while indice>0 and actual['año']<fechas[indice-1]['año']:
            fechas[indice]=fechas[indice-1]
            indice-=1
        fechas[indice]=actual
    for i in range(len(fechas)):
        print(fechas[i]['día'],'/',fechas[i]['mes'],'/',fechas[i]['año'])
orden_año(fechas)