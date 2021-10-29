calificaciones = []
pregunta = input("Deseas comenzar el programa? y/n: ")
while pregunta == "y":
    print("Ingresa la calificación:")
    n = float(input(""))
    calificaciones.append(n)
    pregunta = input("Desea agregar una calificación mas? y/n: ")

promedio = sum(calificaciones)/len(calificaciones)
print("El promedio es:")
print(promedio)