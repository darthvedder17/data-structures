def interpolation_search(arr,x,n):
    lo=0
    hi=(n-1)

    while lo<=hi and x>=arr[lo] and x<=arr[hi]:
        if lo==hi:
            if arr[lo]==x:
                return lo
            return -1
        pos=lo+int(((float(hi-lo)/(arr[hi]-arr[lo]))*(x-arr[lo])))

        if arr[pos]==x:
            return pos
        if arr[pos]<x:
            lo=pos+1
        else:
            hi=pos-1
    return -1

arr=[2,3,5,6,9,12,34,56,77,89,999,7988]
n=len(arr)
x=9
index=interpolation_search(arr,x,n)

if index!=-1:
    print("Element found at index",index)
else:
    print("Element not found")
        
                
