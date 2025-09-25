
print("\nDiccionario de información personal en Python")

#Crear un diccionario con información personal ficticia
informacion_personal = {
    "Nombre": "Robin",
    "Edad": 27,
    "Ciudad": "Guayaquil",
    "Profesion": "Desarrollador"
}
print("")
print(f"\nDiccionario Original:")
print("-------------------------------")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

#Acceder al valor de la clave "ciudad" y modificarlo por otra ciudad
informacion_personal["Ciudad"] = "Quito"

#Agregar una nueva clave-valor que represente la "Profesion"
informacion_personal["Ocupacion"] = "Freelancer"

#Verificar si la clave "Telefono" existe
if "Telefono" in informacion_personal:
    print("\n El teléfono ya existe.")
#Si no existe, agregar un número de teléfono ficticio
else:
    informacion_personal["Telefono"] = "0972582594"

# Eliminar la clave "Edad" ya que no es necesaria
del informacion_personal["Edad"]

# Imprimir el diccionario final
print("")
print(f"\nDiccionario final resultante:")
print("-------------------------------")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

print("\n😺¡Buen día!✨")