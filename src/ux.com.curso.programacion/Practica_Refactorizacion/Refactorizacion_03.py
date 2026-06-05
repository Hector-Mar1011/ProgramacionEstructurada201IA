"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte III)
Alumno: Héctor Luis Garcia Marthen.
"""
import math

# =====================================================================
# RETO 1: Inicializador de Tablero de Juego (Matrices)
# Sentido: Crear una cuadrícula vacía de 4x4 (como el juego 2048 o un tablero)
#          inicializada con ceros antes de colocar las piezas de la IA.
# =====================================================================
def inicializar_tablero_vacio():
    fila_base = [0, 0, 0, 0]
    tablero = [fila_base, fila_base, fila_base, fila_base]
    for i in range(4):
        for j in range(4):
            tablero[i][j] = 0
    return tablero

def inicializar_tablero_vacio_factorizado():
    # Usamos comprensión de listas para crear listas independientes en memoria.
    # Así evitamos que todas las filas apunten a la misma referencia.
    return [[0 for _ in range(4)] for _ in range(4)]

# =====================================================================
# RETO 2: Recortador de Valores Atípicos (Clamping de Datos)
# Sentido: Limitar las señales de los sensores del robot a un rango seguro.
# =====================================================================
def limitar_senal_sensor(valor_lectura, minimo, maximo):
    if valor_lectura < minimo:
        resultado = minimo
    else:
        if valor_lectura > maximo:
            resultado = maximo
        else:
            resultado = valor_lectura
    return resultado

def limitar_senal_sensor_factorizado(valor_lectura, minimo, maximo):
    # Usamos las funciones nativas max() y min() para "encapsular" el valor.
    return max(minimo, min(valor_lectura, maximo))

# =====================================================================
# RETO 3: Buscador del Valor Más Cercano a Cero (Error Mínimo)
# Sentido: Encontrar el menor error absoluto (loss) en una lista de pruebas.
# =====================================================================
def buscar_error_minimo(lista_errores):
    menor_error = 999999.99 
    for i in range(len(lista_errores)):
        valor_actual = lista_errores[i]
        if valor_actual < 0:
            absoluto = valor_actual * -1
        else:
            absoluto = valor_actual
            
        if absoluto < menor_error:
            menor_error = absoluto
    return menor_error

def buscar_error_minimo_factorizado(lista_errores):
    # min() permite usar el parámetro 'key' para aplicar una función (abs)
    # antes de comparar, sin modificar los valores originales.
    return min(lista_errores, key=abs)

# =====================================================================
# RETO 4: Filtro de Valores Únicos (Eliminador de Duplicados)
# Sentido: Limpiar las IDs de los usuarios del servidor para
#          que no se procesen comandos repetidos.
# =====================================================================
def depurar_usuarios_repetidos(lista_ids):
    lista_limpia = []
    for i in range(len(lista_ids)):
        id_actual = lista_ids[i]
        ya_existe = False
        for j in range(len(lista_limpia)):
            if lista_limpia[j] == id_actual:
                ya_existe = True
                break
        if not ya_existe:
            lista_limpia.append(id_actual)
    return lista_limpia

def depurar_usuarios_repetidos_factorizado(lista_ids):
    # Convertir a 'set' elimina los duplicados automáticamente (basado en tablas hash).
    # Se convierte de nuevo a 'list' si se requiere ese formato específico.
    return list(set(lista_ids))

def depurar_usuarios_repetidos_factorizado_ordenado(lista_ids):
    # Si es importante mantener el orden original de las IDs, esta es la mejor opción en Python moderno:
    return list(dict.fromkeys(lista_ids))