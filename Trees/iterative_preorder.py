class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



def iterative_preorder(root):
    if root is None:
        return
    node_stack=[]
    node_stack.append(root)

    while len(node_stack)>0:
        Node=node_stack.pop()
        print (Node.data)

        if Node.right:
            node_stack.append(Node.right)
        if Node.left:
            node_stack.append(Node.left)
    
root=Node(20)
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14)
iterative_preorder(root)       
    








# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        stack=[]
        ans=[]
        while stack or A:
            if A:
                stack.append(A)
                A=A.left
            else:
                tmpnode=stack.pop()
                ans.append(tmpnode.val)
                A=tmpnode.right
        return ans
