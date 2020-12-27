class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftViewUtil(root, level, max_level):
    if root is None:
        return
    if (max_level[0] < level):
        print(root.data, end=" ")
        max_level[0] = level

    leftViewUtil(root.left, level+1, max_level)
    leftViewUtil(root.right, level+1, max_level)


def leftView(root):
    max_level = [0]
    leftViewUtil(root, 1, max_level)

def levelOrderLeftView(root):
    if (not root):
        return
    q = []
    q.append(root)

    while(len(q)):
        n = len(q)
        for i in range(1, n+1):
            temp = q[0]
            q.pop(0)

            if i == 1:
                print(temp.data, end=" ")

            if temp.left != None:
                q.append(temp.left)

            if temp.right != None:
                q.append(temp.right) 

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    leftView(root)
    levelOrderLeftView(root)