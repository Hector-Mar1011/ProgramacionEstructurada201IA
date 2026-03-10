# Creacion de codigo en base al diagrama de flujo hecho en clase
"""
Se definio esta funcion para que sea un bucle y siga preguntando la misma incognita, dicha funcion llamada
Calificaciones clasifica las calificaciones con letras (A,B,C,D,F) mediante condicionales.
"""
def calificaciones():
    while True: # Este while tiene la función de crear un bucle con el cual se repita la pregunta para clasificar los datos.
        cierre = "abierto"

        calificacion = float(input("Ingrese su calificación: "))
        if calificacion >= 90:

            print("Tu calificacion es rango A")

        elif calificacion <90 and  calificacion >=80:
            
            print("Tu calificación es rango B")

        elif calificacion <80 and calificacion >=70:

            print("Tu calificación es rango C")
        
        elif calificacion <70 and calificacion >=69:

            print("Tu calificación es rango D")
        
        elif calificacion <69:
            
            print ("Tu calificacion es rango F")
            

        if cierre == "cerrar":
            break

def main():
    calificaciones()
   
    
    
if __name__ == "__main__":
    main()

