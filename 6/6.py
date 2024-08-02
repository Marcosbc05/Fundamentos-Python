def digitos(n):
    if 0<=n<10:
        dig=1
    else:
        dig=1+digitos(n//10)
    return dig

print(digitos(5544))