def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1

lst=[]
length=int(input("Enter the length of the list : "))
for i in range(0,length):
    ele=int(input())
    lst.append(ele)

print("Before swapping: \n",lst)
merge_sort(lst)
print("After swapping: \n",lst)
    
    
            
                
        
