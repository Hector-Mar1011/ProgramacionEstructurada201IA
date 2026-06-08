"""
Módulo de Procesamiento de Telemetría para Vehículo Autónomo.
Paradigma: Programación Estructurada (Sin POO ni manejo de excepciones).
"""

import sys

def limpiar_lecturas(lista_datos):
    """Filtra una lista de lecturas eliminando valores no numéricos y nulos.

    Esta función adopta un enfoque de programación estructurada y utiliza
    condicionales tradicionales para validar que los datos de entrada
    sean números válidos (enteros o flotantes), descartando strings, 
    booleanos, estructuras vacías o valores None.

    Parámetros:
    ----------
    lista_datos : list
        Una lista que contiene las lecturas a evaluar.

    Retorna:
    -------
    list
        Una nueva lista que contiene únicamente los valores numéricos válidos.
        Si la entrada no es una lista, retorna una lista vacía.
    """
    # 1. Validación de la estructura de entrada
    if lista_datos is None or not isinstance(lista_datos, list):
        return []
        
    lista_filtrada = []
    
    # 2. Procesamiento secuencial de los datos
    for dato in lista_datos:
        # Validamos que no sea None y que sea de tipo int o float.
        # En Python, los booleanos (True/False) son subclase de int, 
        # por lo que se deben excluir explícitamente.
        if dato is not None and isinstance(dato, (int, float)) and not isinstance(dato, bool):
            lista_filtrada.append(dato)
            
    return lista_filtrada


def calcular_alertas(lista_filtrada, umbral_critico):
    """Cuenta el número de lecturas que superan un umbral crítico determinado.

    Esta función evalúa de manera secuencial una lista de datos numéricos y
    contabiliza cuántos de ellos son mayores que el límite establecido.
    Utiliza condicionales tradicionales para verificar que los parámetros
    sean válidos antes de procesar la información.

    Parámetros:
    ----------
    lista_filtrada : list
        Una lista que contiene únicamente valores numéricos (enteros o flotantes).
    umbral_critico : int o float
        El valor límite numérico a partir del cual se considera una alerta.

    Retorna:
    -------
    int
        El número total de alertas detectadas (lecturas > umbral).
        Retorna 0 si los parámetros de entrada no son válidos o si no hay alertas.
    """
    # 1. Validación de seguridad para los parámetros de entrada
    if lista_filtrada is None or not isinstance(lista_filtrada, list):
        return 0
        
    # Validamos que el umbral sea un número y no un booleano
    if not isinstance(umbral_critico, (int, float)) or isinstance(umbral_critico, bool):
        return 0

    contador_alertas = 0

    # 2. Procesamiento y conteo estructurado
    for lectura in lista_filtrada:
        # Validación preventiva por si se coló un dato inválido en la lista
        if isinstance(lectura, (int, float)) and not isinstance(lectura, bool):
            if lectura > umbral_critico:
                contador_alertas = contador_alertas + 1

    return contador_alertas


def generar_log_sistema(total_alertas):
    """Genera un reporte de texto con la plataforma actual y la acción requerida.

    Esta función detecta el sistema operativo subyacente mediante el módulo 'sys'
    y evalúa el número de alertas para determinar si la acción del sistema
    debe ser PERMITIDA o ABORTAR.

    Parámetros:
    ----------
    total_alertas : int
        El número entero de alertas detectadas en el sistema.

    Retorna:
    -------
    str
        Una cadena de texto formateada con la plataforma y la acción del sistema.
        Si el parámetro de entrada es inválido, retorna un mensaje de error.
    """
    # 1. Validación estricta del tipo de dato de entrada
    if total_alertas is None or not isinstance(total_alertas, int) or isinstance(total_alertas, bool):
        return "ERROR: El parámetro 'total_alertas' debe ser un número entero válido."
        
    # Validación de coherencia lógica
    if total_alertas < 0:
        return "ERROR: El número de alertas no puede ser negativo."

    # 2. Identificación de la plataforma (SISTEMA OS) usando el módulo sys
    plataforma = sys.platform.upper()

    # 3. Determinación de la acción mediante condicionales tradicionales
    if total_alertas > 3:
        accion = "ABORTAR"
    else:
        accion = "PERMITIDA"

    # 4. Construcción y formateo de la cadena de texto de retorno
    resultado_log = f"[{plataforma}] Alertas críticas encontradas: {total_alertas}. Acción: {accion}"

    return resultado_log


# --- PIPELINE PRINCIPAL DE EJECUCIÓN ---
if __name__ == "__main__":
    print("=== PROCESAMIENTO DE TELEMETRÍA EN TIEMPO REAL ===")
    umbral_configurado = 25.0

    # CASO NUEVO: Datos 100% Erróneos (Falla crítica de sensor)

    print("\n--- Ejecución Caso Especial: Pérdida Total de Señal Fidedigna ---")
    telemetria_erronea = ["Desconectado", None, True, "Error_Grave", False]
    
    # Paso A: Intento de limpieza
    lecturas_limpias_err = limpiar_lecturas(telemetria_erronea)
    
    # Paso B: Intento de cálculo de alertas
    alertas_err = calcular_alertas(lecturas_limpias_err, umbral_configurado)
    
    # Paso C: Intento de generación de log
    log_err = generar_log_sistema(alertas_err)
    
    print(f"Entrada Corrupta: {telemetria_erronea}")
    print(f"Filtrado Result:  {lecturas_limpias_err}")
    print(f"Log Generado:     {log_err}")


"""
Prompt que mejor resultado me dió:
"Actúa como un programador experto en Python Estructurado.
Escribe el código de una función llamada limpiar_lecturas.
Recibe como parámetro [lista_datos] y debe retornar [Una nueva lista filtrada con los valores válidos.].
Restricciones estrictas: > 1. No utilices programación orientada a objetos (POO).
2.No utilices manejo de excepciones (nada de bloques try-except).
Gestiona los errores de datos usando condicionales if/else tradicionales.
3. Incluye la documentación de la función mediante un Docstring descriptivo."


Auditoria de codigo:
La IA no intentó generar código con POO ni manejo de excepciones, cumpliendo con las restricciones establecidas.
Utilizó condicionales if/else para validar los datos de entrada y gestionar errores, siguiendo el paradigma de programación estructurada.
lo que si intentó fue crear la ultima función sin la libreria solicitada, tuve queagregar la importacion al promt
para que funcionara correctamente, lo cual es un detalle importante a considerar en futuras iteraciones del prompt para asegurar que se incluyan todas las dependencias necesarias desde el inicio.
"""