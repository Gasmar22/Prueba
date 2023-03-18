#1) Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo
#para un rango de números indicado por un usuario.
"""lista=[]
rango= int(input("ingrese el numero de rango de lista: "))
ini= 1 
while ini <= rango:
    lista.append(ini)
    ini=ini+1
print(lista)"""
    #2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por
#ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
"""tabla=int(input("Ingresa un numero para saber sus 10 primeros multiplos: "))
multiplicador=1 
lista= []
while multiplicador <= 10:
    producto=multiplicador*tabla
    lista.append(producto)
    multiplicador=multiplicador+1 
print(lista)"""
#3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir caracteres.
"""lista= []
cad= input("ingrese un texto: ")
cant= len(cad)
for i in range(cant):
    if not cad[i] in lista:
        lista.append(cad[i])
print(lista)"""
#4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios.
"""lista=[]
cadena= input("ingrese una cadena de texto: ")
for i in range(len(cadena)):
    if cadena[i] != " ": 
        lista.append(cadena[i])
print(lista)"""
#5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.
"""t=(1,2,5,4,6,3,2,8,7,9,1,2,4,5,7,8,9,3,2,1)
cont= 0
num= int(input("Ingrese un numero para saber cuantas veces esta en la lista: "))
for i in range(len(t)):
    if t[i] == num:
        cont=cont+1
print("El numero",num,"aparece en la lista",cont,"veces.")"""
#6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta entre 1 y la longitud máxima de la tupla,
#muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero
"""t= ('ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUMBRE','NOVIEMBRE','DICIEMBRE')
while True: 
    num=int(input("Ingresa un numero: "))
    if 1 <= num <= 12:
         print(t[num-1])
    elif num == 0:
         break
    else:
         print("error")"""
#7) Crea una tupla con números e indica el número con mayor valor y el que menor tenga.
"""t=(5,4,7,8,6,9,10,25,2,47,73,14,35,85)
may=0
men= t[1]
for i in range(len(t)):
    if t[i] > may: 
        may= t[i]
    elif t[i] < men:
        men= t[i]
print("El mayor valor de la lista es",may,"y el menor valor de la lista es",men)"""
#8) (Opcional)Escribir un programa que vaya solicitando al usuario que ingrese nombres. - Si el nombre se encuentra en la 
#agenda (implementada con un diccionario), debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no
#es correcto. - Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# El usuario puede utilizar la cadena "*", para salir del programa
"""dicc={"Agustin":"422158","Leandro":"472124","Ivana":"424199","Rocio":"428249","Fernando":"424217"}
while True:
    nombre=input("Ingrese el nombre del alumno: ")
    if nombre in dicc:
        SI=True
        print("El numero de telefono de",nombre,"es",dicc[nombre])
        num=input("Desea modificar su numero de telefono? En caso de que quiera cambiar ingrese SI de lo contrario NO: ")
        if num == SI:
            num_nuevo= int(input("Ingrese el nuevo numero telefonico: "))
            print(num_nuevo)
            (NO ME SALIO)"""
#9) Opcional: Pide números y mételos en una lista, cuando el usuario meta un 0 ya
#dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
"""lista= []
while True:
  num= int(input("ingrese numeros a su lista: "))
  if num != 0 :
     lista.append(num)
  elif num == 0 :
     break
cant= len(lista)
for i in range(cant):
   for y in range(i+1,cant):
      if lista[i] > lista[y]:
         aux=lista[y]
         lista[y]=lista[i]
         lista[i]=aux
print(lista)"""
#10) Opcional: Lo mismo que el anterior, pero ordenando de mayor a menor.
"""lista=[]
while True:
   num= int(input("Ingrese numeros su lista: "))
   if num != 0 :
      lista.append(num)
   elif num == 0 :
      break 
cant= len(lista) 
for i in range(cant):
   for y in range(i+1,cant):
      if lista[y] > lista[i]:
         aux=lista[i]
         lista[i]=lista[y]
         lista[y]=aux
print(lista)"""
