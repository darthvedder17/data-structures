def factorial(n):
    temp=n
    fact=1
    for i in range(1,temp+1):
        fact=fact*i
    return print("The factorial is %d"%fact)
while True:
    sample=int(input("Enter a number:"))
    factorial(sample)

    
        
        
