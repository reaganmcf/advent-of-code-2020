import re

def get_data(test=False):
    ret = list()
    regex = "(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):(\w+|#\w+)?"
    pattern = re.compile(regex, re.I|re.U)
    with open("input.txt" if not test else "test_input.txt", "r") as f:
        curr = {}
        for line in f:
            if len(line) == 1:
                ret.append(curr)
                curr = {}
            else:
                for m in pattern.finditer(line):
                    key, val = m.groups()
                    curr[key] = val
        
        if curr not in ret:
            ret.append(curr)
    return ret

def part_one():
    passports = get_data()
    ans = 0
    required_fields = [
        'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'
    ]
    print(len(passports))
    for passport in passports:
        flag = True
        for f in required_fields:
            if f not in passport:
                flag = False

        ans += 1 if flag else 0
    print(ans)

def part_two():
    passports = get_data()
    ret = list()
    ans = 0
    required_fields = [
        'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'
    ]
    for passport in passports:
        flag = True
        for f in required_fields:
            if f not in passport:
                flag = False
        
        if flag is False:
            continue
        
        byr = int(passport['byr'])
        if byr < 1920 or byr > 2002:
            continue
        iyr = int(passport['iyr'])
        if iyr < 2010 or iyr > 2020:
            continue
        eyr = int(passport['eyr'])
        if eyr < 2020 or eyr > 2030:
            continue

        hgt = int(passport['hgt'][:-2])
        if passport['hgt'][-2:] == 'cm':
            if hgt < 150 or hgt > 193:
                continue
        else:
            if hgt < 59 or hgt > 76:
                continue
        
        hcl = passport['hcl']
        if not re.match("#([0-9a-f]){6}", hcl):
            print('failed hcl match')
            continue


        valid_ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        ecl = passport['ecl']
        if ecl not in valid_ecls:
            continue

        pid = passport['pid']
        if len(pid) != 9:
            continue
        if not re.match("[0-9]+", pid):
            continue

        # ret.append(passport)
        ans += 1

    print(ret)
    print(ans)

part_two()