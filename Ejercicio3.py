#Aplicar el IVA al precio de un producto.
porcentajedeiva = 15
valor = float(input("ingrese el valor a calcular: "))
IVA = valor * (porcentajedeiva / 100)
PrecioconIVA = valor + IVA
print("El valor con IVA es : ", PrecioconIVA)
print("y el valor del IVA que fue agregado es", IVA)