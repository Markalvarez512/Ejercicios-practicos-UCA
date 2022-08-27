
#Dado el primer nombre, segundo nombre, primer apellido y el segundo apellido de un
#estudiante de manera individual, escriba un código en Python que permita crear un correo
#electrónico utilizando la siguiente sintaxis: primer nombre + punto (.) + primer apellido +
#“@est.uca.edu.ni”

print("Hola Bienvenido al sistema de creacion de correos automaticos de la UCA")
print("Para poder crear tu correo solo necesitaremos tu nombre y apellido")
primernombre = input("Dime cual es tu primer nombre?: ")
print("Hola ", primernombre, "Mucho gusto") 
segundonombre=input("cual es tu segundo nombre: ")
primerapellido = input("Ahora dime cual es tu primer apellido?:  ")
segundoapellido = input("Ahora dime cual es tu segundo apellido?:  ")
usuario = primernombre + (".") + primerapellido
print("Hola ",primerapellido,"su correo que sera asignado de la UCA sera:", usuario,"@est.uca.edu.ni")