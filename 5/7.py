gasto_gas=[]
gasto_tienda=[]
gasto_total=[]
for i in range(10):
    a=int(input(f'Inserte gasto en gasolina del cliente nº{i}: '))
    gasto_gas.append(a)
for j in range(10):
    b=int(input(f'Inserte gasto en tienda del cliente nº{j}: '))
    gasto_tienda.append(b)
gasto_total=[]
for i in range(10):
    c=gasto_gas[i]+gasto_tienda[i]
    gasto_total.append(c)
for i in range(10):
    print(f'El gasto del cliente nº{i} es {gasto_gas[i]}€ en gasolina, {gasto_tienda[i]} € en la tienda y en total son {gasto_total[i]} €')
    
gastos={'gas':gasto_gas,'tienda':gasto_tienda,'total':gasto_gas}
print(gastos)