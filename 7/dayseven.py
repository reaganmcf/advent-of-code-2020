import re

def get_data(test = False):
    ret = list()
    with open("input.txt" if not test else "test_input.txt","r") as f:
        for line in f:
            ret.append(line[:-1 if line[-1] == '\n' else len(line)])
    return ret

def part_one():
    inputs = get_data()
    regex = r"(\w+\s\w+) bag"

    bag_map = dict()

    for rule in inputs:
        matches = re.findall(regex, rule)
        color = re.match(r"(.+?) bags contain", rule)[1]
        print(list(re.findall(r"\d+? (\w+\s\w+) bags?", rule)))
        bag_map[color] = list(re.findall(r"\d+? (\w+\s\w+) bags?", rule))

    def has_shiny_gold(color):
        if color == "shiny gold":
            return True
        else:
            return any(has_shiny_gold(c) for c in bag_map[color])

    ans = 0
    for bag in bag_map:
        if has_shiny_gold(bag):
            ans += 1

    print(ans - 1) #always matches with itself

def part_two():
    inputs = get_data()
    regex = r"(\w+\s\w+) bag"

    bag_map = dict()

    for rule in inputs:
        matches = re.findall(regex, rule)
        color = re.match(r"(.+?) bags contain", rule)[1]
        # print(list(re.findall(r"(\d+?) (\w+\s\w+) bags?", rule)))
        bag_map[color] = list(re.findall(r"(\d+?) (\w+\s\w+) bags?", rule))
    
    print(bag_map)

    def bags_in_bag(bag):
        t = 1
        for count, b in bag_map[bag]:
            t += int(count) * bags_in_bag(b)
        return t
    
    ans = bags_in_bag("shiny gold") - 1
    print(ans) 

part_one()
part_two()
