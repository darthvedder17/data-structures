class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        curr_node=self.head
        while curr_node:
            print(curr_node.data)
            curr_node=curr_node.next

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

    def insertafternode(self,prev_node,data):
        if not prev_node:
            print("There is no previous node")
            return

        new_node=node(data)

        new_node.next=prev_node.next
        prev_node.next=new_node

    def delete(self,key):
        curr_node=self.head

        if curr_node and curr_node.data==key:
            self.head=curr_node.next
            curr_node=None
            return

        if curr_node is None:
            return
        
        prev=None

        while curr_node and curr_node.data!=key:
            prev=curr_node
            curr_node=curr_node.next

        prev.next=curr_node.next
        curr_node=None

    def delete_at_pos(self,pos):
        curr_node=self.head
        if pos==0:
            self.head=curr_node.next
            curr_node=None
            return

        if curr_node is None:
            return

        prev=None
        count=1
        while curr_node and count!=pos:
            prev=curr_node
            curr_node=curr_node.next
            count+=1

        prev.next=curr_node.next
        curr_node=None

    def len_i(self):
        count=0
        curr_node=self.head

        while curr_node:
            count+=1
            curr_node=curr_node.next
        return count

    def len_r(self):
        if node is None:
            return 0

        return 1+self.len_r(node.next)

    def swap_nodes(self,key_1,key_2):
        if key_1==key_2:
            return

        prev_1=None
        curr_1=self.head
        while curr_1 and curr_1.data!=key_1:
            prev_1=curr_1
            curr_1=curr_1.next

        prev_2=None
        curr_2=self.head
        while curr_2 and curr_2.data!=key_2:
            prev_2=curr_2
            curr_2=curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next=curr_2
        else:
            self.head=curr_2

        if prev_2:
            prev_2.next=curr_1
        else:
            self.head=curr_1

        curr_1.next, curr_2.next=curr_2.next,curr_1.next

    def reverse_i(self):
        prev=None
        cur=self.head
        while cur:
            nxt=cur.next
            cur.next=prev

            #self.print_helper(prev,"PREV")
            #self.print_helper(cur,"CUR")
            
            prev=cur
            cur=nxt
        self.head=prev

    def reverse_r(self):

        def _reverse_r(cur,prev):
            if not cur:
                return prev

            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
            return _reverse_r(cur,prev)

        self.head=_reverse_r(cur=self.head,prev=None)

    def merge_sorted(self,llist):
        p=self.head
        q=llist.head
        s=None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data<=q.data:
                s=p
                p=s.next
            else:
                s=q
                q=s.next
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
            
    def nth_to_last_node(self,n):
        total_len=self.len_i()

        cur=self.head
        while cur:
            if total_len==n:
                print(cur.data)
                return cur
            total_len -=1
            cur=cur.next
        if cur is None:
            return

    def count_occ_i(self,data):
        count=0
        cur=self.head
        while cur:
            if cur.data==data:
                count+=1
            cur=cur.next
        return count
    def count_occ_r(self,node,data):
        if not node:
            return 0
        if node.data==data:
            return 1 + self.count_occ_r(node.next,data)
        else:
            return self.count_occ_r(node.next,data)

    def rotate(self,k):
        p=self.head
        q=self.head

        prev=None
        count=0

        while p and count<k:
            prev=p
            p=p.next
            q=q.next
            count+=1
        p=prev

        while q:
            prev=q
            q=q.next
        q=prev

        q.next=self.head
        self.head=p.next
        p.next=None

    def is_palindrome(self):
        s=""
        p=self.head
        while p:
            s+=p.data
            p=p.next
        return s==s[::-1]
        
        
    def tail_to_head(self):
        last=self.head
        second_to_last=None
        while last.next:
            second_to_last=last
            last=last.next
        last.next=self.head
        second_to_last.next=None
        self.head=last

    def detectloop(self):
        slow_ptr=self.head
        fast_ptr=self.head
        while(slow_ptr and fast_ptr and fast_ptr.next):
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next
            if slow_ptr==fast_ptr:
                self.removeloop(slow_ptr)
                return 1
        return 0
            

llist=linkedlist()
#llist_2=linkedlist()

llist.prepend("R")
llist.append("A")
llist.append("D")
llist.append("A")
llist.append("R")
#llist.append(6)
#llist_2.prepend(99)
#llist_2.append(1)
#llist_2.append(2)
#llist_2.append(3)
#llist.delete(1)
#llist.delete_at_pos(0)
#llist.insertafternode(llist.head.next,6)
#llist.swap_nodes(2,5)

llist.reverse_i()

#   llist_1.printlist()
#print("\n")
#llist_2.printlist()
#llist_1.merge_sorted(llist_2)
#llist_1.remove_duplicates()
#print(llist_1.nth_to_last_node(2))
#print(llist_1.count_occ_r(llist_1.head,1))
#llist.printlist()
#print("\n")
#llist.rotate(4)
#llist.printlist()
#llist.tail_to_head()
#print("\n")
llist.head.next.next.next=llist.head
llist.detectloop()

#llist.printlist()
#print(llist.is_palindrome())







        
