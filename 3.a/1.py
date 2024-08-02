x=input('inserte valor de compra: ')
try:
    valor=float(x)
except:
    print('introduca solo números con decimales')
else:
    if valor>100:
        print(round((valor*0.95),3))
    else:
        print(valor*0.98)