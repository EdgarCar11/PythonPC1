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