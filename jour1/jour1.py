def main():

    total_cal = 0
    tab_cal = []

    with open("input1.txt", "r") as f:
        for line in f:
            if len(line) == 0 or line == '\n':
                tab_cal.append(total_cal)
                total_cal = 0
            else:
                total_cal += int(line)


    tab_cal.sort()
    top3 = sum(tab_cal[-3:])
    print("Max cal :",tab_cal[-1])
    print("Somme top 3", top3)
    
    
main()
