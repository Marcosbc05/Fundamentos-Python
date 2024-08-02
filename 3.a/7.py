x=str(input('inserte letra en minúsculas: '))
def es_vocal(x):
    '''str->bool
    obj: vocal o no'''
    if x=='a'or x=='e' or x=='i' or x=='o' or x=='u':
        return 'es vocal'
    else:
        return 'es consonante, no vocal'
print(es_vocal(x))