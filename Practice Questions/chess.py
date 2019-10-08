m=int(input("Enter the number of rows: "))
n=int(input("Enter the number of columns: "))
val=[[2 for i in range(n)]for j in range(m)]
val[0][0]=99
for m in val:
    print(m)


       
