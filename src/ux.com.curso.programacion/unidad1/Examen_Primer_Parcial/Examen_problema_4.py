def activacion():
    while True:
        try:
            # pedimos los valores en decimal.
            w = float(input("Ingrese el peso de entrada: "))
            x = float(input("Ingrese el dato de entrada: "))
            
            # Si funciona salimos con un break.
            break 
        except ValueError:
            # Si el usuario ingresa texto o símbolos se genera un error
            print(" Error: Por favor, introduzca solo valores numéricos.")
            print("Reintentando...\n")

    Z = w * x
    print(f"Su valor de activación es: {Z}")

def main():
    activacion()
    
if __name__ == "__main__":
    main()