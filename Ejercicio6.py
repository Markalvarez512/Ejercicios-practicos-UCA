#Leer dos números y decir cual es mayor y cual es menor.
print("Programa para leer que numero es mayor y cual menor")
num1= int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 > num2:
    print (num1, "es el numero mayor de los numeros ingresados")
elif num2> num1:
    print(num2, "es el numero  mayor de los numeros ingresados")
if num1 < num2:
    print(num1, "es el numero menor de los numeros ingresados")
elif num2 < num1:
    print(num2, "es el numero menor de los numeros ingresados ")
        
