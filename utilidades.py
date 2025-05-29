def obtener_entero(pregunta):
    """
    Pide un usuario un valor. Sigue preguntando hasta que el usuario le de un valor valido.
    """

    valor = input(pregunta)

    while not valor.isnumeric():
        print('\nSolo se permiten numeros enteros')
        valor = input(pregunta)

    return int(valor)

def obtener_nota_valida(pregunta):
    """
    Recibe un string y valida que sea una nota valida. Las notas validas son numeros enteros entre 1 y 10 inclusive.
    """

    valor = obtener_entero(pregunta)

    # Dentro del range solo se encuentran los numeros del 1 al 10
    while not valor in range(1,11):
        print('\nLas notas validas son enteros del 1 al 10')
        valor = obtener_entero(pregunta)

    return valor

def obtener_porcentaje_aprobacion(notas):
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

def obtener_opcion(pregunta, opciones):
    """
    Recibe una pregunta como str, y una lista de opciones como lista de strings
    Le pide un usuario un valor. Sigue preguntando hasta que el valor se encuentre en la lista.
    Ignora mayusculas para mayor consistencia
    Devuelve el indice de la opcion seleccionada en la lista de opciones
    """

    # Copio la lista para no modificar la lista original y a su vez, tener todo en minuscula
    opciones_minusc = [opcion.lower() for opcion in opciones]

    value = input(pregunta).lower()

    while not value in opciones_minusc:
        print(f'\nLas opciones validas son: { " - ".join(opciones) }')
        value = input(pregunta).lower()

    return opciones_minusc.index(value)
