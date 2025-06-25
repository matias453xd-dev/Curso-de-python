#edad = int(input())
#if edad >= 18:
#    print('ere mayor de edad')
#else:
#   print('no eres mayor de edad')

ingreso_mensual = 12000
gasto_mensual = 5010
if ingreso_mensual >= 10000:
    if gasto_mensual < 5000:
        print('Estas gastando bien')
    else: print('estas gastando demaciado')
    print('estas bien economicamente')
elif ingreso_mensual >= 5000:
    print('tambien esta bien')
else:
    print('eres pobre')
    
#Conjuncion en if
edad = 19
estatura = 170
if edad >= 18 and estatura >= 170:
    print('aceptado')
else:
    print('no aceptado')