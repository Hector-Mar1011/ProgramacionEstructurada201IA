from faker import Faker
fake = Faker('es_MX')

#1. Declaración de un vector vacio
ciudades_ia = []

#2. Operaciones de llenado (Ciclo)
for _ in range(5):
    ciudades_ia.append(fake.city())

#3. Escritura de arreglos (Mostrar resultados)
print("\n--- DATASET DE CIUDADES GENERANDO ---")

for i in range(len(ciudades_ia)):
    print(f"registro{i+1}: {ciudades_ia[i]}")