class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    q = []
    q.append(root)

    while(len(q)):
        temp = q[0]
        q.pop(0)

        print(temp.data, end=" ")
    
        if (temp.left != None):
            q.append(temp.left)
        if (temp.right != None):
            q.append(temp.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
 
    levelOrderTraversal(root)