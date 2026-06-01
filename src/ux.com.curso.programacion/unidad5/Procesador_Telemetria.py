"""
 Un vehículo autónomo genera ráfagas de datos en tiempo real (telemetría).
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


# --- Ejemplo de uso y comprobación ---
if __name__ == "__main__":
    # Lista de prueba con datos corruptos y de diferentes tipos
    lecturas_sucias = [23.5, "Error_404", 18, None, True, 22.1, False, "100", 19.8]
    
    # Llamada a la función
    lecturas_limpias = limpiar_lecturas(lecturas_sucias)
    
    # Impresión de resultados
    print("Lecturas originales:", lecturas_sucias)
    print("Lecturas filtradas:  ", lecturas_limpias)




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


# --- Ejemplo de uso y comprobación ---
if __name__ == "__main__":
    # Datos previamente limpios (salida de la función anterior)
    datos_sensores = [23.5, 18.0, 22.1, 19.8, 35.4, 28.2, 40.1]
    limite_peligro = 25.0  # Queremos alertar sobre lecturas mayores a 25.0
    
    # Llamada a la función
    total_alertas = calcular_alertas(datos_sensores, limite_peligro)
    
    # Impresión de resultados
    print(f"Lecturas evaluadas: {datos_sensores}")
    print(f"Umbral crítico:     {limite_peligro}")
    print(f"Total de alertas:   {total_alertas}")  # Debería retornar 3 (35.4, 28.2 y 40.1)


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
    # Excluimos booleanos porque en Python isinstance(True, int) evalúa como True.
    if total_alertas is None or not isinstance(total_alertas, int) or isinstance(total_alertas, bool):
        return "ERROR: El parámetro 'total_alertas' debe ser un número entero válido."
        
    # Validación de coherencia lógica
    if total_alertas < 0:
        return "ERROR: El número de alertas no puede ser negativo."

    # 2. Identificación de la plataforma (SISTEMA OS) usando el módulo sys
    # sys.platform devuelve cadenas como 'win32', 'linux', 'darwin' (macOS), etc.
    plataforma = sys.platform.upper()

    # 3. Determinación de la acción mediante condicionales tradicionales
    if total_alertas > 3:
        accion = "ABORTAR"
    else:
        accion = "PERMITIDA"

    # 4. Construcción y formateo de la cadena de texto de retorno
    resultado_log = f"[{plataforma}] Alertas críticas encontradas: {total_alertas}. Acción: {accion}"

    return resultado_log


# --- Ejemplo de uso y comprobación ---
if __name__ == "__main__":
    # Caso 1: Alertas dentro del rango seguro (≤ 3) -> Acción: PERMITIDA
    alertas_bajas = 2
    log_permitido = generar_log_sistema(alertas_bajas)
    print("Prueba 1:", log_permitido)
    
    # Caso 2: Alertas superan el límite (> 3) -> Acción: ABORTAR
    alertas_altas = 5
    log_abortar = generar_log_sistema(alertas_altas)
    print("Prueba 2:", log_abortar)
    
    # Caso 3: Control de datos erróneos
    log_error = generar_log_sistema("Múltiples")
    print("Prueba 3:", log_error)
