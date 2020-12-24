def oneEditAway(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    m = len(str1)
    n = len(str2)

    count = 0
    i=j=0
    while i<m and j<n:
        if str1[i] != str[j]:
            if count == 1:
                return False

            if m > n:
                i+=1
            elif m < n:
                j+=1
            else:
                i+=1
                j+=1
            count+=1
        else:
            i+=1
            j+=1

if __name__ == "__main__":
    str1 = "gfg"
    str2 = "gf"

    if oneEditAway(str1, str2):
        print("Yes")
    else:
        print("No")