"""
Creacion de un programa que verifique la validez de una fecha introducida por el usuario.
"""

def anno():
    Anno = int(input("Ingrese el año: "))
    return Anno

def mes():
    Mes = int(input("Ingrese el mes: "))
    return Mes

def dia():
    Dia = int(input("Ingrese el día: "))
    return Dia

def validar_fecha(anno, mes, dia):
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    if mes == 2:
        if anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0):
            if dia > 29:
                return False
        else:
            if dia > 28:
                return False
    return True

def main():
    anno = anno()
    mes = mes()
    dia = dia()
while True:
        if validar_fecha(anno, mes, dia):
            print("La fecha es válida.")
            break
        else:
            print("La fecha no es válida.")

if __name__ == "__main__":
    main()