"""
part 1
A   ROCK        X   = 1
B   PAPER       Y   = 2
C   Scissors    Z   = 3


défaite     = 0
nul         = 3
victoire    = 6

part 2
X = doit perdre
Y = doit nul
Z = doit win

"""
from enum import IntEnum

# class Values(IntEnum):
#     ROCK = 1
#     PAPER = 2
#     SCISSORS = 3


class ChoixElfe(IntEnum):
    A = 1
    B = 2
    C = 3


class ChoixMoi(IntEnum):
    X = 1
    Y = 2
    Z = 3


class Resultat(IntEnum):
    VICTOIRE = 6
    NUL = 3
    DEFAITE = 0


def main():
    total = 0
    total2 = 0

    with open("input2.txt", "r") as f:
        for line in f:
            elfe, moi = line.rstrip().split(" ")

            if elfe == "A" and moi == "X":
                # part 1 -> nul
                total += Resultat.NUL.value + ChoixMoi.X.value
                # part 2 -> perte
                total2 += Resultat.DEFAITE.value + ChoixMoi.Z.value
            if elfe == "A" and moi == "Y":
                # part 1 -> je gagne
                total += Resultat.VICTOIRE.value + ChoixMoi.Y.value
                # part 2 -> nul
                total2 += Resultat.NUL.value + ChoixMoi.X.value
            if elfe == "A" and moi == "Z":
                # part 1 -> je perds
                total += Resultat.DEFAITE.value + ChoixMoi.Z.value
                # part 2 -> je gagne
                total2 += Resultat.VICTOIRE.value + ChoixMoi.Y.value

            if elfe == "B" and moi == "X":
                # part 1 -> je perds
                total += Resultat.DEFAITE.value + ChoixMoi.X.value
                # part 2 -> perte
                total2 += Resultat.DEFAITE.value + ChoixMoi.X.value
            if elfe == "B" and moi == "Y":
                # part 1 -> nul
                total += Resultat.NUL.value + ChoixMoi.Y.value
                # part 2 -> nul
                total2 += Resultat.NUL.value + ChoixMoi.Y.value
            if elfe == "B" and moi == "Z":
                # part 1 -> je gagne
                total += Resultat.VICTOIRE.value + ChoixMoi.Z.value
                # part 2 -> je gagne
                total2 += Resultat.VICTOIRE.value + ChoixMoi.Z.value

            if elfe == "C" and moi == "X":
                # part 1 -> je gagne
                total += Resultat.VICTOIRE.value + ChoixMoi.X.value
                # part 2 -> perte
                total2 += Resultat.DEFAITE.value + ChoixMoi.Y.value
            if elfe == "C" and moi == "Y":
                # part 1 -> je perds
                total += Resultat.DEFAITE.value + ChoixMoi.Y.value
                # part 2 -> nul
                total2 += Resultat.NUL.value + ChoixMoi.Z.value
            if elfe == "C" and moi == "Z":
                # part 1 -> nul
                total += Resultat.NUL.value + ChoixMoi.Z.value
                # part 2 -> je gagne
                total2 += Resultat.VICTOIRE.value + ChoixMoi.X.value
            # print(total2)

    print(total)
    print(total2)


main()
