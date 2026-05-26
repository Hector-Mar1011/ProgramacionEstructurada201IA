"""
En este codigo se van a usar condicionales if-else para determinar si un numero es par o impar.
"""

# Creamos una funcion que almacene el proceso de verificación.
def verificacion():
    n= int(input("Ingrese un numero: "))
  # 1. Si n es impar, imprime Weird
    if n % 2 != 0:
        print("Weird")
    else:
        # Si entra aquí, ya sabemos que n es par
        # 2. Si es par y está entre 2 y 5 (inclusive), imprime Not Weird
        if 2 <= n <= 5:
            print("Not Weird")
        # 3. Si es par y está entre 6 y 20 (inclusive), imprime Weird
        elif 6 <= n <= 20:
            print("Weird")
        # 4. Si es par y es mayor que 20, imprime Not Weird
        elif n > 20:
            print("Not Weird")


# Llamamos a la funcion para ejecutar el proceso
def main():
    while True:
        verificacion()
    
    if n == str(n):
        print("Ingrese un numero valido.")


if __name__ == "__main__":
    main()  