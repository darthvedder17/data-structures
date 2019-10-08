class node:
    def __init__(self,data):
        self.data=data
        self.next= None

class linkedlist:
    def __init__( self ):
        self.head= None
if __name__=='__main__':
    llist=linkedlist()

    llist.head=node(1)
    second=node(2)
    third=node(3)

    llist.head.next=second;
    second.next=third;
