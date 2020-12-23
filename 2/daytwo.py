import re

def get_data():
    ret = list()
    with open("input.txt", "r") as f:
        for line in f:
            ret.append(line[:-1 if line[-1] == '\n' else len(line)])

    return ret

def part_one():
    inputs = get_data()
    # inputs = ["1-3 b: azcde"]
    res = list()
    regex = r"(\d+)-(\d+)\s(\w):\s(\w+)"
    for line in inputs:
        cnt = 0
        matches = list(re.findall(regex, line)[0])
        for c in matches[3]:
            if c == matches[2]:
                cnt += 1
        
        lower, upper = int(matches[0]), int(matches[1])
        if cnt >= lower and cnt <= upper:
            res.append(matches[-1])

    print(len(res))


def part_two():
    inputs = get_data()
    ans = 0
    regex = r"(\d+)-(\d+)\s(\w):\s(\w+)"
    for line in inputs:
        matches = list(re.findall(regex, line)[0])
        
        i1, i2, target = int(matches[0])-1, int(matches[1])-1, matches[2]
        pos1_bool = matches[3][i1] == target
        pos2_bool = matches[3][i2] == target 
        if pos1_bool != pos2_bool:
            ans = ans + 1

    print(ans)

part_two()