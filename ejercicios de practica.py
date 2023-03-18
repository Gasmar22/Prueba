"""suma=0
print("Ingrese la cant de numeros a sumar: ")
n=int(input())
for i in range(n):
    print(f"Ingrese el numero {i+1}: ")
    a=int(input())
    suma=suma+a
print(f"La suma de los {n} numeros es: {suma}")"""
"""x=0
cont=0
num= int(input("Ingrese el numero de veces que quiere repetir el ciclo: "))
while True:
    cont=cont+1
    x=x+1
    if(x == num):
        break
print(cont)"""
#Ejercicios seba#
#1)Escribí un programa que le solicité al usuario ingresar una fecha formada por 8 números,
#donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro el año (DDMMAAAA). Este dato debe
#guardarse en una variable con tipo int (número entero). Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.
"""num=int(input("Ingrese una fecha formada por 8 numeros: "))
if num != 0:
        año=num%10000
        num=num//10000
        mes=num%100
        num=num//100
        dia=num
        print("Su fecha de nacimiento es:",dia,"/",mes,"/",año)"""
#Escribí un programa que, dada una cadena de texto por el usuario, 
#imprima True si la cantidad de caracteres en la cadena es un número par, o False si no lo es.
"""x = input("Ingrese su cadena de texto y veremos si tiene caracteres pares o impares: ")
cont= len(x) 
if cont%2 == 0:
    print(True)
else:
    print(False)"""
#Escribí un programa que le pida al usuario ingresar dos palabras y las
#guarde en dos variables, y que luego imprima la palabra que tiene mas caracteres.
"""print("Ingrese dos palabras: ")
palabra1= input()
palabra2= input()
cont1= len(palabra1)
cont2= len(palabra2)
if cont1 > cont2: 
    print("La palabra",palabra1,"tiene mas caracteres.")
elif cont2 > cont1:
    print("La palabra",palabra2,"tiene mas caracteres.")
else: 
    print("Las dos tienen igual tamaño de caracteres.")"""
#Escribí un programa que, dado un número entero, muestre su valor absoluto. Recordá que, para los 
#números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los
#negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).
"""abs= int(input("Ingrese el numero: "))
if abs < 0: 
    absoluto= abs*-1
    print("El valor absoluto de",abs,"es",absoluto)
elif abs > 0: 
    print("el valor absoluto de",abs,"es",abs)"""



    