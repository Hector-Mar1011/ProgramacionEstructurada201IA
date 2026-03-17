import math

# demostracione¿ del uso de funciones math

def mostrar_funciones(numero):

    sen_x = math.sin(numero)
    cose_x = math.cos(numero)

    print("el seno de", numero, "es:", sen_x)
    print("el seno de", numero, "es:", cose_x)

    resultado = sen_x ** 2 + cose_x ** 2

    print("El resultado de sen^2(x) + cos^2(x) es:", resultado)

def main():
    numero = float(input("Ingrese un número: "))
    mostrar_funciones(numero)
   
    
    
if __name__ == "__main__":
    main()
