#Leer x cantidad de edades y mostrar el promedio de dichas edades.
resp = "si"
edades = []
while(resp.upper() =="SI" ):
    try:
        edad = int(input("Que edad deseas agregar? "))
        edades.append(edad)
        resp = input("tenes otra edad que agregar mi estimado?")
    except Exception as ex:
        print("Error, porfavor inserte un dato valido")  


suma = 0
for edad in edades:
    suma += edad

media = suma/ len(edades)

print("la media es: ", media)