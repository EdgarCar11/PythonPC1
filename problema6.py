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