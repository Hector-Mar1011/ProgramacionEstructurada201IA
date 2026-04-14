import os
# --- SISTEMA DE MONITOREO INDUSTRIAL ---
def limpiar_dato(lectura):
    """
    FUNCIÓN 1: Recibe un string del archivo, lo convierte a float.
    Si el dato es > 100 o < 0, devuelve None (Ruido detectado).
    """
 # IMPLEMENTAR AQUÍ
    try:
        valor = float(lectura)

        if valor < 0 or valor > 100:
            return None
        return valor

    except ValueError:
        return None
    
def calcular_alerta(valor_normalizado):
    """
    FUNCIÓN 2: Recibe el valor (0.0 a 1.0).
    Devuelve 'CRÍTICO' si es > 0.8, 'PRECAUCIÓN' si es > 0.5,
    y 'NORMAL' en cualquier otro caso.
    """
    # IMPLEMENTAR AQUÍ
    if valor_normalizado > 0.8:
       return 'CRÍTICO'
    elif valor_normalizado > 0.5:
       return 'PRECAUCIÓN'
    else:
       return 'NORMAL'
    

def obtener_estadisticas(lista_datos):
    """
    FUNCIÓN 3: Recibe la lista de datos válidos.
    Devuelve una TUPLA con: (Valor máximo, Valor mínimo, Promedio).
    """
    # IMPLEMENTAR AQUÍ
    if not lista_datos:
       return (0, 0, 0)
    
    maximo = max(lista_datos)
    minimo = min(lista_datos)
    promedio = sum(lista_datos) / len (lista_datos)

    return (maximo, minimo, promedio)

def generar_reporte(total_datos, validos, estadisticas):
    """
    FUNCIÓN 4: Imprime un resumen formateado de los resultados.
    """

    v_max, v_min, v_prom = estadisticas
    descartados = total_datos - validos
    # IMPLEMENTAR AQUÍ	
    print("*" * 30)
    print("REPORTE DE ANILISIS PREDECTIVO")
    print("*" * 30)
    print(f"Total de lecturas prcesadas: {total_datos}")
    print(f"Lecturas válidas: {validos}")
    print(f"Lecturas descartadas: {descartados}")
    print(f"Valor máximo: {v_max}")
    print(f"Valor mínimo: {v_min}")
    print(f"Promedio: {promedio}")
    print("*" * 30)


# --- LÓGICA PRINCIPAL (NO MODIFICAR ESTA PARTE) ---
def ejecutar_pipeline():
 datos_finales = []
 cuenta_total = 0
 # Obtener la ruta absoluta del archivo en la misma carpeta que el script
 ruta_script = os.path.dirname(os.path.abspath(__file__))
 ruta_archivo = os.path.join(ruta_script, "Lectura_sensores.txt")

 with open("lecturas_sensores.txt", "r") as f:
    for linea in f:
        cuenta_total += 1
        valor = limpiar_dato(linea.strip())
    if valor is not None:
     # Normalizar para la IA (0-1)
        datos_finales.append(valor / 100)

    if datos_finales:
        stats = obtener_estadisticas(datos_finales)
        generar_reporte(cuenta_total, len(datos_finales), stats)


if __name__ == "__main__":
    ejecutar_pipeline()