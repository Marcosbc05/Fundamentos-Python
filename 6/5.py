def inversa(palabra):
    if len(palabra)==0 or len(palabra)==1:
        res=palabra
    else:
        res=inversa(palabra[1:])+palabra[0]
    return res
print(inversa('europa'))