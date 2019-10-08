class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.random=None
class circularlinkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        if not self.head:
            self.head=node(data)
            self.head.next=self.head
        else:
            new_node=node(data)
            cur=self.head
            while cur.next!=self.head:
                cur=cur.next
            cur.next=new_node
            new_node.next=self.head

    #def prepend(self,data)

    def printlist(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next
            if cur==self.head:
                break
            

cllist=circularlinkedlist()
cllist.append("C")
cllist.append("D")
cllist.printlist()

            
        
