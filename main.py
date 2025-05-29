from utilidades import obtener_entero, obtener_nota_valida, obtener_opcion
from calculos import porcentaje_aprobacion, promedio

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
        print(f'Porcentaje de aprobacion: {porcentaje_aprobacion(matriz[i_alumno])}%')

def mejor_promedio(matriz):
    """
    Calcula el promedio de cada alumno y determina cuál tiene el mejor.
    Devuelve una tupla con el indice del alumno, y el valor de su promedio
    """
    indice = -1
    max_prom = -1

    for i in range(0,len(matriz)):
        prom = promedio(matriz[i])
        if prom > max_prom:
            max_prom = prom
            indice = i

    return indice, max_prom

def buscar_nota(matriz,nota_a_buscar):
    """
    Recibe la matriz de alumnos y una nota valida
    Devuelve una lista de tuplas
    Cada tupla esta formada por el indice del alumno, y el indice del examen (coordenadas de la matriz)
    """
    notas_encontradas = []

    for i_alumno in range(0,len(matriz)):
        notas = matriz[i_alumno]
        for i_nota in range(0,len(notas)):
            if notas[i_nota] == nota_a_buscar:
                notas_encontradas.append((i_alumno,i_nota))

    return notas_encontradas

def main():

    opciones = ['salir', 'cargar','porcentaje','promedio','buscar']

    print('Bienvenido al sistema de carga. Sus opciones son:')
    print('cargar - genera y carga la matriz de notas de los alumnos')
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

        # Los alumnos y examenes se cuentan desde el 1ro, pero las listas de python empiezan en 0
        # Por lo que siempre hay que sumarle 1 a los indices que quieran mostrarse por pantalla
        match seleccion:
            case 1:
                matriz = cargar_matriz_notas()
            case 2:
                porcentaje_aprobados(matriz)
            case 3:
                i_alumno, prom = mejor_promedio(matriz)
                print(f'El alumno N°{i_alumno + 1} tiene el mejor promedio: {prom}')
            case 4:
                nota = obtener_nota_valida('Que valor de nota desea buscar? ')
                resultados = buscar_nota(matriz,nota)
                if len(resultados) < 1:
                    print('No se ha encontrado esa nota')
                else:
                    print(f'Notas de valor {nota} encontradas:')
                    for resultado in resultados:
                        print(f'- Alumno N°{resultado[0] + 1}, examen N°{resultado[1] + 1}')
            
        print('')
            

if __name__ == "__main__":
    main()