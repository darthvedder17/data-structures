def largest_cont_sum(arr):
    if len(arr)==0:
        return
    maxsum=currentsum=arr[0]
    for i in arr[1:]:
        currentsum=max(currentsum+i,i)
        maxsum=max(currentsum, maxsum)
    return maxsum
sample=[2,5,10,-20,4,2,10]
print(largest_cont_sum(sample))
lauda lele
        
