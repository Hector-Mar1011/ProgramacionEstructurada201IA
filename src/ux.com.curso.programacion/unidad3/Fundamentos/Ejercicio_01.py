"""
Creación de un programa que divide numero enteros sin  utilizar el operador de división, utilizando solo sumas y restas.
"""

def division_entera(a, b):

    Dividendo = int(input("Ingrese el numero a dividir: "))

    Divisor = int(input("Ingrese el numero divisor: "))

    Cociente = 0

    if Divisor == 0:
        print("Error: No se puede dividir por cero.")
        return None

    while Dividendo >= Divisor:
        Dividendo = Dividendo - Divisor
        Cociente = Cociente + 1

    print("El cociente de la división es:", Cociente)
    print("El residuo de la división es:", Dividendo)
    return Cociente

def main():
    division_entera(0, 0)

if __name__ == "__main__":
    main()


