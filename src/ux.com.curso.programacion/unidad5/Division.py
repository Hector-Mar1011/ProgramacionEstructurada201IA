"""
Usando operadores logicos implementaremos la division integral y la divicion flotante.
"""

def DIVISION():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    division_integral = a // b
    division_flotante = a / b
    print(f" {division_integral}")
    print(f"{division_flotante}")

def main():
    DIVISION()  

if __name__ == "__main__":
    main()
    