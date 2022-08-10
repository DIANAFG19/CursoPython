# TIPO DE DATO
mi_tuple = (1, 2, 3, 4)  # mi_tuple = 1,2,3,4
print(type(mi_tuple))

# BUSCAR EN UN DETERMINADO ÍNDICE
print(mi_tuple[2])
print(mi_tuple[-2])

mi_tuple2 = (1, 2, (10,20), 4)
print(mi_tuple2[2][1])

# MODIFICAR TUPLE
# mi_tuple[0] = 5
# print(mi_tuple) # TypeError: 'tuple' object does not support item assignment

# CASTING
mi_tuple2 = list(mi_tuple2)
print(type(mi_tuple2))
print(mi_tuple2)

# ASIGNAR LOS VALORES A VARIABLES
t = (1,2,3)
x,y,z = t
print(x,y,z)

# CANTIDAD DE ELEMENTOS DE TUPLE
tuple1 = (1,2,3,1,1)
print(len(tuple1))

# CONTAR ELEMENTOS REPETIDOS
print(tuple1.count(1))

# BUSCAR EN ÍNDICE DE UN VALOR
print(tuple1.index(3))
