def test():
    with open("test.txt", "r") as f:
        for line in f:
            test_line(line)


def test_line(line):

    for idx in range(0, len(line), 1):
        # print(line[idx : idx + 4], set(line[idx : idx + 4]))
        for letter in line[idx : idx + 4]:
            if len(set(line[idx : idx + 4])) == 4:
                print("FINALE (test) :", idx + 4)
                return 0


def part1():
    f = open("input.txt", "r")
    line = f.readline()

    for idx in range(0, len(line), 1):
        for letter in line[idx : idx + 4]:
            if len(set(line[idx : idx + 4])) == 4:
                print("FINALE :", idx + 4)
                return 0


def part2():
    # comme part 1 mais sur range plus grand ...
    f = open("input.txt", "r")
    line = f.readline()

    for idx in range(0, len(line), 1):
        for letter in line[idx : idx + 14]:
            if len(set(line[idx : idx + 14])) == 14:
                print("FINALE :", idx + 14)
                return 0


test()
part1()
part2()
