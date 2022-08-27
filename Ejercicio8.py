#Leer x cantidad de precios y mostrar el precio mas alto y el precio más bajo.

listadeprecios = []
precio = float(input("cuantos precios quisiera introducir? "))
mayor = 0
menor = 0
i = 1

while (precio > 0):
    cantidadprecio = float(input("Precio #" + str(i) + ": "))
    listadeprecios.append(cantidadprecio)
    i = i+ 1
    precio = precio - 1

mayor = max(listadeprecios)
menor = min (listadeprecios)

print("Precios introducidos: ", listadeprecios)
print("Precio mayor de la lista: ", mayor)
print("Precio menor de la lista: ", menor)

