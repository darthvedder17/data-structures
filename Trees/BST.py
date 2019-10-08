class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None


    def insert(self,data):
        if self.root is None:
            self.root=node(data)
        else:
            self._insert(data,self.root)


    def _insert(self,data,cur_node):
        if data<cur_node.data:
            if cur_node.left is None:
                cur_node.left=node(data)
            else:
                self._insert(data,cur_node.left)
        elif data>cur_node.data:
            if cur_node.right is None:
                cur_node.right=node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value is already present in tree.")


    def find(self,data):
        if self.root:
            is_found=self._find(data,self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None


    def _find(self,data,cur_node):
        if data>cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        if data<cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data==cur_node.data:
            return True

    def inorder(self):
        if self.root is None:
            return
        else:
            self._inorder(self.root)


    def _inorder(self,temp):
        if temp:
            self._inorder(temp.left)
            print(str(temp.data),end="-")
            self._inorder(temp.right)

    def is_bst(self):
        if self.root:
            is_satisfied=self._is_bst(self.root,self.root.data)

            if is_satisfied is None:
                return True
            return False
        return True


    def _is_bst(self,cur_node,data):
        if cur_node.left:
            if data>cur_node.left.data:
                return self._is_bst(cur_node.left,cur_node.left.data)
            else:
                return False
        if cur_node.right:
            if data<cur_node.right.data:
                return self._is_bst(cur_node.right,cur_node.right.data)
            else:
                return False
        
            


bst1=bst()
bst1.insert(2)
bst1.insert(5)
bst1.insert(7)
bst1.insert(12)
bst1.insert(22)
bst1.insert(1)
print(bst1.find(22))
print(bst1.inorder())
print(bst1.is_bst())

            
        
        
        
