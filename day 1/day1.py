import re

#regular expressions to match patterns in strings
letter = re.compile(r'[a-z]')
zero = re.compile(r'zero')
one = re.compile(r'one')
two = re.compile(r'two')
three = re.compile(r'three')
four = re.compile(r'four')
five = re.compile(r'five')
six = re.compile(r'six')
seven = re.compile(r'seven')
eight = re.compile(r'eight')
nine = re.compile(r'nine')


#converts string to number
def converter(input_str):
    parsed = one.sub('o1e', input_str)
    parsed = two.sub('t2o', parsed)
    parsed = three.sub('t3e', parsed)
    parsed = four.sub('f4r', parsed)
    parsed = five.sub('f5e', parsed)
    parsed = six.sub('s6x', parsed)
    parsed = seven.sub('s7n', parsed)
    parsed = eight.sub('e8t', parsed)
    parsed = nine.sub('n9e', parsed)
    parsed = zero.sub('z0o', parsed)
    parsed = letter.sub('', parsed)

    return parsed



def part1():
    file = open("day1.txt", 'r')

    ans = 0

    for line in file.readlines():
        number = letter.sub('', line)
        digits = list(number)[0:-1]
        ans += (10 * int(digits[0])) + int(digits[-1])

    file.close()

    print("part 1:", ans)


def part2():
    file = open("day1.txt", 'r')

    ans = 0

    for line in file.readlines():
        number = converter(line)
        digits = list(number)[0:-1]
        ans += (10 * int(digits[0])) + int(digits[-1])

    file.close()

    print("part 2:", ans)

part1()
part2()