"""
1) If a binary tree node is NULL then it is a full binary tree.
2) If a binary tree node does have empty left and right sub-trees, then it is a full binary tree by definition.
3) If a binary tree node has left and right sub-trees, then it is a part of a full binary tree by definition. In this case recursively check if the left and right sub-trees are also binary trees themselves.
4) In all other combinations of right and left sub-trees, the binary tree is not a full binary tree.

"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def isFullTree(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return(isFullTree(root.left) and isFullTree(root.right))
    return False

root = Node(10); 
root.left = Node(20); 
root.right = Node(30); 
  
root.left.right = Node(40); 
root.left.left = Node(50); 
root.right.left = Node(60); 
root.right.right = Node(70); 
  
root.left.left.left = Node(80); 
root.left.left.right = Node(90); 
root.left.right.left = Node(80); 
root.left.right.right = Node(90); 
root.right.left.left = Node(80); 
root.right.left.right = Node(90); 
root.right.right.left = Node(80); 
root.right.right.right = Node(90); 
  
if isFullTree(root): 
    print("The Binary tree is full")
else: 
    print("Binary tree is not full")