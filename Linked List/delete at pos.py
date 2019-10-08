def deletenode_at_pos(self,pos):
    cur_node=self.head

    if pos==0:
        self.head=cur_node.next
        cur_node=None
        return

    prev=None
    count=1
    while cur_node and count != pos:
        prev=cur_node
        cur_node=cur_node.next
        count+=1

    if cur_node is None:
        return

    prev.next=cur_node.next
    cur_node=None

    
