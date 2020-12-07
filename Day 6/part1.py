def getCount(arr):
    letters = []
    for line in arr:
        for c in line:
            if (not (c in letters)):
                letters.append(c)
    return len(letters)

with open("input.txt") as f:
    lines = f.read().split("\n\n")
    sum = 0
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")
        sum += getCount(lines[i])
    print(sum)