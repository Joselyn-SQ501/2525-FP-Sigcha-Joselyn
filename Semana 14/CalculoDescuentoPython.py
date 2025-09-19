
print("\nCALCULAR EL DESCUENTO EN COMPRAS")

# Función para calcular el descuento
def calcular_descuento(monto_compra, porcentaje_descuento = 10):
    """
    Función que calcula el descuento de una compra.
    :param monto_compra: float, monto total de la compra
    :param porcentaje_descuento: float, que usa el 10% de descuento por defecto.
    :return: float, monto del descuento
    """
    descuento = monto_compra * (porcentaje_descuento / 100) #Operación para calcular el descuento
    return descuento


# Programa principal
if __name__ == "__main__":
    # Primera llamada: el usuario ingresa el monto de su compra
    monto1 = float(input("\n💰 Ingresa el monto de tu primera compra: $ "))
    # Mensaje al usuario sobre el % de descuento por defecto para su primera compra.
    print(f"\n👁‍ El porcentaje de descuento para tu primera compra es del 10% por defecto")
    descuento1 = calcular_descuento(monto1)  # Llamada a la función que usa el 10% de descuento por defecto para el cálculo
    total1 = monto1 - descuento1 #Operación para calcular el monto final a pagar
    # Muestra los resultados obtenidos de la llamada a la función junto con los datos solicitados.
    print(f"\n🛒 Compra 1 -> Monto: ${monto1}. Descuento: ${descuento1:.2f}. Total a pagar: ${total1:.2f}")

    print("-" * 50) #Decoración para separar los datos de cada compra

    # Segunda llamada: usuario ingresa monto + porcentaje deseado
    monto2 = float(input("\n💰 Ingresa el monto de tu segunda compra: $ "))
    # El usuario ingresa el % de descuento
    porcentaje = float(input("\n🏷️ Ingrese el porcentaje de descuento que se aplicará en tu compra: % "))
    descuento2 = calcular_descuento(monto2, porcentaje) # Segunda llamada a la función que usa el % de descuento ingresado por el usuario
    total2 = monto2 - descuento2  #Operación para calcular el monto final a pagar
    # Muestra los resultados obtenidos de la llamada a la función junto con los datos solicitados.
    print(f"\n🛒 Compra 2 -> Monto: ${monto2}. Descuento: ${descuento2:.2f}.Total a pagar: ${total2:.2f}")

    print("-" * 50) #Decoración

print("\n😺¡Vuelve pronto para calcular el descuento de tu próxima compra!🛍️ ¡Buen día!✨")
