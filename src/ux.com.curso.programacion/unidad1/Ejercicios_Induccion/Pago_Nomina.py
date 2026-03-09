#ejercicio de inducción: pago de nómina

numero_horas = float(input("Ingrese el número de horas trabajadas:  "))
Tarifa_hora = float(input("Ingrese la tarifa por hora: "))
Nombre_Empleado = input("Ingrese el nombre del empleado: ")

#Las horas superiores a 35 se pagan como extra

if numero_horas > 35:
    horas_extra = numero_horas -35
    pago_bruto = (35 * Tarifa_hora) + (horas_extra * Tarifa_hora * 1.5)
else:
    pago_bruto = numero_horas * Tarifa_hora

#Calculo de impuesto
if pago_bruto <=2000:
    impuesto = 0
elif pago_bruto <=2220:
    impuesto = (pago_bruto - 2000) * 0.20
else:
    impuesto = (pago_bruto - 2220) * 0.30 + 220 * 0.20

pago_neto = pago_bruto - impuesto

#Mostrar Resultados

print(f"Empleado: {Nombre_Empleado}")
print(f"Pago Bruto: ${pago_bruto:.2f}")
print(f"Impuestos: ${impuesto:.2f}")
print(f"Pago Neto: ${pago_neto:.2f}")

