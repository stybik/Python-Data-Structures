def balanced_paranthesis(expr):
    s = []
    for i in range(len(expr)):

        if (expr[i] == '(' or expr[i] == '{' or expr[i] == '['):
            s.append(expr[i])
            continue

        if(len(s) == 0):
            return False

        if expr[i] == ')':
            x = s.pop()
            if (x == '{' or x == '['):
                return False
        
        if expr[i] == ']':
            x = s.pop()
            if (x == '(' or x == '{'):
                return False
        
        if expr[i] == '}':
            x = s.pop()
            if (x == '(' or x == '['):
                return False

    if len(s) == 0:
        return True
    else:
        return False
        


if __name__ == "__main__":
    expr = "{()}[]"

    if(balanced_paranthesis(expr)):
        print("Balanced")
    else:
        print("Unbalanced")

