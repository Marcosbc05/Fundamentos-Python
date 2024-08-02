n1= input('inserte número: ')
n2= input('inserte número: ')
n3= input('inserte número: ')
try:
    int(n1)
    int(n2)
    int(n3)
except:
    print('valores no válidos, inserte números enteros')
else:
    if n1<n2<n3:
        print(f'{n1},{n2},{n3}')
    elif n1<n3<n2:
        print(f'{n1},{n3},{n2}')
    elif n2<n1<n3:
        print(f'{n2},{n1},{n3}')
    elif n2<n3<n1:
        print(f'{n2},{n3},{n1}')
    elif n3<n2<n1:
        print(f'{n1},{n2},{n3}')
    elif n3<n1<n2:
        print(f'{n3},{n1},{n2}')