def get_data(test = False):
    with open("input.txt" if not test else "test_input.txt","r") as f:
        return [list(x) for x in f.read().splitlines()]

inputs = get_data()
# print(inputs)


old_state = inputs
new_state = []
X, Y = len(inputs)-1, len(inputs[0])-1
neighbors = lambda x, y : [[x2, y2] for x2 in range(x-1, x+2)
                                for y2 in range(y-1, y+2)
                                if (-1 < x <= X and
                                    -1 < y <= Y and
                                    (x != x2 or y != y2) and
                                    (0 <= x2 <= X) and
                                    (0 <= y2 <= Y))]

def get_occupied_neighors(state,x,y):
    t = neighbors(x,y)
    occupied_neigbors = 0
    for [x, y] in t:
        if state[x][y] == '#':
            occupied_neigbors += 1
    
    return occupied_neigbors

def get_occupied_neighors_part2(state, x, y):
    occupied_neigbors = 0
    
    #horizontal -x
    for i in range(1, Y):
        if y - i < 0: break
        if state[x][y-i] == '#':
            occupied_neigbors += 1
            break
        if state[x][y-i] == 'L':
            break
    #horizontal +x
    for i in range(1, Y):
        if y + i > Y: break
        if state[x][y+i] == '#':
            occupied_neigbors += 1
            break
        if state[x][y+i] == 'L':
            break
    
    #vertical -x
    for i in range(1, X):
        if x - i < 0: break
        if state[x-i][y] == '#':
            occupied_neigbors += 1
            break
        if state[x-i][y] == 'L':
            break
    #vertical +x
    for i in range(1, X+1):
        if x + i > X: break
        if state[x+i][y] == '#':
            occupied_neigbors += 1
            break
        if state[x+i][y] == 'L':
            break

    #diag -x-y
    for i in range(1, X+1):
        if x-i < 0 or x-i > X or y-i < 0 or y-i > Y: break
        if state[x-i][y-i] == '#':
            occupied_neigbors += 1
            break
        if state[x-i][y-i] == 'L':
            break
    #diag +x-y
    for i in range(1, X+1): 
        if x+i < 0 or x+i > X or y-i < 0 or y-i > Y: break
        if state[x+i][y-i] == '#':
            occupied_neigbors += 1
            break
        if state[x+i][y-i] == 'L':
            break

    #diag +x+y
    for i in range(1, X+1):
        if x+i < 0 or x+i > X or y+i < 0 or y+i > Y: break
        if state[x+i][y+i] == '#':
            occupied_neigbors += 1
            break
        if state[x+i][y+i] == 'L':
            break
    #diag -x+y
    for i in range(1, X+1):
        if x-i < 0 or x-i > X or y+i < 0 or y+i > Y: break
        if state[x-i][y+i] == '#':
            occupied_neigbors += 1
            break
        if state[x-i][y+i] == 'L':
            break

    return occupied_neigbors

from copy import deepcopy
# print([print(x) for x in old_state])
same = False
i = 0
while same == False and i < 10000:
    i += 1
    new_state = deepcopy(old_state)
    same = True
    for x, row in enumerate(old_state):
        for y, cell in enumerate(row):
            if cell == 'L':
                oc_n = get_occupied_neighors_part2(old_state,x,y)
                if oc_n == 0:
                    new_state[x][y] = '#'
            elif cell == '#':
                oc_n = get_occupied_neighors_part2(old_state,x,y)
                if oc_n >= 5:
                    new_state[x][y] = 'L'

    for x, row in enumerate(new_state):
        for y, cell in enumerate(row):
            # print(x,y,cell,old_state[x][y])
            if old_state[x][y] != cell:
                same = False
            old_state[x][y] = new_state[x][y]
    # for row in old_state:
    #     print(row)
    #     print('')
    # print("--------")

# print([print(x) for x in new_state])
print(sum([x.count('#') for x in new_state]))
