x=input('inserte nota: ')
try:
    x=float(x)
except:
    print('introduca solo números')
else:
    if 0<=x<3.5:
        print(x,' --> CALIFICACION: F')
    elif 3.5<=x<5:
        print(x,' -->CALIFICACION: D')
    elif 5<=x<6.5:
        print(x,' -->CALIFICACION: C')
    elif 6.5<=x<8.5:
        print(x,' -->CALIFICACION: B')
    elif 8.5<=x<=10:
        print(x,' -->CALIFICACION: A')
    elif x<0 or x>10:
        print('solo se pueden insertar entre el 0 y el 10')
