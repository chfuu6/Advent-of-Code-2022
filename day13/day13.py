import json
f = open('day13.txt', 'r')
input = f.read().split('\n\n')

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

answer = 0
for index, pair in enumerate(input):
    leftPair, rightPair = pair.split('\n')
    leftPair = json.loads(leftPair)
    rightPair = json.loads(rightPair)
    result = compare(leftPair, rightPair)
    if result == True:
        answer += index+1
    print(index+1, result)
print(answer)
    