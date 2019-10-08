class node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:
    
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def append(self,data):
        new_node=node(data)
        cur=self.head
        if cur is None:
            self.head=new_node
            return    
        while cur.next:
            cur=cur.next
        cur.next=new_node

    def delete_by_key(self,key):
        
        cur=self.head

        if cur and cur.data==key:
            self.head=cur.next
            cur=None
            return
        
        if cur is None:
            print("There is as such no value present\n")
            return
        
        prev=None
        
        while cur and cur.data!=key:
            prev=self.head
            cur=cur.next
        if not key:
            return print("No value present \n")
            
        prev.next=cur.next
        cur=None

    def delete_at_pos(self,pos):
        cur=self.head
        if cur is None:
            print("No node is present at that position\n")
            return
        if pos==0:
            self.head=cur.next
            cur=None
            return
        prev=None
        count=1
        while cur and count!=pos:
            prev=cur
            cur=cur.next
            count+=1
        prev.next=cur.next
        cur=None

    def make_new_list(self):
        nums=int(input("How many nodes do you want to create : "))
        if nums==0:
            return
        for i in range(nums):
            value=int(input("Enter the value for the node:"))
            self.append(value)

    def insert_at_pos(self,pos,data):
        cur=self.head
           
        new_node=node(data)
        if pos==0:  
            new_node.next=self.head
            self.head=new_node
        if cur is None:
            print("There is no position as you listed")
            return
        for i in range(pos-1):
            cur=cur.next
        new_node.next=cur.next
        cur.next=new_node
    
    def len(self):
        count=0
        cur=self.head
        while cur:
            cur=cur.next
            count+=1
        return count
        
        
    def printlist(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next
        

llist=linkedlist()

while True:
    test=int(input("\nChoose any action from the following : \n 1) Make a new linked list \n 2) Add an element at the starting \n 3) Add an element at the end \n 4) Add an element at the specified position \n 5) Delete an element by the value \n 6) Delete an element by the position \n 7) Length of your linked list \n\n"))
    
    for i in range(test):
        if test==1:
            llist.make_new_list()
            print("Linked List: \n")
            llist.printlist()
            break
        elif test==3:
            data=int(input("Enter data item: "))
            llist.append(data)
            llist.printlist()
            break
        elif test==4:
            position=int(input("Enter the position: "))
            data=int(input("Enter the value at this position: "))
            llist.insert_at_pos(position,data)
            llist.printlist()
            break
        elif test==5:
            data=int(input("Enter the value: "))
            llist.delete_by_key(data)
            llist.printlist()
            break
        elif test==6:
            data=int(input("Enter the position: "))
            llist.delete_at_pos(data)
            llist.printlist()
            break
        elif test==2:
            data=int(input("Enter data item: "))
            llist.push(data)
            llist.printlist()
            break
        elif test==7:
            print("The length of your linked list is ",llist.len())
            break
    



        
