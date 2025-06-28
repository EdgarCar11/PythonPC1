"""
Problema 1:
Escribir un programa que solicite su nombre de usuario por consola y después de que el usuario lo
introduzca muestre por pantalla la cadena “¡Hola <nombre>!”, donde <nombre> es el nombre que el
usuario haya introducido.

"""
#introducir nombre de usuario
nombre_usuario = input('Ingrese nombre de usuario: ')
#mostrar resultado
print('“¡Hola '+nombre_usuario+'!”')

"""
Problema 2:
En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina.

"""
#cuanto consume
consumo = float(input('Cuanto fue su consumo: '))
#el porcentaje propina que deja
porcentaje_propina = float(input('Que porcentaje de propina desea dejar: '))
#cantidad de dinero de propina
propina = consumo*porcentaje_propina/100.0
r=12+12
print(f'La cantidad de propina de dinero es: {propina}')

"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado.

"""

#numero de muneco
muneco = int(input('Ingrese el número de muñecos: '))
#numero de payaso
payaso = int(input('Ingrese el número de payasos: '))
#peso total
peso_total = muneco*75 + payaso*112
print(f'El peso total del paquete es: {peso_total}')

"""
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
puede ser calculada de la siguiente forma:

"""
#numero entero N
numero = int(input('introduzca un numero entero positivo: '))
if numero>0 :
    suma= numero*(numero+1)/2
    print(f'La suma de los {numero} primeros enteros positivos es: {suma}')
else:
    print(f'No es {numero} un entero positivo')

"""
Problema 5:
Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.

"""
#ingrese numero de show musicales
numero_musicales = int(input('Ingrese el número de show de musicales que ha visto en el ultimo año: '))
# si el numero es mayor a 3 es verdad en caso contrario sera falso
if numero_musicales>3 :
    print('Verdad')
else:
    print('Falso')  

"""
Problema 6:
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.

"""
#edad al usuario
edad = int(input('Ingrese su edad: '))
#condiciones del precio
if 0<edad<4:
    print('La entrada es gratis')
elif 4<=edad<=18:
    print('La entrada es $5')
elif edad>18:
    print('La entrada es $10')
else:
    print('La edad no es valida') 

"""
Problema 7:
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.

"""
#ingreso dos numeros
numero_uno=int(input('Ingrese el número 1: '))
numero_dos=int(input('Ingrese el número 2: '))
#elegir la opcion
print('Eliga entre las 3 opciones\na) Mostrar una suma de los dos números')
print('b) Mostrar una resta de los dos números (el primero menos el segundo)')
print('c) Mostrar una multiplicación de los dos números')
opcion=input('Indique que opción quiere escribiendo la letra:')
#condiciones
if opcion=="a":
    suma= numero_uno+numero_dos
    print(f'La suma de {numero_uno} y {numero_dos} es: {suma}')
elif opcion=="b":
    resta =numero_uno-numero_dos
    print(f'La resta de {numero_uno} y {numero_dos} es: {resta}')
elif opcion=="c":
    multiplicacion =numero_uno*numero_dos
    print(f'La multiplicación de {numero_uno} y {numero_dos} es: {multiplicacion}')
else:
    print('No es correcta la opción')


"""
Problema 8:
Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.
"""
#ingreso de hora
time=input('hora')
hours,minutes=time.split(':')
if time==7 or time==8 :
    print('Hora de desyuno')
elif time==12 or time==13 :
    print('Hora de almuerzo')
elif time==18 or time==19:
    print('Hora de cena')  


"""
Problema 9:
Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a',
'día', 'buen', 'Di'].

"""
# lista
lista_elementos= ['Di','buen','día','a','papa']
#invierto la lista con reverse()
lista_elementos.reverse()
#imprimo la lista invertida
print(lista_elementos)

"""
Problema 10:
Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
encuentran en la posición 0, 4 y 5.
lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
Resultado esperado: ['Verde', 'Blanco', 'Negro']

"""
lista=['Rojo','Verde','Blanco','Negro','Rosa','Amarillo']
lista.remove('Rojo')
lista.remove('Rosa')
lista.remove('Amarillo')
print(lista)

"""
Problema 11:
Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
lista. Su programa debe retornar otra lista sin los duplicados.
Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
Lista procesada: [1, 2, 3, 4,, 5]

"""
lista = [1, 1, 2, 3, 4, 4, 5, 1]
lista.remove(1)
lista.remove(4)
lista.remove(1)
print(sorted(lista))