"""
Implementación en python de generación de una serie denumeros impares siguendo un diagrama de 
flujo proporcionado por el profesor
"""

def cont_impar(n):
    contador = 0
    numero = 1

    while contador < n:
        print(numero)
        numero = numero + 2
        contador += 1

def main():
    n = int(input("Ingrese un número para la serie de numeros impares: "))
    proceso = cont_impar(n)
    print("numero ingresado correctamente a la serie, el nuevo número es: ", proceso)
    cont_impar(n)

if __name__ == "__main__":
    main() 