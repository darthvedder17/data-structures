strr=input("Enter a string : ")
length=len(strr)
sum=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in range(length):
    if strr[i] in vowels:
        sum=sum+(length-i)
print(sum)
print(strr[0])
print(strr[1])
        
    
    

        
        
