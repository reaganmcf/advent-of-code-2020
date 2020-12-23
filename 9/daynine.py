def get_data(test = False):
    with open("input.txt" if not test else "test_input.txt","r") as f:
        return [int(x) for x in f.read().splitlines()]


def check_sum(window, curr):
    for i, i_v in enumerate(window):
        for j, j_v in enumerate(window):
            if i_v + j_v == curr: 
                return True
    return False

def decode(preamble_length = 25):
    inputs = get_data()
    window = list()
    for i in range(0, preamble_length):
        window.append(inputs[i])
    
    
    for i in range(preamble_length, len(inputs)):
        # check if the current number is a sum of any 2 values in window
        curr = inputs[i]
        if check_sum(window, curr) == False:
            print(curr)ar
            return curr
        window.pop(0)    
        window.append(curr)
    
invalid_num = decode()
inputs = get_data()

start, end = 0,1
curr_sum = sum(inputs[start:end]) 
while curr_sum != invalid_num and start != len(inputs):
    if curr_sum > invalid_num:
        start += 1
    else:
        end += 1
    curr_sum = sum(inputs[start:end])

print(min(inputs[start:end]) + max(inputs[start:end]))