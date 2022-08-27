#Dado el numero de cuenta, el saldo y el monto de retiro de una cuenta de ahorra verifique
#si la persona puede realizar el retiro. Una vez evaluado debe mostrarse el saldo que queda
#después del retiro.

print("Bienvenido a tu banca en linea favorita")
try:
    Saldo = float(input("Digite cuanto saldo tiene en su cuenta: "))
    Retiro= float(input("Digite cuanto dinero desea sacar de su cuenta: "))
    saldorestante = Saldo - Retiro
    print("Usted acaba de retirar", Retiro, "$ " "con exito!")
    print("El sado restante en su cuenta es: ", saldorestante, "$")
    
    
except Exception as ex:
        print("Error, porfavor inserte un dato valido") 


