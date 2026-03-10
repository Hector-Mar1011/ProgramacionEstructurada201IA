def imprimir_identificadores():
    # Identificadores validos
    nombre_usuario = "Alumno" # Inicia con letra y tiene guion bajo
    sensor = "Temperatura"  # Inicia con letra
    _id_interno =12 # Puede contener guion bajo y números

    print(nombre_usuario)
    print(sensor)
    print(_id_interno)


# Nombre correcto de funciones
def calcular_area():
    print("Calculando el área...")

def main():
    imprimir_identificadores()
    calcular_area()

if __name__ == "__main__":
    main()
    


