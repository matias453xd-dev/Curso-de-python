#Apuestas de caballos
import random
print('Ingrese el monto disponible')
respuesta2 = 'si'
monto = int(input())
while respuesta2 == 'si' and monto > 0:
  apuesta = 0
  caballo = 0  
  print('Quiere apostar? si/no')
  respuesta = input()
  if respuesta == 'si':
      print('Cuanto dinero quiere apostar? ')
      apuesta = int(input())
      print('Elija un caballo: 1, 2, 3 o 4')
      caballo = int(input())
  else:
      print('Usted no esta participando')
  candidatos = [1, 2, 3, 4]
  ganador = random.choice(candidatos)
  print("El ganador es:", ganador)
  if caballo == ganador:
      print('Usted a ganado')
      monto = monto + apuesta*2
  else:
      monto = monto - apuesta
  print(f'Su monto final es de {monto}')
  print('Quiere continuar?')
  respuesta2 = input()
