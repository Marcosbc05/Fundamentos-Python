notas=[5,8,6,4,7,2,1,6,9,8,2,3,4,5,6,1,7,2,5,3,6]

for i in range (len(notas)):
    if notas[i]<5:
        notas[i]='Suspenso'
    elif notas[i]>=5:
        notas[i]='Aprobado'
print(notas)