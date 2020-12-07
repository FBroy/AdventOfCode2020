def getCount(arr):
    letters = []
    for line in arr:
        for c in line:
            contains = True
            for line in arr:
                if not(c in line):
                    contains = False
            if (contains and not (c in letters)):
                letters.append(c)
    return len(letters)

with open("input.txt") as f:
    lines = f.read().split("\n\n")
    sum = 0
    numbers = []
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")
        if i == len(lines)-1:
            del lines[i][-1]
        number = getCount(lines[i])
        sum += number
        numbers.append(number)
    print(sum)

