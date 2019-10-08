def circular_array_search(arr,n,x):
    low=0
    high=n-1
    while high>=low:
        mid=int(low+(high-low/2))
        if arr[mid]==x:
            return mid   #CASE 1 , FOUND X 
        elif arr[mid]<=arr[high]:   #CASE 2 , RIGHT HALF IS SORTED
            if x>arr[mid] and x<=arr[high]:
                low=mid+1   # GO SEARCH IN RIGHT SORTED HALF
            else:
                high=mid-1
        elif arr[mid]>=arr[low]:    #CASE 3 , LEFT HALF IS SORTED 
            if x>=arr[low] and x<=arr[mid]:
                high=mid-1      # GO SEARCH IN LEFT SORTED HALF
            else:
                low=mid+1
    return -1

arr=[4,5,6,7,1,2,3]
search=circular_array_search(arr,7,3)
print("The index of %d is %d"%(3,search))
            
