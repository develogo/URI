enter  = int(input())

count = 0

while count < enter:
    num = int(input())

    if num == 0:
        print("NULL")
     
    if (num % 2) == 0 and num > 0:
        print("EVEN POSITIVE")
    
    if (num % 2) == 0 and num < 0:
        print("EVEN NEGATIVE")
    
    else:
        
        if (num%2) != 0 and num > 0:
            print("ODD POSITIVE")
        
        if (num%2) != 0 and num < 0 :
            print("ODD NEGATIVE")
    
    count += 1