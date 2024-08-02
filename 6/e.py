import math
a=True
num=0
while a:
    b=2**num
    if b%10==0:
        print("2^",num,"= ",b)
        a=False
    if num>100000000:
        print("2^",num,"= ",b)
        a=False
    num+=1
