with open("input.txt") as f:
    lines = f.readlines()
    trees = 0
    index = 0
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
        if lines[i][index%len(lines[i])] == "#":
            trees += 1
        index += 3
    

print(trees)