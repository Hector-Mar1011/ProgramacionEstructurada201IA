#Desarrollo de algoritmo contador de positivos

# Declaración de variables

def contador_positivos():
    contador = 0 
    while True:
        numero = int(input("Ingrese un número (-1 para terminar): "))
        if numero <0:
            break
        contador += 1
    
    print("Cantidad de números positivos ingresados: ", contador)

#Definición de la función main (Controla el flujo del programa)
def main():
    print("Bienvenido al contador de positivos")
    contador_positivos()

#Llamada a la función para iniciar el programa

if __name__ == "__main__":
    main()