# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

cantidad_numeros_positivos = 0  # Inicializo el contador en 0
cant_num_neg = 0
cero = 0
total=0
# for ... in range(....)
for num in range(inicio,fin+1):
    if num<0:
        cant_num_neg +=1
    if num==0:
        cero +=1
    if num>0:
       cantidad_numeros_positivos +=1
    total +=1
print("Hay ", cant_num_neg, " negativos y hay ", cantidad_numeros_positivos, " positivos\n Se contaron un total de ", total, "numeros")

# Imprimir el valor de la cantidad de números positivos y negativos

print("terminamos!")
