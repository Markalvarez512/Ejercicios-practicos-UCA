#Mostrar los numero pares comprendidos entre un valor inicial y un valor final de números
#enteros.
print("ingrese el primer numero: ")
num1= int(input())
print("ingrese el numero final: ")
num2= int(input())
print("Los numeros pares comprendidos entre el"), num1, ("y el"), num2, ("son")
while num1 <= num2:
    if num1 % 2 ==0:
        print(num1)
    num1+=1
