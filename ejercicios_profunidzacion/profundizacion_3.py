# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

notas = [70, 82, -1, 65, 55, 67, 87, 92, -1, 56, 34, 91, 0]

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Similar al ejercicio de "calificaciones":

Debe caluclar el promedio de todas las notas que se encuentra
almacenadas en una lista llamada "notas" que ya
hemos definido al comienzo del archivo

Luego transformar la califiación en una letra
según la siguiente escala:
- Si el puntaje es mayor igual a 90 --> imprimir A
- Si el puntaje es mayor igual a 80 --> imprimir B
- Si el puntaje es mayor igual a 70 --> imprimir C
- Si el puntaje es mayor igual a 60 --> imprimir D
- Si el puntaje es menor a  60      --> imprimir F

A medida que recorre las notas, no debe considerar como válidas aquellas
que son negativas, en ese caso el alumno estuvo ausente

Debe contar la cantidad de notas válidas y la cantidad de ausentes
'''

print("Mi organizador académico (#_#)")
# Empezar aquí la resolución del ejercicio

# Para calcular el promedio primero debe obtener la suma
# de todas las notas, que irá almacenando en esta variable
sumatoria = 0           # Ya le hemos inicializado en 0
reprobado=0
aprobado=0
cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo
cantidadA=0
cantidadB=0
cantidadC=0
cantidadF=0

# Realice aquí el bucle para recorrer todas las notas
# y cacular la sumatoria

# Terminado el bucle calcule el promedio como
# promedio = sumatoria / cantidad_notas

# Utilice la nota promedio calculada y transformela
# a calificación con letras, imprima en pantalla el resultado

# Imprima en pantalla al cantidad de ausentes

for i in notas:

    if i<=0:
        print("AUSENTE")
        cantidad_ausentes+=1
    elif i >= 0 and i <= 59 :
        print ("Usted tiene una F y esta reprobado")
        reprobado+=1
        cantidad_notas+=1
        sumatoria+=i
        cantidadF+=1
    elif i >=60 and i <=69 :
        print ("Usted tiene una C")
        aprobado+=1
        cantidad_notas+=1
        sumatoria+=i
        cantidadC+=1
    elif i >=70 and i <=89 :
        print ("Usted tiene una B")
        aprobado+=1
        cantidad_notas+=1
        sumatoria+=i
        cantidadB+=1
    elif i >=90 and i <=100 :
        print ("Usted tiene una A")
        aprobado+=1
        cantidad_notas+=1
        sumatoria+=i
        cantidadA+=1
print(" aprobaron", aprobado, " y reprobaron", reprobado, " alumnos, de un total de :", cantidad_notas, "alumnos presentes") 
print("hubo ",cantidad_ausentes ," alumnos ausentes") 
print("El promedio fue de ",sumatoria/cantidad_notas)
print("Hubo ", cantidadA, "alumno(s) con A")
print("Hubo ", cantidadB, "alumno(s) con B")
print("Hubo ", cantidadC, "alumno(s) con C")
print("Hubo ", cantidadF, "alumno(s) con F")
