def arePermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    a = sorted(str1)
    b = sorted(str2)
    str1 = "".join(a)
    str2 = "".join(b)

    for index in range(len(str1)):
        if (str1[index] != str2[index]):
            return False

    return True

if __name__ == "__main__":
    str1 = input()
    str2 = input()
    if arePermutation(str1, str2):
        print(f"Both the strings are permutations of each other")
    else:
        print(f"Both the strings are not permutations of each other")