# Imprime la tabla de multiplicar del 1 al 15, con formato de tabla.
def multiplicaciones():
    # Encabezado de la tabla
    print("  ", end=" ")
    for col in range(1, 16):
        if col < 10:
            print(col, end="  ") 
        else:
            print(col, end=" ")  
    print()

    # Línea divisoria
    print("   " + " * " * 15)

def tabla():
    # Cuerpo de la tabla
    for row in range(1, 5):
        # Imprime el número de la fila y el asterisco
        print(row, end="* ")
        
        for col in range(1, 16):
            resultado = row * col
            
            # Lógica manual para que las columnas queden alineadas
            if resultado < 10:
                print(resultado, end="  ")  
            elif resultado < 100:
                print(resultado, end=" ")   
                
        print() # Salto de línea al terminar cada fila


def main():
    multiplicaciones()
    tabla()

if __name__ == "__main__":
    main()