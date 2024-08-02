#Codificar un modulo recursivo que calcule la division entera entre dos numeros 
#A y B sin utilizar multiplicaciones ni divisiones.
def division(a,b):
    '''OBJ: a/b'''
    if a==b:
        cociente=1
    elif a<b:
        cociente=0
    else:
        cociente= 1+division(a-b,b)
    return cociente
print(division(8,4))

#Codificar un modulo recursivo que calcule xn, con x real y n entero
def potencia(x,n):
    if n==0:
        result=1
    else:
        result=x*potencia(x,n-1)
    return result
print(potencia(7,2))

#Codificar un programa recursivo que toma una cadena como 
#parametro y devuelve otra cadena que es la original pero con sus caracteres invertidos.
def invertir(cadena):
    if len(cadena)==1:
        inversa=cadena
    elif len(cadena)==0:
        inversa=''
    else:
        inversa=invertir(cadena[1:])+cadena[0]
    return inversa
print(invertir('melodifestivalen'))

#Los detectives de una agencia se env´ıan todos los mensajes cifrados por motivos 
# de seguridad. El algoritmo que est´an utilizando en la actualidad consiste en intercambiar cada 
# vocal por la letra que la precede (si existe). Por ejemplo: El resultado de codificar el 
# mensaje: esta en Leon esate n eoLn

def cifrar(mensaje,n):
    '''intercambio vocal por letra anterior'''
    if len(mensaje)<=1:
        cifrado=mensaje
    else:
        if mensaje[0] not in ['a','e','i','o','u'] or n==0:
            cifrado=mensaje[n]+cifrar(mensaje[1:],n+1)
        else:
            cifrado=mensaje[n-1]+mensaje[n]+cifrar(mensaje[2:],n+1)
    return cifrado
print(cifrar('europa',0))