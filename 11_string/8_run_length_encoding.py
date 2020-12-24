from collections import OrderedDict

def runLengthEncoding(string):
    dictionary = OrderedDict.fromkeys(string, 0)

    for i in string:
        dictionary[i] += 1

    res = ""
    for key, value in dictionary.items():
        res = res+key+str(value)
    
    return res

if __name__ == "__main__":
    string = "aabbbccc"
    print(runLengthEncoding(string))