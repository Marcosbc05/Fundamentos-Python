def vol(n,T,P,r=0.082):
    '''float,float,float,float->float'''
    return (n*r*T)/P
print(vol(3,6,5))

