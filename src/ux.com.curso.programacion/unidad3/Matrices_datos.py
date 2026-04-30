import statistics

"""
sistema que simula una cámara de baja resolución (una matriz de 3x3) y un vector de sensores de proximidad.
"""

#Declaracion de un vector de tamaño 5.

vector_sensores = 0, 0, 0, 0, 0
#ciclo for para ingresar distancias.

for i in vector_sensores:
    distancia = float(input("Ingrese la distancia detectada para el sensor del robot: "))

# Calculo del promedio de distancia del vector.
promedio_vector = statistics.mean(vector_sensores)
if promedio_vector < 2.0:
    print("!AVISO¡: Reduciendo velocidad global")

# 1. Configuración inicial
DIMENSION = 3
camara_ia = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]
puntos_brillantes = 0
UMBRAL_LUZ_ALTA = 200

print("--- Captura de Imagen (Matriz 3x3) ---")

# 2. Lectura con Validación de Saturación
for i in range(DIMENSION):
    for j in range(DIMENSION):
        while True:
            try:
                valor = int(input(f"Intensidad píxel [{i}][{j}]: "))
                
                # Operación de saturación (Cap at 255)
                if valor > 255:
                    print(f"  > Saturación detectada: {valor} ajustado a 255.")
                    valor = 255
                elif valor < 0:
                    print(f"  > Valor negativo ajustado a 0 (oscuridad total).")
                    valor = 0
                
                camara_ia[i][j] = valor
                break
            except ValueError:
                print("Error: Ingresa un número entero válido.")

# 3. Procesamiento: Contar puntos de luz alta
for fila in camara_ia:
    for pixel in fila:
        if pixel > UMBRAL_LUZ_ALTA:
            puntos_brillantes += 1

# 4. Escritura de Arreglo (Salida formateada)
print("\n" + "="*25)
print(" MATRIZ RESULTANTE (IA)")
print("="*25)

for fila in camara_ia:
    # Formateo con padding para que los números queden alineados
    print(f"| {'  '.join(f'{pixel:3}' for pixel in fila)} |")

print("="*25)
print(f"Puntos de luz alta detectados: {puntos_brillantes}")

# Inicializamos el contador
puntos_brillantes = 0
umbral = 200

# Recorrido de la matriz para análisis
for fila in range(3):
    for columna in range(3):
        if camara_ia[fila][columna] > umbral:
            puntos_brillantes += 1

# Resultado del análisis
print("-" * 30)
print(f"Análisis de exposición: Se detectaron {puntos_brillantes} píxeles con luz alta (>200).")

def main():
    pass    

if __name__ == "__main__":    
    
    main()    