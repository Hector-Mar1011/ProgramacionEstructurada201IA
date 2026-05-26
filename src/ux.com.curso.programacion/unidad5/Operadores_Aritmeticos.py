"""
Usando operadores aritmeticos en python realizando operaciones basicas como suma,
resta y multiplicacion.
"""

def operadores():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicacion: {multiplicacion}")


def main():
    operadores()

if __name__ == "__main__": 
    main()  