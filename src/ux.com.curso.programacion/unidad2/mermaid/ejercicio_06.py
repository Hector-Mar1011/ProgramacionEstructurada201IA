"""
implementación en python un algoritmo de seguimiento de saldo acumulativo
 siguiendo estrictamente la lógica de control de flujo
"""

def fondos():
    saldo = 0
    meta = 1000
    while saldo <= meta:
        deposito = int(input("Ingrese el deposito: "))
        saldo += deposito
    return saldo

def main():
    resultado = fondos()
    print("Meta superada $:", resultado)

if __name__ == "__main__":
    main() 