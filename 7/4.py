productos=[{'nombre':'pan','precio':0.85,'cantidad':34},{'nombre':'pizza','precio':8,'cantidad':7},{'nombre':'patatas','precio':2,'cantidad':15},{'nombre':'regalices','precio':0.3,'cantidad':85},{'nombre':'donuts','precio':3,'cantidad':20},]
def producto_nuevo(productos,nombre,precio,cantidad):
    nuevo={'nombre':nombre,'precio':precio,'cantidad':cantidad}
    productos.append(nuevo)
    return productos
print(producto_nuevo(productos,input('inserte nombre: '),int(input('precio: ')),int(input('cantidad: '))))
def buscar(productos,elem):
    pos=None
    i=0
    while pos==None and i<len(productos):
        if productos[i]['nombre']==elem:
            pos=i
            return productos[pos]
        i+=1
print(buscar(productos,input('Producto buscado: ')))
def orden_precio(productos):
    long=len(productos)-1
    for i in range(long):
        for j in range(long-i):
            if productos[j]['precio']>productos[j+1]['precio']:
                productos[j],productos[j+1]=productos[j+1],productos[j]
    return productos
print(orden_precio(productos))