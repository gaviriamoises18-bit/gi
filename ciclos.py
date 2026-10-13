#Ciclos Repetitivos:

print("=" * 30)
print("#Ciclo for = repite por cantidad de veces")
print("=" * 30)

for i in range (11):
    print(f"{i}     Hola Mundo")


print("=" * 30)
print("#Configurar posicion Inicial y final")
print("=" * 30)

for i in range (1,101):
    print(f"{i}     Hola Mundo")

print("=" * 30)
print("#Configurar posicion Inicial, final y el incremento")
print("=" * 30)

for i in range (0,101,5):
    print(f"{i}     Hola Mundo")


print("=" * 30)
print("#Adivina el numero secreto")
print("=" * 30)

import random

numero_secreto = random.randint(1,10)
intentos = 3

for i in range (intentos): #Ciclo parar que se escriba varias veces el numero
    numero = int(input("Adivina el numero secreto entre 1 y 10: "))

    if numero == numero_secreto :
        print("Felicidades Adivinaste. ")
        break   

    else:
        intentos_restantes = intentos - (i + 1)
        print(f"Te quedan {intentos_restantes} Intentos")

#Verificar si no le quedan intentos y mostrar el numero

if intentos_restantes == 0 :
    print(f"Has perdido, el numero secreto era {numero_secreto}. ")



# Ejercicio 1: Mostrar la tabla de multiplicar de un número

numero = int(input("Ingrese un numero para ver su tabla de multiplicar hasta el 10: "))

for i in range(1,11):          # recorre los valores del 1 al 10
    print(f"{numero} x {i} = {numero * i}")



# Ejercicio 2: Sumar los primeros n números naturales
n = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(1, n + 1):
    suma = suma + i

print(f"La suma de los primeros {n} números naturales es: {suma}")


# Ejercicio 3: Contar cuántos números pares hay entre 1 y n
n = int(input("Ingrese un número entero positivo: "))

contador = 0
numero   = 1
while numero <= n:
    if numero % 2 == 0:
        contador = contador + 1
    numero = numero + 1

print(f"Hay {contador} números pares entre 1 y {n}")

# Ejercicio 4: Solicitar una contraseña hasta que sea correcta
clave_correcta  = "python2026"
clave_ingresada = input("Ingrese la contraseña: ")

while clave_ingresada != clave_correcta:
    print("Contraseña incorrecta, intente de nuevo")
    clave_ingresada = input("Ingrese la contraseña: ")

print("Contraseña correcta, acceso concedido")

# Ejercicio 5: Calcular el factorial de un número

n = int(input("Ingrese un número entero no negativo: "))

factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(f"El factorial de {n} es: {factorial}")