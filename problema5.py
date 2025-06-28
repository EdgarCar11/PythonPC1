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