import re


def isvalid(input_str):
    separate = input_str.split(", ")
    dic = {'blue': 0, 'green': 0, 'red': 0}

    for pair in separate:
        spl = pair.split(' ')
        dic[spl[1]] = int(spl[0])

    return dic["blue"] <= 14 and dic["green"] <= 13 and dic["red"] <= 12

def finddeg(str):
    separate = str.split(", ")
    dic = {'blue': 0, 'green': 0, 'red': 0}

    for pair in separate:
        spl = pair.split(' ')
        dic[spl[1]] = max(int(spl[0]), dic[spl[1]])

    return dic["blue"] * dic["green"] * dic["red"]


def part1():
    file = open("day2.txt", "r")

    ans = 0
    it = 1
    pattern = re.compile(r"^Game [1-9][0-9]?[0]?: ")

    for line in file.readlines():
        cleared = pattern.sub('', line)
        inputs = cleared.replace('\n', '').split("; ")

        flag = True
        for i in inputs:
            if not isvalid(i):
                flag = False
        if flag:
            ans += it
        it += 1

    file.close()

    print("part 1:", ans)


def part2():
    file = open("day2.txt", "r")

    ans = 0
    it = 1
    pattern = re.compile(r"^Game [1-9][0-9]?[0]?: ")

    for line in file.readlines():
        cleared = pattern.sub('', line)
        inputs = cleared.replace('\n', '').replace(";", ",")

        ans += finddeg(inputs)

    file.close()
    print("part 2:", ans)


part1()
part2()