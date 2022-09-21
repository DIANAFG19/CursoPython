texto = input("Escribe un texyo largo: ")
letras = []

texto = texto.lower()

letras.append(input("Escriba la primer letra: ").lower())
letras.append(input("Escriba la segunda letra: ").lower())
letras.append(input("Escriba la tercer letra: ").lower())

print("\n¿CUÁNTAS VECES APARECE CADA LETRA?")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces.")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces.")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces.")

print("\n¿CUÁNTAS PALABRAS HAY EN TOTAL?")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} en el texto.")

print("\nPRIMERA Y ÚLTIMA LETRA DEL TEXTO")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"La primer letra es '{letra_inicio}' y la letra final es '{letra_fin}'.")

print("\nTEXTO EN ORDEN INVERSO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"El orden inverso del texto es: '{texto_invertido}'")

print("\n¿APARECE PYTHON EN EL TEXTO?")
buscar_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto.")

