"""
Implementación en python de un inicio de sesión siguiendo una logica de iteración y desición 
anidada definida.
"""

def Seguridad():

    intentos= 0
    clave_correcta= "1234"

    while intentos <= 3:

        clave = input("Ingresa la contraseña porfavor: ")
        if clave == clave_correcta:
            print("¡Acceso concedido!")

            break

        elif clave:
            intentos = intentos + 1
            print("¡Error!, Contraseña incorrecta")

            if intentos > 3:
                print("Acceso denegado, cuenta bloqueada")    
    

def main():
    Seguridad()

if __name__ == "__main__":
    main() 
