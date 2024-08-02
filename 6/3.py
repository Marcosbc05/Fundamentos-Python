def div(a,b):
    if a==b:
        res=1
    elif a<b:
        res=0
    else:
        res=1+div(a-b,b)
    return res
print(div(35,8))