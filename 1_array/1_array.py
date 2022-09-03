from array import Array
# Test new ssh
import random

valuesList = Array(100)

for i in range(len(valuesList)):
    valuesList[i] = random.random()

for value in valuesList:
    print(value)

