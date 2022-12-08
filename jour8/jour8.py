def test():
    forest = []
    with open("test.txt", "r") as f:
        for line in f.readlines():
            forest.append(line.rstrip())

    for i in range(1, len(forest) - 1, 1):
        for j in range(1, len(forest[i]) - 1, 1):
            print(forest[i][j])
            # break
        break


test()
