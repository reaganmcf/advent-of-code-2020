def get_data(test = False):
    with open("input.txt" if not test else "test_input.txt","r") as f:
        return [x for x in f.read().splitlines()]

inputs = get_data(True)
timestamp = int(inputs[0])
ids_in_service = [int(x) for x in inputs[1].split(",") if x != 'x']

mods = [x - (timestamp % x) for x in ids_in_service]
earliest_time_idx = mods.index(min(mods))
earliest_bus_id = ids_in_service[earliest_time_idx]
print('part 1: ' + str(earliest_bus_id * mods[earliest_time_idx]))

# chinese remainder thoerem

indexes_and_nums = [(i, v) for i, v in enumerate(ids_in_service)]
rests, divisors = [], []
for (ind, num) in indexes_and_nums:
    rests.append((-ind) % num)
    divisors.append(num)

print(rests, divisors)