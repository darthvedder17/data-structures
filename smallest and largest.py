n=int(input("Enter the number of elements : "))
arr=[]
for i in range(0,n):
    temp=int(input())
    arr.append(temp)

print(arr)
small=large=arr[0]
for i in range(0,n):
    if arr[i]>large:
        large=arr[i]            ####        LOGIC       ####
    if arr[i]<small:
        small=arr[i]

print(small)
print(large)

print(min(arr))                 ####  INBUILT FUNCTIONS  ####
print(max(arr))
        
    

