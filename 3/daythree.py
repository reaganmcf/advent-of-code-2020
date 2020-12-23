def get_data():
    ret = list()
    with open("input.txt", "r") as f:
        for line in f:
            ret.append(line[:-1 if line[-1] == '\n' else len(line)])

    return ret

def check_slope(col_slope, row_slope):
    inputs = get_data()
    row,col = 0,0
    width, height = len(inputs[0]), len(inputs)
    ans = 0
    while row < height:
        if inputs[row][col] == '#':
            ans += 1
        row = row + row_slope
        col = (col + col_slope) % (width)
    return ans

def part_one():
    ans = check_slope(1,3)
    assert ans == 162
    print(ans)
    
def part_two():
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    ans = 1
    for slope in slopes:
        print(slope[0], slope[1])
        ans = ans * check_slope(slope[0], slope[1])

    print(ans)

part_two()