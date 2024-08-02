def fibonacci(n):
    if n==0 or n==1:
        res=1
    else:
        res=fibonacci(n-1)+fibonacci(n-2)
    return res
print(fibonacci(12))