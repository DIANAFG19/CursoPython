numero = int(input("Ingresa un número: "))
if numero >= 1 and numero <= 50:
    print(f"El número {numero} está dentro del rango 1 y 50.")
elif numero >= 51 and numero <= 100:
    print(f"El número {numero} está dentro del rango 51 y 100.")
else:
    print(f"El número {numero} está fuera del rango de 1 y 100.")