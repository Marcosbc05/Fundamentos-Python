def mult(a,b):
    if a==0 and b==0:
        res=0
    elif a==1:
        res=b
    elif b==1:
        res=a
    else:
        res=b+mult(a-1,b)
    return res
print(mult(2,9))