texto = "Este es un texto, de Diana para, hacer pruebas"

mayus = texto.upper()
print(mayus)

minus = texto.lower()
print(minus)

dividir = texto.split(',')
print(dividir)

a = "Aprendiendo"
b = "Python"
c = "con"
d = "Diana"
unir = " ".join([a,b,c,d])
print(unir)

encontrar = texto.find("a")
print(encontrar)
encontrar = texto.rfind("a")
print(encontrar)

remplaza = texto.replace("e","x")
print(remplaza)