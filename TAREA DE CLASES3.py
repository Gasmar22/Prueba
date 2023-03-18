#1. Meter los números del 1 al 35 en una lista y mostrarla en pantalla. Hacer lo mismo
#para un rango de números indicado por un usuario.
"""lista= []
num=1
rango= int(input(": "))
while num <= rango:
    lista.append(num)
    num=num+1
print(lista)"""
#2. Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios.(***)
"""lista= []
cadena= input("Ingrese una oracion: ")
caracteres= len(cadena)
for i in range(caracteres):
   if cadena[i] != " ":
      lista.append(cadena[i])
print(lista)"""
#3. Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
#y posteriormente muestre en pantalla cada elemento de la lista junto con su
#cuadrado y su cubo.
"""lista= [1,2,5,4,3,6,2,1,7,9,]
for i in range(len(lista)):
   print("El cuadrado y cubo de:",lista[i],"es:",lista[i]**2,"y",lista[i]**3,"respectivamente.")"""

#1. Crea una tupla con números, pide un numero por teclado e indica cuantas veces
#se repite.
"""cont=0
lista= (1,2,3,4,3,6,7,4,2,3,6,1,2,5,5,2,4,3,3,6,6,4,7,1)
num= int(input("Ingresar un num: "))
for i in range(len(lista)):
   if lista[i] == num:
      cont=cont+1 
print("El numero",num,"aparece",cont,"veces")"""
#2. Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado
#y muestra los valores de la tupla.
"""t=(1,7,8,7,4,8,9,5,6,5)
indice= int(input("ingresa un indice del 0 al 10: "))
print("El indice",indice,"contiene el numero",t[indice])"""
#1. Crea un programa que pida un número al usuario un número de mes (por ejemplo,
#el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Para
#simplificarlo vamos a suponer que febrero tiene 28 días. Usar diccionarios

#NUEVOS-NUEVOS.

#4. Pedir una palabra al usuario, meter los todos sus caracteres en una lista y
#mostrarla en pantalla.
"""lista= []
cadena= input("Ingrese un texto: ")
for i in range(len(cadena)):
    lista.append(cadena[i])
print(lista)"""
#5. Realizar un programa que inicialice una lista con 10 números ingresados por el
#usuario y luego muestre en pantalla cual elemento es el menor
"""lista= []
for i in range(10):
    num= int(input("Ingrese el numero: "))
    lista.append(num)
men= lista[0]
for i in range(1,len(lista)):
    if men > lista[i]:
        men= lista[i]
print(men)"""
# Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso por ejemplo Matemáticas, Física,
# Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y 
# después las muestre por pantalla con el mensaje En «asignatura> has sacado <nota> 
# donde ‹asignatura> es cada una des las asignaturas de la lista y <nota> cada una 
# de las correspondientes notas introducidas por el usuario
"""tupla= ("Matematicas","Fisica","Quimica","Historia","Lengua")
for i in range(len(tupla)):
   nota=int(input(f"Que nota te sacaste en {tupla[i]}: "))
   print("En",tupla[i],"sacaste",nota)
print("Fin")"""
#1. Crea un programa que pida al usuario el nombre de un mes (Enero,
#Febrero, etc.) y diga cuántos días tiene (por ejemplo, 30. Para simplificarlo
#vamos a suponer que febrero tiene 28 días. Usar diccionarios
"""diccionario={"ENERO":"31","FEBRERO":"28","MARZO":"31","ABRIL":"30",
    "MAYO":"31","JUNIO":"30","JULIO":"31","AGOSTO":"31","SEPTIEMBRE":"30","OCTUBRE":"31","NOVIEMBRE":"30","DICIEMBRE":"31"}
nombre_mes= input("Ingrese el nombre de algun mes: ")
print("EL MES",nombre_mes,"CONTIENE",diccionario[nombre_mes])"""
#2. Crear un programa que pida al usuario un nombre de un alumno, y luego muestre
#la lista de notas de ese alumno. Usar diccionarios
nombre_alumno= input("Ingrese el nombre del Alumno: ")
diccionario= {"Gaston":["4","8","9","1","4",],"Franco":["6","2","7","4","1","5"],"Fede":["7","8","6"],
              "Lautaro":["4","10","2","6","7"]}
print("El alumno",nombre_alumno,"tiene una lista de notas de:",diccionario[nombre_alumno])
