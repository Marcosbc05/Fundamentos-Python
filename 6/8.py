def suma_pares(n):
    if n==0 or n==1:
        suma=0
    elif n==2:
        suma=2
    else:
        if n%2==0:
            suma=n+(suma_pares(n-2))
        else:
            suma=(n-1)+(suma_pares(n-2))
    return(suma)
print(suma_pares(11))
