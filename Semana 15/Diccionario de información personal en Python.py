
print("\nDiccionario de información personal en Python")

#Crear un diccionario con información personal ficticia
informacion_personal = {
    "Nombre": "Robin",
    "Edad": 27,
    "Ciudad": "Guayaquil",
    "Profesion": "Desarrollador"
}
# Imprimir el diccionario original
print(f"\nDiccionario Original:\n{informacion_personal}")

#Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["Ciudad"] = "Quito"

#Agregar una nueva clave-valor que represente la "profesion"
informacion_personal["Ocupación"] = informacion_personal["Profesion"]

#Verificar si la clave "Telefono" existe
if "Telefono" in informacion_personal:
    print("\n El teléfono ya existe.")
#Si no existe, agregar un número de teléfono ficticio
else:
    informacion_personal["Telefono"] = "0972582594"

# Eliminar la clave "Edad" ya que no es necesaria
del informacion_personal["Edad"]

# Imprimir el diccionario final
print(f"\nDiccionario final resultante:\n{informacion_personal}")

print("\n😺¡Buen día!✨")