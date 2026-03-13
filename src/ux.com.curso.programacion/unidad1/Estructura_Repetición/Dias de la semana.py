# Ejercicio de dias de la semana

def dias_semanas():
    opcion = input("Ingrese una opcion (1-7):")

    match opcion:
        case "1":
            print("Opcion 1 seleccionada")
            print(f"Hola, tu dia es el LUNES!")
        case "2":
            print("Opcion 2 seleccionada")
            print(f"Hola, tu dia es el MARTES ")
        case "3":
            print("Opcion 3 seleccionada")
            print(f"Hola, tu dia es el MIERCOLES")
        case "4":
            print("Opcion 1 seleccionada")
            print(f"Hola, tu dia es el JUEVES!")
        case "5":
            print("Opcion 2 seleccionada")
            print(f"Hola, tu dia es el VIERNES ")
        case "6":
            print("Opcion 3 seleccionada")
            print(f"Hola, tu dia es el SABADO")
        case "7":
            print("Opcion 3 seleccionada")
            print(f"Hola, tu dia es el DOMINGO")
        case _:
            print("Opción no válida")

def main():
    dias_semanas()
   
    
    
if __name__ == "__main__":
    main()
