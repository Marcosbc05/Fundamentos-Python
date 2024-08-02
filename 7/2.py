frases=['Open Up','Dare To Dream','The Sound of Beauty','United By Music','All Aboard','Celebrate Diversity','Come Together','Building Bridges','Join Us','We Are One','Light Your Fire','Feel Your Heartbeat']
def ordenar_insercion(frases):
    for i in range(1,len(frases)):
        actual=frases[i]
        indice=i
        while indice>0 and len(actual)<len(frases[indice-1]):
            frases[indice]=frases[indice-1]
            indice-=1
        frases[indice]=actual
    return frases
#imprimir
frases=ordenar_insercion(frases)
for i in frases:
    print(i)