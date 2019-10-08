def armstrong(n):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    if sum==n:
        return print("It is an armstrong number")
    else:
        return print("It is not an armstrong number")
sample=int(input("Please enter a number :"))
armstrong(sample)

