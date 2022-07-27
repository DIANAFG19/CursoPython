nombre = input("Dime tu nombre: ")
ventasMes = float(input("¿Cuánto has vendido en este mes? "))
comision = ventasMes * 0.13
total = ventasMes + comision

print(f"OK {nombre}, este mes ganaste ${round(total,2)}")