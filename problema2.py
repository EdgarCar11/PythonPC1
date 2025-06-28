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