nos=int(input("Enter a number: "))
if(nos<=1):
    print("Not a prime")
for i in range(2,nos):
    if(nos%i==0):
        print("Not a prime")
        break
    else:
        print("prime")
        break

        
    

    
        
