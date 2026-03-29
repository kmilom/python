"""1. Variables y Operaciones"""

nombre = "Camilo"
edad = 25
promedio = 4.5

print(f"El estudiante {nombre} tiene {edad} de edad y un promedio de {promedio}")


"""2. Condicionales"""

#nota = float(input("Ingrese la nota: "))
nota = 4.6

if nota > 5.0 or nota < 0:
    print("Error")
elif nota >= 4.0:
    print("Aprobado")
elif nota >= 3.0:
    print("En recuperación")
else:
    print("Reprobado")


"""3. Lista de notas"""

notas = [3.5, 4.0, 2.8, 5.0, 3.2]

notas.sort()

promedio = sum(notas) / len(notas)

print(f"El promedio de las notas es: {promedio}, la nota más baja es {notas[0]} y la nota más alta es {notas[-1]}")


"""4. Filtrado"""

notas = [3.5, 4.0, 2.8, 5.0, 3.2]

aprobadas = [n for n in notas if n >= 3.0]

print(f"Las notas aprobadas son: {aprobadas}")

"""5. Conteo"""

conteo = 0
for n in notas:
    if n < 3.0:
        conteo += 1
print(f"Hay {conteo} notas por debajo de 3.0")

"""6. y 7. Tuplas"""

estudiante = ("Camilo", 25, "Ingeniería")
nombre, edad, carrera = estudiante

print(f"Valores de la tupla: {nombre, edad, carrera}")

"""Diccionarios"""

estudiante = {
    "nombre": "Camilo",
    "edad": 25,
    "notas": [3.5, 4.0, 2.8],
}

estudiante["promedio"] = sum(estudiante["notas"]) / len(estudiante["notas"])

if estudiante["promedio"] < 3.0:
    estudiante["estado"] = "Reprobado"
else:
    estudiante["estado"] = "Aprobado"

print(estudiante)

"""10. Lista de estudiantes"""

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def verificar_probados(estudiantes):
    aprobados = []
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["notas"])
        if promedio >= 3.0:
            aprobados.append(estudiante["nombre"])
    return aprobados

estudiantes = [
    {"nombre": "Camilo", "notas": [3.5, 4.0]},
    {"nombre": "Ana", "notas": [2.0, 2.5]},
    {"nombre": "Luis", "notas": [4.5, 5.0]}
]

print(verificar_probados(estudiantes))