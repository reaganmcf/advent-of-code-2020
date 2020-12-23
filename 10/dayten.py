def get_data(test = False):
    with open("input.txt" if not test else "test_input.txt","r") as f:
        return [int(x) for x in f.read().splitlines()]

inputs = get_data(False)
inputs.append(max(inputs) + 3)
inputs.sort()
adapters = set(inputs)

differences = [0,0,0]
paths = list()
def findDifferences(curr_joltage, path = set()):
    global paths
    flag = False
    if curr_joltage + 1 in adapters:
        flag = True
        differences[0] += 1
        path.add(curr_joltage)
        findDifferences(curr_joltage + 1)
    if curr_joltage + 2 in adapters:
        flag = True
        differences[1] += 1
        path.add(curr_joltage)
        findDifferences(curr_joltage + 2)
    if curr_joltage + 3 in adapters:
        flag = True
        differences[2] += 1
        path.add(curr_joltage)
        findDifferences(curr_joltage + 3)
    
    if not flag:
        paths.append(path)

# findDifferences(0)
# print('Part 1: ' + str(differences[0] * differences[2]))


# part 2
from collections import defaultdict
dp = defaultdict(int)
inputs.append(0)
inputs.sort()
dp[inputs[-1]] = 1
for i in inputs[-2::-1]:
    dp[i] = dp[i+1] + dp[i+2] + dp[i+3]

print('Part 2: ' + str(dp[0]))