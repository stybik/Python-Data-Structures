def isRotation(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    temp = ""

    temp = s1+s2
    if (temp.count(s2) > 0):
        return True
    else:
        return False

if __name__ == "__main__":
    s1 = str(input())
    s2 = str(input())
    if isRotation(s1, s2):
        print(f"{s2} is rotation of {s1}")
    else:
        print(f"{s2} is not a rotation of {s2}")
