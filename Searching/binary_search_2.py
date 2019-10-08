def binary_search(arr,low,high,x):
    result=-1
    while high>=low:
        mid=int(low+(high-low/2))
        if arr[mid]==x:
            #return mid #for the last occurence , apply this and change the
                        #return to -1.
            result=mid
            high=mid-1
        elif arr[mid]>=x:
            high=mid-1
        else:
            low=mid+1
    return result

arr=[1,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,5]
x=4
result=binary_search(arr,0,len(arr)-1,x)
if(result==-1):
    print("element is not present")
else:
    print("element is present at index ",result)
            
        
    
