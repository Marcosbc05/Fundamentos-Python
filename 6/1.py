def num_in_lista(n,lista):
    if len(lista)==0:
        a=False
    else:
        if n==lista[0] or num_in_lista(n,lista[1:]):
            a=True
        else: 
            a=False
    return a
print(num_in_lista(8,[3,6,8,4]))