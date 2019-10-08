def print_spiral(arr,m,n):
    T=0
    B=m-1
    L=0
    R=n-1
    dir=0
    while T<=B and L<=R:
        if dir==0:
            for i in range(L,R):
                print(arr[T][i])
                T+=1
                dir=1
        elif dir==1:
            for i in range(T,B):
                print(arr[i][R])
                R-=1
                dir=2
        elif dir==2:
            for i in range(R,L,-1):
                print(arr[B][i])
                B-=1
                dir=3
        elif dir==3:
            for i in range(B,T,-1):
                print(arr[i][L])
                L+=1
                dir=0

arr=[1,2,3,4,5,6,7,8,9]
test=print_spiral(arr,3,3)
print(test)
    
