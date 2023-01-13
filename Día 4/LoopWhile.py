monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas.")
    monedas -= 1
else:
    print("No tengo más monedas")

####################################################################################
respuesta = 's'
while respuesta == 's':
    respuesta = input("¿Quieres continuar? (s/n): ")
else:
    print("Gracias por visitarnos.")

####################################################################################
while respuesta == 's':
    pass
print("Hola.")

####################################################################################
nombre =input("Ingresa tu nombre: ")
for letra in nombre:
    if letra == 'a':
        break
    print(letra)

####################################################################################
for letra in nombre:
    if letra == 'a':
        continue
    print(letra)

####################################################################################
numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    else:
        numero -= 1
        continue
    numero -= 1