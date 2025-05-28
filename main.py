from utilidades import obtener_entero, obtener_nota_valida, obtener_porcentaje_aprobacion

def cargar_matriz_notas():
    """
    Funcion que le pide al usuario que ingrese una nota para varios alumnos. Las notas van del 1 al 10. Pedir la cantidad de alumnos, y las notas que tuvo cada alumno.
    Primero pide la cantidad de alumnos (n)
    Luego pide la cantidad de examenes (m)
    Crear una matriz. Pedir que ingrese una nota para cada examen, y valide si es una nota valida.
    """

    n = obtener_entero("Ingrese la cantidad de alumnos: ")
    m = obtener_entero("Ingrese la cantidad de examenes: ")

    # Inicializamos la matriz con N listas vacias
    matriz = []
    for x in range(0,n): matriz.append([])

    print('Se inicia la carga de notas')
    for alumno in range(0,n):
        print(f'\nInicio de carga de notas para el alumno n°{alumno+1}')
        for examen in range(0,m):
            nota = obtener_nota_valida(f'- Ingrese la nota del examen n°{examen+1}: ')
            matriz[alumno].append(nota)

    return matriz
            
def porcentaje_aprobados(matriz):
    """
    Recibe una matriz con n alumnos y m examenes por cada alumno.
    Calcula el porcentaje de exámenes aprobados.
    El porcentaje se obtiene haciendo ([Cantidad Examenes Aprobados] * 100) / [Cantidad de Examenes Totales]
    Las notas aprobadas son aquellas >= 6
    Imprime por pantalla un resumen individual por cada alumno
    """
    
    for i_alumno in range(0,len(matriz)):
        print(f'\nDatos del alumno {i_alumno + 1}')
        print(f'Lista de notas: {matriz[i_alumno]}')
        print(f'Porcentaje de aprobacion: {obtener_porcentaje_aprobacion(matriz[i_alumno])}%')

def main():
    matriz = cargar_matriz_notas()

    for coso in matriz:
        print(coso)

    porcentaje_aprobados(matriz)
            

if __name__ == "__main__":
    main()