# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

while True:
    num1= int(input("ingrese el primer numero :"))
    num2= int(input(" ingrese el segundo numero :"))
    print("recuerde escribir FIN para salir")
    operador=str(input("ingrese operador: + suma, -resta, *multiplicar, /dividir, **potencia o FIN si desea salir:"))
    if operador == "FIN":
        print("GRACIAS")
        break
    elif operador=="+":
        suma=num1+num2
        print("El resultado de la suma es : ", suma)
    elif operador =="-":
        resta=num1-num2
        print("El resultado de la resta es : ", resta)  
    elif operador =="*":
        multi=num1*num2
        print("El resultado de la multiplicación es : ", multi)
    elif operador =="/":
        div=num1/num2
        print("El resultado de la división es : ", div)
    elif operador =="**":
        pot=num1**num2
        print("El resultado de la potencia es : ", pot)
    else:
        if (operador != "+" and operador !="-" and operador !="*" and operador !="/" and operador !="**"):
             print("ERROR")
    


    
       



