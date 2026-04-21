"""
Creacion de codigo que convierte numeros enteros positivos a simbolos romanos.
"""
def convertir_a_romano(numero):
    if numero <= 0:
        return "Error: El número debe ser un entero positivo."
    
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    resultado = ""
    for i in range(len(valores)):
        while numero >= valores[i]:
            resultado += simbolos[i]
            numero -= valores[i]
    
    return resultado

def main():
    numero = int(input("Ingrese un número entero positivo: "))
    romano = convertir_a_romano(numero)
    print(f"El número {numero} en números romanos es: {romano}")

if __name__ == "__main__":
    main()  

    