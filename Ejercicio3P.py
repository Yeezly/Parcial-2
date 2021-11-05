#No terminado
import random
canicasjugador = 10
canicascpu = 10

numeroj = int(input("Elige un número del 1 al 10 para apostar: "))
numerocpu = random.randint(1,10)

apuesta = input("¿El número del cpu será par o impar?: ")

canicasj = []
ccpu = []
canicasj.append(numeroj)
ccpu.append(numerocpu)

if numeroj % 2 == 0:
    numeroj = "par"
else:
    numeroj = "impar"

if numerocpu % 2 == 0:
    numerocpu = "par"
else:
    numerocpu = "impar"

if apuesta == numerocpu:
    print("Has acertado")
    recanicas = 10 + ([canicasj][0])
    print("ahora tienes" + recanicas + "canicas")
else:
    print("Has falado")
    recanicas = 10 - ([canicasj][0])
    print("ahora tienes" + recanicas + "canicas")

