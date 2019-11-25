num1=int(input("ingresa el primer numero "))
num2=int(input("ingresa el segundo numero "))


def calcular_numeros(num1,num2):
    if num1>num2:
       print("el primer numero es mayor")
       return num1
        
    else:
         if  num2>num1:
             print("el segundo numero es mayor")

             return num2

mensaje=calcular_numeros(num1,num2)         
print(mensaje)  
