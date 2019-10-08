class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist():
    def __init__(self):
        self.head=None

    def printlist(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next

    def push(self,data):
        if self.head is None:
            self.head=new_node
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def append(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node

##    def insertafternode(self,prev_node,data):
##        if not prev_node:
##            print("There is no previous node")
##            return
##        new_node=node(data)
##        new_node.next=prev_node.next
##        prev_node.next=new_node

    def delete(self,key):
        cur=self.head
        if cur is None:
            return
        
        while cur and cur.data==key:
            self.head=cur.next
            cur=None
            return
        
        prev=None

        while cur and cur.data!=key:
            prev=cur
            cur=cur.next
        prev.next=cur.next
        cur=None

    def middle(self):
        fast_ptr=self.head
        slow_ptr=self.head

        if self.head is not None:
            while fast_ptr is not None and fast_ptr.next is not None:
                fast_ptr=fast_ptr.next.next
                slow_ptr=slow_ptr.next
            print("The middle value is : ", slow_ptr.data)

    def ispalindrome(self):
        s=""
        p=self.head
        while p:
            s=s+p.data
            p=p.next
        return s==s[::-1]

    def remove_duplicates(self):
        cur=self.head
        prev=None

        duplicates=dict()

        while cur:
            if cur.data in duplicates:
                prev.next=cur.next
                cur=None
            else:
                duplicates[cur.data]=1
                prev=cur
            cur=prev.next

    def len_i(self):
        count=0
        cur=self.head
        while cur:
            count+=1
            cur=cur.next
        return count

    def reverse(self):
        prev=None
        cur=self.head
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        self.head=prev
        
    def deletelist(self):
        cur=self.head
        while cur:
            prev=cur.next
            cur=None
            cur=prev

    def count(self):
        count=0
        cur=self.head
        while cur:
            count+=1
            cur=cur.next
        return count

    def getNth(self,key):
        cur=self.head
        count=0
        while cur:
            if count==key:
                return cur.data
            count+=1
            cur=cur.next

    def deletelist(self):
        cur=self.head
        prev=None
        while cur:
            prev=cur.next
            cur=None
            cur=prev

    def pop(self):
        cur=self.head
        if cur :
            self.head=cur.next
            cur=None
        else:
            print("There is no node present")

    def insertatnode(self,pos,data):
        cur=self.head
        count=0
        prev=None
        while cur:
            if count==pos:
                prev.next=data
                data.next=cur
                break
            prev=cur
            cur=cur.next
            count+=1
                    
            
            
              

llist=linkedlist()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
#llist.delete(4)
#llist.middle()
#print("The length is : ",llist.len_i())
#print(llist.reverse())
#llist.deletelist()
#llist.insert(34,3)
#print(llist.count())
#print(llist.getNth(9))
fourthnode=node(99)
llist.insertatnode(3,fourthnode)
#llist.pop()
llist.printlist()





























        

        
        
        
