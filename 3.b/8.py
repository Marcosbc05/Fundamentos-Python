print('_____Tablas de multiplicar______')
print('-------------------------------')
print(' ', end=' ')
for i in range (1,11):
    print(i, end=' ')
print()
m=1
for j in range(1,11):
    n=1
    print(m, end=' ')
    for h in range(1,11):
        print(m*n, end=' ')
        n+=1
    print()
    m+=1