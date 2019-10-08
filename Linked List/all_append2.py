class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next

    def prepend(self,data):
        new_node=node(data)
        
        new_node.next=self.head
        self.head=new_node

    def append(self,data):
        new_node=node(data)

        if self.head is None:
            self_head=new_node
            return

        last_node=self.head

        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
            
        
        
llist=linkedlist()
llist.prepend(3)
llist.prepend(4)
llist.prepend(5)
llist.append("A")
llist.printlist()
