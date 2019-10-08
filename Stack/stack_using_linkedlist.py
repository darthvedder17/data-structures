class stacknode:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        return True if self.head is None else False
    def push(self,data):
        new_node=stacknode(data)
        new_node.next=self.head
        self.head=new_node
        print("%d is pushed to stack"%(data))
    def pop(self):
        if (self.isempty()):
            return float("-inf")
        cur=self.head
        self.head=self.head.next
        popped=cur.data
        return popped
    def peek(self):
        if self.isempty():
            return float("-inf")
        return self.head.data


stack=stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("%d popped from stack"%(stack.pop()))
print("Top element is %d"%(stack.peek()))

