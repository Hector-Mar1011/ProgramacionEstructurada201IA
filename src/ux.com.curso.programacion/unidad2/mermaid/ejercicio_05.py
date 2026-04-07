"""
implementación en python de un algoritmo de acumulación numerica siguiendo estrictamente una lógica 
de repetición. 
"""

def acumulacion():
    
    suma = 0
    while True:
        numero = int(input("Ingrese un número: "))
        if numero >= 10 and numero<= 50:
            suma += numero
        else:
            break
    return suma

def main():
    resultado = acumulacion()
    print("La suma acumulada es:", resultado)

if __name__ == "__main__":
    main() 