def binary_search(arr,n,x,flag):
    low=0
    high=n-1
    result=-1
    while high>=low:
        mid=int(low+(high-low/2))
        if arr[mid]==x:
            result=mid
            if flag:
                high=mid-1#go on searching towards left
            if not flag:
                low=mid+1#go on searching towards right
        elif arr[mid]>=x:
            high=mid-1
        else:
            low=mid+1
    return result

arr=[1,3,4,5,5,5,6]
x=100
flag=bool
n=len(arr)
first_index=binary_search(arr,n,x,True)
if(first_index==-1):
    print("The count of %d is 0"%x)
else:
    last_index=binary_search(arr,n,x,False)
    print("The count of %d is %d"%(x,last_index-first_index+1))

    
            
            
