# Ejemplo de repetición

def ejemplo_for():
    print("Estructura FOR")

    frutas = ["manzana", "banana", "naranja"]

    # For para iterar listas
    for frutas in frutas:
        print(frutas)
    
    # For para iterar rangos
    for i in range(1,5):
        print(i)
    
    # For para iterar rangos con paso
    for i in range(1 ,10, 2):
        print(i)
    
    # Ejemplo de while

def ejemplo_while():
    print("Estructura while")

    contador = 0

    while contador < 5:
        print(contador)
        contador += 1

# Simulación de Do While
def ejemplo_do_while():
    print("Estructura Do While")

    secreto = "Curly123"
    intentos = 0

    while True:
        intentos_usario = "Curly123" # Simulamos la entrada del usuario
        intentos += 1

        if intentos_usario == secreto:
            print("acceso concedido")
            break
        else:
            print("¡Acceso denegado! Intentalo de nuevo.")
            break
        print("\n")

def main():
    ejemplo_for()
    ejemplo_while()
    ejemplo_do_while()
    
    
if __name__ == "__main__":
    main()

