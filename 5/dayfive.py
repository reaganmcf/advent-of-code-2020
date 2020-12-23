def get_data(test = False):
    ret = list()
    with open("input.txt" if not test else "test_input.txt", "r") as f:
        for line in f:
            ret.append(line[:-1 if line[-1] == '\n' else len(line)])
    return ret

def get_seatID(row, col):
    return row * 8 + col

def getIds():
    inputs = get_data()
    ids = list()
    for p in inputs:
        left, right = 0,128-1
        for i in range(7):
            if p[i] == 'F':
                right = (left + right) // 2
            else:
                left = ((left + right) // 2) + 1
        row = min(left, right)

        left, right = 0, 8-1
        for i in range(7,10):
            if p[i] == 'L':
                right = (left + right) // 2
            else:
                left = ((left + right) // 2) + 1
        col = min(left, right)

        ids.append(get_seatID(row,col))
    
    return ids

def part_one():
    ids = getIds()
    print(max(ids))

def part_two():
    ids = getIds()
    ids.sort()
    for i in range(1,len(ids)):
        if ids[i-1] + 1 != ids[i]:
            print(ids[i-1]+1)


part_one()
part_two()
