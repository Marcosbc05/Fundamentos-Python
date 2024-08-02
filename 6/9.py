alumno1={"nombre":"Marcos","edad":17,"titulación":"GIIA"}
alumno2={"nombre":"Pepe","edad":23,"titulación":"ADE"}
alumno3={"nombre":"Herminia","edad":21,"titulación":"Medicina"}
alumno4={"nombre":"Sandra","edad":19,"titulación":"Magisterio"}
alumnos=[alumno1,alumno2,alumno3,alumno4]
def suma_edades(alumnos):
    if len(alumnos)==0:
        suma=0
    else:
        suma=alumnos[0]['edad']+suma_edades(alumnos[1:])
    return suma
print(suma_edades(alumnos))