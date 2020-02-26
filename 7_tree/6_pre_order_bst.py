"""
1) Create an empty stack.
2) Initialize root as INT_MIN.
3) Do following for every element pre[i]
     a) If pre[i] is smaller than current root, return false.
     b) Keep removing elements from stack while pre[i] is greater
        then stack top. Make the last removed item as new root (to
        be compared next).
        At this point, pre[i] is greater than the removed root
        (That is why if we see a smaller element in step a), we 
        return false)
     c) push pre[i] to stack (All elements in stack are in decreasing
        order) 
"""

INT_MIN = 0

def canRepresentBST(pre):
    s = []
    root = INT_MIN
    for value in pre:
        if value < root:
            return False
        while(len(s) > 0 and s[-1] < value):
            root = s.pop()
        s.append(value)
    return True


pre1 = [40 , 30 , 35 , 80 , 100] 
print("true" if canRepresentBST(pre1) == True else "false")
pre2 = [40 , 30 , 35 , 20 ,  80 , 100] 
print("true" if canRepresentBST(pre2) == True else "false")