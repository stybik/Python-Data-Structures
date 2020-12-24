MAX_STR = 256

def uniqueCharacters(str):
    """Time Complexity: O(n)"""
    if (len(str) > MAX_STR):
        return False
    chars = [False] * MAX_STR
    for i in range(len(str)):

        index = ord(str[i])
        if (chars[index]) == True:
            return False
        chars[index] = True

    return True
        

if __name__ == "__main__":
    input = "Gecko"
    if (uniqueCharacters(input)):
        print(f"All characters in {input} are unique")
    else:
        print(f"{input} contains duplicate characters")