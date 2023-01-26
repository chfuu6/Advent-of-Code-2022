import json
import numpy as np
from functools import reduce
f = open('day13.txt', 'r')
input = f.read().split('\n\n')
input = list(map(lambda x: x.split('\n'), input))
input = np.array(input)
input = input.flatten()
# input = reduce(lambda acc, cur: acc+cur, input)
input = list(filter(lambda x: x != '', input))
input = list(map(lambda x: json.loads(x), input))

input.append([[2]])
input.append([[6]])

def compare(leftPair, rightPair):
    result = None
    leftPair_len = len(leftPair)
    rightPair_len = len(rightPair)
    times = min(leftPair_len, rightPair_len)

    for i in range(times):
        if type(leftPair[i]) == int and type(rightPair[i]) == int:
            # print(2)
            if leftPair[i] < rightPair[i]:
                return True
            elif leftPair[i] > rightPair[i]:
                return False
        elif type(leftPair[i]) == list and type(rightPair[i]) == list:
            # print(3)
            result = compare(leftPair[i], rightPair[i])
        else:
            if type(leftPair[i]) == int:
                # print(4)
                temp = [leftPair[i]]
                result = compare(temp, rightPair[i])
            elif type(rightPair[i]) == int:
                # print(5)
                temp = [rightPair[i]]
                result = compare(leftPair[i], temp)

        if result == True:
            return True
        elif result == False:
            return False

    if result == None:
        if leftPair_len < rightPair_len:
            return True
        elif leftPair_len > rightPair_len:
            return False
    elif result == True:
        return True
    elif result == False:
        return False

for i in range(len(input)):
    for j in range(i+1, len(input)):

        leftPair = input[i]
        rightPair = input[j]
        result = compare(leftPair, rightPair)
        # print(leftPair, rightPair, result)

        if result == False:
            input[i], input[j] = input[j], input[i]
        
print((input.index([[2]])+1) * (input.index([[6]])+1))
    