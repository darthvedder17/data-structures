from queue import Queue
class newnode():
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
def inorder(temp):
    if temp==None:
        return
    inorder(temp.left)
    print(temp.key,end=" ")
    inorder(temp.right)

def insert(temp,key):
    q=[]
    q.append(temp)

    while len(q):
        temp=q[0]
        q.pop()

        if not temp.left:
            temp.left=newnode(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right=newnode(key)
            break
        else:
            q.append(temp.right)

def count_leaf_nodes(node):
    if  (not node):
        return 0
    
    q=Queue()
    count=0
    q.put(node)

    while (not q.empty()):
        temp=q.queue[0]
        q.get()

        if (temp.left != None):
            q.put(temp.left)
        if (temp.right != None):
            q.put(temp.right)
        if (temp.left==None and
            temp.right==None):
            count+=1
    return count

    

if __name__=="__main__":
    root=newnode(10)
    root.left=newnode(11)
    root.left.left=newnode(7)
    root.right=newnode(9)
    root.right.left=newnode(15)
    root.right.right=newnode(8)

    print("Inorder Traversal before insertion : " ,end=" ")
    inorder(root)

    key=12
    insert(root,key)

    print()
    print("Inorder Traversal after insertion : ", end=" ")
    inorder(root)
    print()
    print("Number of leaf nodes : ", count_leaf_nodes(root) )
    print()    
    
