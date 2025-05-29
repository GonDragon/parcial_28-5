# Este archivo contiene los calculos matematicos requeridos

def porcentaje_aprobacion(notas):
    """
    Recibe una lista de notas
    Devuelve un float con el porcentaje de notas aprobadas
    El porcentaje se obtiene haciendo ([Cantidad Examenes Aprobados] * 100) / [Cantidad de Examenes Totales]
    Las notas aprobadas son aquellas >= 6
    """
    total = len(notas)
    aprobadas = 0
    for nota in notas:
        if nota >= 6:
            aprobadas += 1

    return (aprobadas * 100) / total

def promedio(notas):
    """
    Recibe una lista de notas. Las notas deben ser int o float.
    Devuelve el promedio de las notas
    """
    suma = 0.0
    for nota in notas:
        if not (isinstance(nota,int) or isinstance(nota,float)):
            print('Aqui debería ir un raise, valor no valido')
            return -1
        suma += nota

    return suma / len(notas)