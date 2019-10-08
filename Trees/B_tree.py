class Stack(object):
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)
    def __len__(self):
        return self.size()

class Queue(object):
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].data
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
        

class node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class binarytree(object):
    
    def __init__(self,root):
        self.root=node(root)

    def print_tree(self,traversal_type):
        if traversal_type=="preorder":
            return self.preorder(tree.root,"")
        elif traversal_type=="inorder":
            return self.inorder(tree.root,"")
        elif traversal_type=="postorder":
            return self.postorder(tree.root,"")
        elif traversal_type=="levelorder":
            return self.levelorder(tree.root)
        elif traversal_type=="reverse_level":
            return self.reverse_level(tree.root)
        else:
            print("Traversal type "+str(traversal_type)+" is not supported.")
            return False
        
    def preorder(self,start,traversal):
        if start:
            traversal+=((str(start.data))+ "-" )
            traversal=self.preorder(start.left,traversal)
            traversal=self.preorder(start.right,traversal)
        return traversal
    
    def inorder(self,start,traversal):
        if start:
            traversal=self.preorder(start.left,traversal)
            traversal+=((str(start.data))+ "-" )
            traversal=self.preorder(start.right,traversal)
        return traversal
    
    def postorder(self,start,traversal):
        if start:
            traversal=self.preorder(start.left,traversal)
            traversal=self.preorder(start.right,traversal)
            traversal+=((str(start.data))+ "-" )
        return traversal
    
    def levelorder(self,start):
        if start is None:
            return
        queue=Queue()
        queue.enqueue(start)
        traversal=""
        while len(queue)>0:
            traversal+=str(queue.peek())+"-"
            node=queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_level(self,start):
        if start is None:
            return

        queue=Queue()
        stack=Stack()
        queue.enqueue(start)
        traversal=""
        while len(queue)>0:                                                             ##### empty child nodes from queue<<<<<<right to left>>>>>>>####
                                                                                        #####                      USE STACK TOO                    ####
            node=queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack)>0:
            node=stack.pop()
            traversal+=str(node.data)+"-"
        return traversal

    def height(self,node):
        if node is None:
            return -1
        left_h=self.height(node.left)
        right_h=self.height(node.right)

        return 1+max(left_h,right_h)

    def size_of_tree(self):
        if self.root is None:
            return 0
        stack=Stack()
        stack.push(self.root)
        size=1
        while stack:
            node=stack.pop()
            if node.left:
                size+=1
                stack.push(node.left)
            if node.right:
                size+=1
                stack.push(node.right)

        return size
                
        
            



        
tree=binarytree(1)
tree.root.left=node(2)
tree.root.right=node(3)
tree.root.left.left=node(4)
tree.root.left.right=node(5)
tree.root.right.left=node(6)
tree.root.right.right=node(7)
tree.root.right.right.right=node(8)


print(tree.print_tree("reverse_level"))
print(tree.height(tree.root))
print(tree.size_of_tree())

