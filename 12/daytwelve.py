def get_data(test = False):
    with open("input.txt" if not test else "test_input.txt","r") as f:
        return [x for x in f.read().splitlines()]

inputs = get_data()
# print(inputs)

# we start by facing east
curr_pos = [0,0]
#0 = North, 1 = East, 2 = South, 3 = West
curr_dir = 1

for ixn in inputs:
    action, value = str(ixn[0]), int(ixn[1:])
    if action == 'N':
        curr_pos[1] += value
    elif action == 'E':
        curr_pos[0] += value
    elif action == 'S':
        curr_pos[1] -= value
    elif action == 'W':
        curr_pos[0] -= value
    elif action == 'L':
        curr_dir = (curr_dir - (value // 90)) % 4
    elif action == 'R':
        curr_dir = (curr_dir + (value // 90)) % 4
    elif action == 'F':
        if curr_dir == 0:
            curr_pos[1] += value
        elif curr_dir == 1:
            curr_pos[0] += value
        elif curr_dir == 2:
            curr_pos[1] -= value
        elif curr_dir == 3:
            curr_pos[0] -= value

manhattan_distance = abs(curr_pos[0]) + abs(curr_pos[1])
print('part 1: ' + str(manhattan_distance))

boat_pos = [0,0]
boat_dir = 1
waypoint_pos = [10,1]

for ixn in inputs:
    action, value = str(ixn[0]), int(ixn[1:])
    if action == 'N':
        waypoint_pos[1] += value
    elif action == 'E':
        waypoint_pos[0] += value
    elif action == 'S':
        waypoint_pos[1] -= value
    elif action == 'W':
        waypoint_pos[0] -= value
    elif action == 'L':
        # rotate waypoint around ship counter clockwise
        degrees = value // 90
        if degrees == 1:
            waypoint_pos[0], waypoint_pos[1] = -waypoint_pos[1], waypoint_pos[0]
        elif degrees == 2:
            waypoint_pos[0], waypoint_pos[1] = -waypoint_pos[0], -waypoint_pos[1]
        elif degrees == 3:
            waypoint_pos[0], waypoint_pos[1] = waypoint_pos[1], -waypoint_pos[0]
    elif action == 'R':
        # rotate waypoint around ship clockwise
        degrees = value // 90
        if degrees == 1:
            waypoint_pos[0], waypoint_pos[1] = waypoint_pos[1], -waypoint_pos[0]
        elif degrees == 2:
            waypoint_pos[0], waypoint_pos[1] = -waypoint_pos[0], -waypoint_pos[1]
        elif degrees == 3:
            waypoint_pos[0], waypoint_pos[1] = -waypoint_pos[1], waypoint_pos[0]
    elif action == 'F':
        boat_pos[0] += waypoint_pos[0] * value
        boat_pos[1] += waypoint_pos[1] * value

manhattan_distance = abs(boat_pos[0]) + abs(boat_pos[1])
print('part 2: ' + str(manhattan_distance))