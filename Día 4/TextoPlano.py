
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
tipo_pago = input("Ingrese su tipo de pago: ")
ingredientes = "Estos son los ingredientes para preparar una michelada"
if edad >= 18:
    print("Estos son los ingredientes para preparar una michelada")
    print()
else:
    print("No eres mayor de edad, no te puedo enlistar los ingredientes de la michelada.")

archivo = open("datos.txt")
archivo.write(nombre)
archivo.write(edad)
archivo.write(tipo_pago)
archivo.write(ingredientes)