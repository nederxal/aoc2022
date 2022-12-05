import pprint
import re


def gen():
    cargo = {}
    orders = []

    with open("input5.txt", "r") as f:

        for line in f:
            for char in range(1, len(line), 4):
                if line[char] != " " and "[" in line:
                    cargo.setdefault(int(char / 4) + 1, []).append(line[char])

            if "move" in line:
                re.findall(r"\d+", line)
                orders.append(map(int, re.findall(r"\d+", line)))

    return cargo, orders


def part1():
    cargo, orders = gen()
    for qte, start, end in orders:
        for i in range(qte):
            cargo[end].insert(0, cargo[start].pop(0))

    print("FINAL 1")
    pprint.pprint(cargo, indent=4)


def part2():
    cargo, orders = gen()
    for qte, start, end in orders:
        to_app = []
        for i in range(qte):
            to_app.append(cargo[start].pop(0))

        to_app.reverse()

        for i in range(len(to_app)):
            cargo[end].insert(0, to_app[i])
        to_app.clear()

    print("FINAL2 ")
    pprint.pprint(cargo, indent=4)


part1()
part2()
