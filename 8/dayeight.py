def get_data(test = False):
    with open("input.txt" if not test else "test_input.txt","r") as f:
        return f.read().splitlines()

def run_program(instructions):
    executed_instructions = set()
    inputs = instructions
    idx, acc = 0, 0
    while idx < len(inputs):
        if idx in executed_instructions:
            return False, acc
        else:
            executed_instructions.add(idx)
            isn = inputs[idx][0:3]
            if isn == 'nop':
                # print('nop')
                idx += 1
            elif isn == 'acc':
                v = int(inputs[idx][4:])
                # print(v)
                acc += v
                idx += 1
            else:
                v = int(inputs[idx][4:])
                # print("jumping " + str(v))
                idx = idx + v
    return True, acc

def part_one():
    status, ans = run_program(get_data())
    print(ans)

def part_two():
    instructions = get_data()
    for i, isn in enumerate(instructions):
        old_isn = isn
        if isn[0:3] == 'acc':
            continue
        elif isn[0:3] == 'nop':
            instructions[i] = 'jmp' + isn[3:]
        elif isn[0:3] == 'jmp':
            instructions[i] = 'nop' + isn[3:]
        
        status, acc = run_program(instructions)
        instructions[i] = old_isn
        if status:
            print(acc)
            return

part_one()
part_two()