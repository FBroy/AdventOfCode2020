def findRecursively(color):
    amount = 0
    i = colors.index(color)
    for j in range(len(inside[i])):
        amount += int(numbers[i][j]) + int(numbers[i][j]) * findRecursively(inside[i][j])
    return amount

with open("input.txt") as f:
    #parsing input
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split(" bags contain ")
        lines[i][1] = lines[i][1].split(", ")
        for j in range(len(lines[i][1])):
            lines[i][1][j] = lines[i][1][j].replace(" bags", "")
            lines[i][1][j] = lines[i][1][j].replace(" bag", "")
            lines[i][1][j] = lines[i][1][j].replace(".", "")
            lines[i][1][j] = lines[i][1][j].split(" ", 1)
        lines[i][1][-1][1] = lines[i][1][-1][1].replace("\n", "")       

    colors = []
    numbers = []
    inside = []
    for i in range(len(lines)):
        colors.append(lines[i][0])
        numbers.append([])
        inside.append([])
        for j in range(len(lines[i][1])):
            if lines[i][1][j][0].isnumeric():
                numbers[i].append(lines[i][1][j][0])
                inside[i].append(lines[i][1][j][1])
    #end of parsing

    """
    color = all the main bags
    inside[i] = the bags inside the bag at index i
    numbers[i] = the amount of bags inside the bag at index i
    """

    amount = 0
    i = colors.index("shiny gold")
    for j in range(len(inside[i])):
        amount += int(numbers[i][j]) + int(numbers[i][j]) * findRecursively(inside[i][j])
    print(amount)