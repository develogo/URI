cont = 0
positivos = 0
negativos = 0

while cont < 6:
    entrada = float(input())

    if entrada > 0:
        positivos += 1
    else:
        negativos += 1

    cont +=1

print (positivos,"valores positivos")