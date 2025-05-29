from utilidades import obtener_entero, obtener_nota_valida, obtener_porcentaje_aprobacion, obtener_opcion

def cargar_matriz_notas():
    """
    Funcion que le pide al usuario que ingrese una nota para varios alumnos. Las notas van del 1 al 10. Pedir la cantidad de alumnos, y las notas que tuvo cada alumno.
    Primero pide la cantidad de alumnos (n)
    Luego pide la cantidad de examenes (m)
    Crear una matriz. Pedir que ingrese una nota para cada examen, y valide si es una nota valida.
    """

    cant_alumnos = obtener_entero("Ingrese la cantidad de alumnos: ")
    cant_examenes = obtener_entero("Ingrese la cantidad de examenes: ")

    # Inicializamos la matriz con N listas vacias
    matriz = []
    for x in range(0,cant_alumnos): matriz.append([])

    print('Se inicia la carga de notas')
    for alumno in range(0,cant_alumnos):
        print(f'\nInicio de carga de notas para el alumno n°{alumno+1}')
        for examen in range(0,cant_examenes):
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
    
    # Iteramos por los alumnos usando un indice
    for i_alumno in range(0,len(matriz)):
        print(f'\nDatos del alumno {i_alumno + 1}')
        print(f'Lista de notas: {matriz[i_alumno]}')
        print(f'Porcentaje de aprobacion: {obtener_porcentaje_aprobacion(matriz[i_alumno])}%')

def main():

    opciones = ['salir', 'cargar','porcentaje','promedio','buscar']

    print('Bienvenido al sistema de carga. Sus opciones son:')
    print('matriz - genera y carga la matriz de notas de los alumnos')
    print('porcentaje - obtiene el porcentaje de aprobacion de cada alumno, y muestra un resumen individual')
    print('promedio - obtener el alumno con mejor promedio')
    print('buscar - permite ingresar una nota y ver quienes sacaron esa nota en qué examen')

    # El bucle principal continua hasta que el usuario quiera salir. Salir es la opcion 0.
    matriz = None
    seleccion = None
    while seleccion != 0:
        seleccion = obtener_opcion('Que desea hacer? ',opciones)

        # Hasta que la matriz no este cargada, lo unico que se puede hacer es cargar la matriz o salir
        if not matriz and not (seleccion == 0 or seleccion == 1):
            print('\nPrimero debe cargar las notas!')
            continue

        match seleccion:
            case 1:
                matriz = cargar_matriz_notas()
            case 2:
                porcentaje_aprobados(matriz)
                print('')
            case 3:
                pass
            case 4:
                pass
            

if __name__ == "__main__":
    main()