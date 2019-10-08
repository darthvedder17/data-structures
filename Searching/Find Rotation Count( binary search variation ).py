def find_rotation_count(arr,n):
    low=0
    high=n-1
    while high>=low:
        if arr[low]<=arr[high]:
            return low  #CASE 1
        mid=int(low+(high-low/2))
        next=(mid+1)%n
        prev=(mid+n-1)%n
        if arr[mid]<=arr[next] and arr[mid]<=arr[prev]:
            return mid  #CASE 2
        elif arr[mid]<=arr[high]:
            high=mid-1  #CASE 3
        elif arr[mid]>=arr[low]:
            low=mid+1   #CASE 4
    return -1

arr=[15,22,23,28,31,38,5,6,8,10,12]
count=find_rotation_count(arr,11)
print("The array is rotated %d times"%count)
