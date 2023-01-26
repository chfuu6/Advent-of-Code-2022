f = open('day15.txt', 'r')
f = f.read().split('\n')
f = list(map(lambda x: x.split(' '), f))

input = []
for item in f:
    temp = []
    for i in range(10):
        if i == 2 or i == 3 or i == 8 or i == 9:
            temp.append(item[i])
    input.append(temp)

for item in input:
    for i in range(4):
        item[i] = item[i].split('=')[1]
        item[i] = item[i].rstrip(':')
        item[i] = item[i].strip(',')

for target in range(4000000):
    beacon_dict = {}
    each_space = []
    for item in input:
        sensorX, sensorY = int(item[0]), int(item[1])
        beaconX, beaconY = int(item[2]), int(item[3])
        # print(sensorX, sensorY, beaconX, beaconY)
        distance = abs(sensorX-beaconX) + abs(sensorY-beaconY)
        if distance - abs(target - sensorY) > 0:
            leftSide = sensorX - (distance - abs(target - sensorY))
            rightSide = sensorX + (distance - abs(target - sensorY))
            each_space.append([leftSide, rightSide])
        # if beaconY == target:
            # beacon_dict[beaconX] = True


    each_space.sort()
    # print(each_space)
    answer = [each_space[0]]
    for item in each_space:
        compare = answer[-1]
        # print(compare, item)
        if item[0] < compare[0] and compare[0] <= item[1] and item[1] <= compare[1]:
            # answer.append([item[0], compare[1]])
            answer[-1] = [item[0], compare[1]]
        elif item[0] >= compare[0] and item[0] <= compare[1] and item[1] > compare[1]:
            # answer.append([compare[0], item[1]])
            answer[-1] = [compare[0], item[1]]
        elif item[0] >= compare[0] and item[1] <= compare[1]:
            # answer.append([compare[0], compare[1]])
            answer[-1] = [compare[0], compare[1]]
        elif item[0] < compare[0] and item[1] > compare[1]:
            # answer.append([item[0], item[1]])
            answer[-1] = [item[0], item[1]]
        else:
            answer.append(item)

    # print(answer[0][1] - answer[0][0] - len(beacon_dict) + 1)
    if len(answer) > 1:
        print(answer, target)
        break
print(3267801*4000000 + 2703981)