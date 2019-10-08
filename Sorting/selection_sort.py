def selection_sort(nums):
    
    for i in range(len(nums)):
        first_index=i
        for j in range(i+1,len(nums)):
            if nums[first_index]>nums[j]:
                first_index=j
        nums[i],nums[first_index]=nums[first_index],nums[i]

lst=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
    
print("Before sorting : \n", lst)
selection_sort(lst)
print("After sorting : \n" , lst)


