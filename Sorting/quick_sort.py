def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]

    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)

def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

lst=[]
length=int(input("Enter the length of the list : "))
for i in range(0,length):
    ele=int(input())
    lst.append(ele)
print("before swapping : ",lst,end="")
quicksort(lst,0,length-1)
print("\nafter swapping : ",lst,end=" ")
