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
