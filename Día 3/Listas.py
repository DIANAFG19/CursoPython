# TIPO DE DATO
mi_lista = ['a', 'b', 'c']
print(type(mi_lista))

# CALCULAR LONGITUD DE LISTA
mi_lista2 = ['hola', 55, 66.1]
print(len(mi_lista2))

# MOSTRAR ELEMENTOS DE LISTA
print(mi_lista2[0])
print(mi_lista2[0:2])

# CONCATENAR LISTAS
mi_lista3 = ['d', 'e', 'f']
mi_lista4 = mi_lista + mi_lista3
print(mi_lista4)

# MODIFICAR LISTA
mi_lista4[0] = 'alfa'
print(mi_lista4)

# AGREGAR A LISTA
mi_lista4.append('g')
print(mi_lista4)

# ELIMINAR DE LISTA
eliminado = mi_lista4.pop(4)
print(mi_lista4)
print(eliminado)

# ORDENAR LISTA
lista = ['g', 'a', 'x', 'm', 'c', 'p', 'f']
lista.sort()
print(lista)

# INVERSIÓN DE ORDEN DE LISTA
lista.reverse()
print(lista)

