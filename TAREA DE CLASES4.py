"""MODULO"""
#1. Escriba una función que muestre todos los números primos entre 1 y un número n que
#es ingresado por parámetro.
"""lista=[]
n= int(input("Ingrese un numero: "))
def ListaPrimos(n):
    i=1
    while i <= n:
        pd=2
        while pd <= i/2 and i%pd != 0:
            pd=pd+1 
        if pd>i/2 and i != 1 : 
            lista.append(i)
        i=i+1
    return lista
print(ListaPrimos(n))"""
#▪ 2. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si
#la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se
#considerará válida si contiene el símbolo "@".
#▪ (find) →
email= input("Ingrese su correo electronico: ") 

def correo_electronico(email):
    if "@" in email:
        print("El correo es valido")
        return True
    else: 
        print("El correo es falso")
        return False

print(correo_electronico(email))
 
   

#▪ 3. Definir una función que muestre el factorial de un número

#▪ 4. Escriba una función que le pida al usuario ingresar condimentos para un sándwich,
#hasta que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un
#mensaje avisando que ya se agregó el condimento al sándwich.