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