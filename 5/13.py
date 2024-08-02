personas={'Pepa':['flores','azul'],'Pepe':['tomates'],'Isabel':['Pizza','barco']}
def agregar_pref(personas,persona,preferencia):
    if persona not in personas:
        personas.update({persona:[preferencia]})
        return personas
    elif persona in personas:
        if preferencia in personas[persona]:
            return 'La preferencia ya fue previamente guardada.'
        else:
            personas[persona].append(preferencia)
            return personas
#probador
print(agregar_pref(personas,'Manolo','coche'))
print(agregar_pref(personas,'Pepe','coche'))
print(agregar_pref(personas,'Pepa','azul'))