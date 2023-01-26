f = open('day12.txt', 'r')
maze = list(map(lambda x: [*x], f.read().split('\n')))
queue = []
path = {}
for row in range(len(maze)):
    for col in range(len(maze[0])):
        if maze[row][col] == 'S':
            queue.append([row, col])
            maze[row][col] = 'a'
        if maze[row][col] == 'E':
            target_row, target_col = row, col
            maze[row][col] = 'z'

count_map = []
for row in range(len(maze)):
    temp = []
    for col in range(len(maze[0])):
        temp.append(0)
    count_map.append(temp)

def check(row, col, num):
    # print(count_map)
    if row-1 >= 0:
        if path.get(str([row-1, col])) != True:
            # print(ord(maze[row-1][col]), ord(maze[row][col]), 'up')
            if (ord(maze[row-1][col]) <= ord(maze[row][col])) or (ord(maze[row-1][col])-1 == ord(maze[row][col])):
                if [row-1, col] not in queue:
                    queue.append([row-1, col])
                count_map[row-1][col] = num + 1
    if row+1 <= len(maze)-1:
        if path.get(str([row+1, col])) != True:
            # print(ord(maze[row+1][col]), ord(maze[row][col]), 'down')
            if (ord(maze[row+1][col]) <= ord(maze[row][col])) or (ord(maze[row+1][col])-1 == ord(maze[row][col])):
                if [row+1, col] not in queue:
                    queue.append([row+1, col])
                count_map[row+1][col] = num + 1
    if col-1 >= 0:
        if path.get(str([row, col-1])) != True:
            # print(ord(maze[row][col-1]), ord(maze[row][col]), 'left')
            if (ord(maze[row][col-1]) <= ord(maze[row][col])) or (ord(maze[row][col-1])-1 == ord(maze[row][col])):
                if [row, col-1] not in queue:
                    queue.append([row, col-1])
                count_map[row][col-1] = num + 1
    if col+1 <= len(maze[0])-1:
        if path.get(str([row, col+1])) != True:
            # print(ord(maze[row][col+1]), ord(maze[row][col]), 'right')
            if (ord(maze[row][col+1]) <= ord(maze[row][col])) or (ord(maze[row][col+1])-1 == ord(maze[row][col])):
                if [row, col+1] not in queue:
                    queue.append([row, col+1])
                count_map[row][col+1] = num + 1

while len(queue) > 0:
    # print(queue)
    position = queue.pop(0)
    path[str(position)] = True
    row, col = position
    num = count_map[row][col]
    check(row, col, num)

print(count_map[target_row][target_col])

