
def part_one():
    with open("input.txt", "r") as f:
        for line in f:
            t = int(line)
            two_sum[2020 - t] = t 
            if t in two_sum:
                print(t * (2020 - t))
                return

def part_two():
    inputs = list()
    with open("input.txt", "r") as f:
        for line in f:
            t = int(line)
            inputs.append(t)

    inputs.sort()
    for i, v in enumerate(inputs[:-2]):
        d = {}
        for x in inputs[i+1:]:
            if x not in d:
                d[2020-v-x] = 1
            else:
                print(v * (2020 - v -x) * x)
                return