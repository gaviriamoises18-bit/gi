"""

# Ejercicio 1: Suma de dos números


numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2

print(f"La suma es: {suma}")


# Ejercicio 2: Área de un rectángulo


base   = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

area = base * altura 

print(f"El área del rectángulo es: {area}")


# Ejercicio 3: Conversión de minutos a horas y minutos
minutos_totales = int(input("Ingrese la cantidad de minutos: "))

horas   = minutos_totales // 60 
minutos = minutos_totales % 60

print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos.")


# Ejercicio 4: Cálculo del precio con descuento
precio    = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

valor_descuento = precio * (descuento / 100)   # valor que se descuenta
precio_final    = precio - valor_descuento

print(f"El precio final con descuento es: {precio_final}")


# Ejercicio 5: Intercambio de valores entre dos variables
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

auxiliar = a   
a = b          
b = auxiliar

print(f"Después del intercambio: a = {a} , b = {b}")
"""

#Taller 

# Ejercicio 1: solicitar el largo y ancho de un terreno rectangular y calcular su perimetro

largo = float(input("Ingrese el largo del terreno: "))
ancho = float(input("Ingrese el ancho del terreno: "))

perimetro = 2 * (largo + ancho)

print(f"El perímetro del terreno es: {perimetro}")

# Ejercicio 2: Promedio 3 numeros

Numero1 = float(input("Ingrese el primer número: "))
Numero2 = float(input("Ingrese el segundo número: "))
Numero3 = float(input("Ingrese el tercer número: "))

print("\n")
print(f"El promedio de los tres numeros es {(Numero1 + Numero2 + Numero3) / 3}")

""""""

# Ejercicio 3: solicitar edad y mostrar mensaje de presentacion

nombre = input("Cual es su nombre?: ")
edad = int(input("Cual es su edad?: "))
860
print(f"Hola, mi nomnbre es {nombre} y tengo {edad} años")


# Ejercicio 4: solicitar un valor en pesos colombianos y mostrar su equivalente aproximado en dolares (tasa fija: 1 USD = 4000cop)


peso = int(input("Cuanto es el valor que quieres convertir?:  "))

dolar = peso / 4000

print(f"El valor en dolares es: {dolar} USD")

# Ejercicio 5: Solicitar una cantidad en segundos y convertirla a horas, minutos y segundos

segundos = int(input("Ingrese la cantidad de segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")