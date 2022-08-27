#Leer los datos de un estudiante como el nombre, los apellidos, la carrera y su promedio.
#Evaluar si apto para beca, el estudiante podrá optar a beca si su promedio es mayor a 85
#en todas las carreras excepto Ingeniería de Sistemas donde su promedio debe ser mayor a
#95.

resp = "ingeneria en sistemas"
promedio = 0
print("Bienvenido al programa donde podras averiguar si eres apto para becas en la UCA")
Nombre = input("Pofavor dime tu nombre: ")
apellido = input("Ahora dime tu apellido: ")

print("Muchas gracias por esa informacion", Nombre)
carrera =input("podrias decirme cual carrera estas cursando actualmente?")
if carrera == resp:
    promedio = int(input ("Digite el promedio que usted tiene: "))
    if promedio >= 95:
        print("Felicides usted puede optar a una beca para su carrera")
    else:
        print("Lo sentimos mucho , usted ", Nombre, "no es apto para una beca")
else:
     promedio = int(input ("digite el promedio que usted tiene: "))

     if promedio >= 85:
        print("Felicides usted puede optar a una beca para su carrera")
     else:
        print("Lo sentimos mucho , usted ", Nombre, "no es apto para una beca")


