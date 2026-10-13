# INTRODUCCIÓN A LAS VARIABLES EN PYTHON

# Una variable permite almacenar un dato para utilizarlo
# posteriormente dentro del programa.

nombre       = "Moises"       
documento    = 54321
direccion    = "Medellin"  
tiene_deudas = True  

# MOSTRAR EL CONTENIDO DE UNA VARIABLE

print(nombre)

# CONCATENACIÓN USANDO +

print("CONCATENACIÓN USANDO +")
print("=" * 30)

print("Mi nombre es: " + nombre + " y mi documento es: " + str(documento))


# ============================================================
# CONCATENACIÓN USANDO ,
# ============================================================

print("\nCONCATENACIÓN USANDO ,")
print("=" * 30)

# Al utilizar comas, Python permite mostrar diferentes
print("Mi nombre es:", nombre, "y mi documento es:", documento)

# CONCATENACIÓN USANDO F-STRINGS

print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)

print(f"Mi nombre es: {nombre} y mi documento es: {documento}")

# F-STRINGS CON VARIAS VARIABLES

print("\nMOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("=" * 30)


# Las f-strings también permiten crear textos
# de varias líneas utilizando triple comilla.
print(f"""
Nombre:         {nombre}
Documento:      {documento}
Dirección:      {direccion}
¿Tiene deudas?: {tiene_deudas}
""")


# F-STRINGS CON COMILLAS SIMPLES

print("=" * 30)

print(f"""
Nombre:         {nombre}
Documento:      {documento}
Dirección:      {direccion}
¿Tiene deudas?: {tiene_deudas}
""")


# SALTO DE LÍNEA EN PYTHON

print(f"\nHola, {nombre}!")
print(f"Bienvenida {nombre} a Python.\n")

