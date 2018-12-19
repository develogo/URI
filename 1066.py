cont = 0

positivos = 0
negativos = 0
par = 0
impar = 0


while cont < 5:
    entrada = int(input())

    if entrada % 2 ==0:
        par +=1
        
    else :
        impar += 1

    if entrada > 0:
        positivos += 1
    
    else:
        if entrada < 0 :
            negativos +=1
    
    
    cont +=1

print (par,"valor(es) par(es)")
print (impar,"valor(es) impar(es)")
print (positivos,"valor(es) positivo(s)")
print (negativos,"valor(es) negativo(s)")