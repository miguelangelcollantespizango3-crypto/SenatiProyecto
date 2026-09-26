# SOMOS DE PERÚ, EL USUARIO VE DECIDIR QUE DINERO HARA EL CAMBIO
# euro, dolar, yuanes.....
print("Escribe el numero del tipo del cambio")
print("1. us Dólares \n"
      "2. eu Euros \n"
      "3. GB Libras \n"
      "4. CN yuanes \n"
      "5.BR Reales")




tipo_cambio = input("Ingrese el número aqui para hacer el cambio: ")
convertir_minuscula = tipo_cambio.lower()
dinero = float(input("Ingresé la cantidad de dinero: "))
cambio = 0
if convertir_minuscula == "1":
    cambio = dinero * 0.2982
    nombre_dinero = "Dólar"
elif convertir_minuscula == "2":
    cambio = dinero *0.256
    nombre_dinero = "Euros"
elif convertir_minuscula == "3":
    cambio = dinero *0.221
    nombre_dinero = "Libras"
elif convertir_minuscula == "4":
    cambio = dinero *2.05
    nombre_dinero = "Yuanes"
elif convertir_minuscula == "5":
    cambio = dinero *1.76
    nombre_dinero = "Reales"

else:
    print("Escoge lo que esta en la lista. ")
print("Usted escogio: ", nombre_dinero.upper())
print("El monto cambiado es: ", cambio)
print(f"El monto cambiado es: {cambio}")
