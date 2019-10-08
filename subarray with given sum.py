A=[1,2,3,4,5,6,7,8,9,10]
n=len(A)
sum=int(input("Enter the sum: "))
def subarraysum(A,n,sum):
    for i in range(n):
        curr_sum=A[i]
        j=i+1
        while j<=n:
            if curr_sum==sum:
                print("Sum found between ")
                print("indexes %d and %d"%(i,j-1))
                
                return 1

            if curr_sum >sum or j==n:
                break

            curr_sum=curr_sum+A[j]
            j+=1

    print("No subarray found")
    return 0

#subarraysum(A,n,sum)


def __subarraysum(A,n,sum):

    curr_sum=A[0]
    start=0
    i=1
    while i<=n:

        while curr_sum>sum and start<i-1:
            curr_sum=curr_sum-A[start]
            start+=1

        if curr_sum==sum:
            print("Sum found between indexes %d and %d"%(start,i-1))            
            return 1

        if i<n:
            curr_sum=curr_sum+A[i]
        i+=1
    print("No sub array found")
    return 0

__subarraysum(A,n,sum)
