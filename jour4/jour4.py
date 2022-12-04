def part1():
    somme = 0
    with open("input4.txt", "r") as f:
        for line in f:
            sec1, sec2 = line.rstrip().split(",")

            l1, u1 = map(int, sec1.split("-"))
            sec1_len = u1 - l1

            l2, u2 = map(int, sec2.split("-"))
            sec2_len = u2 - l2

            if sec1_len <= sec2_len:
                if l1 >= l2 and u1 <= u2:
                    somme += 1

            if sec2_len < sec1_len:
                if l2 >= l1 and u2 <= u1:
                    somme += 1
    print(somme)


def part2():
    somme = 0
    with open("input4.txt", "r") as f:
        for line in f:
            sec1, sec2 = line.rstrip().split(",")

            l1, u1 = map(int, sec1.split("-"))
            l2, u2 = map(int, sec2.split("-"))

            if (
                (l2 <= l1 <= u2 or l2 <= u1 <= u2)
                or (l1 <= l2 and u1 >= u2)
                or (l2 <= l1 and u2 >= u1)
            ):
                print(line.rstrip(), "overlapping")
                somme += 1

    print(somme)


# part1()
part2()
