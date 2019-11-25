usuarios={}
preg="SI"
ingrese=1
contador=0


print("\n bienvenidos a nuestro sistema, es un gusto brindarle nuestros servicios")
while preg=="Si":
        while ingrese==1:
          print("\n ingrese datos para ingresar nuevo usuario\n")

nombre=input("ingrese su nombre")
apellido=input("ingrese su apellido")
edad=input("Ingrese su edad")
documento= input("Ingrese su documento")
peso= input("ingrese su peso")
estatura=input("ingrese su estatura")

mensaje="¡¡Registro exitoso!!" 
print(mensaje)

pregunta=input("\n1. si desea ingresar otro usuario\n2. si desea continuar ")

usuarios[documento]={"nombre":nombre , "apellido":apellido ,"edad":edad ,"peso":peso , "estatura":estatura}

        

menu=("\n marque segun lo pedido\n\n")
menu=("1. para mostrar menu\n")
menu=("2. para consultar")
menu=("3.para seguir con el proceso\n")

print(menu)
pregunta=(input("digite:    "))

if pregunta=="1":
 for key  in usuarios:
     print (key, ":" ,usuarios[key])

if pregunta=="2":
        documento = input ("id para consultar: ") 
        consulta=usuarios[documento]
        print("paciente consultado: ",consulta)
               
pregunta=(input("\n ingrese ok para terminar\n ingrese si para salir:"))
                

print("\n GRACIAS POR UTILIZAR NUESTROS SERVICIOS")


        
