def get_data(test = False):
    ret = list()
    with open("input.txt" if not test else "test_input.txt", "r") as f:
        grp = list()
        for line in f:
            if len(line) == 1:
                ret.append(grp)
                grp = list()
            else:
                grp.append(line[:-1 if line[-1] == '\n' else len(line)])

        if grp not in ret:
            ret.append(grp)
    return ret

def part_one():
    inputs = get_data()
    ans = 0
    for group in inputs:
        answers = set()
        for person in group:
            for answer in person:
                answers.add(answer)
        ans += len(answers)
    print(ans)

def part_two():
    inputs = get_data()
    ans = 0
    for group in inputs:
        answers = set(x for x in group[0])
        for i in range(1, len(group)):
            t_set = set(t for t in group[i])
            answers = answers & t_set
        ans += len(answers)
    print(ans)
    
part_two()
