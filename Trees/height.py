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

def preorder(temp):
    if (not temp):
        return
    print(temp.key,end=" ")
    preorder(temp.left)
    preorder(temp.right)

def postorder(temp):
    if (not temp):
        return
    postorder(temp.left)
    postorder(temp.right)
    print(temp.key, end=" ")

def height(temp):
    if temp is None:
        return -1
    left_h=height(temp.left)
    right_h=height(temp.right)
    
    return 1+max(left_h,right_h)
    

if __name__=="__main__":
    
    tree=newnode(10)
    tree.left=newnode(1)
    tree.right=newnode(2)
    tree.left.left=newnode(7)

    inorder(tree)
    print()
    preorder(tree)
    print()
    postorder(tree)
    print(height(tree))
        
