def bubble_sort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
lst=[]
length=int(input("Enter the number of values: "))
for i in range(0,length):
    ele=int(input())
    lst.append(ele)

print("Before swapping: \n",lst)
bubble_sort(lst)
print("After swapping: \n",lst)

        
