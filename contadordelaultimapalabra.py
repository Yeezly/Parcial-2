s = input("Escribe la frase que quieras: ")
s2 = s.split(" ")
c = -1
s3 = len(s2[c])

while True:
    if (s2[c]) != (' '):
        if s3 == 0:
            c -= 1
            s3 = len(s2[c])
            print(s3)
        else:
            print(s3)
            break


