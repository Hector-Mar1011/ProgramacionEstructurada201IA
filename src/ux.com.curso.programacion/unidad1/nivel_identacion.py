# Ejemplo para visualizar la identación en python

def explicar_identacion():
    # Nivel 1
    mensaje = "Nivel 1 de identación"
    print(mensaje)

    puntos = 10
    if puntos >9:
        #Nivel 2 
        print("Entra al flujo if")

        if puntos == 10:
            #Nivel 3
            print("Puntos es igual a 10")
    
    #Cierra nivel 1

def main():
    explicar_identacion()
    
if __name__ == "__main__":
    main()

