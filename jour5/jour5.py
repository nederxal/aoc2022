import pprint
import re


cargo = {}
orders = []


def gen(f):

    for line in f:
        for char in range(1, len(line), 4):
            if line[char] != " " and re.search(r"\[", line):
                cargo.setdefault(int(char / 4) + 1, []).append(line[char])

        if re.match("move", line):
            orders.append(line.rstrip())


def part1(cargo, orders):
    for instruct in orders:
        qte, start, end = re.findall(r"\d+", instruct)
        for i in range(int(qte)):
            cargo[int(end)].insert(0, cargo[int(start)].pop(0))

    print("FINAL")
    pprint.pprint(cargo, indent=4)


def part2(cargo, orders):
    for instruct in orders:
        qte, start, end = re.findall(r"\d+", instruct)
        to_app = []
        for i in range(int(qte)):
            to_app.append(cargo[int(start)].pop(0))

        to_app.reverse()

        for i in range(len(to_app)):
            cargo[int(end)].insert(0, to_app[i])
        to_app.clear()

    print("FINAL")
    pprint.pprint(cargo, indent=4)


f = open("input5.txt", "r")
gen(f)

part1(cargo, orders)
part2(cargo, orders)
