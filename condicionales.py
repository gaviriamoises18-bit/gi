# Ejercicio 1: Determinar si un número es positivo, negativo o cero
numero = float(input("Ingrese un número: "))

if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print("El número es cero")



# Ejercicio 2: Verificar si una persona es mayor de edad
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")



# Ejercicio 3: Determinar si un número es par o impar
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")


# Ejercicio 4: Clasificar una nota académica
nota = float(input("Ingrese la nota obtenida (0.0 a 5.0): "))

if nota >= 4.5:
    print("Desempeño superior")
elif nota >= 3.5:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Desempeño básico")
else:
    print("Desempeño bajo") 


# Ejercicio 5: Determinar el mayor de tres números
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

print(f"El mayor de los tres números es: {mayor}")


#Taller resuelto en clase 

#Ejercicio 1: soicitar nombre y edad y si es mayor o menor de edad


print("=" * 30)
print("Ejercicio 1: Solicitar nombre y edad y determinar si es mayor o menor de edad")
print("=" * 30)


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
mayor = 18

if edad < 0:
    print(f"Error: La edad {edad} Invalida") 

elif edad < 18:
    print(f"{nombre}, Eres menor de edad, te faltan {(mayor) - (edad)} años para ser mayor de edad")

else:
    print(f"{nombre}, Tienes {edad} años, eres mayor de edad" )

print("=" * 30)
print("Ejercicio 2: Clasificacion de un estudiante")
print("=" * 30)


#Ejercicio 2: Clasificacion de un estudiante

nombre = input("Cual es su nombre?: ")

nota = float(input("Cual es su nota? (De 0.0 a 5.0): "))

if nota < 0.0:
    print("Nota invalida")

elif nota <= 2.9:
    print(f"{nombre}, Su nota final es de {nota} y su desempeño es insuficiente. Esta reprobado ")

elif nota <= 3.5:
    print(f"{nombre}, Su nota final es de {nota} y su desempeño es aceptable. Esta aprobado")

elif nota <= 4.5:
    print(f"{nombre}, Su nota final es de {nota} y su desempeño es bueno. Esta aprobado")

elif nota <= 5.0:
    print(f"{nombre}, Su nota final es de {nota} y su desempeño es exelente. Esta aprobado")

else:
    print("Nota invalida")


print("=" * 30)
print("Ejercicio 3: Calcular el descuento de una compra")
print("=" * 30)


#Ejercicio 3: algoritmo que solicite el nombre del cliente y el valor de la compra, y calcule el descuento según el valor de la compra. 

#cliente y valor


nombre = input("ingrese su nombre: ")
valor_compra =float(input(f"{nombre} ingrese el valor de la compra: ")) 
  
if valor_compra <0:
    print(f"{nombre} el valor de la compra es invalido")  
elif valor_compra <100000:
    print(f"{nombre}el valor de la compra es {valor_compra} y no tiene descuento")

elif valor_compra >=100000 and valor_compra <299999:
    descuento = valor_compra * 0.10
    total = valor_compra - descuento
    print(f"{nombre} el valor de la compra es {valor_compra} y el descuento es 10% {descuento} y el total a pagar es {total}")
    
elif valor_compra >=300000 and valor_compra <499999:
    descuento = valor_compra * 0.15
    total = valor_compra - descuento
    print(f"{nombre} el valor de la compra es {valor_compra} y el descuento es 15% {descuento} y el total a pagar es {total}")

elif valor_compra >=500000 and valor_compra <999999:
    descuento = valor_compra * 0.20
    total = valor_compra - descuento
    print(f"{nombre} el valor de la compra es {valor_compra} y el descuento es 20% {descuento} y el total a pagar es {total}") 


print("=" * 30)
print("Ejercicio 4: Clasificacion de la temperatura por ciudad")
print("=" * 30)


#EJERCICIO 4: algoritmo que solicite la ciudad y la temperatura actual, y clasifique la temperatura según los rangos establecidos.


ciudad = input("Ingrese la ciudad donde actualmente vive: ")
temperatura = int(input("Ingrese la temperatura actual en grados celcius: "))

                 #Validaciones
if temperatura <10:
    print(f"Te vas a congelar, muy fria")
elif temperatura in range (10,17):
    print(f"Hace algo de frio, se recomienda usar abrigo")
elif temperatura in range (18,25):
    print(f"Hace buen clima, está mas bien como templado")
elif temperatura in range (26,32):
    print(f"Que hp chispa, está muy caliente")
elif temperatura >32:
    print(f"Ojo manito que se derrite, insoportable este bochorno")

print(f"Tu ciudad es {ciudad} y la temperatura actual es {temperatura}")


print("=" * 30)
print("Ejercicio 5: Clasificacion de un empleado y su salario")
print("=" * 30)


# Ejercicio 5: empleado y salario


var_nombre = input("Ingrese nombre del empleado: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))

salario = valor_hora * horas_trabajadas
var_seguridad = salario * 0.08 


if horas_trabajadas < 0 or valor_hora < 0:
    print("Error: Las horas trabajadas y el valor por hora deben ser números positivos.")

elif horas_trabajadas <= 160:

    salario_neto = salario - var_seguridad
    print(f""" === RESUMEN DE PAGO SALARIO ===
    -Salario: {salario} 
    -Seguridad social {var_seguridad} 
    -Salario neto es: {salario_neto}
    """)

elif horas_trabajadas > 160:

    horas_extras = horas_trabajadas - 160
    valor_horas_extras= (horas_extras* valor_hora )* 1.25
    salario_neto = (valor_hora * horas_trabajadas) + valor_horas_extras - var_seguridad

    print (f""" == RESUMEN DE PAGO SALARIO ==
    -Horas extras {horas_extras} Valor Horas Extras {valor_horas_extras}
    -Salario basico: {salario}
    -seguridad social {var_seguridad} 
    -salario total {salario_neto} 

""")