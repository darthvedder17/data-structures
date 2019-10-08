class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node

    def deletenode(self,position):
        
        if self.head==None:
            return

        temp=self.head

        if position==0:
            self.head=temp.next
            temp=None
            return

        for i in range(position -1):
            temp=temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        next=temp.next.next

        temp.next=None

        temp.next=next

    def printlist(self):
        temp=self.head
        while(temp):
            print("%d"%(temp.data))
            temp=temp.next

llist=linkedlist()
llist.push(3)
llist.push(4)
llist.push(6)
llist.push(1)
llist.push(0)

print("Created linked list: ")
llist.printlist()
llist.deletenode(3)
print("\nLinked list after deletion at position 3: ")
llist.printlist()
                  
