def part1():
    somme = 0
    with open("input3.txt", "r") as f:
        for line in f:
            semi_len = int(len(line.rstrip()) / 2)
            for char in line.rstrip()[:semi_len]:
                if char in line.rstrip()[semi_len:]:
                    print(char, " <-- doublon")
                    if char in lower:
                        somme += lower.index(char) + 1
                    else:
                        somme += upper.index(char)+27
                    
                    break
    
    print(somme)

def part2():
    somme = 0
    with open("input3.txt", "r") as f:
        foo = [ line.rstrip() for line in f]

    for line in range(0, len(foo), 3):
        for char in foo[line]:
            if char in foo[line+1] and char in foo[line+2]:
                if char in lower:
                    somme += lower.index(char) + 1
                else:
                    somme += upper.index(char)+27
                break
    print(somme)




lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

part1()
part2()