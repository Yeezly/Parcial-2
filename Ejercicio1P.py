c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
pregunta = input("Deseas comenzar el programa? y/n: ")
while pregunta == "y":
    print("Ingresa un valor del 1 al 50:")
    n = int(input(""))
    while n <51 and n >0:
        if n <11 and n >0:
            c1.append(n)
            break
        elif n <21 and n >10:
            c2.append(n)
            break
        elif n <31 and n >20:
            c3.append(n)
            break
        elif n <41 and n >30:
            c4.append(n)
            break
        elif n <51 and n >40:
            c5.append(n)
            break
    pregunta = input("Desea agregar un numero mas? y/n: ")


print([c1][0]) and print([c1][1]) and print([c1][2])
print([c2][0]) and print([c2][1]) and print([c2][2])
print([c3][0]) and print([c3][1]) and print([c3][2])
print([c4][0]) and print([c4][1]) and print([c4][2])
print([c5][0]) and print([c5][1]) and print([c5][2])