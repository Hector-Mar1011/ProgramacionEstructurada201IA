#Desarrollo de algoritmo contador de positivos

# Declaración de variables
"""
Esta función tiene como tarea contar los numeros hasta que el usuario decida 
romper con el bucle poniendo un numero no positivo y reiniciar desde cero el contador.
"""
def contador_positivos():
    contador = 0 
    while True:
        numero = int(input("Ingrese un número (-1 para terminar): "))
        if numero <0:
            break
        contador += 1
    
    print("Cantidad de números positivos ingresados: ", contador)

#Definición de la función main (Controla el flujo del programa)
"""
Esta función imprime un texto en pantalla para el inicio del contador, despues
llama a la función del contador para ejecutar el bucle.
"""
def main():
    print("Bienvenido al contador de positivos")
    contador_positivos()

#Llamada a la función para iniciar el programa

if __name__ == "__main__": # Llama a la funcion main para iniciar con la ejecución del codigo
    main()