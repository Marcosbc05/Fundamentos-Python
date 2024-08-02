matrizA=[[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
for i in range(len(matrizA)):
    for j in range(len(matrizA[i])):
        a=input('inserte nº para A: ')
        matrizA[i][j]=a
matrizB=[[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
for i in range(len(matrizB)):
    for j in range(len(matrizB[i])):
        a=input('inserte nº para B: ')
        matrizB[i][j]=a
for i in matrizA:
    print(i)
print()
for i in matrizB:
    print(i)
#sumar
matrizAB=[[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
for i in range(len(matrizAB)):
    for j in range(len(matrizAB[i])):
        b=int(matrizA[i][j])+int(matrizB[i][j])
        matrizAB[i][j]=b
for i in matrizAB:
    print(i)