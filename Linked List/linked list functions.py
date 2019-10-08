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
    def printlist(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next
    def append(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def insertatanypos(self,pos,data):
        new_node=node(data)
        if pos==0:
             new_node.next=self.head
             self.head=new_node
             return
        cur=self.head
        for i in range(pos-1):
            cur=cur.next
        new_node.next=cur.next
        cur.next=new_node
    def delete(self,key):
        cur=self.head
        if cur is None:
            print("there is no node to be deleted")
        if key==0:
            self.head=cur.next
            cur=None
            return
        prev=None
        count=1
        while cur and count!=key:
            prev=cur
            cur=cur.next
            count+=1
        if not key:
            print("ehhhhh")
        prev.next=cur.next
        cur=None
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
        dup=dict()
        while cur:
            if cur.data in dup:
                prev.next=cur.next
                cur=None
            else:
                dup[cur.data]=1
                prev=cur
            cur=prev.next
    def len_i(self):
        cur=self.head
        count=0
        while cur:
            cur=cur.next
            count+=1
        return count
    def reverse(self):
        prev=None
        cur=self.head
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        self.head=prev
            
    def merge(self,lllist):
        p=self.head
        q=lllist.head
        s=None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data<=q.data:
                s=p
                p=p.next
            else:
                s=q
                q=q.next
            new_head=s
        while p and q:
            if p.data<=q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next
        if not p:
            s.next=q
        if not q:
            s.next=p
        return new_head

    def nthfromlastnode(self,n):
        p=self.head
        q=self.head
        count=0
        while q and count<n:
            q=q.next
            count+=1
        if not q:
            print(str(n)+" is greater than the number of nodes in the list")
            return
        while p and q:
            p=p.next
            q=q.next
        return p.data
    def reversek(self,head,k):
        prev=None
        next=None
        cur=head
        count=0
        while cur and count<k:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
            count+=1
        if next is not None:
            head.next=self.reversek(next,k)
        return prev
    
llist=linkedlist()
llist_1=linkedlist()
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.append(8)
llist.push(1)
llist_1.push(10)
llist_1.push(9)
llist_1.push(7)
#llist.insertatanypos(0,890)

#print(llist.ispalindrome())
#llist.remove_duplicates()
#print(llist.len_i())
llist.printlist()
print("\n")
llist.reverse()
llist.printlist()
#print("The linked list before deletion :")
#llist.printlist()
#llist.delete(10)
#print("The linked list after deletion :")
#llist.merge(llist_1)
#print("Given linked list")
#llist.printlist()
#print("\n")
#llist.head=llist.reversek(llist.head,2)
#llist.printlist()

#print(llist.nthfromlastnode(1))
#llist.printlist()
#print("\n")

#llist_1.printlist()
