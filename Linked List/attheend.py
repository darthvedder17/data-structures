class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next
    def append(head,data):
        new_node=node(data)
        if head is None:
            return new_node
        last_node=head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
        return head

llist=linkedlist()
llist.append(6)
llist.append(5)
llist.append(4)
llist.append(3)
llist.append(2)
llist.printlist()
