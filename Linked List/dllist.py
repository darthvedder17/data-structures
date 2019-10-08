class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class doublylinkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        if self.head is None:
            new_node=node(data)
            new_node.prev=None
            self.head=new_node
        else:
            new_node=node(data)
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=new_node
            new_node.prev=cur
            new_node.next=None
        
    def prepend(self,data):
        if self.head is None:
            new_node=node(data)
            new_node.prev=None
            self.head=new_node
        else:
            new_node=node(data)
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
            new_node.prev=None
    def printlist(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next
    def reverse(self):
        tmp=None
        cur=self.head
        while cur:
            tmp=cur.prev
            cur.prev=cur.next
            cur.next=tmp
            cur=cur.prev
        if tmp:
            self.head=tmp.prev
        

dllist=doublylinkedlist()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
#dllist.prepend(-1)
dllist.printlist()
print("\n")
dllist.reverse()
dllist.printlist()

        
