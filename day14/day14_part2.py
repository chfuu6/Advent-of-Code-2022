f = open('day14.txt', 'r')
rock = f.read().split('\n')

rock = list(map(lambda x: x.split(' -> '), rock))

width_max = 0
height_max = 0
width_min = 10000
for wall in rock:
    for item in wall:
        width_max = max(width_max, int(item.split(',')[0]))
        height_max = max(height_max, int(item.split(',')[1]))
        width_min = min(width_min, int(item.split(',')[0]))
# print(width_max, height_max, width_min)

structure = []
for i in range(height_max+3):
    temp = []
    for j in range(1000):
        temp.append('.')
    structure.append(temp)

for i in range(len(structure[0])):
    structure[height_max+2][i] = '#'

def printStructure(): 
    for i in range(0, height_max+3):
        for j in range(300, 700):
            print(structure[i][j], end='')
        print('')

for wall in rock:
    for i in range(len(wall)-1):
        first_posx, first_posy = wall[i].split(',')
        second_posx, second_posy = wall[i+1].split(',')
        first_posx = int(first_posx)
        first_posy = int(first_posy)
        second_posx = int(second_posx)
        second_posy = int(second_posy)
        # print(first_posx, second_posx, first_posy, second_posy)
        if first_posx == second_posx:
            if first_posy < second_posy:
                for pos in range(first_posy, second_posy+1):
                    structure[pos][first_posx] = '#'
            else:
                for pos in range(second_posy, first_posy+1):
                    structure[pos][first_posx] = '#' 
        else:
            if first_posx < second_posx:
                for pos in range(first_posx, second_posx+1):
                    structure[first_posy][pos] = '#'
            else:
                for pos in range(second_posx, first_posx+1):
                    structure[first_posy][pos] = '#'


def check_sand(row, col, height_max):
    global count
    if structure[row+1][col] == '.':
        # 可以通過
        row += 1
        row = check_sand(row, col, height_max)
    elif structure[row][col] == 'o':
        structure[row][col] = 'o'
        return row
    else:
        if structure[row+1][col-1] == '.':
            # 可以通過
            row += 1
            col -= 1
            row = check_sand(row, col, height_max)
            
        else:
            if structure[row+1][col+1] == '.':
                # 可以通過
                row += 1
                col += 1
                row = check_sand(row, col, height_max)               
            else:
                structure[row][col] = 'o'
                count += 1
                

count = 0
while True:
    row, col = 0, 500
    row = check_sand(row, col, height_max)
    if row == 0:
        break

# printStructure()
print(count)