a=[1,2,3,4,5]
print(a)
n=(len(a)-1)
pos=int(input("Where do you want to add the element : "))                       ####  INSERT IN ARRAY   #### 
data=input("Enter the data: ")
a.insert(pos,data)

pos=int(input("Where do you want to delete the element : "))                   ####  DELETE IN ARRAY   ####
a.remove(a[pos])

ele=int(input("Enter the element that you want to search : "))
for i in range(0,n):
    if(a[i]==ele):                                                              ####  SEARCH AN ELEMENT ####
        print("element found")
    

print(a)
    

