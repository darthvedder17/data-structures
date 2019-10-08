class node:
    def __init__(self,data):
        self.data=head
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next

    def push(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node

    def InsertAfter(self,new_data,prev_node):
        if prev_node is None:
            print("the given previous node must be inlinkedlist")
            return
        new_node=node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def append(self,new_data):
        new_node=node(new_data)
        if self_head is None:
            self_head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next

        last.next=new_node


if __name__=='__main__':
    
        
