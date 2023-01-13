nombres = ['Juan', 'Diana', 'Laura', 'Jesús', 'Luis', 'Fernando']

for nombre in nombres:
    indice = nombres.index(nombre)
    print(f"Hola {nombre}, tu índice en el arreglo es {indice}.")

for nombre in nombres:
    if nombre.startswith('L'):
        print(nombre)

##############################################################################################################
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mi_valor = 0
for num in numeros:
    mi_valor += num
print(f"Mi valor final es: {mi_valor}")

##############################################################################################################
palabra = "Python"
for letra in palabra:
    print(letra)

##############################################################################################################
for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)

##############################################################################################################
dic = {'clave1':'a', 'clave2':'b', 'clave3':'c', 'clave4':'d'}
for item in dic:
    print(item)

for item in dic.items():
    print(item)

for item in dic.values():
    print(item)

for a, b in dic.items():
    print(a, b)
