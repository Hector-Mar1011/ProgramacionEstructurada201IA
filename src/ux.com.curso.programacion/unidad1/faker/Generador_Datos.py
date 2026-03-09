#importar la libreria Faker
from faker import Faker

faker = Faker("es_MX")

print("Generando Datos Dummy con Faker")

print(f"nombre: {faker.name()}")
print(f"nombre: {faker.address()}")
print(f"nombre: {faker.phone_number()}")
print(f"nombre: {faker.email()}")

